---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09474v1"
published: "2026-08-10T11:42:52Z"
age_days: 0
score: 31
created: 2026-08-11
concepts: ["多模态基础模型", "智能体 Agent", "Sim2Real", "具身智能评测与基准"]
---

# FaLCon: Facet-Anchored Retrieval with Late Consensus for Sim2Real Text-Based Person Anomaly Search

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[Sim2Real]], [[具身智能评测与基准]]

## 摘要

Text-based person anomaly search requires retrieving real-world pedestrian images from
detailed natural-language descriptions using models trained primarily on synthetic data.
This Sim2Real setting is particularly challenging because visually similar candidates
may differ only in subtle actions, object interactions, or appearance attributes, while
applying multimodal large language models to the entire gallery is computationally
expensive. We propose an anchor-constrained coarse-to-fine retrieval framework that
combines global semantic matching with fine-grained verification. First, each query is
represented by its original caption, a structured concatenation, and several semantic
facets. Heterogeneous vision-language retrievers are then integrated through robust per-
query score calibration and soft claim-aware fusion. Full and concatenated captions
serve as anchors to preserve candidate recall, whereas appearance, action, and object
facets provide bounded corrective evidence. The resulting candidate pool is further
refined by a discriminative Qwen3 reranker and two complementary semantic verification
modules based on anomaly-aware cloze completion and multi-agent evidence reasoning.
Finally, an uncertainty-gated consensus module adaptively reweights the three experts on
ambiguous queries. Experiments on the PAB benchmark show that the proposed soft claim-
aware retrieval achieves 86.44% mAP@10, substantially outperforming individual retrieval
backbones. The complete framework further improves performance to 95.41% mAP@10, 94.44%
R@1, and 99.09% R@5. These results demonstrate that preserving strong global retrieval
while restricting expensive semantic reasoning to a small candidate pool is effective
for fine-grained Sim2Real person anomaly search. Our code will be available on Github.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09474v1
- Authors: Hieu Dinh Trung Pham, Phuong Huu Vu Tran, Thuan Duc Mai, Son Nguyen Minh Le, Khang Le Minh, Hoang Vo, Minh-Chi Phung, Huy Minh Nhat Nguyen, Cuong Tuan Nguyen
- Published: 2026-08-10T11:42:52Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
