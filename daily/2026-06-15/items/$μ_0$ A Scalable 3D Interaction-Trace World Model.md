---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13769v1"
published: "2026-06-11T17:59:56Z"
age_days: 3
score: 36
created: 2026-06-15
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# $μ_0$: A Scalable 3D Interaction-Trace World Model

## 为什么重要

自动筛选分数：36

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[机器人学习]]

## 摘要

World models that capture how actions induce physical change enable scalable robot
learning without reliance on embodiment-specific action labels. Pixel-space video models
provide broad visual priors but expend model capacity on dense appearance
reconstruction, while direct action models require embodiment-specific labels that
hinder scalability. We present $μ_0$, a scalable world model based on 3D traces. Rather
than predicting dense pixels or directly modeling actions, $μ_0$ forecasts smooth 3D
trajectories for salient interaction points such as objects, tools, hands, and contact
regions, yielding a compact, embodiment-agnostic motion interface. To enable training
from diverse video sources, our TraceExtract system automatically extracts 3D
supervision by selecting keypoints, constructing globally aligned traces, and
associating motion segments with hierarchical language captions. This TraceExtract
supervision pretrains $μ_0$ by combining a pretrained vision-language backbone with a
modular trace expert, which represents each query via B-spline control points and
predicts future traces. Experiments show that $μ_0$ outperforms baselines in both 2D and
3D trace prediction, including trace prediction models and tokenized VLM methods.
Because $μ_0$ is frozen and reusable, it can be paired with action experts for
downstream robot embodiments. Despite action-free pretraining, the resulting trace-
conditioned policies achieve performance competitive with VLA models pretrained with
action supervision, such as $π_0$. These results establish 3D traces as a scalable and
transferable representation for cross-embodiment manipulation.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13769v1
- Authors: Seungjae Lee, Yoonkyo Jung, Jusuk Lee, Jonghun Shin, Amir Hossein Shahidzadeh, Yao-Chih Lee, H. Jin Kim, Jia-Bin Huang, Furong Huang
- Published: 2026-06-11T17:59:56Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
