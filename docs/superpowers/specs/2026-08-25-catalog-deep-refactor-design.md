# Catalog Deep Refactor Design

## Goal

Turn Awesome Scientific Agent from a hand-maintained README into a data-driven catalog that remains pleasant to read, easy for one maintainer to update, and mechanically verifiable before every push to `main`.

## Scope

The refactor will:

- Move taxonomy rows, level reading lists, broader repository watchlists, construction resources, enhancement resources, and benchmarks into structured JSON files.
- Keep editorial prose, navigation, figures, method-guide introductions, and the citation block in a README template.
- Generate the public `README.md` deterministically from the template and catalog data.
- Validate required fields, controlled vocabulary, URLs, duplicate identities, taxonomy counts, and generated-file freshness.
- Add unit tests, contributor instructions, schema documentation, and GitHub Actions checks.
- Refresh the catalog with recent scientific-agent resources only after verifying each addition against primary sources.
- Preserve the existing visual identity, section anchors, figures, citation, and useful content unless a factual or structural correction is required.

This refactor will not create a website, add a database, depend on a hosted service, or automatically publish unreviewed search results.

## Repository Structure

```text
.
├── data/
│   ├── agents.json
│   ├── benchmarks.json
│   └── resources.json
├── docs/
│   ├── catalog-schema.md
│   └── superpowers/
│       └── specs/
├── scripts/
│   ├── catalog.py
│   ├── render_readme.py
│   └── validate_catalog.py
├── templates/
│   └── README.md
├── tests/
│   └── test_catalog.py
├── .github/workflows/
│   └── validate.yml
├── CONTRIBUTING.md
└── README.md
```

Each file has one responsibility:

- `data/agents.json` is the source of truth for the Assistant, Partner, and Avatar taxonomy and their level-specific reading lists.
- `data/benchmarks.json` stores benchmark metadata and evaluation categories.
- `data/resources.json` stores construction, enhancement, and broader auto-research repositories.
- `templates/README.md` contains all hand-authored prose and named insertion tokens.
- `scripts/catalog.py` loads data, validates records, and exposes deterministic render helpers.
- `scripts/render_readme.py` renders `README.md` or checks that the committed file is current.
- `scripts/validate_catalog.py` provides a small command-line validation entry point.
- `tests/test_catalog.py` covers schema errors, duplicate detection, taxonomy counts, rendering, and local links.

JSON is preferred over YAML because Python can parse it without third-party packages. This keeps both local use and GitHub Actions reproducible with only the Python standard library.

## Data Model

Every record will have a stable `id`, a display `name`, and the fields required by its section. Stable IDs are lowercase kebab-case and are used for duplicate detection and actionable error messages.

Agent taxonomy records include:

- `id`, `name`, `level`, `domain`, `backbone`
- `capability_envelope`, `capability_maturity`
- `reasoning`, `memory`, `collaboration`
- `stages`, `description`

Reading-list and method-resource records include:

- `id`, `title`, `year`, `venue`
- at least one primary `links` entry, with a typed label such as `arxiv`, `paper`, `code`, `project`, or `dataset`

Benchmark records additionally include an `evaluation_angle`. Repository watchlist records include `repository`, `scope`, and `rationale`.

Controlled vocabularies will be enforced for taxonomy levels, capability codes, yes/no component flags, research stages, evaluation angles, and link types. Records remain ordered in JSON so the maintainer controls public presentation without a separate ranking field.

## Rendering

The template will use explicit tokens for generated sections. Rendering replaces each token with Markdown derived from its data file and writes one complete `README.md`. The output will include a short generated-file notice pointing maintainers to the template and data directory.

Rendering must be deterministic: the same template and data produce byte-identical output. `python3 scripts/render_readme.py --check` compares the expected output with the committed README and exits nonzero on drift.

The generated taxonomy dashboard derives role counts from data rather than storing manual totals. Markdown escaping prevents table-breaking characters from corrupting output. Existing anchors are retained so inbound links continue to work.

## Validation and Error Handling

Catalog loading fails fast with messages containing the data filename and record ID. Validation rejects:

- Missing or unknown fields.
- Duplicate IDs, duplicate normalized titles within a section, and duplicate primary URLs within a section.
- Invalid URLs or unsupported link types.
- Invalid taxonomy levels, capability values, or research stages.
- Empty descriptions and non-specific links to generic arXiv home pages.
- A generated README that does not match its inputs.
- Missing local Markdown and HTML image targets.

External links are checked separately because network failures and anti-bot responses are operationally different from catalog errors. The workflow will use retries and a documented exclusion list only for domains that consistently reject automated clients; exclusions cannot hide malformed URLs or missing local files.

## Content Refresh Policy

New entries must be supported by a primary source: an arXiv abstract page, publisher page, official project page, official dataset page, or canonical repository. Search snippets, secondary summaries, and model-generated claims are not accepted as evidence.

For each new scientific agent, the maintainer verifies title, year, link, domain, workflow stages, and claimed autonomy before assigning Assistant, Partner, or Avatar. Ambiguous systems are added to a reading list rather than forced into the taxonomy. Existing entries are corrected only when primary evidence contradicts current metadata.

The first refresh targets high-confidence resources published or materially updated after the current catalog snapshot. It favors a smaller verified set over broad but weak coverage.

## Automation

GitHub Actions will run on pushes to `main`, pull requests, manual dispatch, and a weekly schedule. Required local-equivalent checks are:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_catalog.py
python3 scripts/render_readme.py --check
```

The workflow also checks external links. Python runtime and third-party actions are pinned to stable versions or immutable revisions where practical.

## Contribution Workflow

`CONTRIBUTING.md` will describe how to add or edit a record, how to choose a taxonomy level, what evidence is required, how to regenerate the README, and which checks must pass. Although this repository currently has one maintainer and changes are pushed directly to `main`, the workflow remains usable by future contributors.

The normal edit path is:

1. Edit a JSON catalog file and, when needed, `templates/README.md`.
2. Run validation and tests.
3. Regenerate `README.md`.
4. Run the complete check suite.
5. Commit and push directly to `main` only when the working tree contains the intended files.

## Commit and Release Strategy

The refactor is delivered in auditable commits:

1. Record this design.
2. Add the catalog model, migrated data, renderer, and tests.
3. Add the verified content refresh and documentation.
4. Add CI and perform final generated-output verification.

No history rewriting or force push is used. If GitHub authentication remains invalid after local completion, all verified commits stay local until the maintainer re-authenticates; no alternate remote or credential bypass is attempted.

## Acceptance Criteria

- The existing catalog content is represented in structured data without silent loss.
- `README.md` is reproducible from the template and data.
- Dashboard counts exactly match taxonomy records.
- Validation reports actionable failures for malformed or duplicate data.
- Unit tests pass with the system Python and no installed packages.
- All local Markdown/image references resolve.
- New resources have primary-source evidence and no non-specific links.
- Contributor documentation explains the complete maintenance loop.
- GitHub Actions runs the same core checks used locally.
- The final working tree is clean after commits, and commits are pushed directly to `origin/main` once GitHub authentication succeeds.
