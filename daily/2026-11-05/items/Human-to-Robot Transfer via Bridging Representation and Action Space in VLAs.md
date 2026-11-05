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
url: "https://arxiv.org/abs/2611.04391v1"
published: "2026-11-03T06:24:29Z"
age_days: 1
score: 32
created: 2026-11-05
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs

> [!summary] 这篇论文到底做了什么（基于摘要）
> H2RB 想让预训练 VLA 用上更容易采集的人类示范。它同时处理“人和机器人看到的东西如何对应”与“相似行为如何变成各自的动作”，共享动作潜变量，但保留不同的动作解码映射。

## 问题

任务是用未配对的人类和机器人示范，把已有 VLA 适配到目标机器人与环境。直接混合数据的困难在于身体结构不同：相似行为既可能产生不同观测，也需要不同动作。主要用机器人数据预训练的 VLA，不能自然把人的行为当成可执行的机器人监督。

### 用一个例子理解

理解用例（非论文实验）：输入人把杯子移到托盘的视频和另一批机器人示范，两者无需逐段配对。几何对齐帮助对应杯子与目标位置，共享动作潜变量表达搬运行为，再由机器人侧解码器生成自身可执行的动作。

## 创新点或方法

直接共同训练容易要求两类数据使用不合适的统一接口。H2RB 在观测端用几何锚定对齐，让人和机器人的表示具有可对应的基础；在动作端共享潜变量，用分离的解码器处理各自动作映射。训练使用未配对示范，意图保留预训练先验并吸收人类行为监督；部署输出机器人动作，具体解码和训练损失摘要未说明。

### 方法如何工作

1. 读取未配对的人类和机器人示范，获得两种身体下的观测与动作监督。
2. 用几何锚定对齐观测表示，减少相同场景关系因视角和身体不同而难以对应的问题。
3. 让动作共享潜变量，同时保留分离解码映射，使共同行为不必对应同一组动作数值。
4. 共同适配预训练 VLA，再在机器人上执行并测试物体、技能及摆放变化下的迁移。

### 必要术语

- 未配对示范：两类演示没有逐条对应关系；训练不能依靠同步动作配对。
- 几何锚定对齐：借助几何信息建立观测对应；具体锚定方式摘要未展开。
- 动作潜变量：动作的内部编码；这里用于共享行为信息。
- 分离解码器：将共享编码转换为不同身体的动作；避免强迫人和机器人使用同一映射。

## 证据

摘要报告真机任务中，物体迁移表现从 8.0 提高到 51.8，技能迁移得分达到 62.7，而共同训练基线未能迁移人类示范技能。物体摆放变化下，分布外迁移从 6.0 提高到 45.3。摘要没有定义这些分数的单位、统计方式、任务数量和示范预算，因此不能直接称为成功率或百分点提升。

## 局限

真机结果支持所测任务中的迁移效果，但不能据此判断任意人类视频都能使用。几何信息如何获取、需要多少目标机器人示范，以及两项设计各贡献多少，都是影响复用成本的待核查问题。

- **判断**：值得读到两个接口的实现和分别消融；这决定它究竟减少了多少机器人数据需求，以及额外几何处理是否划算。

## 研究关联

可借鉴的是把共享内容限定为行为层面的信息，同时允许不同身体使用不同动作映射。尝试跨身体复用数据时，观测对齐与动作兼容需要一起检查，仅把两种示范放进同一训练集可能不够。

### 下一步读哪里

先核查几何锚点来自什么传感器或估计器，再看动作潜变量的学习目标、解码器如何分离，以及固定机器人示范预算下加入人类数据的收益。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-05/Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Pretrained Vision-Language-Action (VLA) policies provide a strong starting point for deployment, but adapting them to a target robot and environment still requires costly embodiment-specific demonstrations. Human demonstrations are far easier to collect, yet directly leveraging them is challenging due to the substantial human-robot embodiment gap, particularly when the underlying VLA has been pretrained primarily on robot data. We introduce H2RB (Human-To-Robot Bridge), a human-robot co-training framework for adapting pretrained VLA policies from unpaired human and robot demonstrations. H2RB bridges the embodiment gap at both interfaces: geometry-anchored alignment grounds human and robot observations in a compatible representation, while a decoupled-decoder tokenizer shares action latents without forcing both domains through a single action mapping. This design allows human demonstrations to provide useful behavioral supervision while retaining the rich visual, semantic, and control priors of the pretrained VLA. Across real-world tasks, H2RB substantially improves object transfer performance from 8.0 to 51.8 and enables skill transfer to score 62.7, in settings where co-train baselines totally fail to transfer human-demonstrated skills. The benefit also persists under object-placement shifts, improving out-of-distribution transfer from 6.0 to 45.3. H2RB suggests a way for human demonstrations to serve as a scalable supervision source for adapting pretrained robotic policies, reducing the dependence on costly target-robot data collection.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.04391v1
- Authors: Junhyeong Park, Wook Jung, Taeyoung Kim, Huiwon Jang, Jinwoo Shin
- Published: 2026-11-03T06:24:29Z
- Age days: 1

</details>
