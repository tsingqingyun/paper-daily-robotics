---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23675v1"
published: "2026-06-22T17:58:03Z"
age_days: 1
score: 34
created: 2026-06-24
concepts: ["AI 核心知识地图"]
---

# IMAGIN-4D: Image-Guided Controllable Interaction Generation

> [!summary] 一句话结论（基于摘要）
> Experiments on FBM and BEHAVE show that IMAGIN-4D improves fine- grained interaction control over single-token and uniformly image-conditioned baselines while preserving waypoint-following and motion quality.

## 关键点

- **问题**：However, these signals underspecify interaction: the same prompt and trajectory can produce different grasps, approach directions, body poses, object poses, contacts, and body-object layouts.
- **创新点 / 方法**：Since HOI motion datasets lack paired images, we build a synthetic motion-to-image rendering pipeline from FullBodyManipulation (FBM) and introduce an image-adherence metric to evaluate whether generated motions match the reference snapshot.
- **证据**：Experiments on FBM and BEHAVE show that IMAGIN-4D improves fine- grained interaction control over single-token and uniformly image-conditioned baselines while preserving waypoint-following and motion quality.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-24/IMAGIN-4D Image-Guided Controllable Interaction Generation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generating human-object interactions (HOI) is central to character animation, robotics,
AR/VR, and embodied AI. Recent HOI generation methods synthesize motion from text,
object geometry, and sparse waypoints, controlling action semantics and object
trajectories. However, these signals underspecify interaction: the same prompt and
trajectory can produce different grasps, approach directions, body poses, object poses,
contacts, and body-object layouts. We address this ambiguity with a reference image as a
visual specification of the desired interaction snapshot. However, a single global image
representation conflates distinct cues and conditions all frames on identical visual
evidence. We therefore introduce IMAGIN-4D, a diffusion-based HOI generator that
decomposes image conditioning spatio-temporally. For spatial conditioning, IMAGIN-4D
extracts supervised interaction-state tokens for body pose, object pose, body-object
contact, and spatial relationships at the depicted frame. For temporal conditioning, it
computes frame-aware tokens by querying image patches per generated frame, allowing
sequence segments to attend to different visual cues from the same image. To balance
image, text, and waypoint cues, IMAGIN-4D uses role-aware conditioning: text, waypoints,
and interaction-state tokens use separate AdaLN streams, while frame-aware visual tokens
cross-attend with motion tokens. Since HOI motion datasets lack paired images, we build
a synthetic motion-to-image rendering pipeline from FullBodyManipulation (FBM) and
introduce an image-adherence metric to evaluate whether generated motions match the
reference snapshot. Experiments on FBM and BEHAVE show that IMAGIN-4D improves fine-
grained interaction control over single-token and uniformly image-conditioned baselines
while preserving waypoint-following and motion quality. Code and models will be released
at https://imagin4d.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23675v1
- Authors: Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch, Tomas Hodan, Michael J. Black, Dimitrios Tzionas, Shreyas Hampali
- Published: 2026-06-22T17:58:03Z
- Age days: 1

</details>
