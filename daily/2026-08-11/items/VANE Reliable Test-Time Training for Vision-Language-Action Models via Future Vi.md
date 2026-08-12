---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09448v1"
published: "2026-08-10T11:22:54Z"
age_days: 0
score: 32
created: 2026-08-11
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# VANE: Reliable Test-Time Training for Vision-Language-Action Models via Future Visual Representation Prediction

> [!summary] 一句话结论（基于摘要）
> On SimplerEnv WidowX, VANE improves average success by $3.2$ percentage points over the corresponding TTT baseline.

## 关键点

- **问题**：Test-time training (TTT) offers a lightweight way to adapt vision--language--action (VLA) policies from unlabeled deployment streams, but it remains difficult to use reliably in closed-loop manipulation.
- **创新点 / 方法**：We introduce a reliable TTT framework for VLA policies (VANE).
- **证据**：On SimplerEnv WidowX, VANE improves average success by $3.2$ percentage points over the corresponding TTT baseline.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-11/VANE Reliable Test-Time Training for Vision-Language-Action Models via Future Vi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Test-time training (TTT) offers a lightweight way to adapt vision--language--action
(VLA) policies from unlabeled deployment streams, but it remains difficult to use
reliably in closed-loop manipulation. A shared adaptation space can mix incompatible
task corrections, while an online update can alter subsequent actions before its
consequences are known. We introduce a reliable TTT framework for VLA policies (VANE).
VANE conditions prompt adaptation on the current vision--language context and learns
from the future visual consequences of executed actions. Candidate updates are isolated
from the live policy, evaluated on subsequent observations, and committed only when
supported by future evidence, making adaptation selective and reversible. On SimplerEnv
WidowX, VANE improves average success by $3.2$ percentage points over the corresponding
TTT baseline. Results on Google Robot further show that deployment-time gains remain
task- and embodiment-dependent. Together, these results demonstrate a constrained,
evidence-based approach to adapting VLA policies during interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09448v1
- Authors: Hongjin Ji, Guoyang Xia, Luoyang Sun, Fangxiang Feng, Lei Ren
- Published: 2026-08-10T11:22:54Z
- Age days: 0

</details>
