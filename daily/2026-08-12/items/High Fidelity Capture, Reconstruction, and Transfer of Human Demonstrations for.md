---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09127v1"
published: "2026-08-10T05:07:08Z"
age_days: 1
score: 27
created: 2026-08-12
concepts: ["机器人学习", "具身智能评测与基准"]
---

# High Fidelity Capture, Reconstruction, and Transfer of Human Demonstrations for Robot-Assisted Bathing

> [!summary] 一句话结论（基于摘要）
> We present a straightforward, but effective framework for doing so with high fidelity by utilizing contact regions as a key processing primitive.

## 关键点

- **问题**：Despite the demand for robots in high-value clinical tasks like bathing, contemporary systems still lack the safety and reliability required for complex, sustained physical interaction with humans.
- **创新点 / 方法**：We present a straightforward, but effective framework for doing so with high fidelity by utilizing contact regions as a key processing primitive.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-12/High Fidelity Capture, Reconstruction, and Transfer of Human Demonstrations for.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Despite the demand for robots in high-value clinical tasks like bathing, contemporary
systems still lack the safety and reliability required for complex, sustained physical
interaction with humans. A key challenge hindering the development of such systems is
that collecting, understanding, and effectively transferring highly dynamic, contact-
rich human bathing demonstrations is difficult, even with modern motion and tactile
sensing equipment. We present a straightforward, but effective framework for doing so
with high fidelity by utilizing contact regions as a key processing primitive. We use
our framework to build a dataset of bathing demonstrations performed by trained
clinicians on human subjects. We then use this dataset to design and control an arm-
mounted dexterous soft hand to perform bathing tasks on a mannequin using open- and
closed-loop strategies. Our dataset is the first to provide high quality synchronized
motion, shape, contact, and force during sustained, contact-rich human-human
interaction, and our transfer strategies demonstrate effective use of these data across
multiple levels of the robotics stack. All relevant materials will be publicly released
to enable further advancements in physical human-robot interaction (pHRI) research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09127v1
- Authors: Arjun S. Lakshmipathy, Jonathan P. King, Ethan Zuo, Rohit Satishkumar, Hongyi Chen, Jeffrey Ichnowski, Dan Ding, Zackory Erickson, Nancy S. Pollard
- Published: 2026-08-10T05:07:08Z
- Age days: 1

</details>
