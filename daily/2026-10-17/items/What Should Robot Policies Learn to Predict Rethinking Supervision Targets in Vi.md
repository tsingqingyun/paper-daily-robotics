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
url: "https://arxiv.org/abs/2610.21915v1"
published: "2026-10-15T14:01:06Z"
age_days: 1
score: 31
created: 2026-10-17
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇问的是：训练 VLA 时，每份数据都用来预测动作，是否划算？作者用统一模型和样本路由器比较监督分配，发现同样预算下，把不少样本用于预测潜在动作或未来视觉表示，可能比继续堆动作预测更好。

## 问题

任务仍是根据视觉和语言控制机器人，瓶颈却在训练资源如何分配。动作预测直接对应执行，但辅助目标也要占用预算；如果只报告增加辅助训练后的收益，就难以判断收益来自监督内容还是更多训练。本文明确比较固定预算下的取舍。

### 用一个例子理解

理解用例（非论文实验）：输入带指令的开抽屉轨迹；一部分训练样本要求预测机器人动作，另一部分要求预测抽屉打开后的视觉表示；训练后的策略面对当前画面与指令输出开抽屉动作。

## 创新点或方法

旧做法以动作监督为主、再添加辅助损失；本文让样本级路由器把每个训练样本分给动作或辅助预测，使分配比例可比较。统一骨干是双流多模态扩散 Transformer，测试三类潜在动作目标和三类未来视觉目标。部署仍要输出动作；辅助预测如何与动作分支共享表示、推理是否保留辅助计算，摘要未说明，不能自行补全。

### 方法如何工作

1. 把视觉、语言及轨迹送入统一双流模型，为不同监督目标提供可比较的学习条件。
2. 由样本级路由器分配训练样本，明确哪些用于动作、哪些用于辅助目标，控制预算取舍。
3. 分别训练不同潜在动作或未来视觉目标，比较监督内容对最终控制能力的影响。
4. 在仿真基准与真机任务上执行策略，并用诊断分析表示偏好；推理分支细节摘要只说明到此。

### 必要术语

- VLA：把视觉、语言输入转为机器人动作的模型；是本文比较训练目标的载体。
- 潜在动作目标：用编码后的动作或变化表示作为预测答案；提供不同于直接动作回归的监督。
- 未来视觉目标：预测未来画面的特征表示；帮助模型学习动作之后会出现什么状态。
- 样本级路由：为每个训练样本选择监督任务；使训练资源分配成为显式变量。

## 证据

摘要覆盖 LIBERO、CALVIN 和四项真机任务：合适的辅助目标在同预算下超过纯动作训练，即使动作预测获得的样本不超过一半。未给成功率、误差条或预算计量方式。未来视觉总体更好，但最强潜在动作目标在 CALVIN 上仍有竞争力。诊断提示两类目标分别偏向相对运动、绝对位置与任务身份；这是解释线索，尚不能单凭摘要确认收益的因果来源。

## 局限

摘要强调只有合适的辅助目标有效，不能概括为辅助监督越多越好。我的待核查问题是预算是否按算力严格对齐、目标表示的预训练成本如何处理，以及各任务最优分配是否一致；这些都会影响实际采用价值。

- **判断**：值得读到预算对齐和目标分配消融，因为这篇最有用的结论是何时值得减少动作监督，而非哪种表示名字最新。

## 研究关联

可以借鉴的是，把“训练时预测什么”和“给它多少样本”同时当作设计变量。若动作数据训练收益趋缓，可以在固定预算内替换一部分监督，检查未来状态信息是否更有帮助，而非默认所有样本都应直接预测动作。

### 下一步读哪里

先核查路由比例、样本复用和算力核算，再比较六种目标在各任务上的结果；诊断部分应检查相对运动、绝对位置与任务身份究竟如何测量。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/What Should Robot Policies Learn to Predict Rethinking Supervision Targets in Vi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies are typically trained with action prediction as the primary supervision signal, since robots ultimately execute actions. Auxiliary objectives such as latent-action (LA) and future-vision (FV) prediction are often added to improve policy learning, yet they compete with action prediction for the same training budget. We ask whether, under a fixed budget, allocating a substantial share of training samples to such objectives, rather than to further action prediction, can improve policy learning. We build a unified VLA framework that couples a two-stream multimodal diffusion transformer (MMDiT) with a sample-level router, which assigns each training sample to either action prediction or an auxiliary objective and thus makes supervision allocation explicit. Within this framework, we instantiate three LA targets based on LAPA and its DINO-feature variants, and three FV targets based on DINOv3, V-JEPA 2, and Wan2.2 representations. Across LIBERO, CALVIN, and four real-robot tasks, suitable LA and FV supervision outperforms action-only training under the same budget, even when action prediction receives no more than half of the training samples. FV generally outperforms LA, although the strongest LA target remains competitive on CALVIN. Diagnostic analyses suggest that DINO-based LA targets emphasize relative motion, whereas FV targets emphasize absolute position and task identity. We therefore argue that what robot policies learn to predict, and how training is allocated among these targets, should be treated as explicit design choices rather than defaulting to action-dominant training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21915v1
- Authors: Haitao Shen, Hanyu Liu, Yihan Lin, Huiping Liu, Junbo Cui, Daoheng Li, Yang Li, Jing Zhang, Wenxin Li, Yuan Yao
- Published: 2026-10-15T14:01:06Z
- Age days: 1

</details>
