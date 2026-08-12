---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18363v1"
published: "2026-06-16T18:09:26Z"
age_days: 2
score: 38
created: 2026-06-19
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# Guava: An Effective and Universal Harness for Embodied Manipulation

## 为什么重要

自动筛选分数：38

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Language models trained on large-scale vision-language data have demonstrated strong
potential for embodied agents. Harnessing models through embodied tools use offers a
promising alternative to end-to-end vision-language-action systems by combining high-
level reasoning with external modules for perception, planning, and control. However, it
remains unclear what makes an effective harness for embodied manipulation, and to what
extent such a harness can unlock embodied capabilities in a wide range of reasoning
models. In this work, we present Guava, a harness framework for embodied tool use
developed through systematic exploration of the design space of agent workflows, action
spaces, and observation spaces. Our study identifies three key ingredients for effective
embodied agents: iterative perception-reasoning-action loops, semantic action
abstractions, and multimodal observations. To understand whether these design principles
are universal even to small models, we develop an end-to-end training pipeline that
distills embodied manipulation capabilities into a 4B open-source model using fewer than
2K trajectories collected entirely in simulation. Experimental results in both
simulation and real-world environments show performance comparable to frontier
proprietary models while exhibiting strong generalization to unseen objects, novel
instructions, and long-horizon tasks. Results suggest that a well-designed harness can
serve as a scalable, model-agnostic interface for embodied manipulation, enabling strong
emergent embodied capabilities in compact open-source models with minimal training data.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18363v1
- Authors: Haowen Liu, Xirui Li, Shaoxiong Yao, Peng Shi, Tianyi Zhou, Jia-Bin Huang, Furong Huang, Jiayuan Mao
- Published: 2026-06-16T18:09:26Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
