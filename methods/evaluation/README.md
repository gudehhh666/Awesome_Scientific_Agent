# Scientific-Agent Evaluation Methods

Evaluation methods should test both scientific competence and agentic execution. A strong scientific agent is not only a good question-answering model; it must retrieve evidence, operate tools, generate artifacts, and survive long workflows.

## Evaluation Map

| Evaluation angle | What it tests | Example benchmarks or resources | Evidence to collect |
| --- | --- | --- | --- |
| Scientific knowledge and reasoning | Expert-level concepts, domain reasoning, and multi-step inference. | BioMaze, SuperGPQA, Humanity's Last Exam, MR-Ben, SciEval. | Answer accuracy, reasoning trace, domain constraint checks. |
| Literature and citation grounding | Whether claims are supported by real papers and faithful citations. | CiteBench, ALCE, SurveyForge, PaperQA-style tasks. | Source IDs, citation spans, quote-to-claim checks. |
| Code, data, and experiment execution | Whether the agent can implement and run research workflows. | MLAgentBench, DSBench, SciCode, PaperBench. | Code diffs, logs, metrics, artifacts, reproducibility scripts. |
| Domain and embodied environments | Whether the agent works in simulated or physical scientific settings. | DiscoveryWorld, AgentClinic, GenoTEX, LLM-SRBench. | Environment state, action trace, safety checks, task outcome. |
| Long-horizon research quality | Whether the agent can sustain an end-to-end project. | AI Scientist-style systems, Agent Laboratory, CycleResearcher. | Novelty, correctness, reproducibility, review quality, cost. |

## Recommended Evaluation Protocol

1. Define the claim: assistance, partnership, or avatar-level autonomy.
2. Choose tasks that match the claimed research stage.
3. Record the full trajectory: prompts, retrieved sources, tool calls, code, logs, and outputs.
4. Score final outputs and intermediate actions separately.
5. Add human or expert review for scientific validity when automatic metrics are weak.
6. Run ablations for retrieval, memory, tools, and collaboration.
7. Report cost, failures, retries, and safety interventions.

## Red Flags

- The benchmark only scores final text while the system claims autonomous execution.
- Citations are counted as strings but not checked against source content.
- Code is generated but not executed.
- Multi-agent systems are compared against a weak single-agent baseline.
- The system claims discovery without novelty checks, negative results, or expert validation.
