---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15890v1"
published: "2026-07-17T12:05:07Z"
age_days: 2
score: 37
created: 2026-07-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Exo2EgoPose: Leveraging Exocentric Demonstrations for Vision-Language guided Egocentric 3D Hand Pose Forecasting

> [!summary] 一句话结论（基于摘要）
> Extensive experiments on \textit{AssemblyHands}, \textit{Ego-Exo4D}, and our newly constructed \textit{EgoMe-pose} benchmarks show the superiority of our method, which outperforms state-of-the-art methods by a large margin.

## 关键点

- **问题**：However, previous studies either rely mainly on under-informed visual inputs to predict coarse human motions or follow the VRM/VLA paradigm, which suffers from insufficient robot data and the gap between human and robot embodiments.
- **创新点 / 方法**：To overcome the limited field-of-view and highly dynamic motions in the Ego view, we propose a framework dubbed Exo2EgoPose, which innovatively leverages holistic and stable exocentric (Exo) demonstrations as guidance to compensate for partial and dynamic Ego-view cues.
- **证据**：Extensive experiments on \textit{AssemblyHands}, \textit{Ego-Exo4D}, and our newly constructed \textit{EgoMe-pose} benchmarks show the superiority of our method, which outperforms state-of-the-art methods by a large margin.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Perceiving multimodal cues and forecasting fine-grained actions from an egocentric (Ego)
perspective is vital for applications like robot manipulation. However, previous studies
either rely mainly on under-informed visual inputs to predict coarse human motions or
follow the VRM/VLA paradigm, which suffers from insufficient robot data and the gap
between human and robot embodiments. We observe that 3D hand pose naturally serves as a
unified representation to bridge human-robot actions. Hence, we investigate an under-
explored Vision-Language guided Egocentric 3D Hand Pose Forecasting (VL-EHPF) task,
which aims to predict future Ego 3D hand poses from visual observations, a language
instruction, and pose states. To overcome the limited field-of-view and highly dynamic
motions in the Ego view, we propose a framework dubbed Exo2EgoPose, which innovatively
leverages holistic and stable exocentric (Exo) demonstrations as guidance to compensate
for partial and dynamic Ego-view cues. Specifically, we introduce a Dual-level
Exocentric Reconstruction Module (DERM), which incorporates the paired Exo videos as
supervision to reconstruct their video-level and chunked frame-level representations,
thereby modeling spatial contexts and temporal dynamics. Then, the Global-to-Local
Modulation Module (GLMM) utilizes the reconstructed hierarchical Exo representations for
progressive feature refinement via attention mechanisms and adaptive modulation,
enabling comprehensive Exo guidance for accurate Ego hand pose forecasting. Extensive
experiments on \textit{AssemblyHands}, \textit{Ego-Exo4D}, and our newly constructed
\textit{EgoMe-pose} benchmarks show the superiority of our method, which outperforms
state-of-the-art methods by a large margin. Moreover, it demonstrates an effective
human-to-robot transfer capability and yields improvements on the \textit{CALVIN}
dataset. Code will be released.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15890v1
- Authors: Zhaofeng Shi, Heqian Qiu, Lanxiao Wang, Xiang Li, Hongliang Li
- Published: 2026-07-17T12:05:07Z
- Age days: 2

</details>
