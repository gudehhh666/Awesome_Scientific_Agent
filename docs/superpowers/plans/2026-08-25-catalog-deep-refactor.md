# Catalog Deep Refactor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace hand-maintained catalog sections with validated structured data, deterministic README generation, refreshed primary-source-backed content, contributor documentation, and automated checks.

**Architecture:** Three standard-library JSON catalogs feed a pure-Python loader, validator, and Markdown renderer. A README template owns editorial prose while generated sections own repeated tables and lists; unit tests, command-line checks, and GitHub Actions enforce consistency.

**Tech Stack:** Python 3.11+ standard library, JSON, Markdown, `unittest`, GitHub Actions, Lychee link checker.

---

## File Map

- `data/agents.json`: taxonomy records and Assistant/Partner/Avatar reading lists.
- `data/resources.json`: repository watchlist plus construction and enhancement resources.
- `data/benchmarks.json`: evaluation-angle definitions and benchmark records.
- `scripts/catalog.py`: loading, schema validation, duplicate checks, and Markdown rendering.
- `scripts/render_readme.py`: write/check entry point for the generated README.
- `scripts/validate_catalog.py`: validation-only command.
- `templates/README.md`: editorial source with eight generated-section tokens.
- `tests/test_catalog.py`: real-data, invalid-data, rendering, and local-link tests.
- `docs/catalog-schema.md`: field reference, controlled vocabularies, and examples.
- `CONTRIBUTING.md`: maintainer workflow and acceptance policy.
- `.github/workflows/validate.yml`: tests, catalog validation, README drift check, and external-link checks.

### Task 1: Characterize the Current Catalog

**Files:**
- Create: `tests/test_catalog.py`
- Read: `README.md`

- [ ] **Step 1: Record baseline invariants**

Run:

```bash
ruby -e 's=File.read("README.md"); puts s.scan(/^\| (Assistant|Partner|Avatar) \|/).length; puts s.scan(/^\- \*\*/).length'
```

Expected: `65` taxonomy rows followed by `131` bulleted catalog resources.

- [ ] **Step 2: Add the first failing tests**

Create `tests/test_catalog.py` with tests that import `scripts.catalog`, load the repository catalogs, require exactly three taxonomy levels, require at least 65 taxonomy records, reject duplicate IDs, reject an invalid stage, and require deterministic rendering.

The invalid-record tests use `tempfile.TemporaryDirectory()` and write complete minimal JSON fixtures so each failure tests one rule. Each assertion checks that `CatalogError` includes both the record ID and the violated field.

- [ ] **Step 3: Prove the tests fail before implementation**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: failure with `ModuleNotFoundError: No module named 'scripts.catalog'`.

### Task 2: Implement the Catalog Core

**Files:**
- Create: `scripts/__init__.py`
- Create: `scripts/catalog.py`
- Modify: `tests/test_catalog.py`

- [ ] **Step 1: Define the public catalog API**

Implement `CatalogError(ValueError)` and these exact public signatures in `scripts/catalog.py`: `load_catalog(root: Path) -> dict[str, object]`, `validate_catalog(catalog: dict[str, object]) -> None`, `render_readme(template: str, catalog: dict[str, object]) -> str`, and `find_missing_local_links(root: Path, markdown_files: Iterable[Path]) -> list[str]`.

Use `json.loads`, `urllib.parse.urlparse`, `collections.Counter`, `re`, and `pathlib.Path` only. Define controlled constants for levels, stages, capability codes, component values, evaluation angles, and link kinds.

- [ ] **Step 2: Implement strict validation**

Require exact top-level keys and exact record keys. Validate stable IDs with `^[a-z0-9]+(?:-[a-z0-9]+)*$`, require `https` URLs, reject `https://arxiv.org/` and `https://arxiv.org/abs/`, and detect duplicate IDs globally plus duplicate normalized titles and URLs within each section.

Normalize titles by Unicode case-folding and removing non-alphanumeric characters. Format every exception as `<file-or-section>:<record-id>: <message>`.

- [ ] **Step 3: Implement deterministic Markdown renderers**

Add render helpers for taxonomy dashboard/table, level reading lists, repository watchlist, construction resources, enhancement resources, benchmark dashboard, and benchmark list. Escape `|`, normalize internal whitespace, keep source order, and end output with one newline.

Render resource links as stable text links, for example:

```markdown
- **Paper title** — arXiv, 2025 · [paper](https://arxiv.org/abs/2501.00001) · [code](https://github.com/example/project)
```

- [ ] **Step 4: Run focused tests**

