---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19769v1"
published: "2026-06-18T04:10:16Z"
age_days: 1
score: 39
created: 2026-06-20
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI

> [!summary] 一句话结论（基于摘要）
> We develop three insights.

## 关键点

- **问题**：Second, its value depends on physical coherence: multimodal streams are reusable only when timing, coordinate frames, calibration, kinematics, units, and synchronization assumptions remain inspectable.
- **创新点 / 方法**：We develop three insights.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/Data Standards for Humanoid Robotics The Missing Infrastructure for Physical AI.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The scalability of humanoid robots will depend not only on models and hardware, but also
on whether physical experience can accumulate across robots, tasks, organizations, and
time. Drawing on the authors' work in developing ISO/WD 26264-1, Humanoid robot datasets
-- Part 1: General requirements, within ISO/TC 299/WG 16, this article argues that data
standards are becoming foundational infrastructure for Physical AI. We develop three
insights. First, humanoid robot data is embodied interaction data, not a collection of
isolated digital samples; a useful dataset must preserve the relationship among robot
body, action, task, scene, execution trace, and outcome. Second, its value depends on
physical coherence: multimodal streams are reusable only when timing, coordinate frames,
calibration, kinematics, units, and synchronization assumptions remain inspectable.
Third, the main bottleneck is not only data scarcity, but non-cumulative data caused by
high collection costs, data silos, and inconsistent evaluation. We argue that humanoid
robot data standards address these bottlenecks by making embodied experience
interpretable, shareable, traceable, and reusable. A general standard should provide
horizontal infrastructure for lifecycle management, metadata, provenance, quality,
versioning, and traceability, while capability-specific parts should define domain
grammar for manipulation, locomotion, human-robot interaction, cognition, and future
humanoid capabilities. As AI moves from screens into bodies, data standards must evolve
from organizing digital information to structuring physical interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19769v1
- Authors: Shaoshan Liu, Xiugong Qin, Xuan Wu, Xuan Xia, Ning Ding, Jialu Liu, Jie Tang
- Published: 2026-06-18T04:10:16Z
- Age days: 1

</details>
