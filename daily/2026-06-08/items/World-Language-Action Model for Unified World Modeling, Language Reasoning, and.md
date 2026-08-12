---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.05979v1"
published: "2026-06-04T10:23:01Z"
age_days: 3
score: 47
created: 2026-06-08
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis

> [!summary] 一句话结论（基于摘要）
> Our WLA-0 prototype, with 2B active parameters, achieves 40 ms per inference on an NVIDIA RTX 5090.

## 关键点

- **问题**：We propose world-language-action (WLA) models as a new class of embodied foundation models.
- **创新点 / 方法**：We propose world-language-action (WLA) models as a new class of embodied foundation models.
- **证据**：Our WLA-0 prototype, with 2B active parameters, achieves 40 ms per inference on an NVIDIA RTX 5090.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：47
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/World-Language-Action Model for Unified World Modeling, Language Reasoning, and.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We propose world-language-action (WLA) models as a new class of embodied foundation
models. WLA takes textual instructions, images, and robot states as inputs to jointly
predict textual subtasks, subgoal images, and robot actions, conjoining the \emph{world
modeling interface} to learn from extensive egocentric videos as in the world-action
model (WAM) and the \emph{language reasoning} capacities to solve complex long-horizon
tasks as in vision-language-action (VLA) models. At the core of WLA lies an
\emph{autoregressive (AR)} Transformer backbone, instead of a bidirectional diffusion
Transformer as in WAMs, to predict the \emph{next state}, comprising the \emph{semantic-
level} textual intention and complementary \emph{fine-grained} physical dynamics. The
physical dynamics are supervised by the world modeling objective based on a dedicated
World Expert, and are leveraged to ease the characterization of the state-action
correlation for the Action Expert. WLA leverages meta-queries to make the world
prediction \emph{implicitly} impact the action generation so that the former can be
disabled during inference. The world prediction can also be activated to enable test-
time scaling for improved robot control. Our WLA-0 prototype, with 2B active parameters,
achieves 40 ms per inference on an NVIDIA RTX 5090. Evaluations across simulated and
real-world environments demonstrate that WLA-0 achieves state-of-the-art multi-task and
long-horizon learning abilities, e.g., 92.94\% success rate on RoboTwin2.0 Clean and
56.5\% success rate on RMBench. WLA-0 also holds the promise to learn novel tasks
directly from \emph{cross-embodiment robot videos} without action annotations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.05979v1
- Authors: Yi Yang, Zhihong Liu, Siqi Kou, Yiyang Chen, Yanzhe Hu, Jianbo Zhou, Boyuan Zhao, Zhijie Wei, Xiao Xia, Xueqi Li, Pengfei Liu, Zhijie Deng
- Published: 2026-06-04T10:23:01Z
- Age days: 3

</details>