Run:

```bash
python3 -m unittest tests.test_catalog -v
```

Expected: schema-focused tests pass; real-data tests remain skipped until Task 3 creates the catalogs.

### Task 3: Migrate Existing README Content Without Loss

**Files:**
- Create: `data/agents.json`
- Create: `data/resources.json`
- Create: `data/benchmarks.json`
- Create: `templates/README.md`
- Modify: `tests/test_catalog.py`

- [ ] **Step 1: Extract taxonomy records mechanically**

Parse the table between `<!-- taxonomy-table:start -->` and `<!-- taxonomy-table:end -->`. Map every row to the agent schema, preserving source order and the exact 65 names, levels, domains, backbone types, E/M values, component flags, stages, and descriptions.

- [ ] **Step 2: Extract repeated resource sections**

Parse the three level reading lists, broader repository table, construction list, enhancement list, and benchmark list. Preserve every title and destination URL. Convert badges to normalized `venue`, `year`, and typed links; when an existing line has a non-specific URL, verify and replace it with a primary destination before migration.

- [ ] **Step 3: Create the README template**

Copy the existing editorial text and figures into `templates/README.md`. Replace only the generated bodies with these exact tokens:

```text
{{GENERATED_TAXONOMY}}
{{GENERATED_ASSISTANT_RESOURCES}}
{{GENERATED_PARTNER_RESOURCES}}
{{GENERATED_AVATAR_RESOURCES}}
{{GENERATED_WATCHLIST}}
{{GENERATED_CONSTRUCTION}}
{{GENERATED_ENHANCEMENT}}
{{GENERATED_BENCHMARKS}}
```

Add a generated-file notice to the root README output, not to the public prose inside sections.

- [ ] **Step 4: Add migration-preservation assertions**

Assert that taxonomy record count is 65 before the refresh, all legacy destination URLs occur in either JSON data or an explicitly documented correction map, and all ten figure paths remain in rendered output.

- [ ] **Step 5: Run the migration tests**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: all migration, schema, and rendering tests pass.

### Task 4: Add README and Validation Commands

**Files:**
- Create: `scripts/render_readme.py`
- Create: `scripts/validate_catalog.py`
- Modify: `README.md`
- Modify: `tests/test_catalog.py`

- [ ] **Step 1: Add the render CLI**

`scripts/render_readme.py` resolves the repository root from `__file__`, loads the catalogs, renders `templates/README.md`, and either writes `README.md` atomically or checks byte equality under `--check`. Drift prints `README.md is stale; run python3 scripts/render_readme.py` and exits 1.

- [ ] **Step 2: Add the validation CLI**

`scripts/validate_catalog.py` loads and validates all catalogs, scans `README.md`, `templates/README.md`, `CONTRIBUTING.md` when present, `docs/**/*.md`, and `methods/**/*.md` for missing local targets, prints record counts by section, and exits nonzero with one error per line on failure.

- [ ] **Step 3: Generate the root README**

Run:

```bash
python3 scripts/render_readme.py
python3 scripts/render_readme.py --check
python3 scripts/validate_catalog.py
```

Expected: README generation succeeds, check reports it is current, validation prints section counts, and all commands exit 0.

- [ ] **Step 4: Commit the data-driven core**

Run:

```bash
git add data scripts templates tests README.md
git commit -m "refactor: generate catalog from structured data"
```

### Task 5: Refresh Recent Scientific-Agent Content

**Files:**
- Modify: `data/agents.json`
- Modify: `data/resources.json`
- Modify: `data/benchmarks.json`
- Modify: `README.md`

- [ ] **Step 1: Search primary discovery channels**

Search arXiv and the web for 2025–2026 work using these queries:

```text
scientific agent autonomous research 2026
AI scientist agent automated scientific discovery 2026
LLM laboratory agent scientific discovery 2026
scientific agent benchmark research automation 2026
```

Open the arXiv abstract, publisher, official project, dataset, or canonical repository for every candidate. Do not accept search-result snippets as metadata.

- [ ] **Step 2: De-duplicate and classify candidates**

Match by arXiv ID, DOI, canonical repository URL, then normalized title. Add only records whose title, year, URL, scientific scope, and classification can be verified. Put ambiguous systems into a reading list instead of the taxonomy.

- [ ] **Step 3: Correct existing factual defects found during verification**

Replace generic arXiv home-page links, inconsistent titles, duplicate benchmark entries, incorrect badge years, and known canonical-name errors. Record substantive corrections in the commit body.

- [ ] **Step 4: Regenerate and test**

