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
url: "https://arxiv.org/abs/2609.37165v1"
published: "2026-09-29T09:56:17Z"
age_days: 0
score: 32
created: 2026-09-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Disentangling Spurious Correlations in Vision-Language-Action Models via Predicting Domain-Invariant Latent Lookahead

> [!summary] 这篇论文到底做了什么（基于摘要）
> 机器人换张桌布就不会干活，可能是它记住了背景，没有学会任务。DILL 让它额外预测“任务接下来会变成什么状态”，并尽量从这个预测目标里去掉背景和风格信息，把注意力拉回动作真正要改变的东西。

## 问题

任务是在视觉分布变化后仍完成机器人操作。瓶颈是策略可能把域特有的背景、纹理等因素当成动作依据，这些线索在训练中有效，换环境却失效；摘要指出这类捷径依赖，但未逐一解释现有鲁棒训练方法的不足。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放上托盘”和桌面图像→策略预测一个表达杯子接近托盘的未来潜变量→输出操作动作。更换桌布后，理想的任务潜变量仍相近，使桌布不再主导动作选择。

## 创新点或方法

通常的策略学习可能同时吸收任务信息与外观关联；DILL 增加一个经过去域变化处理的未来预测目标。训练先利用经过域变换的轨迹，以对比目标和高斯解耦正则训练 Task-Domain Encoder，分离任务结构与域变化。随后由该编码器提供未来潜变量，监督 VLA 的前瞻预测和域解耦。这样，同一任务在不同外观下应指向更一致的未来表示。推理时是否仍需编码器、预测多远以及额外计算量，摘要未说明。

### 方法如何工作

1. 对轨迹施加域变换，获得外观变化的数据，为区分任务与域提供训练材料；具体变换未说明。
2. 用对比目标和解耦正则训练编码器，得到尽量分开的任务与域表示。
3. 把编码器给出的未来潜变量作为策略监督，让 VLA 学习预测任务进展并减少域依赖。
4. 在视觉变化和反事实条件下测试动作结果，再结合表示诊断判断模型是否仍靠捷径。

### 必要术语

- 伪相关：训练中经常一起出现、却未必决定任务的关联；本文要减少策略对它的依赖。
- 潜变量前瞻：预测未来的压缩表示；本文用它给策略增加任务导向的监督。
- 域不变：外观条件变化时仍保留稳定信息；本文希望稳定的是任务结构。

## 证据

摘要给出 LIBERO-Plus 平均成功率 69.1%，比最强基线高 11.4 个百分点，但未给基线名称及分项结果。反事实 task-view 评测支持捷径依赖减少；真实机器人操作实验支持一定实用性，但任务、数量和成功率未列出。潜空间诊断显示任务结构保留与域信息抑制伴随行为改善，这支持设计动机，单凭伴随变化不能确定收益的唯一原因。

## 局限

摘要没有交代的关键问题是：域变换会不会改变任务所需颜色等信息，解耦是否损害细粒度操作，以及真实场景是否覆盖训练外的变化。LIBERO-Plus 的仿真结果与真机证据应分别判断，后者的范围目前无法量化。

- **判断**：研究视觉变化下的机器人可靠性，优先读。摘要报告 LIBERO-Plus 成功率提高 11.4 个百分点，也提到真机实验；下一步最该看的是它去掉了哪些信息、又保住了哪些信息。

## 研究关联

如果策略在训练场景很好、换外观就掉分，可以试着改监督目标：让不同外观下的同一任务指向相近的未来表示。关键是只去掉无关信息；如果任务本身是“拿红杯子”，颜色就不能被当作干扰一起抹掉。

### 下一步读哪里

下一步核查域变换种类、任务与域的正负样本构造、高斯正则的具体约束、未来预测跨度，以及反事实评测究竟改变了什么；真机部分需确认训练与测试条件差异。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Disentangling Spurious Correlations in Vision-Language-Action Models via Predict.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models remain brittle under visual distribution shifts, often relying on spurious correlations tied to domain-specific factors rather than task-relevant structure. We propose Domain-Invariant Latent Lookahead (DILL), a representation-learning framework that mitigates shortcut learning in VLA policies. Our key idea is to supervise policies with domain-invariant future latents learned from domain-transformed trajectory data. A Task-Domain Encoder is trained with contrastive objectives and Gaussian disentanglement regularization to separate task-relevant structure from domain-specific visual variation. The learned encoder then provides future latents for VLA policy learning through lookahead prediction and domain disentanglement, encouraging the policy to focus on task-relevant structure rather than incidental visual factors. Counterfactual task-view evaluations show that DILL reduces shortcut reliance, while LIBERO-Plus evaluations demonstrate improved visual robustness, with 69.1% average success, 11.4 percentage points above the strongest baseline. Real-world manipulation experiments further support DILL's applicability beyond controlled simulation. Complementary latent-space diagnostics show that these behavioral gains are accompanied by representations that better preserve task-consistent structure while suppressing domain-specific variation. Our project page is available at https://dill-vla.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37165v1
- Authors: Junghyun Kim, Ngseo Kim, ChungWoo Lee, Seoyeon Lee, Woo-Jeong Baek, Adam Zhou, Chip Huyen, Jun-Ki Lee, Gi-Cheon Kang, Byoung-Tak Zhang
- Published: 2026-09-29T09:56:17Z
- Age days: 0

</details>
