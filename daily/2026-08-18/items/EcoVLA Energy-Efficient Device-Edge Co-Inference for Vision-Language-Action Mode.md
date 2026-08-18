---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15502v1"
published: "2026-08-16T03:08:40Z"
age_days: 1
score: 32
created: 2026-08-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints

> [!summary] 一句话结论（基于摘要）
> Experimental results across VLA models show that EcoVLA improves system energy efficiency by up to 236% over existing co-inference approaches under a 20 Hz action output frequency constraint, while consistently maintaining SLO satisfaction under dynamic netwo…

## 关键点

- **问题**：Vision-Language-Action (VLA) models have emerged as a promising foundation for Embodied AI, but their high inference cost poses significant challenges for deployment in robotic systems.
- **创新点 / 方法**：Thus, we propose EcoVLA, an adaptive device-edge co-inference framework for VLA models that maximizes system energy efficiency under real-time constraints.
- **证据**：Experimental results across VLA models show that EcoVLA improves system energy efficiency by up to 236% over existing co-inference approaches under a 20 Hz action output frequency constraint, while consistently maintaining SLO satisfaction under dynamic network and edge workload conditions.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/EcoVLA Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Mode.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have emerged as a promising foundation for Embodied AI, but their high inference cost poses significant challenges for deployment in robotic systems. In practice, on-device inference is constrained by limited compute capacity and energy budgets, struggling to simultaneously satisfy real-time control and energy efficiency requirements. Alternatively, offloading the inference workload to an edge server is susceptible to fluctuations in system conditions, introducing unpredictable latency risks. Device-edge co-inference offers a promising solution, but systematic research tailored to VLA models remains scarce, particularly a unified co-inference framework that jointly addresses real-time constraints and system-level energy efficiency. Thus, we propose EcoVLA, an adaptive device-edge co-inference framework for VLA models that maximizes system energy efficiency under real-time constraints. EcoVLA first introduces a unified stage-level abstraction over different VLA paradigms, establishing an architecture-agnostic co-inference design space. It then formulates a joint device-edge-network latency and energy prediction model to enable rapid runtime evaluation of candidate co-inference schemes. Building on this, EcoVLA continuously selects the energy-optimal scheme satisfying real-time constraints with millisecond-level overhead, adapting to runtime variations in network and system states. Furthermore, EcoVLA incorporates a lightweight transmission mechanism for inter-stage intermediate tensors to reduce the communication overhead incurred by cross-device collaboration. Experimental results across VLA models show that EcoVLA improves system energy efficiency by up to 236% over existing co-inference approaches under a 20 Hz action output frequency constraint, while consistently maintaining SLO satisfaction under dynamic network and edge workload conditions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15502v1
- Authors: Ao Zhou, Bo Dai, Le Yu, Xingyu Liu, Zeyu Hao, Lingkun Long, Chunming Hu, Jianlei Yang
- Published: 2026-08-16T03:08:40Z
- Age days: 1

</details>
