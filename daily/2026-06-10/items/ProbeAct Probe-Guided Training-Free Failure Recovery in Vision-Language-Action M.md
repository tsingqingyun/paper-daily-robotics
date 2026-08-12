---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.09740v1"
published: "2026-06-08T17:04:24Z"
age_days: 1
score: 42
created: 2026-06-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# ProbeAct: Probe-Guided Training-Free Failure Recovery in Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Evaluated on the LIBERO-plus benchmark, our framework acts as18 a universal safety net, improving the success rate of the OpenVLA-OFT model19 from 69.6% to 74.1%, while demonstrating broad applicability to both base and20 fine-tuned VLA policies.

## 关键点

- **问题**：Vision-Language-Action (VLA) models demonstrate strong perfor-1 mance on language- conditioned robotic manipulation within their training dis-2 tribution, yet their generalization capabilities remain fundamentally limited.
- **创新点 / 方法**：We propose PROBEACT, a training-free runtime intervention frame-6 work that detects and recovers from grasping and placement failures in pre-7 trained VLA policies without modifying their weights or requiring additional8 demonstrations.
- **证据**：Evaluated on the LIBERO-plus benchmark, our framework acts as18 a universal safety net, improving the success rate of the OpenVLA-OFT model19 from 69.6% to 74.1%, while demonstrating broad applicability to both base and20 fine-tuned VLA policies.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-10/ProbeAct Probe-Guided Training-Free Failure Recovery in Vision-Language-Action M.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models demonstrate strong perfor-1 mance on language-
conditioned robotic manipulation within their training dis-2 tribution, yet their
generalization capabilities remain fundamentally limited. They3 lack the robustness
required to handle perturbations, frequently failing when con-4 fronted with lighting
changes, altered camera viewpoints, or small initial-state5 variations. We propose
PROBEACT, a training-free runtime intervention frame-6 work that detects and recovers
from grasping and placement failures in pre-7 trained VLA policies without modifying
their weights or requiring additional8 demonstrations. PROBEACT combines three
components: (i) a lightweight multi-9 target hidden-state probe that predicts the 3D
positions of task-relevant objects10 from intermediate VLA features, with Hungarian-
matched identity tracking for11 multi-object scenes; (ii) an object-agnostic kinematic
state machine that detects12 grasp, transport, and placement failures using only
gripper-internal signals and13 end-effector kinematics; and (iii) a hierarchical Control
Barrier Function (CBF)14 filter that encodes repeated-failure locations as soft safe-set
constraints, mini-15 mally correcting VLA actions while preserving baseline behavior. As
a plug-and-16 play, training-free intervention loop, PROBEACT is orthogonal to existing
train-17 ing pipelines. Evaluated on the LIBERO-plus benchmark, our framework acts as18
a universal safety net, improving the success rate of the OpenVLA-OFT model19 from 69.6%
to 74.1%, while demonstrating broad applicability to both base and20 fine-tuned VLA
policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.09740v1
- Authors: Fan Zhang, Seongbin Park, Baharan Mirzasoleiman, Shariar Talebi, Nader Sehatbakhsh
- Published: 2026-06-08T17:04:24Z
- Age days: 1

</details>
