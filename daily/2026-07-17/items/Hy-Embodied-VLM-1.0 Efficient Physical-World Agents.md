---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.12894v1"
published: "2026-07-14T15:34:17Z"
age_days: 2
score: 31
created: 2026-07-17
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Hy-Embodied-VLM-1.0: Efficient Physical-World Agents

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Building capable embodied agents requires not only multimodal perception and
understanding, but also agentic capabilities for reasoning about actions, adapting to
evolving situations, and interacting with the physical world. In this report, we
introduce Hy-Embodied-VLM-1.0, an efficient and powerful embodied foundation model
specifically designed for embodied agents operating in the physical world. To cultivate
such capabilities from the pre-training stage onward, we define an action-centric
capability taxonomy comprising three progressive dimensions: Action-Relevant State
Understanding, Action-Transition Reasoning, and Sequential and Adaptive Reasoning.
Guided by this taxonomy, we develop a systematic data pipeline and curate data mixtures
spanning both pre-training and post-training. To deliver strong physical-world
understanding and interaction capabilities while supporting latency-sensitive
deployment, we build our model on the Hy3-A3B language backbone and the Hy-ViT2 vision
encoder. Its efficient Mixture-of-Experts architecture combines strong model capacity
with high inference efficiency. We evaluate Hy-Embodied-VLM-1.0 on a comprehensive suite
of 38 benchmarks covering embodied perception, physical-world understanding, and
embodied reasoning. The model achieves the best performance among similarly sized models
on 19 of the 38 benchmarks and substantially outperforms strong competitors, including
Qwen3.6-A3B and Cosmos 3. Compared with the previous-generation Hy-Embodied-0.5 MoT-2B,
Hy-Embodied-VLM-1.0 improves average performance by 8.4%. Despite activating only 3B
parameters, it achieves performance close to that of the previous-generation model with
32B activated parameters. Beyond static benchmark evaluation, Hy-Embodied-VLM-1.0 also
demonstrates strong performance on embodied agentic tasks requiring multi-turn
interaction and long-horizon reasoning.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.12894v1
- Authors: Ziyi Wang, Xumin Yu, Yongming Rao, Yonggen Ling, Yunheng Li, Oran Wang, Mingqi Gao, Yuchen Zhou, Yves Liang, Zuyan Liu, Yani Zhang, Rui Huang, Xiaoran Xu, Bowen Yuan, Yifu Yuan, Xu Tan, He Zhang, Yufei Huang, Shenghao Zhang, Hongsheng Wu, Han Hu, Zhengyou Zhang
- Published: 2026-07-14T15:34:17Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
