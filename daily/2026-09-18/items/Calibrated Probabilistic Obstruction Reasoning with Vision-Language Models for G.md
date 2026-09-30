---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.18718v1"
published: "2026-09-16T14:21:52Z"
age_days: 1
score: 31
created: 2026-09-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Calibrated Probabilistic Obstruction Reasoning with Vision-Language Models for Grasping in Clutter

> [!summary] 先说人话（基于摘要）
> CPOR-Grasp不急着认定唯一的遮挡关系，而是综合多种可能场景，决定直接抓目标、先移开障碍，还是暂缓行动。

## 问题

杂乱场景抓取中，单一遮挡图忽视解释不确定性；VLM预测可能失准，成对遮挡关系也可能彼此矛盾。简化推理时丢弃假设，还可能改变最终动作却没有误差界。

## 创新点或方法

校准并融合VLM、深度和非模态掩码证据，构造合法遮挡图分布，对图边缘化以计算目标可达性和移障选择。保留高概率图，并对舍弃概率质量建立总变差界，用于决策认证、自适应停止和暂缓。

## 证据

在合成及真实UNOBench场景上优于基线；Gemini Robotics骨干的校准误差从0.1416降至0.0185。使用少56倍的图仍有99.74%的决策与精确推理一致，实机平均成功率为77.8%。

## 局限

图截断的认证针对近似推理误差，不等于真实抓取安全或成功保证；需核查概率模型校准与实际场景之间的条件。

- **判断**：值得精读概率建模与误差界，因其同时提供校准、推理压缩和实机抓取证据。

## 研究关联

对多模态机器人决策与评测，提供了从感知校准到动作选择的完整不确定性处理路径，也可供VLA外围决策模块参考。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/Calibrated Probabilistic Obstruction Reasoning with Vision-Language Models for G.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Retrieving a target from clutter requires deciding whether to grasp the target, remove a blocker, or defer. Existing methods typically commit to a single obstruction graph or removal strategy, ignoring uncertainty across alternative scene interpretations. They also rely on miscalibrated vision-language model (VLM) predictions and can produce pairwise obstruction relations that are jointly inconsistent. Moreover, current approximations provide no guarantees about the impact of discarded hypotheses on the final decision. We propose CPOR-Grasp, a calibrated probabilistic obstruction-reasoning framework that propagates uncertainty from pairwise evidence to action decisions. CPOR-Grasp calibrates and fuses VLM, depth, and amodal-mask cues to estimate obstruction probabilities, induces a distribution over valid obstruction graphs, and marginalizes over these graphs to compute the likelihood that the target is accessible or that a given blocker should be removed. To make inference tractable, it retains only the highest-probability graphs and derives a total-variation bound on the discarded probability mass, enabling certified decisions, adaptive stopping, and principled deferral. On synthetic and real UNOBench scenes, CPOR-Grasp outperforms state-of-the-art baselines. Calibration error decreases from 0.1416 to 0.0185 on the Gemini Robotics backbone, while graph truncation matches exact inference on 99.74\% of decisions using 56 times fewer graphs. In real-world experiments, CPOR-Grasp achieves a 77.8\% average success rate, surpassing SOTA baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.18718v1
- Authors: Thanh-Tuan Tran, Ngoc-Chien Chu, Thanh Nguyen Canh, Nak Young Chong, Nguyen-Viet Ha, Xiem HoangVan
- Published: 2026-09-16T14:21:52Z
- Age days: 1

</details>
