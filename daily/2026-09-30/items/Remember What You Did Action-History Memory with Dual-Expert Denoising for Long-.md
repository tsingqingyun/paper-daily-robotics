---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37307v1"
published: "2026-09-29T11:43:19Z"
age_days: 0
score: 36
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

> [!summary] 先说人话（基于摘要）
> ActMem-VLA 让机器人记住自己执行过哪些动作，避免相似画面下分不清任务阶段。记忆专家先在去噪早期引导任务进度，冻结的原策略随后细化动作。

## 问题

长任务不同阶段可能出现相似观察和机器人状态，缺少历史的 VLA 因而容易选错动作。已有记忆方法若同时微调记忆模块与基础策略，会增加策略训练成本。

## 创新点或方法

Mamba 编码已执行动作历史，结合当前上下文条件化轻量 PreAction Expert，在高噪声阶段引导去噪，再交给冻结的 Action Expert 完成低噪声细化。训练仅更新 Mamba 和 PAE，基础 VLA 是已微调后冻结的策略。

## 证据

LIBERO-Mem 十项任务平均成功率 80.8%，π₀.₅ 为 65.2%，MemoryVLA 为 49.5%；额外参数为 3.45%。四项真实任务上，相比 π₀.₅ 平均成功率提高 28.8%，摘要未说明该增幅是否为百分点。

## 局限

额外参数少不直接等于训练或推理成本低；需核查历史编码与专家交接开销，以及动作历史如何应对执行偏差。

- **判断**：值得精读双专家交接机制与历史依赖任务，摘要给出的基准差距足以支持认真复现。

## 研究关联

对长时程 VLA，提供了将历史决策与动作细化分开训练的具体方案。对具身 Agent，也有助于区分任务阶段记忆与通用语言记忆的作用。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Remember What You Did Action-History Memory with Dual-Expert Denoising for Long-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have driven rapid progress in robotic manipulation, demonstrating strong fine-grained control and promising performance on long-horizon tasks. However, many existing VLAs lack explicit access to interaction history, making them vulnerable to perceptual aliasing: similar current observations and robot states at different task stages may induce action ambiguity and lower success rate. Existing methods incorporate temporal or progress cues through feature conditioning, action-prior modification, or sampling guidance. However, methods that jointly fine-tune memory modules and the base VLA incur additional policy-training costs, motivating the separation of trainable history-conditioned steering from frozen base-policy refinement. We propose ActMem-VLA, a dual-expert handover architecture that augments a frozen, fine-tuned VLA with a memory plugin comprising a Mamba-based memory module and a lightweight PreAction Expert (PAE). Specifically, Mamba encodes executed-action history into memory that conditions PAE alongside current context. With these inputs, PAE steers task progression during early, high-noise denoising, then passes the partially denoised action to the frozen Action Expert (AE) to refine action details during the remaining low-noise steps. The fine-tuned base VLA remains frozen throughout training, while only the Mamba module and PAE are jointly optimized. On LIBERO-Mem, ActMem-VLA achieves 80.8\% average success across all ten tasks, compared with 65.2\% for $π_{0.5}$ and 49.5\% for MemoryVLA, while introducing only 3.45\% additional parameters. Across four real-world tasks, it improves the average success rate over $π_{0.5}$ by 28.8\%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37307v1
- Authors: Yaxin Zhao, Dianye Huang, Chenwei Wang, Chenguang Yang, Zhongliang Jiang
- Published: 2026-09-29T11:43:19Z
- Age days: 0

</details>
