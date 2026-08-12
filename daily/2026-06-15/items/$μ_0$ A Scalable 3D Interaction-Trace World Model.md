---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13769v1"
published: "2026-06-11T17:59:56Z"
age_days: 3
score: 36
created: 2026-06-15
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# $μ_0$: A Scalable 3D Interaction-Trace World Model

> [!summary] 一句话结论（基于摘要）
> Experiments show that $μ_0$ outperforms baselines in both 2D and 3D trace prediction, including trace prediction models and tokenized VLM methods.

## 关键点

- **问题**：World models that capture how actions induce physical change enable scalable robot learning without reliance on embodiment-specific action labels.
- **创新点 / 方法**：We present $μ_0$, a scalable world model based on 3D traces.
- **证据**：Experiments show that $μ_0$ outperforms baselines in both 2D and 3D trace prediction, including trace prediction models and tokenized VLM methods.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World models that capture how actions induce physical change enable scalable robot
learning without reliance on embodiment-specific action labels. Pixel-space video models
provide broad visual priors but expend model capacity on dense appearance
reconstruction, while direct action models require embodiment-specific labels that
hinder scalability. We present $μ_0$, a scalable world model based on 3D traces. Rather
than predicting dense pixels or directly modeling actions, $μ_0$ forecasts smooth 3D
trajectories for salient interaction points such as objects, tools, hands, and contact
regions, yielding a compact, embodiment-agnostic motion interface. To enable training
from diverse video sources, our TraceExtract system automatically extracts 3D
supervision by selecting keypoints, constructing globally aligned traces, and
associating motion segments with hierarchical language captions. This TraceExtract
supervision pretrains $μ_0$ by combining a pretrained vision-language backbone with a
modular trace expert, which represents each query via B-spline control points and
predicts future traces. Experiments show that $μ_0$ outperforms baselines in both 2D and
3D trace prediction, including trace prediction models and tokenized VLM methods.
Because $μ_0$ is frozen and reusable, it can be paired with action experts for
downstream robot embodiments. Despite action-free pretraining, the resulting trace-
conditioned policies achieve performance competitive with VLA models pretrained with
action supervision, such as $π_0$. These results establish 3D traces as a scalable and
transferable representation for cross-embodiment manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13769v1
- Authors: Seungjae Lee, Yoonkyo Jung, Jusuk Lee, Jonghun Shin, Amir Hossein Shahidzadeh, Yao-Chih Lee, H. Jin Kim, Jia-Bin Huang, Furong Huang
- Published: 2026-06-11T17:59:56Z
- Age days: 3

</details>
