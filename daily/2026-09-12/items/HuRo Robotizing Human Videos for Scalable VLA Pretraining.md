---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10706v1"
published: "2026-09-09T18:02:05Z"
age_days: 2
score: 39
created: 2026-09-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# HuRo: Robotizing Human Videos for Scalable VLA Pretraining

> [!summary] 先说人话（基于摘要）
> HuRo把人类视频同时转换成机器人视角的观测和动作轨迹，让VLA能从更大规模的人类活动中预训练。关键是共同处理视觉与动作的跨具身差异。

## 问题

真实机器人数据昂贵，人类视频虽丰富，却与机器人观测和动作空间不一致。已有方法或依赖任务匹配的视频，或在规模化处理中分别解决视觉和动作对齐。

## 创新点或方法

流水线接收异构、标注程度不同的人类视频，推断缺失中间信号，生成机器人对齐的观测与重定向动作，用于VLA端到端预训练。

## 证据

数据来自五个人类视频源，约63万段episode、1.42亿处理帧。四项真实操作任务中，扩大预训练规模使总体完成率从51.5%升至80.3%，空间与视觉偏移下的OOD完成率从34.9%升至72.2%；消融支持视觉转换及动作监督的作用。


## 局限

真实任务仅四项；需核查数据转换质量、规模对照设置，以及这些收益对任务和具身的依赖。

- **判断**：值得精读流水线和规模实验，是本批次中数据路线证据较直接的一篇。

## 研究关联

为VLA研究者提供了扩大预训练数据的具体路径，并把数据规模收益与真实机器人泛化联系起来。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/HuRo Robotizing Human Videos for Scalable VLA Pretraining.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human video datasets have emerged as a compelling alternative to expensive real-robot data, offering rich diversity at scale. To bridge the human-to-robot embodiment gap, existing approaches either robotize videos in task-matched settings or address observation and action alignment separately at scale. In this work, we systematically examine whether robotized human videos can provide effective and scalable supervision for pretraining vision-language-action (VLA) policies. To this end, we develop a robotization pipeline that converts heterogeneous human videos into robot-aligned observations and action trajectories while inferring missing intermediate signals across annotation levels. Using this pipeline, we construct the HuRo dataset, comprising about 630K robotized episodes and 142M processed frames from five human-video sources. Across four real-world manipulation tasks, increasing robotized pretraining scale improves overall completion from 51.5% to 80.3% and OOD completion under spatial and visual shifts from 34.9% to 72.2%. Ablations further show that visual robotization improves OOD robustness and that end-to-end pretraining with retargeted actions outperforms visual-only transfer. Code and data are released on our website: https://3587jjh.github.io/HuRo.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10706v1
- Authors: Jinho Jeong, Se June Joo, Jaehyun Kang, Dongyun Kim, Yena Kim, Hanjung Kim, Seon Joo Kim
- Published: 2026-09-09T18:02:05Z
- Age days: 2

</details>
