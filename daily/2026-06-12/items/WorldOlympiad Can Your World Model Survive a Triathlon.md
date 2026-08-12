---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11129v1"
published: "2026-06-09T17:24:36Z"
age_days: 2
score: 40
created: 2026-06-12
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# WorldOlympiad: Can Your World Model Survive a Triathlon?

## 为什么重要

自动筛选分数：40

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

We introduce WorldOlympiad, a benchmark for diagnosing video-based world models across
physical faithfulness, geometric consistency, and interaction fidelity. While existing
benchmarks often focus on visual quality, semantic alignment, or short-term temporal
coherence, they provide limited insight into whether generated videos obey physical
rules, preserve coherent 3D structure, and sustain controllable interactions over long
horizons. To address this gap, WorldOlympiad decomposes world-model evaluation into
three complementary dimensions. The physical track uses object segmentation and MLLM-as-
judge to assess whether generated videos follow interpretable rules in mechanics,
thermal phenomena, and material properties. The geometry track reconstructs generated
videos with Gaussian splatting and evaluates structural consistency, cross-view
coherence, and camera-trajectory alignment. The interaction track assesses whether
generated rollouts follow complex action prompts and maintain smooth, coherent
transitions across consecutive video chunks. WorldOlympiad further covers three major
downstream scenarios, including gaming, robotics, and general real-world videos,
capturing diverse challenges from interactive control and embodied manipulation to open-
domain motion and camera dynamics. Together, these tracks and scenarios form a scalable
and interpretable evaluation suite that exposes failure modes beyond generic video
quality. Experiments on state-of-the-art models reveal substantial gaps in physical
reasoning, 3D consistency, and long-horizon interaction, underscoring the need for more
structured evaluation protocols for generative world models.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11129v1
- Authors: Yuke Zhao, Wangbo Zhao, Weijie Wang, Zeyu Zhang, Dakai An, Akide Liu, Yinghao Yu, Jiasheng Tang, Fan Wang, Wei Wang, Bohan Zhuang
- Published: 2026-06-09T17:24:36Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
