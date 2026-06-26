# Scientific-Agent Construction Methods

Construction methods describe how a scientific agent is assembled before it is evaluated: what knowledge it can access, how it injects domain context, which tools it can operate, and how the workflow is coordinated.

## Core Method Map

| Method family | What it does | Typical design choices | Representative resources |
| --- | --- | --- | --- |
| Knowledge organization | Structures scientific information into retrievable and actionable forms. | Literature graphs, concept graphs, paper chunks, experiment logs, domain databases. | GraphRAG, LightRAG, SciAgents, domain knowledge graphs. |
| Knowledge injection | Adapts the base model or prompt context to scientific constraints. | Instruction tuning, retrieval-augmented prompting, domain exemplars, constrained templates. | SciTUNE, InstructBio, Context Engineering. |
| Tool integration | Gives the agent external actions beyond text generation. | Search APIs, code execution, simulation engines, chemistry/biology tools, robotic interfaces. | ChemCrow, OctoTools, FoamAgent, VASPilot. |
| Workflow orchestration | Controls multi-step execution and dependencies. | Planner-executor loops, state machines, graph workflows, multi-agent coordination. | LangGraph, AutoGen, CrewAI, Virtual Lab. |
| Domain interface | Connects the agent to scientific environments and file formats. | Notebook execution, lab automation, CFD/DFT pipelines, bioinformatics scripts. | MetaOpenFoam, StarWhisper, Organa, CellVoyager. |

## Practical Checklist

- Define the target research stage before choosing tools: literature, hypothesis, design, verification, analysis, or evaluation.
- Keep a clear boundary between retrieval, reasoning, and action. This makes failures easier to diagnose.
- Prefer structured tool outputs when possible, especially for code, tables, citations, molecules, proteins, and experiment logs.
- Track provenance for every retrieved claim and every executed action.
- Evaluate the orchestration layer separately from the base model, because many scientific-agent failures come from workflow control rather than language generation alone.

## Common Failure Modes

| Failure mode | Symptom | Mitigation |
| --- | --- | --- |
| Context overload | The agent retrieves many documents but misses the decisive evidence. | Add query decomposition, reranking, and evidence summarization. |
| Tool mismatch | The selected tool cannot solve the actual scientific subtask. | Add tool metadata, input validation, and tool-use demonstrations. |
| Silent execution failure | Code or simulation errors are hidden inside a final answer. | Require logs, exit codes, artifacts, and independent result checks. |
| Weak orchestration | The workflow loops, skips steps, or stops before validation. | Use explicit states, checkpoints, and stop conditions. |
