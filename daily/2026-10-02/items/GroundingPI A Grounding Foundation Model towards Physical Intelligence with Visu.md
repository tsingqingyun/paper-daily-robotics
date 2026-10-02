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
url: "https://arxiv.org/abs/2609.39601"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 46
created: 2026-10-02
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives

> [!summary] 这篇论文到底做了什么（基于摘要）
> GroundingPI 把“按描述找到目标，并准确指出位置”作为专门能力训练，用统一词表输出点和框的离散坐标。它再充当机器人和驾驶模型的视觉骨干，让后续决策获得更精确的目标定位信息。

## 问题

机器人需要在杂乱场景里定位小物体，还要及时更新位置以支持闭环控制。摘要指出，VLA 和世界—动作模型沿用通用视觉语言或视频生成骨干，在这些条件下仍会失准；理解场景内容并不自动意味着能准确指出该操作哪里。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“拿起钥匙旁的小螺母”→模型依据描述定位螺母，输出点或框→下游控制器结合深度与机器人状态计算抓取动作；定位输出本身不是完整抓取轨迹。

## 创新点或方法

旧做法从通用视觉能力出发，本文把定位本身放进预训练核心：将点、框坐标离散化，纳入共享词表，训练模型生成位置。训练包含多模态与空间预训练、监督微调及 GRPO 强化学习，监督来自公开数据和专门的数据引擎。推理时可输出定位结果，也可作为下游视觉骨干；如何把内部特征接入动作模型、强化学习奖励如何定义，摘要未说明。

### 方法如何工作

1. 把定位监督表示为点和框的离散坐标，使空间位置成为模型可直接生成的内容。
2. 结合多模态与空间预训练，再做监督微调和强化学习，让识别目标与输出位置共同受训练约束。
3. 将所得模型用于定位，或接入下游动作系统；摘要只说明到骨干替换，具体特征接口仍待核查。

### 必要术语

- 定位（grounding）：把语言所指落实到图像位置；本文的核心训练能力。
- 量化坐标：用有限离散值表示位置；使点和框能进入共享词表。
- 开环评估：在固定记录上比较预测与参考轨迹；本文驾驶指标不直接衡量闭环驾驶表现。

## 证据

摘要报告：4B 模型在涵盖 11 类感知能力的 34 个定位基准上，与 44 个基线比较，平均成绩为 73.68%，GPT-6 Astra 为 71.54%；平均指标的聚合方式未给出。RoboTwin 2.0 的四种分布外设置均优于所测主流骨干，相对最强骨干最多提高 24.8%。RoboCasa-GR1 上，使用 50% 演示超过使用 75% 演示的基线。nuScenes 开环平均 L2 误差为 0.296 米，但未给对应基线数值。这支持所测任务中的迁移收益，不能据此确定真机闭环可靠性。

## 局限

定位准确是否也足够快，是这里影响实用性的待核查问题：摘要强调闭环需求，却未报告延迟。下游收益还需结合训练预算、骨干接入方式和数据控制判断；驾驶的开环误差不包含车辆行动改变后续观测的影响。

- **判断**：值得重点读坐标表示、数据配方和下游对照设置，因为最可借鉴的是如何把感知训练目标对准行动瓶颈。

## 研究关联

当动作失败源于目标选错、位置偏差时，可以先改视觉训练数据与定位监督。摘要的数据配方分析尤其提示密集定位值得检查；OCR 的作用仍被表述为潜在促进因素，不能直接当作通用配方。

### 下一步读哪里

先核查坐标量化精度及小目标误差，再看密集定位、OCR 的消融是否控制数据量，最后检查四种分布外设置、推理延迟和下游训练预算。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：46
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/GroundingPI A Grounding Foundation Model towards Physical Intelligence with Visu.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.39601v1 Announce Type: cross Abstract: Precise grounding matters. It specifies which object is the target and where that object is, even in clutter and for tiny objects, and it has to be fast enough for closed-loop control. Yet vision-language-action (VLA) and world-action models (WAMs) take perception from general-purpose vision-language and video-generation backbones, which still fail in these settings. We introduce GroundingPI, a 4B grounding foundation model that generates points and boxes as quantized coordinates in a shared vocabulary. Training combines multimodal and spatial pretraining, supervised fine-tuning, and reinforcement learning with GRPO, using supervision from public datasets and dedicated data engines. Against 44 baselines across 34 grounding benchmarks spanning 11 perceptual capabilities, GroundingPI establishes a new state of the art, averaging 73.68%, above the larger GPT-6 Astra (71.54%). As a downstream visual backbone, GroundingPI improves performance on robotic manipulation and autonomous driving. On RoboTwin 2.0, it outperforms every mainstream backbone we evaluate in all four out-of-distribution settings, by up to 24.8% relative to the strongest backbone. On RoboCasa-GR1, GroundingPI trained with 50% of the demonstrations outperforms those baselines trained with 75%. On nuScenes, used as the visual backbone, GroundingPI attains an average open-loop L2 error of 0.296 m. We systematically analyze GroundingPI's pretraining in scale and data composition. Downstream autonomous driving and robotic manipulation improve as the pretraining is scaled. Analyzing the data recipe across these 11 perceptual capabilities shows dense grounding's substantial benefits for both, and OCR's potential as a catalyst for perceptual learning. These results support grounding as a perceptual foundation, and dedicated perceptual pretraining as a promising direction for foundation models of physical intelligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.39601
- Authors: Qize Yu, Lianrui Fan, Boyu Chen, Jiaqi Liang, Xini Ding, Yue Chen, Zetian Song, Yuran Wang, Yi Zou, Kaixuan Wang, Tianxing Chen, Wenxuan Song, Bohan Zhou, Mingleyang Li, Siqiao Huang, Yuqi Ye, Caigao Jiang, Wei Wei, Ruihai Wu, Hang Zhang, Yixiao Ge, Shuchang Zhou, Shilong Liu, Xianming Liu, Ping Luo, Shiyu Huang
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
