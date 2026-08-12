---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13494v1"
published: "2026-06-11T15:44:36Z"
age_days: 2
score: 25
created: 2026-06-14
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation

> [!summary] 一句话结论（基于摘要）
> Across offline benchmarks and closed-loop real-robot deployment, NavWAM improves over planning-based world-model baselines in our evaluations while using the default policy mode without CEM-style action search.

## 关键点

- **问题**：Navigation world models provide such visual foresight, but they remain prediction modules that require an external planner to convert predicted futures into closed-loop control.
- **创新点 / 方法**：We propose Navigation World Action Model (NavWAM), a diffusion-transformer policy that turns navigation world-model prediction into executable action by representing future observations, goal-progress values, and action chunks in a shared latent sequence.
- **证据**：Across offline benchmarks and closed-loop real-robot deployment, NavWAM improves over planning-based world-model baselines in our evaluations while using the default policy mode without CEM-style action search.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-14/NavWAM A Navigation World Action Model for Goal-Conditioned Visual Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Goal-conditioned visual navigation requires a robot to act under partial observability
by anticipating how its motion will change the future egocentric view and whether that
change brings it closer to the goal. Navigation world models provide such visual
foresight, but they remain prediction modules that require an external planner to
convert predicted futures into closed-loop control. We propose Navigation World Action
Model (NavWAM), a diffusion-transformer policy that turns navigation world-model
prediction into executable action by representing future observations, goal-progress
values, and action chunks in a shared latent sequence. By learning future prediction
jointly with the action and value targets that determine closed-loop behavior, NavWAM
makes visual foresight directly usable for robot control. We build NavWAM through
simulation pretraining and real-robot adaptation, and evaluate it on image-goal
navigation against planning-based world models and a representative direct navigation
policy. Across offline benchmarks and closed-loop real-robot deployment, NavWAM improves
over planning-based world-model baselines in our evaluations while using the default
policy mode without CEM-style action search. Project page: https://dachii-
azm.github.io/navwam/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13494v1
- Authors: Daichi Azuma, Taiki Miyanishi, Koya Sakamoto, Shuhei Kurita, Yaonan Zhu, Petr Khrapchenkov, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo
- Published: 2026-06-11T15:44:36Z
- Age days: 2

</details>
