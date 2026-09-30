---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.38087v1"
published: "2026-09-29T17:40:11Z"
age_days: 0
score: 35
created: 2026-09-30
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# CrossBFM: Distilling a Shared Latent Behavior Space Across Humanoid Embodiments

> [!summary] 先说人话（基于摘要）
> CrossBFM 尝试让不同人形机器人共享同一个行为潜空间，使相同潜向量能跨机器人表达运动、目标姿态或奖励偏好。它先蒸馏共享编码器，再训练各自的潜变量条件控制器。

## 问题

Forward-Backward 行为基础模型为单个机器人训练就需要数百 GPU 小时；换机器人重新训练后，潜空间又彼此无关，难以共享和迁移行为表示。

## 创新点或方法

利用动作重定向提供的逐帧跨形态对应，蒸馏一个没有机器人专属参数的统一编码器。随后通过常规 PPO 训练潜变量条件全身跟踪器，将共享表示转成具体机器人动作；共享的是行为空间，执行仍需控制器。

## 证据

摘要报告编码器蒸馏不足 1 GPU 小时，跟踪器再需 10 GPU 小时。三个人形机器人上，潜变量条件跟踪较关节条件跟踪仅差 0.025 rad，姿态间到达无跌倒，支持全部 41 个奖励提示。未见且形态相似机器人最高恢复已见机器人 89% 的跟踪性能，并验证了三种提示模式的实机执行。

## 局限

需核查蒸馏所依赖源模型的训练成本，以及所报 GPU 小时的计费范围；未见形态的结论明确限于形态相似机器人。

- **判断**：做人形基础控制值得精读共享编码器与迁移实验，尤其要分清表示迁移和控制器训练各自节省了什么。

## 研究关联

对具身基础模型，价值是把跨机器人复用目标明确为行为表示，可能减少为每种形态重建语义空间的成本。它并非语言视觉 VLA，但与可提示的通用运动能力直接相关。

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/CrossBFM Distilling a Shared Latent Behavior Space Across Humanoid Embodiments.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Behavior Foundation Models (BFMs) give humanoids a promptable policy over a latent behavior space, enabling one single vector to represent a motion to imitate, a pose to reach, or a reward to maximize. Forward-Backward representations successfully produce such spaces, but at the cost of hundreds of GPU-hours for a single robot. Moreover, when the training process is repeated for a second robot, it produces a second space unrelated to the first, resulting in embodiment-specific latents that do not unify or transfer. We address these problems with CrossBFM, treating the latent space as the transferable asset for various embodiments. As retargeting provides frame-level cross-embodiment correspondence, we propose a unified encoder architecture with no robot-specific parameters for distilling the behavior space to address all training embodiments simultaneously in less than a GPU-hour. Following this encoder, latent-conditioned trackers turn the distilled latent into whole-body control in a conventional PPO training manner in just 10 more GPU-hours. On three distilled humanoids, all three prompting modes transfer: motion tracking with latent-conditioned policy losing only $0.025$ rad to its joint-conditioned counterpart, smooth goal reaching between poses with no falls, and reward optimization for all $41$ reward prompts. Our experiments further reveal that 1) regressing the encoder on a quarter of the motion corpus costs only $5\%$ of tracking performance and 2) training the encoder on a subset of robots and evaluating on an unseen one recovers up to $89\%$ of the tracking performance of seen robots, demonstrating cross-embodiment generalization to morphologically similar robots. We also verify the pipeline on real robots across all three prompting modes and with flow-based generated latents. Project website: https://dotandung.github.io/crossbfm/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.38087v1
- Authors: Tan-Dzung Do, Tuan Dat Phuong, Nico Bohlinger, Cuc T. Trinh, Siwei Ju, Vien Anh Ngo, Jan Peters, Xinchao Wang, An T. Le
- Published: 2026-09-29T17:40:11Z
- Age days: 0

</details>
