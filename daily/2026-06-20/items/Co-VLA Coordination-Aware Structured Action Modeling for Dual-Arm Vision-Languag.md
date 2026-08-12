---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20285v1"
published: "2026-06-18T14:28:37Z"
age_days: 1
score: 41
created: 2026-06-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems

> [!summary] 一句话结论（基于摘要）
> Experiments across simulation and real-world benchmarks show Co-VLA significantly outperforms monolithic baselines, achieving a 27% success rate gain in tight- coordination tasks, more than doubling performance in OOD real-world scenarios (from 13% to 27%), a…

## 关键点

- **问题**：However, as bimanual tasks become tightly coupled and execution constraints become critical, implicit coordination alone is insufficient to ensure reliable, interpretable, and stable behavior.
- **创新点 / 方法**：In this work, we propose Co-VLA, a coordination- aware bimanual manipulation framework introducing explicit structural priors into VLA models.
- **证据**：Experiments across simulation and real-world benchmarks show Co-VLA significantly outperforms monolithic baselines, achieving a 27% success rate gain in tight- coordination tasks, more than doubling performance in OOD real-world scenarios (from 13% to 27%), and reducing task completion time by up to 25%.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/Co-VLA Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Languag.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models show strong capabilities in single and dual-arm
robotic manipulation. Prior works show coordinated bimanual behaviors can emerge from
end-to-end learning, leveraging large vision-language backbones with continuous action
prediction. However, as bimanual tasks become tightly coupled and execution constraints
become critical, implicit coordination alone is insufficient to ensure reliable,
interpretable, and stable behavior. In this work, we propose Co-VLA, a coordination-
aware bimanual manipulation framework introducing explicit structural priors into VLA
models. We instantiate our method on a state-of-the-art vision-language backbone by
replacing its monolithic action head with a Structured Action Expert (SAE) designed for
bimanual coordination. Specifically, we introduce explicit structure at the action
generation level with a modular coordination-aware loss that shapes shared and residual
latents according to task-specific structures. The shared latent encodes task-level
coordination intent, while residual latents capture execution adjustments for each arm.
At deployment, a Latent-Aware Controller (LAC) interprets the learned representations to
modulate synchronization strength, execution asymmetry, smoothness, and safety
constraints in real time. LAC operates at the joint-command level and remains compatible
with standard control pipelines without requiring force or impedance control.
Experiments across simulation and real-world benchmarks show Co-VLA significantly
outperforms monolithic baselines, achieving a 27% success rate gain in tight-
coordination tasks, more than doubling performance in OOD real-world scenarios (from 13%
to 27%), and reducing task completion time by up to 25%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20285v1
- Authors: Yandong Wang, Jiaqian Yu, Xiongfeng Peng, Lu Xu, Yamin Mao, Weiming Li, Jaewook Yoo, Dongwook Lee, Daehyun Ji, Mingbo Zhao, Chao Zhang
- Published: 2026-06-18T14:28:37Z
- Age days: 1

</details>
