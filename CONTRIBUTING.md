# Contributing to Awesome Scientific Agent

Thanks for helping keep the catalog accurate and useful. The repository is data-driven: repeated catalog sections in `README.md` are generated from files in `data/`.

## What to Edit

- Edit `data/agents.json` for taxonomy entries and Assistant/Partner/Avatar reading lists.
- Edit `data/resources.json` for the broader repository watchlist, construction resources, and enhancement resources.
- Edit `data/benchmarks.json` for benchmark categories and benchmark entries.
- Edit `templates/README.md` for editorial prose, navigation, figures, and section layout.
- Do not directly edit generated tables or lists in `README.md`; regeneration overwrites those changes.

See [the catalog schema](./docs/catalog-schema.md) for field definitions and complete record examples.

## Evidence Requirements

Every new entry needs a primary source. Accepted sources include:

- An arXiv abstract page or publisher landing page for a paper.
- An official project or dataset page.
- The canonical repository owned by the authors or organization.

Search-result snippets, secondary summaries, copied awesome-list descriptions, and model-generated metadata are not sufficient evidence. Verify the exact title, year, destination URL, scientific scope, and claimed workflow coverage before adding an entry.

Prefer a small, well-supported update over a large speculative batch. If an agent's autonomy level is unclear, add its paper to a reading list and leave it out of the taxonomy until the evidence is strong enough.

## Choosing a Taxonomy Level

- **Assistant**: supports bounded tasks under direct human steering.
- **Partner**: coordinates multiple research steps, tools, or feedback loops with meaningful human collaboration.
- **Avatar**: executes long-horizon discovery loops or operates scientific environments with high autonomy.

Set workflow stages only when the paper or official project demonstrates them. Do not infer end-to-end coverage from a broad project name.

## Maintenance Workflow

1. Update the relevant JSON file and, if needed, `templates/README.md`.
2. Run the unit tests and catalog validation.
3. Generate `README.md`.
4. Check that the generated README is current.
5. Review the diff and commit only the intended files.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_catalog.py
python3 scripts/render_readme.py
python3 scripts/render_readme.py --check
git diff --check
git status --short
```

This repository currently uses a single-maintainer, direct-to-`main` workflow. Before pushing directly, confirm the full test suite passes and review the outgoing commits:

```bash
git log --oneline origin/main..main
git diff --stat origin/main..main
git push origin main
```

Never force-push routine catalog maintenance.

## Commit Style

Keep structural work and content refreshes separately auditable. Examples:

```text
refactor: generate catalog from structured data
docs: refresh verified scientific agent catalog
ci: validate catalog and documentation links
```

When correcting factual metadata, summarize the corrected titles or canonical links in the commit body.
