---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26544v1"
published: "2026-08-27T02:35:30Z"
age_days: 3
score: 24
created: 2026-08-31
concepts: ["多模态基础模型"]
---

# Chart2SVG: Editable SVG Generation from Raster Chart Images

> [!summary] 先说人话（基于摘要）
> Chart2SVG 把栅格图表恢复为结构化、带语义且可编程编辑的 SVG，而不仅追求像素复刻。它在视觉语言模型中加入图表语义 token，并用 Chart Structure Graph 暴露元素依赖关系。

## 这篇到底在做什么

- **卡在哪里**：静态图表图像缺少原始结构，普通重建即使外观相似，也可能不知道坐标轴、标记和文本的功能角色，因而无法可靠编辑、复用布局或交互探索。
- **关键解法**：模型输入栅格图表、输出规范组织的 SVG；图表专用语义 token 同时编码几何原语与功能角色，Beagle+ 提供结构蒸馏样本，专用目标和渲染感知后训练改善外观与结构。CSG 进一步表示视觉依赖。
- **拿什么证明**：Beagle+ 含 3.3 万个规范化、结构蒸馏的图表样本。摘要称重建保真度和下游编辑效用显著超过基线，但未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对多模态基础模型研究者，它是从视觉识别走向结构化生成和工具可操作输出的清晰案例；与机器人和世界模型没有直接价值。
- **先别急着信**：需核查复杂图表类型、文本识别错误和 SVG 结构正确性的评测方式；仅凭渲染相似度不能证明可编辑性。
- **判断**：做文档智能或结构化视觉生成者值得精读；具身研究者可略读，因为任务关联较弱。

## 研究关联

- **概念**：[[多模态基础模型]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/Chart2SVG Editable SVG Generation from Raster Chart Images.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present Chart2SVG, a multimodal large language model that converts static raster charts into structurally organized, semantically enriched SVGs that support programmatic editing. By incorporating chart-specific semantic tokens into a vision-language model, Chart2SVG captures both geometric primitives and their functional roles. To support robust structural recovery, we introduce Beagle+, a dataset of 33K canonicalized and structurally distilled chart samples. Our approach combines specialized training objectives with a rendering-aware post-training phase, producing SVGs that are both visually accurate and structurally consistent. To facilitate higher-level manipulations, we construct a Chart Structure Graph (CSG) that exposes visual dependencies, enabling tasks such as interactive exploration, chart repurposing, and layout reuse. Experiments show that Chart2SVG substantially outperforms baselines in reconstruction fidelity and downstream editing utility, advancing the development of intelligent and interactive visualization tools.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26544v1
- Authors: Jinning Cui, Lu Chen, Haoyan Shi, Yue He, Chenglong Wang, Mengyu Zhou, Weidong Huang, Yunhai Wang
- Published: 2026-08-27T02:35:30Z
- Age days: 3

</details>
