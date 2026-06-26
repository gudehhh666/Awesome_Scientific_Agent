# Scientific-Agent Enhancement Methods

Enhancement methods strengthen an agent after the basic construction layer is in place. They target reasoning reliability, memory, collaboration, reflection, and self-improvement.

## Capability Families

| Enhancement family | Goal | Common techniques | What to inspect |
| --- | --- | --- | --- |
| Reasoning enhancement | Improve multi-step scientific inference. | Chain-of-thought style decomposition, self-consistency, symbolic deduction, domain rules, theorem or equation checks. | Does the reasoning path preserve scientific constraints and units? |
| Memory enhancement | Preserve useful state across long tasks. | Working memory, episodic memory, vector memory, structured experiment logs, self-updating memories. | Is memory grounded in evidence, or does it amplify previous mistakes? |
| Collaboration enhancement | Coordinate multiple roles or agents. | PI-student roles, critic-reviewer loops, specialist agents, debate, division of labor. | Are roles actually complementary, or just repeated prompts? |
| Workflow search | Improve the agent process itself. | Automated prompt search, tree search, evolutionary workflows, reflection-driven repair. | Is the search evaluated on held-out tasks? |
| Self-review and repair | Catch errors before final output. | Review agents, unit tests, citation checks, execution replay, verifier models. | Does the verifier have access to independent evidence? |

## How to Read Enhancement Papers

1. Identify which capability is being improved: reasoning, memory, collaboration, or workflow control.
2. Check whether the paper separates base-model gains from agent-design gains.
3. Look for ablations that remove memory, tools, reviewers, retrieval, or multi-agent roles.
4. Prefer evidence that includes executable artifacts, not only final text quality.
5. Check whether the enhancement helps long-horizon tasks or only short benchmark prompts.

## Design Notes

- Reasoning methods are most useful when the task has explicit constraints, such as equations, reaction rules, statistical tests, or protocol steps.
- Memory methods should store observations, decisions, artifacts, and citations separately; mixing them makes later verification hard.
- Collaboration methods need role-specific permissions and outputs. Without that, multi-agent systems often become expensive paraphrasing loops.
- Reflection methods should trigger concrete repairs, such as rerunning code, changing a hypothesis, updating a plan, or asking for missing evidence.
