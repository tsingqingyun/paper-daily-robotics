---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23685v1"
published: "2026-06-22T17:59:52Z"
age_days: 1
score: 36
created: 2026-06-24
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> With online correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy using only 20 minutes of OOL glove data.

## 关键点

- **问题**：Human-hand demonstrations provide a direct and scalable source of physical interaction data for robot learning.
- **创新点 / 方法**：To address this, we introduce LaST-HD, a novel human-to- robot action learning paradigm that extends reasoning-before-acting VLA by aligning human-hand and robot demonstrations in a shared latent reasoning space.
- **证据**：With online correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy using only 20 minutes of OOL glove data.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human-hand demonstrations provide a direct and scalable source of physical interaction
data for robot learning. While manual retargeting is indispensable for establishing
kinematic action correspondence across different morphologies, robust transfer requires
going beyond geometry to address the underlying alignment of physical dynamics between
human and robot manipulation. To address this, we introduce LaST-HD, a novel human-to-
robot action learning paradigm that extends reasoning-before-acting VLA by aligning
human-hand and robot demonstrations in a shared latent reasoning space. Rather than
mimicking human kinematics, LaST-HD trains an auxiliary action-conditioned world model
on unpaired human-hand and robot trajectories to synthesize unified latent targets.
After aligning cross-embodiment representations in this shared forward-dynamics space,
these targets supervise LaST-HD's latent reasoning process, enabling it to internalize
shared physical dynamics and drive efficient human-hand action learning. Moreover, we
develop Out-of-Lab (OOL) Glove, a low-cost motion-capture glove tailored to LaST-HD for
human-hand data collection. The captured human data provide precise keypoints and serve
as universal action supervision across grippers and dexterous hands. Armed with the
aligned latent space and high-fidelity human-hand data, we develop a progressive mixed-
to-human training recipe comprising mixed human-robot co-training and human-hand online
correction post-training. Through mixed co-training, LaST-HD improves generalization to
novel objects, scenes, and positions using only human-hand demonstrations. With online
correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy
using only 20 minutes of OOL glove data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23685v1
- Authors: Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi, Hao Chen, Jiawei Chen, Qingpo Wuwu, Xiaoqi Li, Nuowei Han, Yiming Zhang, Xuheng Zhang, Yang Yue, Yeqing Yang, Lei Wang, Peng Jia, Hao Tang, Shanghang Zhang
- Published: 2026-06-22T17:59:52Z
- Age days: 1

</details>
