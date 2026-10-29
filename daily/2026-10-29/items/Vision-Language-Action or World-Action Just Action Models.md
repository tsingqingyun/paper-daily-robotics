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
url: "https://arxiv.org/abs/2610.37219v1"
published: "2026-10-27T13:29:28Z"
age_days: 1
score: 28
created: 2026-10-29
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Vision-Language-Action or World-Action? Just Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> JAM 让机器人训练时学习“从现在的观察预判未来的特征”，部署时只保留动作预测所需部分。它说明未来信息可以帮助控制，而不必让模型生成未来图像或在推理时携带额外预测模块。

## 问题

VLA 与 WAM 的比较常把三个因素混在一起：骨干从哪里初始化、未来观察用什么目标训练，以及预测未来的模块是否留到部署。若三者同时变化，成绩差异就不能简单归因于语言视觉预训练或视觉生成。本文通过拆开这些选择，研究未来监督怎样帮助动作学习。

### 用一个例子理解

理解用例（非论文实验）：训练机器人开抽屉时，输入当前画面，除预测动作外，还要求当前特征预测稍后抽屉状态的编码。部署时输入新画面直接输出动作，未来预测头已经移除。

## 创新点或方法

相对于用视觉生成承担未来学习，JAM 用当前观察特征预测已记录未来观察的冻结编码，并同时训练动作专家。未来目标来自固定编码器，不要求生成图像。训练需要未来观察、预测头和动作损失；推理丢弃预测头，只执行控制。作者先在固定策略结构中比较训练目标，再跨骨干来源测试，试图减少架构差异造成的混淆。目标还可以缓存，减少训练更新时重复计算。

### 方法如何工作

1. 把记录中的未来观察编码成固定目标，给当前状态提供后果监督。
2. 让当前观察特征经过预测头逼近未来目标，学习与后续变化有关的信息。
3. 同时训练动作专家，使这些特征服务于控制任务。
4. 训练结束移除预测头，保留动作路径，避免增加部署时的未来预测步骤。

### 必要术语

- 骨干初始化：主干网络训练的起点；本文分别检验视觉生成与视觉语言来源。
- 前瞻损失：预测未来观察编码的误差；本文用它改善当前特征。
- 冻结编码：由参数固定的编码器产生的表示；本文把它作为稳定训练目标。
- FLOPs：计算运算量的估计单位；本文用它比较指定训练环节的成本。

## 证据

摘要报告，相比匹配的 FastWAM，JAM 在 LIBERO、LIBERO-Plus、RoboTwin 上的成功率分别从 97.0%／55.3%／91.2% 变为 98.2%／64.5%／91.4%；也优于匹配的 ImageWAM，但未给其具体数值。缓存未来目标后，每样本每次更新的估算在线训练 FLOPs 比 FastWAM 少 73%。这些结果支持所测设置中的未来特征监督，尤其 LIBERO-Plus 上收益较明显；摘要没有提供真机结果。

## 局限

73% 指特定统计口径下的估算在线训练计算量，不能直接当作总训练成本或实际耗时减少 73%；缓存生成与存储成本仍需核查。RoboTwin 的差异很小，还要看重复实验波动，才能判断是否稳定。

- **判断**：值得细读目标定义和受控比较；它对“未来监督需要保留哪些部件”给出了清楚、可检验的答案。

## 研究关联

一个直接启示是：想让策略考虑动作后果，可以先试预测未来表征，不必先承担图像生成的成本。另一个可借鉴点是比较方法时固定架构，再替换目标，才能更清楚判断收益来自哪里。

### 下一步读哪里

先核查未来取样间隔、冻结编码器来源和两种损失的权重，再看固定架构下的目标对照。计算部分要核查缓存准备是否计入成本，以及不同骨干是否使用相当的数据和训练预算。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/Vision-Language-Action or World-Action Just Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The vision-language-action (VLA) and world-action model (WAM) communities debate whether control policies should inherit pretrained knowledge from vision-language models or from visual generators. The debate, however, bundles three separable choices: backbone initialization, the objective applied to future observations, and whether the machinery for that future loss is kept at inference. A gap between a VLA and a WAM therefore cannot simply be attributed to any one of them. We show that decoupling these choices yields a common framework for both families, which we term Just Action Model (JAM): a pretrained visual backbone with an action expert, trained with an action loss and a foresight loss. The foresight loss trains current-observation features to predict frozen encodings of the recorded future through a prediction head discarded after training, so no visual generation is involved in either training or inference, and the backbone can be chosen freely. We first compare objectives within fixed policy architectures, then evaluate the foresight recipe across backbone families. The resulting JAM policies outperform their matched FastWAM and ImageWAM counterparts on LIBERO and LIBERO-Plus, and achieve similar or slightly higher success rates on RoboTwin. Compared with FastWAM, JAM improves the success rates from 97.0%/55.3%/91.2% to 98.2%/64.5%/91.4%, respectively. With cached foresight targets, JAM reduces estimated online training FLOPs per sample per update by 73% relative to FastWAM. Our results show that future supervision improves control without visual generation or additional inference machinery, and strong foresight performance is attainable with either generator-initialized or vision-language backbones. Project Page: https://y0uroy.github.io/JAM

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37219v1
- Authors: Yonghao Yu, Lang Huang, Runyi Li, Toshihiko Yamasaki
- Published: 2026-10-27T13:29:28Z
- Age days: 1

</details>
