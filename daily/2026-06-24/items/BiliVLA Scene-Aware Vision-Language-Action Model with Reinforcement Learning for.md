---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23531v1"
published: "2026-06-22T16:11:15Z"
age_days: 1
score: 35
created: 2026-06-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation

## 为什么重要

自动筛选分数：35

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic
navigation and stable biliary cannulation within a narrow monocular field characterized
by specular reflections, partial occlusions, and frequent tissue contact. Although
recent robotic systems and vision-based assistance techniques improve operator
ergonomics and provide perceptual cues, their performance degrades under pronounced
anatomical variability and safety-critical visual artifacts, which hinders reliable
autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware
Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as
an instruction-conditioned visuomotor learning problem. Given an endoscopic observation
and a stage-specific language instruction, BiliVLA jointly predicts the target category,
a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for
a continuum endoscope. The proposed framework incorporates scene-aware supervision to
enhance semantic target consistency and safety-aware recovery supervision to induce
conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is
a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning
(SFT) with Group Relative Policy Optimization (GRPO), which significantly improves
action reliability and decision consistency during closed-loop navigation. Across three
ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall
success rate (SR) of 84.85\% in real-world phantom experiments. These results indicate
that integrating semantic grounding, scene-aware learning, and reward-guided
optimization improves perception-action alignment and enables robust autonomous
endoscopic navigation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23531v1
- Authors: Jinsong Lin, Chi kit Ng, Zhiyong Xiong, Zikang Pan, Yihan Hu, Tabassum Tamima, Ziyi Hao, Eddie Cheung, Jiewen Lai, Huxin Gao, Hongliang Ren
- Published: 2026-06-22T16:11:15Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
