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
url: "https://arxiv.org/abs/2610.40356v1"
published: "2026-10-29T16:11:05Z"
age_days: 2
score: 29
created: 2026-11-01
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# JEDI: Joint-Embedding Demonstration Compression for In-Context Imitation Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> JEDI 把长示范压成少量潜在槽位，但要求它们能帮助预测当前任务接下来会出现的关键画面。它用这个目标迫使压缩结果保留执行过程，并支持测试时参考更多示范。

## 问题

上下文模仿学习在测试时通过示范适应任务，但长视频、动作等多模态轨迹挤占上下文，限制可参考的示范数量。真正难点是压缩后保留什么：只围绕动作压缩，未必保住当前情境下决定后续执行的细节。摘要中的动作压缩对照也围绕这一问题设置。

### 用一个例子理解

理解用例（非论文实验）：输入几段“先移开挡物、再放杯子”的示范和当前画面；JEDI 压缩示范，并用预测下一阶段画面的目标保留先后关系；策略参考槽位输出下一步动作。这里的任务顺序仅用于说明，不是论文已验证的案例。

## 创新点或方法

JEDI 将示范压成潜在槽位，训练这些槽位帮助预测查询回合下一阶段关键帧在冻结 video-JEPA 中的表示。预测未来相当于给压缩设一道要求：留下的信息应能解释执行将如何继续。任务与过程反事实进一步促使槽位保留执行细节，预测器还从示范库中选择示范；具体反事实构造和选择规则未说明。训练后再用关键点 token 做后训练，支持人手条件输入；测试时使用压缩示范作为上下文。

### 方法如何工作

1. 把长示范编码为潜在槽位，降低每条示范占用，为更多参考腾出上下文。
2. 用冻结 video-JEPA 表示查询回合后续关键帧，给槽位提供与未来执行相关的训练目标。
3. 加入任务与过程反事实，促使表示区分执行细节；具体样本构造摘要只说明到此。
4. 测试时由预测器从库中选择示范，使用压缩上下文支持动作策略；动作解码机制未说明。
5. 用关键点 token 后训练，使系统支持人手条件输入；其数据要求与适用边界需查正文。

### 必要术语

- 上下文模仿学习：测试时给策略示范作为参考；本文试图增加能放入上下文的示范数量。
- 潜在槽位：固定数量的可学习表示位置；本文用来承载压缩后的示范信息。
- video-JEPA 空间：视频编码器产生的特征空间；本文在其中预测未来关键帧，编码器保持冻结。
- 反事实：有针对性地改变条件以区分解释；本文借任务与过程变化约束槽位保留执行细节。

## 证据

摘要报告 LIBERO 与真实机器人实验，称 JEDI 支持多示范上下文。LIBERO 上控制训练目标的比较显示，相对仅动作压缩，成功率和遵循示范程度更好，但没有数值、示范数量、指标定义或真机任务清单。因此证据支持未来预测目标的方向，尚不能量化压缩效率或人手到机器人的适用范围。

## 局限

我会核查关键帧如何选，以及冻结表示是否忽略细小但关键的接触差异。人手条件输入也不等于任意人类视频都能直接驱动机器人；关键点来源、后训练数据及形态差异处理都需核查。

- **判断**：值得优先读目标函数、反事实构造和等预算对照，因为论文最有参考性的部分是“如何判断压缩保住了有用信息”。

## 研究关联

最值得借鉴的是根据下游需求定义压缩目标：若需要保留执行过程，就让压缩表示承担后续状态预测，而不只重建已有信息。何种目标有效仍需对应任务的控制实验。

### 下一步读哪里

先查下一阶段关键帧的定义、反事实样本改变什么；再核查动作压缩对照是否匹配槽位数和上下文预算，以及示范数量扩展、选择器和人手关键点后训练各自的贡献。

- **概念**：多模态基础模型 机器人学习 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-01/JEDI Joint-Embedding Demonstration Compression for In-Context Imitation Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

In-context imitation learning (ICIL) adapts robot policies through test-time demonstrations, but long multimodal trajectories constrain how many examples fit in context. We ask what a compressed demonstration should preserve. We propose JEDI, which compresses demonstrations into latent slots trained to predict the query episode's next-stage keyframe in a frozen video-JEPA space. Task and process counterfactuals help the slots preserve execution details, while the predictor selects demonstrations from a bank. Post-training with keypoint tokens enables human-hand conditioning on robots. Experiments on LIBERO and real robots show that JEDI supports many-shot context; LIBERO objective controls show improved success and demonstration following over action-only compression. These findings support query-future prediction as a training objective for preserving execution-relevant information in compressed demonstrations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.40356v1
- Authors: Jiazhao Liang, Zhewen He, Shuaihang Yuan, Hao Huang, Yi Fang
- Published: 2026-10-29T16:11:05Z
- Age days: 2

</details>
