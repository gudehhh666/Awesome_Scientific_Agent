import importlib
import copy
import unittest
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def minimal_catalog() -> dict:
    return {
        "agents": {
            "schema_version": 1,
            "taxonomy": [
                {
                    "id": "paper-agent",
                    "name": "Paper Agent",
                    "level": "Assistant",
                    "domain": "General",
                    "backbone": "General-purpose",
                    "capability_envelope": "E1",
                    "capability_maturity": "M1",
                    "reasoning": "Yes",
                    "memory": "No",
                    "collaboration": "No",
                    "stages": ["Literature"],
                    "description": "Evidence-grounded literature assistance.",
                }
            ],
            "reading_lists": {
                "assistant": [],
                "partner": [],
                "avatar": [],
            },
        },
        "resources": {
            "schema_version": 1,
            "watchlist": [],
            "construction": [],
            "enhancement": [],
        },
        "benchmarks": {
            "schema_version": 1,
            "evaluation_angles": [
                {
                    "id": "scientific-reasoning",
                    "name": "Scientific reasoning",
                    "focus": "Scientific knowledge and multi-step inference.",
                    "use_when": "Testing scientific reasoning.",
                }
            ],
            "items": [],
        },
    }


class CatalogApiTests(unittest.TestCase):
    def test_catalog_module_exposes_loader(self) -> None:
        catalog = importlib.import_module("scripts.catalog")

        self.assertTrue(callable(catalog.load_catalog))

    def test_minimal_catalog_is_valid(self) -> None:
        catalog = importlib.import_module("scripts.catalog")

        catalog.validate_catalog(minimal_catalog())

    def test_invalid_agent_stage_is_rejected_with_record_context(self) -> None:
        catalog = importlib.import_module("scripts.catalog")
        data = minimal_catalog()
        data["agents"]["taxonomy"][0]["stages"] = ["Inventing"]

        with self.assertRaisesRegex(
            catalog.CatalogError, r"taxonomy:paper-agent: stages"
        ):
            catalog.validate_catalog(data)

    def test_duplicate_ids_are_rejected_globally(self) -> None:
        catalog = importlib.import_module("scripts.catalog")
        data = minimal_catalog()
        duplicate = copy.deepcopy(data["agents"]["taxonomy"][0])
        duplicate["name"] = "Another Agent"
        data["agents"]["taxonomy"].append(duplicate)

        with self.assertRaisesRegex(
            catalog.CatalogError, r"taxonomy:paper-agent: duplicate id"
        ):
            catalog.validate_catalog(data)

    def test_non_specific_arxiv_link_is_rejected(self) -> None:
        catalog = importlib.import_module("scripts.catalog")
        data = minimal_catalog()
        data["resources"]["construction"].append(
            {
                "id": "tool-agent",
                "title": "Tool Agent",
                "venue": "arXiv",
                "year": 2025,
                "links": [
                    {
                        "kind": "paper",
                        "label": "paper",
                        "url": "https://arxiv.org/",
                    }
                ],
            }
        )

        with self.assertRaisesRegex(
            catalog.CatalogError, r"construction:tool-agent: links"
        ):
            catalog.validate_catalog(data)

    def test_unknown_agent_field_is_rejected(self) -> None:
        catalog = importlib.import_module("scripts.catalog")
        data = minimal_catalog()
        data["agents"]["taxonomy"][0]["notes"] = "not in the schema"

        with self.assertRaisesRegex(
            catalog.CatalogError, r"taxonomy:paper-agent: unknown fields: notes"
        ):
            catalog.validate_catalog(data)

    def test_rendering_replaces_every_generated_token_deterministically(self) -> None:
        catalog = importlib.import_module("scripts.catalog")
        template = "\n".join(
            [
                "Agents={{AGENT_COUNT}}",
                "{{GENERATED_TAXONOMY}}",
                "{{GENERATED_ASSISTANT_RESOURCES}}",
                "{{GENERATED_PARTNER_RESOURCES}}",
                "{{GENERATED_AVATAR_RESOURCES}}",
                "{{GENERATED_WATCHLIST}}",
                "{{GENERATED_CONSTRUCTION}}",
                "{{GENERATED_ENHANCEMENT}}",
                "{{GENERATED_BENCHMARKS}}",
            ]
        )

        first = catalog.render_readme(template, minimal_catalog())
        second = catalog.render_readme(template, minimal_catalog())

        self.assertEqual(first, second)
        self.assertNotIn("{{", first)
        self.assertIn("Agents=1", first)
        self.assertIn("| **Assistant** |", first)
        self.assertTrue(first.endswith("\n"))

    def test_real_catalog_preserves_legacy_taxonomy(self) -> None:
        catalog = importlib.import_module("scripts.catalog")

        data = catalog.load_catalog(ROOT)

        self.assertGreaterEqual(len(data["agents"]["taxonomy"]), 65)
        self.assertEqual(
            {"Assistant", "Partner", "Avatar"},
            {record["level"] for record in data["agents"]["taxonomy"]},
        )
        resource_count = sum(
            len(records) for records in data["agents"]["reading_lists"].values()
        )
        resource_count += sum(
            len(data["resources"][section])
            for section in ("construction", "enhancement")
        )
        resource_count += len(data["benchmarks"]["items"])
        self.assertGreaterEqual(resource_count, 131)

        template = (ROOT / "templates" / "README.md").read_text(encoding="utf-8")
        rendered = catalog.render_readme(template, data)
        for figure in (
            "overall_short.png",
            "overall.png",
            "level.png",
            "level_2.png",
            "construction_overview.png",
            "knowledge_organization.png",
            "orchestration_flat.png",
            "enhancement_overview.png",
            "memory.png",
            "reasoning.png",
            "benchmark_overview.png",
        ):
            self.assertIn(f"./figures/{figure}", rendered)

    def test_verified_refresh_entries_are_present(self) -> None:
        catalog = importlib.import_module("scripts.catalog")
        data = catalog.load_catalog(ROOT)

        taxonomy_ids = {record["id"] for record in data["agents"]["taxonomy"]}
        benchmark_ids = {record["id"] for record in data["benchmarks"]["items"]}

        self.assertTrue(
            {
                "agent-evoscientist",
                "agent-sr-scientist",
                "agent-self-evolving-fluid-control",
            }.issubset(taxonomy_ids)
        )
        self.assertTrue(
            {"benchmark-aisb", "benchmark-dsagentbench"}.issubset(benchmark_ids)
        )

    def test_missing_local_links_reports_markdown_and_html_targets(self) -> None:
        catalog = importlib.import_module("scripts.catalog")
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            markdown = root / "guide.md"
            markdown.write_text(
                "[missing](./missing.md)\n"
                '<img src="./missing.png" alt="missing">\n',
                encoding="utf-8",
            )

            missing = catalog.find_missing_local_links(root, [markdown])

        self.assertEqual(
            ["guide.md: ./missing.md", "guide.md: ./missing.png"], missing
        )

    def test_validation_workflow_enforces_repository_contract(self) -> None:
        workflow = (
            ROOT / ".github" / "workflows" / "validate.yml"
        ).read_text(encoding="utf-8")
        lychee_config = (ROOT / ".lychee.toml").read_text(encoding="utf-8")

        for trigger in ("push:", "pull_request:", "workflow_dispatch:", "schedule:"):
            self.assertIn(trigger, workflow)
        for command in (
            "python3 -m unittest discover -s tests -v",
            "python3 scripts/validate_catalog.py",
            "python3 scripts/render_readme.py --check",
        ):
            self.assertIn(command, workflow)
        for pinned_action in (
            "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97",
            "lycheeverse/lychee-action@e7477775783ea5526144ba13e8db5eec57747ce8",
        ):
            self.assertIn(pinned_action, workflow)
        for setting in (
            "max_retries = 3",
            "retry_wait_time = 2",
            "timeout = 20",
            "accept = [200, 206, 429]",
        ):
            self.assertIn(setting, lychee_config)


if __name__ == "__main__":
    unittest.main()
