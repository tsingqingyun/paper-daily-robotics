---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09813v1"
published: "2026-06-08T17:55:41Z"
age_days: 1
score: 40
created: 2026-06-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# iMaC: Translating Actions into Motion and Contact Images for Embodied World Models

> [!summary] 一句话结论（基于摘要）
> The results demonstrate that iMac outperforms vector-based action control baselines in prediction accuracy, task success rate and cross-scene generalization ability.

## 关键点

- **问题**：However, conventional embodied frameworks rely on low-dimensional structured action vectors (e.g., joint angles and end-effector poses), which suffer from limited expressive capacity, poor generalization across diverse embodiments, and unnatural dynamic modeling for complex physical interactions.
- **创新点 / 方法**：To address these limitations, this paper proposesiMac (Image as Action Control), a novel unified control paradigm that treats raw visual images as native action representations for embodied world models.
- **证据**：The results demonstrate that iMac outperforms vector-based action control baselines in prediction accuracy, task success rate and cross-scene generalization ability.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/iMaC Translating Actions into Motion and Contact Images for Embodied World Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied world models have emerged as a pivotal paradigm for visual robotic decision-
making and interactive environment simulation. However, conventional embodied frameworks
rely on low-dimensional structured action vectors (e.g., joint angles and end-effector
poses), which suffer from limited expressive capacity, poor generalization across
diverse embodiments, and unnatural dynamic modeling for complex physical interactions.
To address these limitations, this paper proposesiMac (Image as Action Control), a novel
unified control paradigm that treats raw visual images as native action representations
for embodied world models. Departing from traditional explicit kinematic action
encoding, iMac formulates continuous visual manipulation as image-based action tokens,
which inherently encapsulate spatial motion intentions, interactive geometric
constraints and subtle physical dynamics. We construct a dual-branch embodied
architecture consisting of an image-action encoder and a dynamic world predictor: the
encoder compresses target-driven visual images into compact action embeddings, while the
predictor learns environment transition rules conditioned on image actions to achieve
high-fidelity future state prediction and closed-loop embodied control. Extensive
experiments are conducted on public embodied manipulation benchmarks and real-world
robotic scenarios. The results demonstrate that iMac outperforms vector-based action
control baselines in prediction accuracy, task success rate and cross-scene
generalization ability. Moreover, our image-action design eliminates the reliance on
manually defined action spaces, realizing flexible and universal control for
heterogeneous embodied agents. This work provides an innovative visual-action
perspective for embodied world models, offering a simple yet effective paradigm for
scalable robotic perception and manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09813v1
- Authors: Zhenyu Wu, Xiuwei Xu, Yukun Zhou, Yifan Li, Qiuping Deng, Xiaofeng Wang, Zheng Zhu, Bingyao Yu, Ziwei Wang, Jiwen Lu, Haibin Yan
- Published: 2026-06-08T17:55:41Z
- Age days: 1

</details>
