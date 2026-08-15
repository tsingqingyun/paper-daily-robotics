---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.11671v1"
published: "2026-08-12T05:30:53Z"
age_days: 2
score: 31
created: 2026-08-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> On the VLA-Arena leaderboard(Aug 1, 2026), StellaVLA ranks first with an overall score of 0.63, versus 0.44 and 0.22 for the strong prior models ($π_{0.5}$ and LingBot-VLA), and it further leads on LIBERO with 98.8% average success rate and LIBERO-Plus with 8…

## 关键点

- **问题**：Vision-Language-Action (VLA) models can follow instructions and manipulate objects, but their performance often collapses out of distribution (OOD), when the scene, viewpoint, or object differs from training.
- **创新点 / 方法**：We present StellaVLA, a framework that instead adapts at test time by conditioning on a single retrieved demonstration.
- **证据**：On the VLA-Arena leaderboard(Aug 1, 2026), StellaVLA ranks first with an overall score of 0.63, versus 0.44 and 0.22 for the strong prior models ($π_{0.5}$ and LingBot-VLA), and it further leads on LIBERO with 98.8% average success rate and LIBERO-Plus with 85.1% success rate.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/StellaVLA In-Context Structured Demonstration for Generalizable Vision-Language-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models can follow instructions and manipulate objects, but their performance often collapses out of distribution (OOD), when the scene, viewpoint, or object differs from training. Adapting to each new situation typically requires collecting more data and fine-tuning. We present StellaVLA, a framework that instead adapts at test time by conditioning on a single retrieved demonstration. The key idea is to move beyond imitating what an expert did and instead convey why: an automated offline pipeline converts each raw trajectory into a structured demonstration, e.g., a task plan, sub-goal descriptions, and verbalized 3D motion, at zero human-annotation cost. Provided as in-context guidance, this structured demonstration lets the policy reason about the task rather than mimic a pixel trajectory, which also makes it transferable across embodiments (real-robot, human-hand, or XR demonstrations). A parallel dual-training design internalizes this reasoning during training through a joint action-and-language objective, while inference uses the action expert alone, preserving real-time, high-frequency control with no added latency. On the VLA-Arena leaderboard(Aug 1, 2026), StellaVLA ranks first with an overall score of 0.63, versus 0.44 and 0.22 for the strong prior models ($π_{0.5}$ and LingBot-VLA), and it further leads on LIBERO with 98.8% average success rate and LIBERO-Plus with 85.1% success rate. Our real-robot benchmark demonstrates that StellaVLA can use both human/robot demos and human-to-robot (XR) demos as in-context structured demonstration to help VLA model adapt to OOD tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.11671v1
- Authors: Siyu Xu, Yunke Wang, Zijian Wang, Dihao Zhu, Chenghao Xia, Chengbin Du, Daochang Liu, Tao Huang, Chang Xu
- Published: 2026-08-12T05:30:53Z
- Age days: 2

</details>
