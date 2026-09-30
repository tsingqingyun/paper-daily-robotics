---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.21031v1"
published: "2026-08-21T12:28:58Z"
age_days: 2
score: 34
created: 2026-08-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration

> [!summary] 一句话结论（基于摘要）
> The results show that existing passive and naive interactive baselines either fail when physical properties are hidden or over-explore, whereas PhysCaP achieves comparable performance with fewer interactions and reduced execution time.

## 问题

To balance exploration costs and the efficiency of information obtained, PhysCaP employs a dual-agent design: a Planner that decides when to explore and when to stop, and a Prioritizer that filters implausible interactions and ranks the remainder using a heuristic priority score, enabling efficient, targeted explorati…

## 创新点或方法

We present PhysCaP, a Physics-Informed Code-as-Policy agent for active perception in robotic manipulation.

## 证据

The results show that existing passive and naive interactive baselines either fail when physical properties are hidden or over-explore, whereas PhysCaP achieves comparable performance with fewer interactions and reduced execution time.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/PhysCaP Grounding Code-as-Policy Agent with Physics-Informed Exploration.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present PhysCaP, a Physics-Informed Code-as-Policy agent for active perception in robotic manipulation. While vision-language-action policies excel at imitating demonstrations, they rely on passive observation and fail to infer latent physical properties critical for manipulation. PhysCaP augments code-as-policy frameworks with a physics-informed exploration layer that enables explicit information-seeking through interaction. It introduces training-free physical property extraction modules that estimate object mass and stiffness from robot proprioception without additional sensors. To balance exploration costs and the efficiency of information obtained, PhysCaP employs a dual-agent design: a Planner that decides when to explore and when to stop, and a Prioritizer that filters implausible interactions and ranks the remainder using a heuristic priority score, enabling efficient, targeted exploration. We evaluate PhysCaP on real-world tabletop manipulation tasks (searching for hidden objects, detecting empty cans, and finding ripe avocados) and a simulated task in LIBERO. The results show that existing passive and naive interactive baselines either fail when physical properties are hidden or over-explore, whereas PhysCaP achieves comparable performance with fewer interactions and reduced execution time. Ablation studies further validate the effectiveness of the proposed physical property extraction modules. Project page: https://physcap.github.io

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.21031v1
- Authors: Chen-Yu Lin, Jing-Wen Chen, Hsueh-En Chang, Hung-An Chen, Sheng-Hsun Chang, Chi-Pin Huang, Fu-En Yang, Min-Hung Chen, Yi-Ting Chen, Yu-Chiang Frank Wang, Shao-Hua Sun
- Published: 2026-08-21T12:28:58Z
- Age days: 2

</details>
