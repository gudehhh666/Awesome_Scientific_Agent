<div align="center">

# Awesome Scientific Agent

**A curated map of LLM-based agents for automated scientific research.**

[![Survey](https://img.shields.io/badge/Survey-Scientific%20Agents-2f6fed)](#overview)
[![Taxonomy](https://img.shields.io/badge/Taxonomy-{{AGENT_COUNT}}%20Agents-16a34a)](#taxonomy)
[![Benchmarks](https://img.shields.io/badge/Benchmarks-Scientific%20Agent%20Evaluation-f97316)](#benchmarks)
[![Watchlist](https://img.shields.io/badge/Watchlist-Agentic%20Repos-8b5cf6)](#auto-research-watchlist)
[![License](https://img.shields.io/badge/License-Apache--2.0-64748b)](./LICENSE)

[Overview](#overview) • [Taxonomy](#taxonomy) • [Methods](#method-guides) • [Agentic Repos](#auto-research-watchlist) • [Construction](#construction) • [Enhancement](#enhancement) • [Benchmarks](#benchmarks) • [Citation](#citation)

</div>

<!-- Generated from templates/README.md and data/*.json. Do not edit generated catalog sections in README.md directly. -->

<a id="overview"></a>

## ✨ Overview

Large language model agents are becoming a practical interface for AI for Science (AI4S): reading literature, generating hypotheses, designing experiments, operating tools, analyzing results, and reviewing research outputs. This repository organizes the scientific-agent landscape around the research workflow and the autonomy level of each system.

| What this repository maps | How to read it |
| --- | --- |
| **Agent levels** | Assistant, Partner, and Avatar describe increasing autonomy and responsibility in scientific workflows. |
| **Research stages** | Literature, Hypothesis, Design, Verification, Analysis, and Evaluation show where each method contributes. |
| **Agent components** | Reasoning, memory, and collaboration enhancements highlight how systems are built beyond a base LLM. |
| **Evaluation resources** | Benchmarks and datasets help compare scientific-agent capabilities across domains. |

![Scientific agents across the research lifecycle](./figures/overall_short.png)

<a id="reading-map"></a>

## 📖 Reading Map

| Section | Use it for |
| --- | --- |
| [💡 Taxonomy](#taxonomy) | Compare representative scientific agents by level, domain, backbone, capability, components, and research stage. |
| [🧩 Method Guides](#method-guides) | Read focused method notes for construction, enhancement, evaluation, and auto-research systems. |
| [✈️ Scientific Agents Construction](#construction) | Find papers and systems about building agent workflows, prompts, tools, context, and domain interfaces. |
| [🚀 Scientific Agents Enhancement](#enhancement) | Explore reasoning, memory, workflow, and self-improvement techniques for stronger agents. |
| [⚖️ Benchmark For Scientific Agents](#benchmarks) | Locate benchmarks for scientific reasoning, code generation, data analysis, citation, and domain evaluation. |
| [🧭 Broader Agentic & Auto-Research Repositories](#auto-research-watchlist) | Track influential repositories beyond scientific agents, including Karpathy-style training stacks, coding agents, browser agents, and orchestration frameworks. |

<a id="survey-figures"></a>

## 🖼️ Survey Figure Index

The figures below are synchronized from the TPAMI survey materials so the repository mirrors the paper's structure rather than acting only as a paper list.

| Figure | What it explains | Repository file |
| --- | --- | --- |
| Research lifecycle | How scientific agents support literature, hypothesis, design, verification, analysis, and evaluation. | [overall_short.png](./figures/overall_short.png) |
| Survey organization | High-level organization of the survey and repository map. | [overall.png](./figures/overall.png) |
| E/M role taxonomy | Capability envelope and capability maturity, inducing Assistant, Partner, and Avatar roles. | [level.png](./figures/level.png) |
| Extended role view | Additional role-level view used by the survey materials. | [level_2.png](./figures/level_2.png) |
| Construction overview | Agent construction methodology. | [construction_overview.png](./figures/construction_overview.png) |
| Knowledge organization | How scientific agents organize domain knowledge. | [knowledge_organization.png](./figures/knowledge_organization.png) |
| Orchestration | Coordination and workflow orchestration in scientific-agent construction. | [orchestration_flat.png](./figures/orchestration_flat.png) |
| Enhancement overview | Overview of scientific-agent capability enhancement. | [enhancement_overview.png](./figures/enhancement_overview.png) |
| Memory systems | Memory structures for scientific agents. | [memory.png](./figures/memory.png) |
| Reasoning enhancement | Reasoning enhancement patterns for scientific agents. | [reasoning.png](./figures/reasoning.png) |
| Benchmark overview | Scientific-agent benchmark and evaluation metric landscape. | [benchmark_overview.png](./figures/benchmark_overview.png) |

<a id="taxonomy"></a>

## 💡 Taxonomy

![overall](./figures/level.png)

{{GENERATED_TAXONOMY}}

### Level 1: Agent As Assistant

<details open>
<summary><b>Level 1: Agent as Assistant - bounded task support and domain-specific assistance</b></summary>

{{GENERATED_ASSISTANT_RESOURCES}}

</details>

### Level 2: Agent As Partner

<details open>
<summary><b>Level 2: Agent as Partner - multi-step collaboration and workflow orchestration</b></summary>

{{GENERATED_PARTNER_RESOURCES}}

</details>

### Level 3: Agent As Avatar

<details open>
<summary><b>Level 3: Agent as Avatar - autonomous research execution and long-horizon discovery</b></summary>

{{GENERATED_AVATAR_RESOURCES}}

</details>

<a id="method-guides"></a>

## 🧩 Method Guides

The root README keeps the curated map compact; the method guides provide deeper explanations for readers who want to understand how scientific agents are built, improved, evaluated, and connected to broader auto-research systems.

| Guide | What it covers |
| --- | --- |
| [Construction Methods](./methods/construction/README.md) | Knowledge organization, knowledge injection, tool integration, orchestration, and domain interfaces. |
| [Enhancement Methods](./methods/enhancement/README.md) | Reasoning, memory, collaboration, workflow search, and self-review. |
| [Evaluation Methods](./methods/evaluation/README.md) | Benchmark selection, executable evaluation, citation grounding, and long-horizon validation. |
| [Auto-Research Systems](./methods/auto-research/README.md) | End-to-end research loops, coding/browser agents, training resources, and orchestration frameworks. |

<a id="auto-research-watchlist"></a>

## 🧭 Broader Agentic & Auto-Research Repositories

Beyond scientific-agent papers, the broader agent ecosystem is moving quickly across model training, software engineering, web automation, and multi-agent orchestration. This watchlist keeps a lightweight bridge from the survey taxonomy to practical repositories that shape how autonomous research and agentic systems are built.

{{GENERATED_WATCHLIST}}

<a id="construction"></a>

## ✈️ Scientific Agents Construction

<p align="center">
  <img src="./figures/construction_overview.png" alt="Agent construction methodology" width="95%">
</p>

<p align="center">
  <img src="./figures/knowledge_organization.png" alt="Knowledge organization in scientific agents" width="47%">
  <img src="./figures/orchestration_flat.png" alt="Orchestration and coordination in scientific-agent construction" width="47%">
</p>

<details open>
<summary><b>Construction resources - prompts, context, tools, workflows, and domain interfaces</b></summary>

{{GENERATED_CONSTRUCTION}}

</details>

<a id="enhancement"></a>

## 🚀 Scientific Agents Enhancement

<p align="center">
  <img src="./figures/enhancement_overview.png" alt="Scientific-agent ability enhancement" width="95%">
</p>

<p align="center">
  <img src="./figures/memory.png" alt="Scientific agents' memory systems" width="47%">
  <img src="./figures/reasoning.png" alt="Illustration of scientific agent reasoning enhancement" width="47%">
</p>

<details open>
<summary><b>Enhancement resources - reasoning, memory, workflow search, reflection, and collaboration</b></summary>

{{GENERATED_ENHANCEMENT}}

</details>

<a id="benchmarks"></a>

## ⚖️ Benchmark For Scientific Agents

Use this section as an evaluation map rather than a flat benchmark list. The resources below cover different failure modes of scientific agents: domain knowledge, executable experiments, citation grounding, data analysis, and long-horizon discovery.

<p align="center">
  <img src="./figures/benchmark_overview.png" alt="Scientific-agent benchmark and evaluation landscape" width="95%">
</p>

{{GENERATED_BENCHMARKS}}

<a id="citation"></a>

## 🌞 Citation

```
@article{wang2025hitchhiker,
  title={The Hitchhiker's Guide to Autonomous Research: A Survey of Scientific Agents},
  author={Wang, Xinming and Xu, Jian and Feng, Aslan H and Chen, Yi and Guo, Haiyang and Zhu, Fei and Shao, Yuanqi and Ren, Minsi and Yi, Hongzhu and Lian, Sheng and others},
  year={2025}
}
```
