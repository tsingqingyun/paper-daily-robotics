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
url: "https://arxiv.org/abs/2610.12386v1"
published: "2026-10-08T17:38:04Z"
age_days: 1
score: 36
created: 2026-10-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# ARC: A Reasoning Recipe for Robot Foundation Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> ARC 从已有机器人示范自动补出解释：下一步为什么这样做、预计会产生什么效果，再训练现有模型使用这些解释控制机器人。巧处是把推理紧贴下一步动作，而非只让模型泛泛描述任务。

## 问题

任务是提高机器人基础模型在未专门训练的任务上的执行成功率。常见路径是扩大模型、增加机器人示范和进行昂贵的大规模训练。ARC 寻找另一种补充路径：已有示范包含动作，却未必明确表达动作理由与预期效果，这些关系能否成为额外监督？摘要没有逐一分析既有推理方法为何失败。

### 用一个例子理解

理解用例（非论文实验）：输入画面与“打开抽屉”；轨迹解释“先抓住把手，便于随后向外拉”，策略据此输出接近和抓握动作。若抽屉尚未移动，下一步解释应对应当前状态；摘要没有保证模型一定按这段文字执行。

## 创新点或方法

旧做法主要依赖观察与动作对应关系；ARC 在示范上增加与下一步动作绑定的推理轨迹，解释动作为何合适以及应带来什么变化。自动标注流程从 DROID 构建 ARC-Trace-DROID，不新增机器人采集。随后按模型架构微调，让 VLA 或世界动作模型使用这些轨迹进行控制。训练用轨迹作监督，推理过程也按架构适配；是否每次先生成文字、轨迹如何进入动作预测，摘要未说明。

### 方法如何工作

1. 从已有 DROID 示范取得观察与行动，作为无需新采集的训练基础。
2. 自动生成绑定下一步动作的理由和预期效果，得到 ARC-Trace-DROID；标注与质检细节未说明。
3. 按模型架构微调，使解释与控制建立联系，而非只训练描述场景。
4. 采用对应架构的推理方式执行任务，再比较适配前后的成功率；具体推理流程摘要只说明到此。

### 必要术语

- 推理轨迹：记录动作理由与预期效果的解释序列；本文用它补充控制监督。
- 自动标注：用程序化流程为已有示范添加标签；本文借此避免新增机器人采集。
- 百分点：两个百分比直接相减的单位；摘要中的成功率提升不是相对增长百分比。

## 证据

摘要称适配后的模型在 RoboLab-120 和 MolmoSpaces 达到新的最好成绩，在 RoboLab-Reasoning-50 上提升最多 50 个百分点；真机上 π₀.₅ 的任务成功率提高 82.2 个百分点。适配对象包括 π₀.₅ 和 Cosmos3-Nano-Policy。未提供各基线绝对成功率、测试次数、具体任务及上述基准的环境性质，因此能确认的是所报告测试中的明显收益，无法判断收益分布或直接比较不同模型。

## 局限

摘要描述的是预期因果关系，不代表解释已被独立证明为真实因果机制。我会核查自动标注是否有事实错误，以及模型是否真正依赖解释内容。没有新增机器人示范也不等于没有成本：自动标注、微调和推理开销仍需评估。

- **判断**：值得读到轨迹示例与内容消融，因为决定可复用性的不是“加推理”这个说法，而是哪些解释实际帮助了动作选择。

## 研究关联

可以借鉴的动作标注方式是同时记录“为什么现在做”和“做完应发生什么”。这会让模型学习动作与条件、后果的联系。若已有示范而新增采集成本高，补充这种监督是一条值得验证的路线；但文字解释是否带来收益，需要消融支持。

### 下一步读哪里

核查自动标注使用什么信息、如何避免把未来信息带入部署，以及各架构怎样使用轨迹。重点看去掉理由、预期效果或打乱轨迹后的结果，再核对真机提升的原始成功率与统计范围。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/ARC A Reasoning Recipe for Robot Foundation Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to this recipe as ARC. It consists of three key ingredients: a reasoning trace, a scalable automatic labeling pipeline, and a strategy for adapting pretrained RFMs to use these traces for control. First, we find that effective reasoning traces should be grounded in the robot's next action and explain its causal structure: why the action is appropriate and what effect it should produce. Second, we show that these traces can be generated automatically from existing demonstrations, enabling us to construct ARC-Trace-DROID from DROID without collecting new robot data. Third, we show how state-of-the-art VLAs such as $π_{0.5}$ and WAMs such as Cosmos3-Nano-Policy can learn to use these traces for control, with fine-tuning and inference tailored to each model's architecture and capabilities. Using ARC, we obtain gains in zero-shot RFM performance that, to our knowledge, are unprecedented without additional robot demonstrations or foundation-scale training. The adapted models establish a new state of the art on RoboLab-120 and MolmoSpaces, with gains of up to 50 percentage points on RoboLab-Reasoning-50. On real robots, ARC improves $π_{0.5}$'s task success by 82.2 percentage points. Project website: https://arc-robot-reasoning.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12386v1
- Authors: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout, Moritz Reuss, Zhaoshuo Li, Fabio Ramos, Ankit Goyal, Jenai Xuning Yang
- Published: 2026-10-08T17:38:04Z
- Age days: 1

</details>
