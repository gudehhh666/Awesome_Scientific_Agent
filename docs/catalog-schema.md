# Catalog Schema

The public catalog is generated from three JSON files in `data/`. This document defines their schema and the validation rules enforced by `scripts/catalog.py`.

## Shared Rules

Every record has a globally unique `id` in lowercase kebab case:

```text
^[a-z0-9]+(?:-[a-z0-9]+)*$
```

IDs are stable identifiers, not display labels. Do not rename an ID solely because capitalization or punctuation in a title changes.

All links use this shape:

```json
{
  "kind": "paper",
  "label": "paper",
  "url": "https://arxiv.org/abs/2603.08127"
}
```

Allowed link kinds are `paper`, `code`, `project`, `dataset`, and `website`. URLs must be absolute HTTPS destinations. Generic destinations such as `https://arxiv.org/` and `https://arxiv.org/abs/` are rejected.

Within a section, normalized titles and destination URLs must be unique. A paper may appear in different sections when it serves different reading paths, but each appearance needs a distinct stable ID.

## `data/agents.json`

Top-level fields:

| Field | Type | Meaning |
| --- | --- | --- |
| `schema_version` | integer | Must be `1`. |
| `taxonomy` | array | Scientific-agent capability records. |
| `reading_lists` | object | Exactly `assistant`, `partner`, and `avatar` arrays. |

### Taxonomy record

```json
{
  "id": "agent-evoscientist",
  "name": "EvoScientist",
  "level": "Avatar",
  "domain": "Computer Science",
  "backbone": "General-purpose",
  "capability_envelope": "E3",
  "capability_maturity": "M2",
  "reasoning": "Yes",
  "memory": "Yes",
  "collaboration": "Yes",
  "stages": [
    "Literature",
    "Hypothesis",
    "Design",
    "Verification",
    "Analysis",
    "Evaluation"
  ],
  "description": "Self-evolving multi-agent end-to-end discovery"
}
```

Controlled values:

- `level`: `Assistant`, `Partner`, or `Avatar`.
- `capability_envelope`: `E1`, `E2`, or `E3`.
- `capability_maturity`: `M1`, `M2`, or `M3`.
- `reasoning`, `memory`, and `collaboration`: `Yes` or `No`.
- `stages`: one or more of `Literature`, `Hypothesis`, `Design`, `Verification`, `Analysis`, and `Evaluation`.

### Reading-list record

```json
{
  "id": "reading-avatar-evoscientist",
  "title": "EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery",
  "venue": "arXiv",
  "year": 2026,
  "links": [
    {
      "kind": "paper",
      "label": "paper",
      "url": "https://arxiv.org/abs/2603.08127"
    },
    {
      "kind": "code",
      "label": "code",
      "url": "https://github.com/EvoScientist/EvoScientist"
    }
  ]
}
```

`title` and `venue` must be non-empty. `year` is an integer between 1900 and 2100. At least one link is required.

## `data/resources.json`

Top-level fields are `schema_version`, `watchlist`, `construction`, and `enhancement`.

Construction and enhancement records use the reading-list record shape above.

### Watchlist record

```json
{
  "id": "watch-evoscientist",
  "repository": "EvoScientist/EvoScientist",
  "scope": "Self-evolving end-to-end AI scientist",
  "rationale": "Tracks persistent research memory, multi-agent experimentation, and human-on-the-loop research workflows.",
  "links": [
    {
      "kind": "project",
      "label": "repository",
      "url": "https://github.com/EvoScientist/EvoScientist"
    }
  ]
}
```

`repository`, `scope`, and `rationale` must be non-empty. The first link is used for the repository name in the generated table.

## `data/benchmarks.json`

Top-level fields:

| Field | Type | Meaning |
| --- | --- | --- |
| `schema_version` | integer | Must be `1`. |
| `evaluation_angles` | array | Defines the benchmark dashboard categories. |
| `items` | array | Benchmark records. |

### Evaluation-angle record

```json
{
  "id": "code-data-and-experiment-execution",
  "name": "Code, data, and experiment execution",
  "focus": "MLAgentBench, DSBench, SciCode, PaperBench",
  "use_when": "Whether an agent can implement, run, debug, and reproduce research workflows."
}
```

### Benchmark record

```json
{
  "id": "benchmark-dsagentbench",
  "title": "DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?",
  "venue": "arXiv",
  "year": 2026,
  "links": [
    {
      "kind": "paper",
      "label": "paper",
      "url": "https://arxiv.org/abs/2608.10366"
    },
    {
      "kind": "code",
      "label": "code",
      "url": "https://github.com/vis-nlp/DSAgentBench"
    }
  ],
  "evaluation_angle": "code-data-and-experiment-execution"
}
```

`evaluation_angle` must match the ID of an evaluation-angle record in the same file.

## Generation and Validation

Run the complete local maintenance loop from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_catalog.py
python3 scripts/render_readme.py
python3 scripts/render_readme.py --check
```

`README.md` is a generated artifact. Edit `templates/README.md` for prose or layout changes and edit the JSON catalogs for repeated content.
