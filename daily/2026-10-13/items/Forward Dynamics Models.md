---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.13117v1"
published: "2026-10-09T07:12:16Z"
age_days: 3
score: 36
created: 2026-10-13
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Forward Dynamics Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> FDM 让动作特征同时承担“选动作”和“预测动作之后世界怎样变化”两项任务，用真实未来纠正动作学习。执行时只生成动作，省去未来画面生成，也避免预测画面出错后再误导动作。

## 问题

任务是根据视觉和语言选择机器人动作。普通 VLA 没有显式的未来世界状态监督；某些 WAM 先预测未来，再据此选动作，会增加推理开销，还可能把视觉预测错误传给动作。难点是怎样获得未来监督的好处，同时避免执行时依赖预测未来。

### 用一个例子理解

理解用例（非论文实验）：输入是桌面图像和“把杯子移到垫子上”；训练时动作特征还要帮助预测移动后的桌面状态，预测偏差提供学习信号；执行时同样输入直接得到移动动作，不生成未来图像。

## 创新点或方法

旧做法要么只学动作，要么让预测未来成为动作的输入；FDM 把方向改成动作特征到未来预测。训练时，真实未来状态产生的监督通过这些特征影响策略；推理时跳过未来生成。巧处在于学习信号可以向动作侧反传，执行时的信息依赖却不需要从未来预测流向动作。具体损失、特征接入位置和状态表示未说明。

### 方法如何工作

1. 从当前观察和指令形成动作特征，为动作输出提供依据。
2. 训练时用这些特征预测未来，使特征必须包含动作后果的信息。
3. 用真实未来监督联合训练，让预测误差参与塑造动作特征。
4. 执行时仅保留动作路径，避免未来生成开销；摘要只说明到此。

### 必要术语

- 动作特征：用于产生动作的内部表示；也是未来预测的条件。
- 未来状态监督：用实际后续世界状态检验预测；提供额外训练信号。
- 端到端训练：相连部分一起优化；让未来任务影响策略学习。
- 骨干：模型的基础结构；本文在两类基础模型上实现同一依赖方向。

## 证据

摘要报告同时使用 VLM 和视频生成模型两类骨干，在仿真与真机测试。LIBERO 平均成功率为 99.4%，作者称达到当时最佳水平；真机任务相较 VLA 和 WAM 方法，绝对提升最高 13 个百分点。摘要未给任务明细、基线名称、重复次数及推理耗时，支持两类骨干上的有效性，但不能据此判断所有任务平均提高多少。

## 局限

摘要没有列出作者明确承认的局限。我的待核查问题是：收益究竟来自未来监督，还是其他训练差异；预测分支虽不会在执行时直接误导动作，其训练梯度仍可能影响动作质量。还需确认真实未来数据的需求和额外训练成本。

- **判断**：值得细读方法和消融，因为“训练时利用未来、执行时删除未来生成”是清晰可复用的设计，但要确认成功率提升确实由它带来。

## 研究关联

可借鉴的是把昂贵的预测任务用作训练监督，而不必把它变成执行链中的必经步骤。当未来结果有助于辨别动作质量、但在线生成成本较高时，这种依赖方向值得尝试。

### 下一步读哪里

下一步检查动作特征与未来分支的连接、监督梯度路径、删去未来分支后的推理流程，以及保持训练条件一致的消融；核查 LIBERO 汇总方式和真机逐任务结果。输入未提供正文。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/Forward Dynamics Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models and world action models (WAMs) have advanced robotic policy learning by building on pretrained vision-language models (VLMs) and video generative models (VGMs), respectively. Yet VLAs learn without explicit supervision from future world states, while WAMs that condition actions on predicted futures incur extra inference cost and let visual prediction errors propagate into actions. We present Forward Dynamics Models (FDM), a family of robotic action models that couples action and future world-state prediction through an action-to-future paradigm. Future prediction is conditioned on action features, never the reverse: end-to-end training lets ground-truth future states supervise the policy through these features, while prediction errors cannot propagate into actions. At inference, FDM skips future generation entirely, avoiding its computational cost. The paradigm is backbone-agnostic, and we instantiate it with both VLM and VGM backbones. Experiments in simulation and on real robots demonstrate the effectiveness of FDM across both backbone families, achieving a state-of-the-art 99.4% average success rate on LIBERO and absolute gains of up to 13% over VLA and WAM methods on real-world tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.13117v1
- Authors: Zipei Ma, Junzhe Jiang, Jiahui Zhang, Juntong Zhang, Chun Gu, Bozhou Zhang, Jiankang Deng, Xiatian Zhu, Li Zhang
- Published: 2026-10-09T07:12:16Z
- Age days: 3

</details>
