---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15714v1"
published: "2026-07-17T07:51:03Z"
age_days: 2
score: 35
created: 2026-07-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# AC-VLA: Robust Out-of-Distribution Action Execution via Compositional Learning

> [!summary] 一句话结论（基于摘要）
> Instantiated on $π_{0.5}$ and evaluated on LIBERO and LIBERO-OOD benchmarks, AC-VLA achieves a ~28% absolute improvement on compositional OOD tasks while maintaining near-perfect in- distribution performance.

## 关键点

- **问题**：Vision-Language-Action (VLA) models excel at end-to-end robotic manipulation but struggle with out-of-distribution (OOD) generalization when familiar sub-tasks are recombined in unseen configurations.
- **创新点 / 方法**：To address both, we introduce \textbf{AC-VLA}, a plug-and-play Action Compositional learning framework comprising two architecture-agnostic components: \textbf{(i)} a compositional learning module that uses an LLM-driven instruction decomposer and a proprioceptive trajectory aligner to generate dense sub-task supervis…
- **证据**：Instantiated on $π_{0.5}$ and evaluated on LIBERO and LIBERO-OOD benchmarks, AC-VLA achieves a ~28% absolute improvement on compositional OOD tasks while maintaining near-perfect in- distribution performance.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-20/AC-VLA Robust Out-of-Distribution Action Execution via Compositional Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models excel at end-to-end robotic manipulation but
struggle with out-of-distribution (OOD) generalization when familiar sub-tasks are
recombined in unseen configurations. We identify two mutually reinforcing failure modes:
\emph{trajectory overfitting}, where models overfit to holistic trajectory patterns
rather than compositional sub-skill semantics; and \emph{perceptual shortcut}, where
action tokens over-rely on wrist-view textures at the expense of global spatial
grounding. To address both, we introduce \textbf{AC-VLA}, a plug-and-play Action
Compositional learning framework comprising two architecture-agnostic components:
\textbf{(i)} a compositional learning module that uses an LLM-driven instruction
decomposer and a proprioceptive trajectory aligner to generate dense sub-task
supervision, followed by mixed training on complete demonstrations and decomposed data
to endow the model with compositional generalization; and \textbf{(ii)} a state-
conditioned asymmetric masking strategy that suppresses wrist-view inputs during closed-
gripper phases, enforcing global semantic grounding. All components are architectural
modification-free and directly integrable into any VLA backbone. Instantiated on
$π_{0.5}$ and evaluated on LIBERO and LIBERO-OOD benchmarks, AC-VLA achieves a ~28%
absolute improvement on compositional OOD tasks while maintaining near-perfect in-
distribution performance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15714v1
- Authors: Xiaojiang Peng, Kai Peng, Jie Lu, Zheng Lian, Zitong YU, Xiaobo Wang
- Published: 2026-07-17T07:51:03Z
- Age days: 2

</details>
