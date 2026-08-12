---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13435v1"
published: "2026-06-11T14:59:38Z"
age_days: 1
score: 38
created: 2026-06-13
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# GIVE: Grounding Human Gestures in Vision-Language-Action Models

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Human communication is inherently multimodal, where language is often accompanied by
non-verbal cues such as gestures to convey intentions. However, current Vision-Language-
Action (VLA) models treat robotic manipulation as a pure text-driven task, overlooking
the important role of gestures in Human-Robot Interaction (HRI). This often leads to
inaccurate intent grounding and unreliable manipulation when language instructions are
ambiguous or underspecified. To address this challenge, we propose GIVE (Gesture Intent
via Visual-Semantic Enhancement), an effective approach that enhances pre-trained VLA
models with human gesture understanding without architectural modifications.
Specifically, GIVE incorporates gesture information through two complementary pathways:
a visual pathway that overlays hand skeletons and fingertip rays onto robot observations
for explicit object grounding, and a semantic pathway that generates high-level
descriptions of human gestures and task instructions for robust intent grounding. By
jointly leveraging visual and semantic guidance, GIVE enables VLA policies to better
associate gestures with manipulation behaviors and adapt to dynamic interaction intents.
In real-world HRI experiments, GIVE substantially outperforms the baseline, improving
target object recognition accuracy by 40% and overall task success rate by 80%, while
demonstrating strong robustness and generalization to unseen spatial layouts and diverse
participants.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13435v1
- Authors: Pengfei Liu, Gen Li, Junqiao Fan, Boyu Ma, Jindou Jia, Yang Xiao, Jianfei Yang
- Published: 2026-06-11T14:59:38Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
