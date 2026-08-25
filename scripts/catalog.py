"""Load, validate, and render the scientific-agent catalog."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, Iterator, Mapping, Sequence, Tuple
from urllib.parse import urlparse

STAGES = {
    "Literature",
    "Hypothesis",
    "Design",
    "Verification",
    "Analysis",
    "Evaluation",
}
LINK_KINDS = {"paper", "code", "project", "dataset", "website"}
NON_SPECIFIC_URLS = {"https://arxiv.org", "https://arxiv.org/abs"}
LEVELS = {"Assistant", "Partner", "Avatar"}
CAPABILITY_ENVELOPES = {"E1", "E2", "E3"}
CAPABILITY_MATURITIES = {"M1", "M2", "M3"}
COMPONENT_VALUES = {"Yes", "No"}
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

TAXONOMY_FIELDS = {
    "id",
    "name",
    "level",
    "domain",
    "backbone",
    "capability_envelope",
    "capability_maturity",
    "reasoning",
    "memory",
    "collaboration",
    "stages",
    "description",
}
RESOURCE_FIELDS = {"id", "title", "venue", "year", "links"}
WATCHLIST_FIELDS = {"id", "repository", "scope", "rationale", "links"}
ANGLE_FIELDS = {"id", "name", "focus", "use_when"}
BENCHMARK_FIELDS = {
    "id",
    "title",
    "venue",
    "year",
    "evaluation_angle",
    "links",
}
LINK_FIELDS = {"kind", "label", "url"}


class CatalogError(ValueError):
    """Raised when catalog data violates the repository schema."""


def _iter_records(catalog: Dict[str, object]) -> Iterator[Tuple[str, dict]]:
    agents = catalog["agents"]
    yield from (("taxonomy", record) for record in agents["taxonomy"])
    for level, records in agents["reading_lists"].items():
        yield from ((f"reading_lists.{level}", record) for record in records)

    resources = catalog["resources"]
    for section in ("watchlist", "construction", "enhancement"):
        yield from ((section, record) for record in resources[section])

    benchmarks = catalog["benchmarks"]
    yield from (
        ("evaluation_angles", record)
        for record in benchmarks["evaluation_angles"]
    )
    yield from (("benchmarks", record) for record in benchmarks["items"])


def _expect_keys(
    value: Mapping[str, object], expected: set, section: str, record_id: str
) -> None:
    actual = set(value)
    unknown = sorted(actual - expected)
    missing = sorted(expected - actual)
    if unknown:
        raise CatalogError(
            f"{section}:{record_id}: unknown fields: {', '.join(unknown)}"
        )
    if missing:
        raise CatalogError(
            f"{section}:{record_id}: missing fields: {', '.join(missing)}"
        )


def _expect_non_empty_text(
    value: object, section: str, record_id: str, field: str
) -> None:
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f"{section}:{record_id}: {field} must be non-empty text")


def _normalize_title(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return "".join(character for character in normalized if character.isalnum())


def _validate_links(section: str, record_id: str, links: object) -> None:
    if not isinstance(links, list) or not links:
        raise CatalogError(f"{section}:{record_id}: links must be a non-empty list")
    for index, link in enumerate(links):
        if not isinstance(link, dict):
            raise CatalogError(
                f"{section}:{record_id}: links[{index}] must be an object"
            )
        _expect_keys(link, LINK_FIELDS, section, record_id)
        _expect_non_empty_text(link["label"], section, record_id, "links.label")
        url = link["url"]
        parsed = urlparse(url) if isinstance(url, str) else None
        if parsed is None or parsed.scheme != "https" or not parsed.netloc:
            raise CatalogError(
                f"{section}:{record_id}: links must use absolute https URLs"
            )
        if url.rstrip("/") in NON_SPECIFIC_URLS:
            raise CatalogError(
                f"{section}:{record_id}: links must target a specific resource"
            )
        if link["kind"] not in LINK_KINDS:
            raise CatalogError(
                f"{section}:{record_id}: links contain unsupported kind"
            )


def _validate_resource(section: str, record: dict) -> None:
    record_id = str(record.get("id", "<missing>"))
    _expect_keys(record, RESOURCE_FIELDS, section, record_id)
    for field in ("title", "venue"):
        _expect_non_empty_text(record[field], section, record_id, field)
    if not isinstance(record["year"], int) or not 1900 <= record["year"] <= 2100:
        raise CatalogError(f"{section}:{record_id}: year must be an integer")
    _validate_links(section, record_id, record["links"])


def load_catalog(root: Path) -> Dict[str, object]:
    """Load catalog data rooted at *root*."""
    data_dir = root / "data"
    catalog = {}
    for name in ("agents", "resources", "benchmarks"):
        path = data_dir / f"{name}.json"
        try:
            catalog[name] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise CatalogError(f"{path}: {error}") from error
    validate_catalog(catalog)
    return catalog


def validate_catalog(catalog: Dict[str, object]) -> None:
    """Validate in-memory catalog data."""
    _expect_keys(catalog, {"agents", "resources", "benchmarks"}, "catalog", "root")
    agents = catalog["agents"]
    resources = catalog["resources"]
    benchmarks = catalog["benchmarks"]
    for name, value, fields in (
        ("agents", agents, {"schema_version", "taxonomy", "reading_lists"}),
        (
            "resources",
            resources,
            {"schema_version", "watchlist", "construction", "enhancement"},
        ),
        (
            "benchmarks",
            benchmarks,
            {"schema_version", "evaluation_angles", "items"},
        ),
    ):
        if not isinstance(value, dict):
            raise CatalogError(f"catalog:{name}: must be an object")
        _expect_keys(value, fields, name, "root")
        if value["schema_version"] != 1:
            raise CatalogError(f"{name}:root: schema_version must equal 1")

    if set(agents["reading_lists"]) != {"assistant", "partner", "avatar"}:
        raise CatalogError(
            "agents:reading_lists: levels must be assistant, partner, and avatar"
        )

    seen_ids = set()
    for section, record in _iter_records(catalog):
        if not isinstance(record, dict):
            raise CatalogError(f"{section}:<unknown>: record must be an object")
        record_id = record["id"]
        if not isinstance(record_id, str) or not ID_PATTERN.fullmatch(record_id):
            raise CatalogError(f"{section}:{record_id}: id has invalid format")
        if record_id in seen_ids:
            raise CatalogError(f"{section}:{record_id}: duplicate id")
        seen_ids.add(record_id)

    for record in agents["taxonomy"]:
        record_id = str(record.get("id", "<missing>"))
        _expect_keys(record, TAXONOMY_FIELDS, "taxonomy", record_id)
        for field in ("name", "domain", "backbone", "description"):
            _expect_non_empty_text(record[field], "taxonomy", record_id, field)
        if record["level"] not in LEVELS:
            raise CatalogError(f"taxonomy:{record_id}: level is unsupported")
        if record["capability_envelope"] not in CAPABILITY_ENVELOPES:
            raise CatalogError(
                f"taxonomy:{record_id}: capability_envelope is unsupported"
            )
        if record["capability_maturity"] not in CAPABILITY_MATURITIES:
            raise CatalogError(
                f"taxonomy:{record_id}: capability_maturity is unsupported"
            )
        for field in ("reasoning", "memory", "collaboration"):
            if record[field] not in COMPONENT_VALUES:
                raise CatalogError(f"taxonomy:{record_id}: {field} is unsupported")
        if not isinstance(record["stages"], list) or not record["stages"]:
            raise CatalogError(
                f"taxonomy:{record_id}: stages must be a non-empty list"
            )
        unknown = set(record["stages"]) - STAGES
        if unknown:
            raise CatalogError(
                f"taxonomy:{record['id']}: stages contain unsupported values: "
                f"{', '.join(sorted(unknown))}"
            )

    for level, records in agents["reading_lists"].items():
        for record in records:
            _validate_resource(f"reading_lists.{level}", record)

    for record in resources["watchlist"]:
        record_id = str(record.get("id", "<missing>"))
        _expect_keys(record, WATCHLIST_FIELDS, "watchlist", record_id)
        for field in ("repository", "scope", "rationale"):
            _expect_non_empty_text(record[field], "watchlist", record_id, field)
        _validate_links("watchlist", record_id, record["links"])

    for section in ("construction", "enhancement"):
        for record in resources[section]:
            _validate_resource(section, record)

    angle_ids = set()
    for record in benchmarks["evaluation_angles"]:
        record_id = str(record.get("id", "<missing>"))
        _expect_keys(record, ANGLE_FIELDS, "evaluation_angles", record_id)
        for field in ("name", "focus", "use_when"):
            _expect_non_empty_text(record[field], "evaluation_angles", record_id, field)
        angle_ids.add(record_id)

    for record in benchmarks["items"]:
        record_id = str(record.get("id", "<missing>"))
        _expect_keys(record, BENCHMARK_FIELDS, "benchmarks", record_id)
        for field in ("title", "venue", "evaluation_angle"):
            _expect_non_empty_text(record[field], "benchmarks", record_id, field)
        if record["evaluation_angle"] not in angle_ids:
            raise CatalogError(
                f"benchmarks:{record_id}: evaluation_angle does not exist"
            )
        if not isinstance(record["year"], int) or not 1900 <= record["year"] <= 2100:
            raise CatalogError(f"benchmarks:{record_id}: year must be an integer")
        _validate_links("benchmarks", record_id, record["links"])

    title_groups = defaultdict(dict)
    url_groups = defaultdict(dict)
    for section, record in _iter_records(catalog):
        title = record.get("title") or record.get("name") or record.get("repository")
        if title:
            normalized = _normalize_title(str(title))
            if normalized in title_groups[section]:
                raise CatalogError(
                    f"{section}:{record['id']}: duplicate normalized title"
                )
            title_groups[section][normalized] = record["id"]
        for link in record.get("links", []):
            url = link["url"].rstrip("/")
            if url in url_groups[section]:
                raise CatalogError(f"{section}:{record['id']}: duplicate URL")
            url_groups[section][url] = record["id"]


def _markdown(value: object) -> str:
    text = " ".join(str(value).split())
    return text.replace("|", "\\|")


def _render_links(links: Sequence[dict]) -> str:
    return " · ".join(
        f"[{_markdown(link['label'])}]({link['url']})" for link in links
    )


def _render_resource_list(records: Sequence[dict]) -> str:
    if not records:
        return "<!-- No entries. -->"
    return "\n".join(
        f"- **{_markdown(record['title'])}** — "
        f"{_markdown(record['venue'])}, {record['year']} · "
        f"{_render_links(record['links'])}"
        for record in records
    )


def _render_taxonomy(records: Sequence[dict]) -> str:
    counts = {level: 0 for level in ("Assistant", "Partner", "Avatar")}
    for record in records:
        counts[record["level"]] += 1

    lines = [
        "<!-- taxonomy-table:start -->",
        "### Taxonomy Dashboard",
        "",
        "| Level | Role in scientific work | Count | Typical scope |",
        "| --- | --- | ---: | --- |",
        f"| **Assistant** | Helps with bounded scientific tasks under direct human steering. | {counts['Assistant']} | Literature synthesis, QA, design assistance, and analysis support. |",
        f"| **Partner** | Collaborates across multiple workflow steps with stronger tool use or feedback loops. | {counts['Partner']} | Ideation, experiment planning, automation, review, and domain reasoning. |",
        f"| **Avatar** | Acts as a higher-autonomy research executor in digital or physical environments. | {counts['Avatar']} | Autonomous labs, discovery loops, and end-to-end research. |",
        "",
        "| Capability / component | Meaning |",
        "| --- | --- |",
        "| **E** | Capability envelope: the breadth of scientific workflow coverage. |",
        "| **M** | Capability maturity: the maturity of autonomy and execution. |",
        "| **R / Mem. / C** | Reasoning enhancement, memory enhancement, and collaboration enhancement. |",
        "| **Stages** | Literature, Hypothesis, Design, Verification, Analysis, and Evaluation. |",
        "",
        "<details open>",
        f"<summary><b>Full taxonomy table</b> — {len(records)} scientific agents across levels, domains, capabilities, components, and research stages</summary>",
        "",
        "Capability envelope is abbreviated as `E`, capability maturity as `M`, reasoning enhancement as `R`, memory enhancement as `Mem.`, and collaboration enhancement as `C`.",
        "",
        "| Level | Method | Domain | LLM Backbone | E | M | R | Mem. | C | Application Stages | Task Description |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            "| "
            + " | ".join(
                _markdown(value)
                for value in (
                    record["level"],
                    record["name"],
                    record["domain"],
                    record["backbone"],
                    record["capability_envelope"],
                    record["capability_maturity"],
                    record["reasoning"],
                    record["memory"],
                    record["collaboration"],
                    ", ".join(record["stages"]),
                    record["description"],
                )
            )
            + " |"
        )
    lines.extend(["", "</details>", "<!-- taxonomy-table:end -->"])
    return "\n".join(lines)


def _render_watchlist(records: Sequence[dict]) -> str:
    if not records:
        return "<!-- No entries. -->"
    lines = [
        "| Repository | Scope | Why follow it |",
        "| --- | --- | --- |",
    ]
    for record in records:
        primary = record["links"][0]
        repository = f"[{_markdown(record['repository'])}]({primary['url']})"
        lines.append(
            f"| {repository} | {_markdown(record['scope'])} | "
            f"{_markdown(record['rationale'])} |"
        )
    return "\n".join(lines)


def _render_benchmarks(data: dict) -> str:
    lines = [
        "| Evaluation angle | Representative focus | Useful when you need to test... |",
        "| --- | --- | --- |",
    ]
    for angle in data["evaluation_angles"]:
        lines.append(
            f"| **{_markdown(angle['name'])}** | {_markdown(angle['focus'])} | "
            f"{_markdown(angle['use_when'])} |"
        )
    lines.extend(
        [
            "",
            "<details open>",
            "<summary><b>Benchmark resources</b> — evaluation suites for scientific reasoning, data analysis, citation, coding, and agentic discovery</summary>",
            "",
            _render_resource_list(data["items"]),
            "",
            "</details>",
        ]
    )
    return "\n".join(lines)


def render_readme(template: str, catalog: Dict[str, object]) -> str:
    """Render a complete README from an editorial template and catalog data."""
    validate_catalog(catalog)
    agents = catalog["agents"]
    resources = catalog["resources"]
    replacements = {
        "{{AGENT_COUNT}}": str(len(agents["taxonomy"])),
        "{{GENERATED_TAXONOMY}}": _render_taxonomy(agents["taxonomy"]),
        "{{GENERATED_ASSISTANT_RESOURCES}}": _render_resource_list(
            agents["reading_lists"]["assistant"]
        ),
        "{{GENERATED_PARTNER_RESOURCES}}": _render_resource_list(
            agents["reading_lists"]["partner"]
        ),
        "{{GENERATED_AVATAR_RESOURCES}}": _render_resource_list(
            agents["reading_lists"]["avatar"]
        ),
        "{{GENERATED_WATCHLIST}}": _render_watchlist(resources["watchlist"]),
        "{{GENERATED_CONSTRUCTION}}": _render_resource_list(
            resources["construction"]
        ),
        "{{GENERATED_ENHANCEMENT}}": _render_resource_list(
            resources["enhancement"]
        ),
        "{{GENERATED_BENCHMARKS}}": _render_benchmarks(catalog["benchmarks"]),
    }
    rendered = template
    for token, markdown in replacements.items():
        if rendered.count(token) != 1:
            raise CatalogError(f"template:{token}: expected exactly one token")
        rendered = rendered.replace(token, markdown)
    return rendered.rstrip() + "\n"


def find_missing_local_links(
    root: Path, markdown_files: Iterable[Path]
) -> list[str]:
    """Return missing local Markdown and HTML targets with source context."""
    missing = []
    markdown_pattern = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)")
    html_pattern = re.compile(r"(?:src|href)=[\"']([^\"']+)[\"']")
    for markdown_file in markdown_files:
        content = markdown_file.read_text(encoding="utf-8")
        targets = markdown_pattern.findall(content) + html_pattern.findall(content)
        for target in targets:
            if target.startswith(("https://", "http://", "mailto:", "#", "data:")):
                continue
            path_text = target.split("#", 1)[0]
            if not path_text:
                continue
            target_path = (markdown_file.parent / path_text).resolve()
            if not target_path.exists():
                source = markdown_file.relative_to(root).as_posix()
                missing.append(f"{source}: {path_text}")
    return sorted(set(missing))
