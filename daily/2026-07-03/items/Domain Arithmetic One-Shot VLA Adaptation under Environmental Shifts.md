---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.00666v1"
published: "2026-07-01T09:13:40Z"
age_days: 1
score: 32
created: 2026-07-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts

> [!summary] 一句话结论（基于摘要）
> In both simulated and real- world experiments, DART outperforms existing VLA adaptation methods in one-shot scenarios across diverse visual and embodiment shifts.

## 关键点

- **问题**：Vision-Language-Action (VLA) models often fail to perform the same learned tasks under environmental shifts, such as changes in camera pose and shifts to a different but similar robot (e.g., from Panda to UR5e).
- **创新点 / 方法**：To reduce the burden of data curation and training, we propose an analogy-based method that adapts VLA models under environmental shifts through weight vector arithmetic with domain-specific information addition, named Domain ARiThmetic (DART).
- **证据**：In both simulated and real- world experiments, DART outperforms existing VLA adaptation methods in one-shot scenarios across diverse visual and embodiment shifts.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-03/Domain Arithmetic One-Shot VLA Adaptation under Environmental Shifts.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models often fail to perform the same learned tasks under
environmental shifts, such as changes in camera pose and shifts to a different but
similar robot (e.g., from Panda to UR5e). Adapting these models to the shifted
environment (i.e., target domain) often requires training on multiple demonstrations for
each task, which are costly to collect. To reduce the burden of data curation and
training, we propose an analogy-based method that adapts VLA models under environmental
shifts through weight vector arithmetic with domain-specific information addition, named
Domain ARiThmetic (DART). Unlike prior approaches, DART requires collecting only a
single demonstration, enabling efficient adaptation. To accurately isolate domain-
specific information for addition, DART performs subspace alignment between singular
components in weight vectors to filter out noisy components. In both simulated and real-
world experiments, DART outperforms existing VLA adaptation methods in one-shot
scenarios across diverse visual and embodiment shifts. Code is available at
https://github.com/snumprlab/dart.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.00666v1
- Authors: Taewook Kang, Taeheon Kim, Donghyun Shin, Jonghyun Choi
- Published: 2026-07-01T09:13:40Z
- Age days: 1

</details>
