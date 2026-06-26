# Method Guides

This directory expands the main README into short, practical guides for reading scientific-agent methods. Each guide is organized around the survey structure, so readers can move from the high-level taxonomy to concrete implementation and evaluation patterns.

| Guide | Focus | Start here when... |
| --- | --- | --- |
| [Construction](./construction/README.md) | Knowledge organization, knowledge injection, tool use, orchestration, and domain interfaces. | You want to understand how a scientific agent is built. |
| [Enhancement](./enhancement/README.md) | Reasoning, memory, collaboration, reflection, and workflow improvement. | You want to improve an agent beyond a base LLM pipeline. |
| [Evaluation](./evaluation/README.md) | Benchmarks, execution tests, citation grounding, expert review, and long-horizon validation. | You need to compare or stress-test scientific agents. |
| [Auto-Research](./auto-research/README.md) | End-to-end automated research systems and broader agentic repositories. | You want to track systems that connect ideation, coding, experiments, and writing. |

## Reading Order

1. Start with the taxonomy in the repository root to identify the agent role: Assistant, Partner, or Avatar.
2. Read the construction guide to understand the system substrate: what knowledge, tools, prompts, and workflow controller the agent uses.
3. Read the enhancement guide to identify which capabilities are being strengthened.
4. Read the evaluation guide to check whether the reported evidence matches the claimed autonomy.
5. Use the auto-research guide as a watchlist for fast-moving repositories outside narrowly scientific-agent papers.
