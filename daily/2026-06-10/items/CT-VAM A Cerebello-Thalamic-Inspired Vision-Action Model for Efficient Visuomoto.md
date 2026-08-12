---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09572v1"
published: "2026-06-08T14:46:43Z"
age_days: 1
score: 33
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control

> [!summary] 一句话结论（基于摘要）
> With only 68M parameters, CT-VAM achieves LIBERO success rates competitive with substantially larger VLA models, while reducing inference latency.

## 关键点

- **问题**：Vision-language-action models have shown strong promise for robot manipulation, yet raw language is primarily needed to specify task intent rather than to be repeatedly processed during high-frequency low-level execution.
- **创新点 / 方法**：Motivated by this separation, we propose a cerebello-thalamic-inspired vision-action model (CT-VAM) for efficient task- conditioned visuomotor control.
- **证据**：With only 68M parameters, CT-VAM achieves LIBERO success rates competitive with substantially larger VLA models, while reducing inference latency.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/CT-VAM A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomoto.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action models have shown strong promise for robot manipulation, yet raw
language is primarily needed to specify task intent rather than to be repeatedly
processed during high-frequency low-level execution. Motivated by this separation, we
propose a cerebello-thalamic-inspired vision-action model (CT-VAM) for efficient task-
conditioned visuomotor control. CT-VAM acts as a compact local execution policy that
predicts action chunks from dualview visual observations, proprioception, and a
lightweight task condition, potentially enabling a practical cloud-edge paradigm in
which high-level semantic reasoning can be handled by large models while fast closed-
loop control runs on local hardware. To fuse heterogeneous inputs effectively, CT-VAM
introduces TARS (Thalamic Action Routing Stream), a stream-separated conditional
attention decoder that independently routes action, visual and task streams, preventing
dense sensory tokens from overwhelming compact task-relevant conditions. With only 68M
parameters, CT-VAM achieves LIBERO success rates competitive with substantially larger
VLA models, while reducing inference latency. Together with flow-consistent inpainting
for asynchronous chunk execution, CT-VAM supports high-frequency control and
demonstrates robust realworld deployment on resource-constrained robotic platforms.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09572v1
- Authors: Jiacheng Li, Yize Guo, Jiabin Guo, Qingchen Liu, Jiahu Qin
- Published: 2026-06-08T14:46:43Z
- Age days: 1

</details>
