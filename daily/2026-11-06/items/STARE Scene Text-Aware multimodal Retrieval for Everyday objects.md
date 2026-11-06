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
url: "https://arxiv.org/abs/2611.06089v1"
published: "2026-11-04T07:32:37Z"
age_days: 1
score: 32
created: 2026-11-06
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# STARE: Scene Text-Aware multimodal Retrieval for Everyday objects

> [!summary] 这篇论文到底做了什么（基于摘要）
> STARE 帮服务机器人按自由描述找对要取的物品，即使区别藏在包装文字或旁边的标牌里。它用 Crosslingual Visual Prompt 辅助理解现场文字，再把文字、外观和物体之间的关系与指令对应起来。

## 问题

用户可能只说去拿门牌旁边那包写着某个词的东西。机器人得从画面里认出候选物品，读懂文字，还要弄清文字究竟印在目标上，还是出现在用来定位的参照物上。只认物体类别会漏掉文字区别，只读出文字也可能把词绑定到错误的物体。摘要没有逐一交代已有基线在哪些场景失手。

### 用一个例子理解

理解用例（非论文实验）：用户说“拿 EXIT 指示牌下方、印着 decaf 的那包咖啡”。输入是指令和货架画面。系统要把 EXIT 绑定到参照标牌，把 decaf 绑定到候选包装，再检查包装是否在标牌下方，最后输出应取的那包咖啡。

## 创新点或方法

把按整条指令找相似画面的思路拆成两个问题。先借助 Crosslingual Visual Prompt 帮模型解释场景文字，再判断指令里提到的实体分别对应画面中的哪些物体，以及它们的外观和空间关系是否符合描述。这样，读到正确的字还要通过物体关系的检查。检索推理的输入是自由指令和场景视觉信息，输出用于后续取物。摘要没有说明提示词如何构造、文字怎样定位、匹配模块怎样训练，也没有说明检索结果怎样接入导航和抓取。

### 方法如何工作

1. 接收自由指令和场景画面，从指令中识别要匹配的目标、文字和参照物。
2. 用跨语言视觉提示辅助解释画面里的文字，形成可与指令对应的文字线索。具体提示构造，摘要只说明到此。
3. 将指令中的实体对应到候选物体，再结合外观、文字和空间关系缩小目标范围。
4. 把匹配结果用于后续取物。摘要未说明从检索结果到导航和抓取指令的接口。

### 必要术语

- 场景文字：出现在包装、门牌、标识等图像区域里的文字；本文用它区分物品或定位参照物。
- Crosslingual Visual Prompt：用于辅助模型解释现场文字的跨语言视觉提示；本文用它帮助指令与图像中的文字线索对应。
- 实体对应：判断指令里的每个名称或描述在画面中指向什么；本文用它区分待取目标及其参照物。

## 证据

据摘要，GoGetIt 和 TextCaps-test 使用真实室内外图像以及涉及导航、物体操作的指令。STARE 在标准多模态检索指标上超过所有受测基线，摘要未给出指标名称、基线名单和具体差值。另据摘要，零样本迁移的实体机器人实验总体成功率为 80%。图像评测支持所测数据上的检索优势，真机数字说明系统在所测设置下能执行任务，样本量、成功判据和失败分布仍需核查。

## 局限

我会核查零样本迁移具体留出了什么，例如场地、物品还是指令，以及真机失败发生在文字理解、目标定位、导航还是抓取。总体成功率把这些环节合在一起，单凭这个数字无法判断跨语言提示贡献了多少。

- **判断**：值得读到场景文字怎样绑定候选物体，以及真机失败如何分类，这两处决定了方法对哪类取物指令有帮助。

## 研究关联

物品描述里的文字有时直接标识目标，有时只提供地标。如果指令经常混用这两种线索，可以分别检查字有没有读对、词有没有指到正确物体。即使两套系统的最终取物成功率相同，这种拆分也能指出哪一环值得改。

### 下一步读哪里

先查 Crosslingual Visual Prompt 的实际输入与输出，再查匹配如何区分目标文字和地标文字。读实验时找文字与关系建模的单独对照，并核对零样本划分、真机试次数和成功判据。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-06/STARE Scene Text-Aware multimodal Retrieval for Everyday objects.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

In this study, we focus on service robots that retrieve and transport everyday objects based on free-form instructions that may refer to visual features and scene text. This is challenging because it requires a multimodal understanding of the visual features and spatial relationships of objects, as well as scene text embedded in the environment. To address this, we propose Scene Text-Aware multimodal Retrieval for Everyday objects (STARE), which leverages visual and textual cues in response to free-form instructions. STARE introduces Crosslingual Visual Prompt to enhance scene text interpretation, and models the complex relationships between named entities in the instructions and their corresponding objects. We evaluate STARE using two novel benchmarks, GoGetIt and TextCaps-test, both of which consist of real-world indoor/outdoor images and instructions involving object manipulation and navigation. The results show that STARE outperforms all baseline methods on standard multimodal retrieval metrics. Furthermore, in physical experiments conducted under a zero-shot transfer setting, STARE achieves an overall success rate of 80%. Our project page and code are provided in the Supplementary Materials.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.06089v1
- Authors: Kento Tokura, Ryosuke Korekata, Daichi Yashima, Kei Katsumata, Kanon Amemiya, Miyu Goko, Komei Sugiura
- Published: 2026-11-04T07:32:37Z
- Age days: 1

</details>
