---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19784v1"
published: "2026-06-18T04:36:57Z"
age_days: 1
score: 37
created: 2026-06-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Instantiated on GR00T~N1.5 and evaluated across four LIBERO suites, CALVIN ABCD$\to$D, and five real- robot tasks on Mobile ALOHA, \textsc{EquiVLA} achieves $92.6\%$ average success on LIBERO (vs.

## 关键点

- **问题**：Vision-Language-Action (VLA) models have emerged as a powerful paradigm for generalist robot manipulation, yet they lack geometric inductive biases: policies trained at specific orientations require substantially more data to generalize across rotational configurations.
- **创新点 / 方法**：We present \textsc{EquiVLA}, the first general framework for end-to-end $\mathrm{SO}(2)$-equivariant VLA models, applicable to any architecture coupling a frozen vision-language backbone with a flow-matching Diffusion Transformer action head.
- **证据**：Instantiated on GR00T~N1.5 and evaluated across four LIBERO suites, CALVIN ABCD$\to$D, and five real- robot tasks on Mobile ALOHA, \textsc{EquiVLA} achieves $92.6\%$ average success on LIBERO (vs.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/EquiVLA A General Framework for Rotationally Equivariant Vision-Language-Action.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for generalist
robot manipulation, yet they lack geometric inductive biases: policies trained at
specific orientations require substantially more data to generalize across rotational
configurations. We present \textsc{EquiVLA}, the first general framework for end-to-end
$\mathrm{SO}(2)$-equivariant VLA models, applicable to any architecture coupling a
frozen vision-language backbone with a flow-matching Diffusion Transformer action head.
\textsc{EquiVLA} introduces \textsc{EquiPerceptor}, which produces approximately
$\mathrm{SO}(2)$-equivariant visual representations from frozen ViT features; and
\textsc{EquiActor}, an exactly $\mathrm{SO}(2)$-equivariant flow-matching Diffusion
Transformer action head. Together, they establish an approximate $\mathrm{SO}(2)$
equivariance chain from camera observations to predicted action sequences. Instantiated
on GR00T~N1.5 and evaluated across four LIBERO suites, CALVIN ABCD$\to$D, and five real-
robot tasks on Mobile ALOHA, \textsc{EquiVLA} achieves $92.6\%$ average success on
LIBERO (vs. $78.1\%$ baseline), an average sequence length of $4.03$ on CALVIN (vs.
$3.45$), and improves real-robot success from $54\%$ to $72\%$.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19784v1
- Authors: Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho, Long Dinh, Minh Duc Nguyen, Gia-Binh Nguyen, Pham Tri Quang, Minh N. Vu, Duy M. H. Nguyen, An Thai Le, Ngo Anh Vien
- Published: 2026-06-18T04:36:57Z
- Age days: 1

</details>
