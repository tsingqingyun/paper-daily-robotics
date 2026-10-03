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
url: "https://arxiv.org/abs/2609.32193"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-10-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Devol-ONE: One Autoregressive Mixture of Transformers to Unify Vision-Language-Action and Latent World Modeling

> [!summary] 这篇论文到底做了什么（基于摘要）
> Devol-ONE 把语言视觉理解、未来状态预测和动作生成放进同一个自回归系统。它让动作生成持续接触语义信息和预测的物理变化，避免只在开始时接收一次固定的视觉语言表示。

## 问题

任务是根据图像和指令生成机器人动作。普通 VLA 直接从当前信息生成动作，没有显式描述场景之后怎样变化；已有 WAM 虽预测未来，却常把预测与策略分开训练或分开组织，只通过预测输出连接，限制了两者在生成过程中的信息交互。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“把杯子放进托盘”，视觉语言流处理目标，动力学流预测相关场景的未来隐状态，动作专家在逐层计算中结合这两类信息输出控制动作。例子只说明信息如何进入动作生成，不假定系统会比较多条候选轨迹。

## 创新点或方法

本文把多个 Transformer 流放在统一自回归过程中：视觉语言流与基于 V-JEPA 预训练的动力学流联合预测，动力学预测在每层读取视觉语言的键值缓存，在语言引导下预测未来隐状态；动作专家持续结合语义和预测动力学。预训练来源明确到 V-JEPA，但联合训练的损失、更新范围和监督构造未说明。推理时强调逐层交互，而非先得到固定表示再交给动作专家；具体生成顺序及是否评估候选动作，摘要未说明。

### 方法如何工作

1. 处理当前视觉和语言信息，形成可供后续各层读取的语义上下文。
2. 让动力学流逐层读取视觉语言缓存，在语言引导下预测未来隐状态，使预测与任务目标相联系。
3. 让动作专家持续结合语义与预测动力学，避免动作只依赖预先固定的一份表示。
4. 在统一自回归过程中生成动作；各流的精确生成顺序和执行循环，摘要只说明到此。

### 必要术语

- 隐状态：用特征表示场景，而不是生成完整像素图像；本文在这种表示中预测未来。
- 自回归：利用已有内容继续生成后续内容；本文用同一生成过程组织多个信息流。
- 键值缓存：保存注意力计算可读取的信息；动力学流用它反复获取视觉语言上下文。
- V-JEPA：本文动力学流采用的预训练来源；具体接入和训练方式需查正文。

## 证据

摘要列出 LIBERO、LIBERO-PLUS、RoboTwin2.0，以及 Flexiv 单臂和双臂真机评测，并称消融支持动态流预测和逐层统一注意力的作用。但没有给出对比方法名称、成功率、误差、运行速度或消融差值。因此能确认测试覆盖多个基准和真机设置，尚不能判断优势大小，也不能断言模型通过搜索候选未来选择动作。

## 局限

摘要把逐层交互作为核心机制，但效果是否来自这一机制，需要查看消融是否控制模型容量、训练数据和计算量。未来隐状态也不自动等于准确的动作后果预测；应核查动力学流是否以动作作为条件，以及它的预测误差怎样关联任务成功。

- **判断**：值得深入读信息流和消融实验，因为本文最有辨识度的选择是预测与动作在哪些层交互，摘要还不足以证明这种耦合的收益与成本。

## 研究关联

具体启示是：未来预测除了作为最终输出，也可以在动作计算过程中持续提供信息。如果预测模块已经存在，但策略只读取一次它的结果，可以考虑检验更深层的信息交互是否有帮助；代价则是训练耦合和推理成本需要一起评估。

### 下一步读哪里

先核查各流的 token 排序、注意力可见范围、动作条件和训练目标；再看逐层交互与固定表示的消融是否公平。真机部分应检查任务、数据量、成功率和延迟，判断复杂结构是否带来可执行的收益。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/Devol-ONE One Autoregressive Mixture of Transformers to Unify Vision-Language-Ac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.32193v2 Announce Type: replace Abstract: Vision Language Action (VLA) models condition actions directly on current visual and language context, without an explicit account of how the scene evolves under candidate actions. World Action Models (WAM) attempt to address this limitation by predicting future states, but existing designs keep prediction and policy learning architecturally separate, connecting them only through the predicted output, whether through pixel space video generation or a latent forecasting module trained independently of the policy. We present Devol-ONE, a Mixture of Transformers architecture that unifies vision language understanding, latent world dynamics prediction, and action generation within a single autoregressive framework. Instead of encoding vision language tokens once and feeding them to the action expert, Devol-ONE runs autoregressive prediction jointly across a vision language stream and a V-JEPA pretrained dynamics stream, attending to the vision language key-value cache at every layer to forecast future latent states under language guidance. The action expert is in turn shaped continuously by semantic reasoning and predicted physical dynamics rather than by a fixed representation computed in advance. Extensive experiments are conducted on LIBERO, LIBERO-PLUS, RoboTwin2.0 along with real-world evaluation on Flexiv single-arm and dual-arm setups. Ablation studies show the effectiveness of dynamic stream prediction and layer-wise unified attention to validate our model architectural coherency.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.32193
- Authors: Hongyi Cai, Yi Herng Ong, Tingshiuan C. Wu, Chiew Hui Lim, Hanxia Li, Kehong Guo, Sze Yuan Cheong
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
