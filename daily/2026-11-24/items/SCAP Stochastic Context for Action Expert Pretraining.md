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
url: "https://arxiv.org/abs/2611.27187v1"
published: "2026-11-20T06:20:06Z"
age_days: 3
score: 27
created: 2026-11-24
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# SCAP: Stochastic Context for Action Expert Pretraining

> [!summary] 这篇论文到底做了什么（基于摘要）
> SCAP 让动作专家在预训练时看到随机缺失部分视觉和文字的输入，保住后续需要的视觉语言联合建模通路。这样做也让模型更愿意根据指令行动，减少仅凭画面猜动作的情况。

## 问题

语言条件操控需要把画面里的物体和指令指定的目标对应起来。如果训练场景常有明显的视觉线索，模型可能光看画面就能猜中动作。先用视觉加动作或语言加动作预训练可以避开模态间竞争，但诊断模型显示，这也可能关闭原本活跃的联合建模通路。在该模型里，后续给齐两种输入，即使不限适配时间，也无法恢复通路。

### 用一个例子理解

理解用例（非论文实验）：画面里有红杯和蓝杯，输入指令是“拿蓝杯”。预训练随机遮掉部分画面和文字，改变每次动作预测可依赖的线索。训练完成后给齐画面和指令，期望输出伸手拿蓝杯的动作。把指令改成“拿红杯”可以检查输出是否随语言改变。

## 创新点或方法

旧做法是在预训练时固定只给一种模态，或始终给齐两种。SCAP 改成在视觉语言模型读入之前，随机遮掉部分图像和文字 token。训练中能用的线索会变化，这给联合通路留下参与预测的机会。之后进入完整输入训练。摘要只说明了两个训练阶段，未交代部署时的遮蔽设置或动作生成细节。

### 方法如何工作

1. 把图像和指令切成视觉与文字 token，让遮蔽可以作用在输入的一部分。
2. 在送入视觉语言模型前随机遮蔽两类 token，使不同训练样本可用的线索发生变化。
3. 用这种输入预训练动作专家，检查联合建模通路能否保持活跃。
4. 恢复完整输入并继续训练，检查保留下来的通路是否仍参与预测。

### 必要术语

- 视觉捷径：靠画面中碰巧与正确动作共现的线索猜答案；本文试图减少这种对指令不敏感的行为。
- 联合建模通路：让视觉和语言共同影响预测的路径；诊断模型用它判断预训练有没有保住跨模态交互能力。

## 证据

摘要报告，在同一个诊断模型里，SCAP 在预训练及后续完整输入训练中保住了联合通路。与直接用完整输入训练相比，它还减少了对视觉捷径的依赖，增加了对语言指令的依赖，摘要未给出依赖程度的测量方式。摘要称四种 VLA 架构的表现均有改善。真机上，三项指令条件操控任务的平均成功率为 76.67%，比完整输入预训练高 25 个百分点。摘要未给逐任务结果或试验次数。

## 局限

作者把不可恢复的结论限定在所构造的诊断模型。真机结果支持 SCAP 在所测任务上的效果，但这些成功率本身无法确定增益有多少来自通路保留。我会核查遮蔽强度变化后，通路和真机表现是否仍一起变化。

- **判断**：值得读到诊断模型的推导和对照设置，因为复用 SCAP 前，最该弄懂的是哪种训练条件会让联合通路失活。

## 研究关联

设计预训练时，可以检查它有没有保住下游真正需要的输入组合。若同一画面换一条指令，正确动作就应改变，那么固定画面、只换指令的测试，比训练损失更能告诉你模型是否听懂了指令。

### 下一步读哪里

先检查诊断模型如何定义通路活跃与关闭，以及不可恢复依赖哪些模型假设。再找遮蔽比例、预训练时长和对照训练预算，最后看真机任务有没有在相似场景里更换指令。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/SCAP Stochastic Context for Action Expert Pretraining.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Single-modality action-expert pretraining controls competition from visual shortcuts before vision--language--action (VLA) adaptation. Yet single-modality pretraining can impair the vision--language interactions needed for subsequent joint prediction. We construct a diagnostic model in which VA or LA pretraining can disable an initially active pathway for joint vision--language modeling. In this model, subsequent training with complete visual and language inputs cannot restore the pathway, even with unlimited adaptation. We therefore introduce Stochastic Context for Action Expert Pretraining (SCAP), a new action-expert pretraining stage that precedes full-input training. During this stage, visual and text tokens are randomly masked before entering the VLM. In this unified diagnostic model, SCAP can preserve the joint vision--language modeling pathway during pretraining and subsequent full-input training. Compared with direct full-input training, it can also reduce reliance on visual shortcuts and increase reliance on language instructions. SCAP consistently improves performance across four different VLA architectures. In real-robot experiments, it achieves 76.67% average success across three instruction-conditioned manipulation tasks, outperforming full-input pretraining by 25 percentage points.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.27187v1
- Authors: Xiao Lin, Yaoxu Lyu, Ronghao Dang, Zhili Liu, Kaijing Ma, Yang Zhou, Dingning Liu, Runzhe Teng, Jun Cen, Shanghang Zhang, Chengju Liu, Qijun Chen
- Published: 2026-11-20T06:20:06Z
- Age days: 3

</details>
