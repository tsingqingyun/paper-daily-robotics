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
url: "https://arxiv.org/abs/2610.25927v1"
published: "2026-10-19T07:26:13Z"
age_days: 1
score: 31
created: 2026-10-21
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# CondenseVLA: Learnable History Condensation for Efficient Multi-Frame VLA

> [!summary] 这篇论文到底做了什么（基于摘要）
> CondenseVLA 让机器人从近期多帧画面中挑出互补信息，再交给动作解码器。它用固定数量的槽位 token 压缩历史，并约束这些槽位少重复关注同一内容。

## 问题

操作中的短暂接触、遮挡和中间状态，单看当前画面可能无法辨认。直接增加历史帧数又会增加计算，而且许多画面重复，固定采样也不随任务需要调整。瓶颈因此不是有没有历史，而是怎样从有限历史中保留能消除当前动作歧义的证据。

### 用一个例子理解

理解用例（非论文实验）：机器人要把刚推过的零件放入盒子，当前画面里零件被手遮住；输入包含近期画面特征，凝缩模块保留遮挡前的位置和移动线索，动作端据此输出后续抓放动作。例子只解释历史为何有用，不代表已验证这一任务。

## 创新点或方法

旧做法主要靠扩大历史窗口；本文把缓存的逐帧 VLM 特征送入解码器侧的凝缩模块。可学习查询通过多头交叉注意力，从历史中提取固定数量的槽位表示，供动作解码使用。训练时，辅助正则惩罚槽位注意力重叠，并降低槽位嵌入的相关性，推动它们提取不同线索；推理时则用学到的模块压缩近期缓存。摘要未说明主动作损失、窗口长度或缓存更新细节。

### 方法如何工作

1. 缓存近期各帧的视觉特征，使当前决策能访问已消失的线索。
2. 让可学习查询对历史做交叉注意力，得到固定数量的槽位，限制动作端输入规模。
3. 训练时惩罚槽位重复关注和表示相关，使有限槽位尽量携带互补信息。
4. 把凝缩结果用于动作解码；关键证据若已离开窗口，这个机制就无法继续访问它。

### 必要术语

- VLA：把视觉、语言和动作联系起来的策略；本文改动的是它利用视觉历史的方式。
- 槽位 token：固定数量的信息容器；本文用它们承接多帧历史的提炼结果。
- 交叉注意力：用查询从另一组特征中选择并汇总信息；本文用它读取历史。
- 去相关正则：训练时减少表示重复的约束；本文希望借此提高槽位互补性。

## 证据

摘要报告 Simpler-WidowX 成功率从 58.7% 到 69.8%，增加 11.1 个百分点；LIBERO 为 97.2%，真机任务为 52.8%，依赖记忆的 RMBench 为 21.6%。这些数字均来自摘要。除首项外，摘要未给对应基线，也未交代任务数量、重复次数和计算开销。因此支持其在所测任务中有效利用近期视觉，但不足以证明普遍优于其他压缩方法，或确定实际节省多少推理成本。

## 局限

摘要明确承认有限历史窗口在更难的多观测任务上存在边界，RMBench 的结果也提醒人们别把它当成长时记忆方案。我的待核查问题是：增益有多少来自历史本身，有多少来自凝缩与正则，以及速度收益是否包含视觉骨干的计算。

- **判断**：值得读到模块实现和消融实验，重点判断固定槽位是否以可接受的成本保住了关键瞬间。

## 研究关联

值得借鉴的是把“记多少”与“交给动作端多少”分开：保留一段历史，却只让动作端处理少量提炼结果。若任务关键线索发生在近期、画面重复较多，这比盲目加长输入更有针对性。

### 下一步读哪里

下一步核查历史窗口、槽位数量、缓存成本，以及单帧、直接多帧、凝缩和去掉正则的对照；还应确认 RMBench 的失败是否与关键证据超出窗口有关。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/CondenseVLA Learnable History Condensation for Efficient Multi-Frame VLA.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot manipulation often depends on short-term cues - such as brief contacts, temporary occlusions, and intermediate object states - that are ambiguous in a single frame and can only be resolved by integrating observations over time. However, injecting historical information solely by enlarging the history window is computationally costly and frequently yields limited gains due to substantial redundancy and task-agnostic, inflexible sampling of observations. We propose CondenseVLA, a multi-frame VLA policy with a learnable decoder-side history condensation module for using short-term visual context in action decoding. Given a sequence of cached per-frame features from the VLM backbone, CondenseVLA distills observation history into a fixed set of slot tokens using learnable queries and multi-head cross-attention. Simple auxiliary regularization penalizes overlap among slot attention maps and decorrelates slot embeddings, encouraging complementary attention and reducing slot redundancy. Across the evaluated tasks, CondenseVLA improves Simpler-WidowX success from 58.7% to 69.8% (+11.1 percentage points), achieves 97.2% on LIBERO, and reaches 52.8% on real-world tasks. It achieves 21.6% success on memory-dependent RMBench tasks. These results support selective condensation of bounded recent visual evidence for action decoding, while harder multi-observation tasks expose the limits of a finite history window. Project page: https://github.com/FeiyangHong/CondenseVLA

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.25927v1
- Authors: Feiyang Hong, Yujie Wei, Bo Zhao, Xiu Su, Hongxun Yao, Shuo Yang
- Published: 2026-10-19T07:26:13Z
- Age days: 1

</details>
