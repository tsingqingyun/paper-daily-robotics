---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11743v1"
published: "2026-06-10T07:20:36Z"
age_days: 1
score: 42
created: 2026-06-12
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# TacCoRL: Integrating Tactile Feedback into VLA via Simulation

> [!summary] 一句话结论（基于摘要）
> Across four bimanual contact-rich tasks, the final visuo-tactile policy achieves an average success rate of 72.5%, compared to baseline of 50.0%.

## 关键点

- **问题**：The key idea is not only adding touch as an input, but learning how contact readings should modulate action responses in near-failure states that are rare in demonstrations and risky to collect on hardware.
- **创新点 / 方法**：We present TacCoRL, a scalable framework that injects Tactile feedback into VLA policies and improves them through sim-real Co-training and simulation-based reinforcement learning (RL), without requiring large-scale tactile pretraining or extensive real-world contact exploration.
- **证据**：Across four bimanual contact-rich tasks, the final visuo-tactile policy achieves an average success rate of 72.5%, compared to baseline of 50.0%.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/TacCoRL Integrating Tactile Feedback into VLA via Simulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models provide strong visual, language, and action priors
for robot manipulation, but visual observations alone often miss the local contact state
required for contact-rich tasks. We present TacCoRL, a scalable framework that injects
Tactile feedback into VLA policies and improves them through sim-real Co-training and
simulation-based reinforcement learning (RL), without requiring large-scale tactile
pretraining or extensive real-world contact exploration. The key idea is not only adding
touch as an input, but learning how contact readings should modulate action responses in
near-failure states that are rare in demonstrations and risky to collect on hardware. We
use a real-aligned simulator as a closed-loop training environment for contact
interaction. Mixed simulated and real trajectories first warm-start tactile-conditioned
actions in the pretrained policy. Reinforcement learning with verifiable task rewards
then optimizes the policy using simulated contact rollouts. It reinforces tactile-
conditioned actions that lead to task completion, while a supervised objective on real
trajectories keeps the refined policy anchored to deployment visual, tactile, and action
distributions. The resulting policy transfers directly to the real robot without
privileged simulation state or online real-world RL. Across four bimanual contact-rich
tasks, the final visuo-tactile policy achieves an average success rate of 72.5%,
compared to baseline of 50.0%. Result videos and more details are available at
https://tac-corl.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11743v1
- Authors: Siyu Ma, Yuqi Liang, Chang Yu, Yunuo Chen, Hao Su, Yixin Zhu, Yin Yang, Chenfanfu Jiang
- Published: 2026-06-10T07:20:36Z
- Age days: 1

</details>
