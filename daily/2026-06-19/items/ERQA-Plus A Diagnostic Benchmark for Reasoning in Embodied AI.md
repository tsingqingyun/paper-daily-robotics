---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.17639v2"
published: "2026-06-16T07:56:33Z"
age_days: 2
score: 31
created: 2026-06-19
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI

## 为什么重要

自动筛选分数：31

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Generalist embodied agents require more than object recognition: they must reason about
spatial relations, actions, procedures, human intentions, environmental constraints, and
commonsense consequences from situated visual observations. Yet existing visual and
embodied question answering benchmarks often provide limited control over the reasoning
dependencies being tested, making it difficult to distinguish grounded embodied
reasoning from shortcut-driven visual or linguistic pattern matching. We present ERQA-
Plus, a diagnostic benchmark for reasoning in embodied AI. ERQA-Plus contains 1,766
question-answer instances grounded in 711 robot-centric images and organized according
to a structured taxonomy spanning perceptual, action-centric, social-interaction,
navigation-environmental, and contextual commonsense reasoning. The dataset is
constructed using a multi-stage generation and validation pipeline that combines
taxonomy-guided question generation, automatic quality judging, iterative revision, and
human assessment to improve visual grounding, answer validity, and reasoning quality. We
benchmark representative general-purpose vision-language models and embodied models,
including LLaVA-NeXT-8B, Prismatic-7B, MiniCPM-V-4.5-8B, Qwen3-VL, RoboRefer-8B, and
RoboBrain2.5-8B. Although the strongest model, Qwen3-VL-32B, achieves 83.4% overall
accuracy and 61.4 SBERT score, category-level results reveal persistent weaknesses in
spatial reasoning, procedural reasoning, event prediction, and intention inference.
ERQA-Plus therefore provides a fine-grained evaluation framework for measuring not only
whether embodied agents answer correctly, but also which forms of embodied reasoning
they can and cannot perform reliably. The dataset is available
https://huggingface.co/datasets/huggingdas/erqa-plus and the project page at
https://github.com/LUNAProject22/erqa-plus.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.17639v2
- Authors: Hong Yang, Basura Fernando
- Published: 2026-06-16T07:56:33Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
