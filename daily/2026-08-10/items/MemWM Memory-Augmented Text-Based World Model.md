---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.07107v1"
published: "2026-08-07T11:03:32Z"
age_days: 3
score: 24
created: 2026-08-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# MemWM: Memory-Augmented Text-Based World Model

## 为什么重要

自动筛选分数：24

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

World models are increasingly used to support planning in agents by predicting how
environment states evolve in response to agent actions. Yet fluent next-state
predictions can still omit task-critical facts, corrupt product attributes, or apply
incorrect transition rules. To address such systematic prediction errors, we introduce
MemWM, a memory-augmented text-based world model. MemWM uses world memory, a curated
memory bank of transition rules, state caches, and hard-to-predict facts, to condition
next-state imagination. We evaluate factual state preservation with Structured State
Fidelity (SSF), which scores predicted states through benchmark-specific facts and
fields. Compared with SFT, memory-augmented training improves SSF by up to 206.3%. In
the full planning setting, we keep the policy model frozen and provide policy-side world
skill: retrieved task-level skills and step-wise corrective guidance for action
selection. Across ALFWorld, WebShop, and ScienceWorld, memory-augmented agents improve
downstream success over an SFT-trained world-model agent, with up to a 65.4% relative
gain. Sensitivity analyses further show that retrieved memory improves task success and
efficiency under different memory and action-budget settings.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.07107v1
- Authors: Yujun Wang, Tao Zhang, Jinhe Bi, Aniri, Wenxuan Ye, Boliang Liu, Sikuan Yan, Shuning Wang, Xuebing Zhou, Sören Pirk, Hinrich Schütze, Yunpu Ma
- Published: 2026-08-07T11:03:32Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
