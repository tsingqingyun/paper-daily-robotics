---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25558v1"
published: "2026-09-22T01:43:55Z"
age_days: 1
score: 33
created: 2026-09-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery

> [!summary] 先说人话（基于摘要）
> GC-VLA 学习预测操作将引起的几何变化，而不只表示当前几何；GCRF 再利用闭环反馈训练一个受限的残差策略，在需要时修正动作。

## 问题

当前帧几何监督没有明确表达操作带来的变化。论文希望先学习可跨机器人与第一视角视频使用的视觉接口，再对齐特定机器人的动作。

## 创新点或方法

当前观测用于预测多视角未来相对当前的几何变化 token，离线帧对提供名义 0.5 秒预测目标。训练先建立 GC-VLM，再分阶段阻断、开放动作流梯度完成 ActionExpert 对齐；最后冻结 GC-VLA，由二元路由器决定是否启用有界残差速度策略。

## 证据

GC-VLA 在 LIBERO 上成功率为 95.20%，加入 GCRF 后为 99.55%。推理仅使用当前观测和学到的几何表示，不运行离线目标编码器。

## 局限

跨具身视觉接口在摘要中是设计动机，尚未提供对应迁移数字；需区分几何变化监督和后续闭环残差学习各自的贡献。

- **判断**：值得细读表示目标和四阶段训练流程，但不能仅凭 LIBERO 提升认定已实现跨具身泛化。

## 研究关联

对多模态模型与 VLA 研究者，几何变化提供了连接视觉预训练和机器人动作的候选接口，残差阶段则展示如何在冻结基础策略后补强闭环控制。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/HABILIS Brain 0 Geometry-Change Supervision for Vision-Language-Action and Resid.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action policies benefit from geometric supervision, but current-frame geometry alone does not explicitly describe the changes associated with manipulation. This design is motivated by the goal of learning an embodiment-agnostic visual interface that can be pretrained across robot and egocentric video before robot-specific action alignment. We introduce Geometry-Change VLA (GC-VLA), which learns to predict multiview future-current geometry-change tokens from current observations. Offline frame pairs define a nominal 0.5-second prediction horizon; future observations are used only to construct training targets. Stage 1 trains a geometry-change vision-language model (GC-VLM). Stage 2 introduces a continuous ActionExpert and aligns it with robot actions while stopping action-flow gradients at the VLM interface. Stage 3 enables these gradients to update the trainable VLM components jointly with the ActionExpert. Stage 4 freezes GC-VLA and applies Geometry-Conditioned Residual Flow (GCRF), using a binary intervention router and a single bounded residual velocity policy learned from closed-loop feedback. GC-VLA achieves 95.20% success on LIBERO, and GC-VLA with GCRF achieves 99.55%. Inference uses current observations and the learned GC representation without executing the offline target encoders.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25558v1
- Authors: Jinu Pahk, Jesoon Kang, Taegeon Park, Jisu An, Soo Min Kimm, Jaejoon Kim, Byoung-Tak Zhang
- Published: 2026-09-22T01:43:55Z
- Age days: 1

</details>
