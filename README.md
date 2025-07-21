# Awesome-Scientific-Agent

## ✨ Introduction

The advancement of LLM-based agents heralds a new perspective for AI for Science (AI4S), automation science research. Prominent large language models have exhibited expertise across multiple domains, prompting researchers to develop agents for the natural sciences and investigate the frontiers of scientific knowledge. Nevertheless, the divergences between the natural sciences and AI have hindered the development and advancement of scientific agents across various fields. This survey is grounded in the standardized scientific research process and elucidates the construction and evaluation of scientific agents.

* We elucidate the objective orientation of scientific research agents, which directly guides the construction for scientific agents.
* We systematically taxonomizing existing scientific research agents into three levels, with show strong hierarchical characteristics in terms of construction strategy and capability scope.
* We provides substantial and detailed answers to the questions of "how to construct a scientific agent from scratch" and "how to enhance the capabilities of existing scientific agents".

![overall](./figures/overall_short.drawio.svg)

## 📖 Framework

  * [Taxonomy](#Taxonomy)
  * [Scientific Agent Construction](#scientific-agent-construction)
  * [Scientific Agent Enhancement](#scientific-agent-enhancement)
  * [Benchmarks For Scientific Agent](#benchmark-for-scientific-agent)

## 💡Taxonomy

![overall](./figures/level.png)

### Level 1: Agent As Assistant

- **AstroLLaMA‑Chat: Scaling AstroLLaMA with Conversational and Diverse Datasets** — [![](https://img.shields.io/badge/arXiv-2024.01-red)](https://arxiv.org/abs/2401.01916)
- **BioGPT: Generative Pre‑trained Transformer for Biomedical Text Generation and Mining** — [![img](https://img.shields.io/badge/arXiv-2022.10-red)](https://arxiv.org/abs/2210.10341)
- **DARWIN 1.5: Large Language Models as Materials‑Science Foundation Models** — [![img](https://img.shields.io/badge/arXiv-2024.12-red)](https://arxiv.org/abs/2412.11970)
- **ChemBERTa: Large‑Scale Self‑Supervised Pre‑training for Molecular Property Prediction** — [![img](https://img.shields.io/badge/arXiv-2020.10-red)](https://arxiv.org/abs/2010.09885)
- **ChemAU: Harness the Reasoning of LLMs in Chemical Research with Adaptive Uncertainty Estimation** — [![img](https://img.shields.io/badge/arXiv-2025.06-red)](https://arxiv.org/abs/2506.01116)
- **ChemDFM: A Large Language Foundation Model for Chemistry** — [![img](https://img.shields.io/badge/arXiv-2024.01-red)](https://arxiv.org/abs/2401.14818)
- **LlaSMol: Advancing Large Language Models for Chemistry with a Large‑Scale, Comprehensive, High‑Quality Instruction Tuning Dataset** — [![img](https://img.shields.io/badge/arXiv-2024.02-red)](https://arxiv.org/abs/2402.09391)
- **InstructMol: Multi‑modal Integration for Building a Versatile and Reliable Molecular Assistant in Drug Discovery** — [![img](https://img.shields.io/badge/arXiv-2023.11-red)](https://arxiv.org/abs/2311.16208)
- **ether0: A Scientific Reasoning Model for Chemistry** — [![img](https://img.shields.io/badge/arXiv-2025.06-red)](https://arxiv.org/abs/2506.17238)
- **Leveraging Large Language Models for Predictive Chemistry** — [![img](https://img.shields.io/badge/Nature-2024.02-blue)](https://www.nature.com/articles/s42256-023-00788-1) 
- **Multi‑modal Molecule Structure–Text Model for Text‑based Retrieval and Editing** — [![img](https://img.shields.io/badge/Nature-2023.12-blue)](https://www.nature.com/articles/s42256-023-00759-6)
- **ClimateGPT: Towards AI Synthesizing Interdisciplinary Research on Climate Change** — [![img](https://img.shields.io/badge/arXiv-2024.01-red)](https://arxiv.org/abs/2401.09646)
- **Sparks of Science: Hypothesis Generation Using Structured Paper Data** — [![img](https://img.shields.io/badge/arXiv-2025.04-red)](https://arxiv.org/abs/2504.12976)
- **DeepSeek‑Prover‑V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition** — [![img](https://img.shields.io/badge/arXiv-2025.04-red)](https://arxiv.org/abs/2504.21801)
- **BiMediX: Bilingual Medical Mixture of Experts LLM** — [![img](https://img.shields.io/badge/arXiv-2024.02-red)](https://arxiv.org/abs/2402.13253)
- **ChatDoctor: A Medical Chat Model Fine‑tuned on a Large Language Model (LLAMA) Using Medical Domain Knowledge** — [![img](https://img.shields.io/badge/arXiv-2023.03-red)](https://arxiv.org/abs/2303.14070)
- **AgentMD: Empowering Language Agents for Risk Prediction with Large‑Scale Clinical Tool Learning** — [![img](https://img.shields.io/badge/arXiv-2024.02-red)](https://arxiv.org/abs/2402.13225)
- **MedAlpaca: An Open‑Source Collection of Medical Conversational AI Models and Training Data** — [![img](https://img.shields.io/badge/arXiv-2023.04-red)](https://arxiv.org/abs/2304.08247)
- **DrugGen Enhances Drug Discovery with Large Language Models and Reinforcement Learning** — [![img](https://img.shields.io/badge/Nature-2025.04-blue)](https://www.nature.com/articles/s41598-025-98629-1) 
- **LLM‑SR: Scientific Equation Discovery via Programming with Large Language Models** — [![img](https://img.shields.io/badge/arXiv-2024.04-red)](https://arxiv.org/abs/2404.18400)
- **LitLLM: A Toolkit for Scientific Literature Review** — [![img](https://img.shields.io/badge/arXiv-2024.02-red)](https://arxiv.org/abs/2402.01788)
- **SciBERT: A Pretrained Language Model for Scientific Text** — [![img](https://img.shields.io/badge/arXiv-2019.03-red)](https://arxiv.org/abs/1903.10676)
- **SciMON: Scientific Inspiration Machines Optimized for Novelty** — [![](https://img.shields.io/badge/arXiv-2023.05-red)](https://arxiv.org/abs/2305.14259)
- **SCITUNE: Aligning Large Language Models with Scientific Multimodal Instructions** — [![img](https://img.shields.io/badge/arXiv-2023.07-red)](https://arxiv.org/abs/2307.01139)
- **NatureLM: Deciphering the Language of Nature for Scientific Discovery** — [![img](https://img.shields.io/badge/arXiv-2025.02-red)](https://arxiv.org/abs/2502.07527)

### Level 2: Agent As Partner

- **StarWhisper Telescope: Agent‑Based Observation Assistant System to Approach an AI Astrophysicist** — [![img](https://img.shields.io/badge/arXiv-2024.12-red)](https://arxiv.org/abs/2412.06412)
- **From Intention to Implementation: Automating Biomedical Research via LLMs** — [![img](https://img.shields.io/badge/arXiv-2024.12-red)](https://arxiv.org/abs/2412.09429)
- **CRISPR‑GPT: An LLM Agent for Automated Design of Gene‑Editing Experiments** — [![img](https://img.shields.io/badge/arXiv-2024.04-red)](https://arxiv.org/abs/2404.18021)
- **Towards an AI Co‑Scientist** — [![img](https://img.shields.io/badge/arXiv-2025.02-red)](https://arxiv.org/abs/2502.18864)
- **DrBioRight 2.0: An LLM‑Powered Bioinformatics Chatbot for Large‑Scale Cancer Functional Proteomics Analysis** — [![img](https://img.shields.io/badge/Nature-2025.03-blue)](https://www.nature.com/articles/s41467-025-57430-4)
- **ProtAgents: Protein Discovery via Large Language Model Multi‑Agent Collaboration** — [![img](https://img.shields.io/badge/arXiv-2024.02-red)](https://arxiv.org/abs/2402.04268)
- **MOOSE‑Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses** — [![img](https://img.shields.io/badge/arXiv-2024.10-red)](https://arxiv.org/abs/2410.07076)
- **Autonomous Chemical Research with Large Language Models** — [![img](https://img.shields.io/badge/Nature-2023.12-blue)](https://www.nature.com/articles/s41586-023-06792-0)
- **ChemCrow: Augmenting Large‑Language Models with Chemistry Tools** — [![img](https://img.shields.io/badge/arXiv-2023.04-red)](https://arxiv.org/abs/2304.05376)
- **ORGANA: A Robotic Assistant for Automated Chemistry Experimentation and Characterization** — [![img](https://img.shields.io/badge/arXiv-2024.01-red)](https://arxiv.org/abs/2401.06949)
- **xChemAgents: Agentic AI for Explainable Quantum Chemistry** — [![img](https://img.shields.io/badge/arXiv-2025.05-red)](https://arxiv.org/abs/2505.20574)
- **ChemAgent: Self‑Updating Memories in Large Language Models Improves Chemical Reasoning** — [![img](https://img.shields.io/badge/arXiv-2025.01-red)](https://arxiv.org/abs/2501.06590)
- **Large Language Models to Accelerate Organic Chemistry Synthesis** — [![img](https://img.shields.io/badge/arXiv-2025.04-red)](https://arxiv.org/abs/2504.18340)
- **MyCrunchGPT: A ChatGPT‑Assisted Framework for Scientific Machine Learning** — [![img](https://img.shields.io/badge/arXiv-2023.06-red)](https://arxiv.org/abs/2306.15551)
- **MetaOpenFoam: An LLM‑Based Multi‑Agent Framework for CFD** — [![img](https://img.shields.io/badge/arXiv-2024.07-red)](https://arxiv.org/abs/2407.21320)
- **FoamAgent: Towards Automated Intelligent CFD Workflows** — [![img](https://img.shields.io/badge/arXiv-2025.05-red)](https://arxiv.org/abs/2505.04997)
- **AI‑Researcher: Autonomous Scientific Innovation** — [![img](https://img.shields.io/badge/arXiv-2025.05-red)](https://arxiv.org/abs/2505.18705)
- **Jupybara: Operationalizing a Design Space for Actionable Data Analysis and Storytelling with LLMs** — [![img](https://img.shields.io/badge/arXiv-2025.01-red)](https://arxiv.org/abs/2501.16661)
- **FlowAgent: Achieving Compliance and Flexibility for Workflow Agents** — [![img](https://img.shields.io/badge/arXiv-2025.02-red)](https://arxiv.org/abs/2502.14345)
- **The AI Scientist: Towards Fully Automated Open‑Ended Scientific Discovery** — [![img](https://img.shields.io/badge/arXiv-2024.08-red)](https://arxiv.org/abs/2408.06292)
- **GeoGPT: Understanding and Processing Geospatial Tasks through an Autonomous GPT** — [![img](https://img.shields.io/badge/arXiv-2023.07-red)](https://arxiv.org/abs/2307.07930)
- **PaperQA: Retrieval‑Augmented Generative Agent for Scientific Research** — [![img](https://img.shields.io/badge/arXiv-2023.12-red)](https://arxiv.org/abs/2312.07559)
- **ChatCite: LLM Agent with Human Workflow Guidance for Comparative Literature Summary** — [![img](https://img.shields.io/badge/arXiv-2024.03-red)](https://arxiv.org/abs/2403.02574)
- **PiFlow: Principle‑Aware Scientific Discovery with Multi‑Agent Collaboration** — [![img](https://img.shields.io/badge/arXiv-2025.05-red)](https://arxiv.org/abs/2505.15047)
- **Aviary: Training Language Agents on Challenging Scientific Tasks** — [![img](https://img.shields.io/badge/arXiv-2024.12-red)](https://arxiv.org/abs/2412.21154)
- **An Autonomous Laboratory for the Accelerated Synthesis of Novel Materials** — [![img](https://img.shields.io/badge/Nature-2023.12-blue)](https://pubmed.ncbi.nlm.nih.gov/38030721/)
- **Construction of a Knowledge Graph for Framework Material Enabled by Large Language Models and Its Application** — [![img](https://img.shields.io/badge/npjCM-2025.02-blue)](https://www.nature.com/articles/s41524-025-01540-6)
- **MultiCrossModal Automated Agent for Integrating Diverse Materials Science Data** — [![img](https://img.shields.io/badge/arXiv-2025.05-red)](https://arxiv.org/abs/2505.15132)
- **LLMatDesign: Autonomous Materials Discovery with Large Language Models** — [![img](https://img.shields.io/badge/arXiv-2024.06-red)](https://arxiv.org/abs/2406.13163)
- **Honeycomb: A Flexible LLM‑Based Agent System for Materials Science** — [![img](https://img.shields.io/badge/arXiv-2024.09-red)](https://arxiv.org/abs/2409.00135)
- **DrugAgent: Automating AI‑Aided Drug Discovery Programming through LLM Multi‑Agent Collaboration** — [![img](https://img.shields.io/badge/arXiv-2024.11-red)](https://arxiv.org/abs/2411.15692)
- **Toward a Team of AI‑Made Scientists for Scientific Discovery from Gene Expression Data** — [![img](https://img.shields.io/badge/arXiv-2024.02-red)](https://arxiv.org/abs/2402.12391)
- **MedAgents: Large Language Models as Collaborators for Zero‑Shot Medical Reasoning** — [![img](https://img.shields.io/badge/arXiv-2023.11-red)](https://arxiv.org/abs/2311.10537)
- **Automation of Systematic Reviews with Large Language Models** — [![img](https://img.shields.io/badge/medRxiv-2025.06-blue)](https://www.medrxiv.org/content/10.1101/2025.06.13.25329541v2)
- **MRAgent: An LLM‑Based Automated Agent for Causal Knowledge Discovery in Disease via Mendelian Randomization** — [![img](https://img.shields.io/badge/BriefBioinf-2025.03-blue)](https://academic.oup.com/bib/article/26/2/bbaf140/8107848)
- **GeneGPT: Augmenting Large Language Models with Domain Tools for Improved Access to Biomedical Information** — [![img](https://img.shields.io/badge/arXiv-2023.04-red)](https://arxiv.org/abs/2304.09667)

### Level 3: Agent As Avatar

- **CycleResearcher: Improving Automated Research via Automated Review** — [![img](https://img.shields.io/badge/arXiv-2024.11-red)](https://arxiv.org/abs/2411.00816)
- **The AI Scientist‑v2: Workshop‑Level Automated Scientific Discovery via Agentic Tree Search** — [![img](https://img.shields.io/badge/arXiv-2025.04-red)](https://arxiv.org/abs/2504.08066)
- **AgentRxiv: Towards Collaborative Autonomous Research** — [![img](https://img.shields.io/badge/arXiv-2025.03-red)](https://arxiv.org/abs/2503.18102)
- **Agent Laboratory: Using LLM Agents as Research Assistants** — [![img](https://img.shields.io/badge/arXiv-2025.01-red)](https://arxiv.org/abs/2501.04227)
- **BiOMNI: A General‑Purpose Biomedical AI Agent** — [![img](https://img.shields.io/badge/bioRxiv-2025.05-blue)](https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1)
- **OriGene: A Self‑Evolving Virtual Disease Biologist Automating Therapeutic Target Discovery** — [![img](https://img.shields.io/badge/bioRxiv-2025.06-blue)](https://www.biorxiv.org/content/10.1101/2025.06.03.657658v1)
- **CellVoyager: AI CompBio Agent Generates New Insights by Autonomously Analyzing Biological Data** — [![img](https://img.shields.io/badge/bioRxiv-2025.06-blue)](https://www.biorxiv.org/content/10.1101/2025.06.03.657517v1)
- **Sparks: Multi‑Agent Artificial Intelligence Model Discovers Protein Design Principles** — [![img](https://img.shields.io/badge/arXiv-2025.04-red)](https://arxiv.org/abs/2504.19017)
- **AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery** — [![img](https://img.shields.io/badge/arXiv-2025.06-red)](https://arxiv.org/abs/2506.13131)
- **Robin: A Multi‑Agent System for Automating Scientific Discovery** — [![img](https://img.shields.io/badge/arXiv-2025.05-red)](https://arxiv.org/abs/2505.13400)

## ✈️ Scientific Agent Construction

![overall](./figures/section3.drawio.svg)

- **SciTUNE: Aligning Large Language Models with Scientific Multimodal Instructions** — [![img](https://img.shields.io/badge/arXiv-2023.07-red)](https://arxiv.org/abs/2307.01139)
- **ClimateGPT: Towards AI Synthesizing Interdisciplinary Research on Climate Change** — [![img](https://img.shields.io/badge/arXiv-2024.01-red)](https://arxiv.org/abs/2401.09646)
- **SciMON: Scientific Inspiration Machines Optimized for Novelty** — [![img](https://img.shields.io/badge/arXiv-2023.05-red)](https://arxiv.org/abs/2305.14259)
- **TAIS: Gene Expression Agent with LLMs** — [![img](https://img.shields.io/badge/arXiv-2025.03-red)](https://arxiv.org/abs/2503.02973)
- **StarWhisper Telescope: Agent‑Based Observation Assistant System to Approach an AI Astrophysicist** — [![img](https://img.shields.io/badge/arXiv-2024.12-red)](https://arxiv.org/abs/2412.06412)
- **PromptAgent** — [![img](https://img.shields.io/badge/GitHub-PromptAgent-green)](https://github.com/OpenBMB/PromptAgent)
- **AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts** — [![img](https://img.shields.io/badge/arXiv-2020.10-red)](https://arxiv.org/abs/2010.15980)
- **Context Engineering** — [![img](https://img.shields.io/badge/GitHub-Context--Engineering-green)](https://github.com/davidkimai/Context-Engineering)
- **LlamaIndex** — [![img](https://img.shields.io/badge/GitHub-LlamaIndex-green)](https://github.com/jerryjliu/llama_index)
- **OpenRLHF** — [![img](https://img.shields.io/badge/GitHub-OpenRLHF-green)](https://github.com/OpenLMLab/OpenRLHF)
- **LLaMA-Factory** — [![img](https://img.shields.io/badge/GitHub-LLaMA--Factory-green)](https://github.com/hiyouga/LLaMA-Factory)
- **ChemCrow: Augmenting Large‑Language Models with Chemistry Tools** — [![img](https://img.shields.io/badge/arXiv-2023.04-red)](https://arxiv.org/abs/2304.05376)
- **MetaOpenFoam: An LLM-Based Multi-Agent Framework for CFD** — [![img](https://img.shields.io/badge/arXiv-2024.07-red)](https://arxiv.org/abs/2407.21320)
- **FoamAgent: Towards Automated Intelligent CFD Workflows** — [![img](https://img.shields.io/badge/arXiv-2025.05-red)](https://arxiv.org/abs/2505.04997)
- **Virtual Lab** — [![img](https://img.shields.io/badge/arXiv-2024.04-red)](https://arxiv.org/abs/2404.12699)
- **OctoTools** — [![img](https://img.shields.io/badge/GitHub-OctoTools-green)](https://github.com/LIANGZIMO/OctoTools)

## 🚀 Scientific Agent Enhancement

- **MemGPT** — [![img](https://img.shields.io/badge/arXiv-2023.10-red)](https://arxiv.org/abs/2310.08572)
- **AFlow: Memory-Augmented Agent for Scientific Workflows** — [![img](https://img.shields.io/badge/arXiv-2023.07-red)](https://arxiv.org/abs/2307.02933)
- **ChemAgent: Self-Updating Memories in Large Language Models Improves Chemical Reasoning** — [![img](https://img.shields.io/badge/arXiv-2025.01-red)](https://arxiv.org/abs/2501.06590)
- **DeepSeek‑Prover‑V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition** — [![img](https://img.shields.io/badge/arXiv-2025.04-red)](https://arxiv.org/abs/2504.21801)
- **LLM‑SR: Scientific Equation Discovery via Programming with LLMs** — [![img](https://img.shields.io/badge/arXiv-2024.04-red)](https://arxiv.org/abs/2404.18400)
- **Sparks: Multi-Agent Artificial Intelligence Model Discovers Protein Design Principles** — [![img](https://img.shields.io/badge/arXiv-2025.04-red)](https://arxiv.org/abs/2504.19017)
- **ether0: A Scientific Reasoning Model for Chemistry** — [![img](https://img.shields.io/badge/arXiv-2025.06-red)](https://arxiv.org/abs/2506.17238)
- **Robin: A Multi-Agent System for Automating Scientific Discovery** — [![img](https://img.shields.io/badge/arXiv-2025.05-red)](https://arxiv.org/abs/2505.13400)
- **AgentRxiv: Towards Collaborative Autonomous Research** — [![img](https://img.shields.io/badge/arXiv-2025.03-red)](https://arxiv.org/abs/2503.18102)
- **ChatGPT Research Group** — [![img](https://img.shields.io/badge/arXiv-2024.06-red)](https://arxiv.org/abs/2406.07800)
- **AI Co-Scientist** — [![img](https://img.shields.io/badge/arXiv-2025.03-red)](https://arxiv.org/abs/2503.12984)

![overall](./figures/section4.drawio.svg)

## ⚖️ Benchmark For Scientific Agent
- **ScienceQA: A Dataset for Multimodal Science Question Answering** — [![img](https://img.shields.io/badge/arXiv-2022.10-red)](https://arxiv.org/abs/2210.01904)
- **MMLU-Pro: A Professional-Level Multidisciplinary Benchmark for LLMs** — [![img](https://img.shields.io/badge/arXiv-2024.01-red)](https://arxiv.org/abs/2401.12357)
- **SciCap** — [![img](https://img.shields.io/badge/GitHub-SciCap-green)](https://github.com/OpenBMB/SciCap)
- **ALaS: Agent Learning and Simulation Benchmark** — [![img](https://img.shields.io/badge/GitHub-AlaS-green)](https://github.com/AILab-CVC/ALaS)
- **AgentBoard** — [![img](https://img.shields.io/badge/arXiv-2024.03-red)](https://arxiv.org/abs/2403.11289)
- **DeepSeek-Prover Benchmark** — [![img](https://img.shields.io/badge/arXiv-2025.04-red)](https://arxiv.org/abs/2504.21801)

## 🌞 Citation