Run:

```bash
python3 scripts/render_readme.py
python3 -m unittest discover -s tests -v
python3 scripts/validate_catalog.py
python3 scripts/render_readme.py --check
```

Expected: all commands exit 0 and generated counts reflect the refreshed data.

- [ ] **Step 5: Commit the refresh**

Run:

```bash
git add data README.md
git commit -m "docs: refresh verified scientific agent catalog"
```

### Task 6: Document the Maintenance Contract

**Files:**
- Create: `docs/catalog-schema.md`
- Create: `CONTRIBUTING.md`
- Modify: `templates/README.md`
- Modify: `README.md`

- [ ] **Step 1: Write the schema reference**

Document every field, allowed value, uniqueness rule, primary-source rule, and one complete valid record for each catalog type. Include exact commands for validation and generation.

- [ ] **Step 2: Write contributor instructions**

Document taxonomy decisions, evidence requirements, edit/regenerate/test order, direct-`main` maintainer flow, and commit expectations. State that generated sections in `README.md` must not be edited directly.

- [ ] **Step 3: Link maintenance docs from the README**

Add a concise Contributing section to the template linking to `CONTRIBUTING.md` and `docs/catalog-schema.md`, then regenerate the README.

- [ ] **Step 4: Test and commit documentation**

Run:

```bash
python3 scripts/render_readme.py
python3 -m unittest discover -s tests -v
python3 scripts/validate_catalog.py
```

Expected: all commands exit 0 and all new local links resolve.

Run:

```bash
git add CONTRIBUTING.md docs/catalog-schema.md templates/README.md README.md
git commit -m "docs: define catalog contribution workflow"
```

### Task 7: Add Continuous Validation

**Files:**
- Create: `.github/workflows/validate.yml`
- Create: `.lychee.toml`
- Modify: `tests/test_catalog.py`

- [ ] **Step 1: Add the GitHub Actions workflow**

Configure `push` on `main`, `pull_request`, `workflow_dispatch`, and a weekly cron. The core job checks out the repository, installs Python 3.12, runs unit tests, validates data/local links, and checks README freshness. A separate link job runs Lychee against tracked Markdown and HTML files with retries and accepted status 429.

- [ ] **Step 2: Add explicit link-checker configuration**

Set `max_retries = 3`, `retry_wait_time = 2`, `timeout = 20`, `accept = [200, 206, 429]`, and exclude only documented anti-bot endpoints after observing a reproducible automated-client failure. Do not exclude whole domains when a narrower URL pattern works.

- [ ] **Step 3: Add workflow contract tests**

Read `.github/workflows/validate.yml` as text and assert it invokes these exact commands:

```text
python3 -m unittest discover -s tests -v
python3 scripts/validate_catalog.py
python3 scripts/render_readme.py --check
```

Also assert the workflow contains `push`, `pull_request`, `workflow_dispatch`, and `schedule` triggers.

- [ ] **Step 4: Run all local checks**

Run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_catalog.py
python3 scripts/render_readme.py --check
git diff --check
```

Expected: all commands exit 0.

- [ ] **Step 5: Commit automation**

Run:

```bash
git add .github/workflows/validate.yml .lychee.toml tests/test_catalog.py
git commit -m "ci: validate catalog and documentation links"
```

### Task 8: Final Verification and Direct Push

**Files:**
- Verify all tracked files.

- [ ] **Step 1: Run the complete fresh verification suite**

Run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_catalog.py
python3 scripts/render_readme.py --check
git diff --check
git fsck --full
git status --short --branch
```

Expected: tests pass, catalog and README checks pass, Git reports no whitespace or object-integrity errors, and the working tree is clean with local `main` ahead of `origin/main` only by the intended commits.

- [ ] **Step 2: Review the outgoing commit range**

Run:

```bash
git log --oneline --decorate origin/main..main
git diff --stat origin/main..main
git diff --name-status origin/main..main
```

Expected: only the design, structured catalog, generator/tests, verified refresh, documentation, and CI files appear.

- [ ] **Step 3: Restore GitHub authentication if required**

Run `gh auth status`. If invalid, run `gh auth login -h github.com` and complete the GitHub device/browser authorization as `gudehhh666`.

- [ ] **Step 4: Push directly to main**

Run:

```bash
git push origin main
```

Expected: `origin/main` advances to the verified local `main` without force-pushing.

- [ ] **Step 5: Verify the remote commit**

Run:

```bash
git fetch origin main
git rev-parse HEAD
git rev-parse origin/main
```

Expected: both commit hashes are identical.
