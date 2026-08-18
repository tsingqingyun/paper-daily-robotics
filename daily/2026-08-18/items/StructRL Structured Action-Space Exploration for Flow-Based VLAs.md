---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15139v1"
published: "2026-08-15T09:31:29Z"
age_days: 2
score: 41
created: 2026-08-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# StructRL: Structured Action-Space Exploration for Flow-Based VLAs

> [!summary] 一句话结论（基于摘要）
> We show that simply switching the in-chain noise to a structured form does not suffice: noise added at an intermediate flow time can be weakened by the remaining denoising steps before execution, a phenomenon we call \emph{Structured Noise Dilution}.

## 关键点

- **问题**：However, effective robot exploration calls for structured noise: temporally smooth and scaled differently across action groups.
- **创新点 / 方法**：We propose \textbf{StructRL}, which avoids dilution by relocating policy stochasticity to the action space via three coupled choices: (i) a deterministic ODE decoder, (ii) structured noise injected directly in the action space, and (iii) last-step replay, where policy-gradient updates avoid assigning likelihoods to in…
- **证据**：We show that simply switching the in-chain noise to a structured form does not suffice: noise added at an intermediate flow time can be weakened by the remaining denoising steps before execution, a phenomenon we call \emph{Structured Noise Dilution}.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/StructRL Structured Action-Space Exploration for Flow-Based VLAs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Flow-based Vision-Language-Action (VLA) models are now widely used for continuous robotic manipulation, and online reinforcement learning (RL) is emerging as a key technique for adapting them to new tasks. Existing RL methods typically inject stochasticity inside the denoising chain, often through isotropic or temporally independent noise. However, effective robot exploration calls for structured noise: temporally smooth and scaled differently across action groups. We show that simply switching the in-chain noise to a structured form does not suffice: noise added at an intermediate flow time can be weakened by the remaining denoising steps before execution, a phenomenon we call \emph{Structured Noise Dilution}. We propose \textbf{StructRL}, which avoids dilution by relocating policy stochasticity to the action space via three coupled choices: (i) a deterministic ODE decoder, (ii) structured noise injected directly in the action space, and (iii) last-step replay, where policy-gradient updates avoid assigning likelihoods to intermediate denoising states. This keeps structured exploration tied to the executed action while providing a tractable training signal for the flow decoder. Across three flow-based VLA models on multiple simulated manipulation benchmarks and two real-world tasks, StructRL improves exploration efficiency and OOD performance over prior in-chain baselines, demonstrating the effectiveness of structured action-space exploration for adapting flow-based VLA with RL. \textbf{Project page:} https://flyfaerss.github.io/structrl/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15139v1
- Authors: Jiarui Yang, Bin Zhu, Jingjing Chen, Na Zou, Yanwei Fu, Jianggang Zhu, Yu-Gang Jiang
- Published: 2026-08-15T09:31:29Z
- Age days: 2

</details>
