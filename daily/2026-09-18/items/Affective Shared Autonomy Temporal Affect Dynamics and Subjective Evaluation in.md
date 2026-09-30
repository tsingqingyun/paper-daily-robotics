---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19802v1"
published: "2026-09-17T07:14:18Z"
age_days: 0
score: 31
created: 2026-09-18
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# Affective Shared Autonomy: Temporal Affect Dynamics and Subjective Evaluation in Bimanual Teleoperation Tasks

> [!summary] 先说人话（基于摘要）
> 这项共享自主遥操作系统根据操作者持续出现的不良状态决定何时帮忙，而不是只看机械臂是否偏离目标。

## 问题

高难度双臂遥操作会造成认知负担、挫败和执行中断。传统共享自主主要依赖空间误差等任务规则，可能在不合适的时候介入，因为它不了解操作者的即时状态。

## 创新点或方法

融合面部视频、心脏信号和双臂运动，输出七类情感状态分布及中性、有效、不良三类操作状态；持续检测到不良状态时才触发辅助，减少对有效投入的打断。

## 证据

30人用户研究中，有效状态最多增加39.7%，摘要称未损害用户自主感。多模态融合模型在时序状态追踪上优于Qwen和MiniCPM-V零样本基线，并采集了连续多模态遥操作数据集。

## 局限

需核查情感状态标注、39.7%的计算口径，以及自主感如何测量；有效状态增加不等同于任务成功率提高。

- **判断**：人机协作与遥操作方向值得精读用户研究，纯VLA控制方向可重点浏览辅助触发机制。

## 研究关联

对机器人学习和具身评测，价值在于把操作者状态纳入交互系统评价；对世界模型研究的直接贡献不明确。

- **概念**：[[多模态基础模型]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/Affective Shared Autonomy Temporal Affect Dynamics and Subjective Evaluation in.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physical teleoperation integrates human cognitive flexibility with robotic precision, yet demanding manipulation tasks frequently induce severe cognitive workload, acute frustration, and execution breakdown. Conventional shared autonomy paradigms rely primarily on task-based rules, such as spatial error boundaries, which disregard the operator's transient affective state and risk misaligned control interventions. To address this limitation, we propose an affect-aware shared autonomy teleoperation framework that dynamically modulates robotic assistance based on real-time operator state estimation. The system estimates operator affective states from synchronized facial video, cardiac signals, and bilateral arm kinematics, outputting a seven-state affective distribution and a three-category operational abstraction (neutral, productive, adverse). Affect-aware assistance is selectively triggered when the user is detected in a continuous adverse state, preserving task-positive engagement without unnecessary disruption. The empirical user study ($N = 30$) confirms that the proposed affective assistance increases the productive states by up to 39.7% without compromising user agency. The collected dataset represents the first multimodal dataset that provides continuous visual, physiological, and operator's bilateral motion tracking of temporal affective state shifts during bimanual teleoperation. Our multimodal fusion model outperforms zero-shot baselines (Qwen, MiniCPM-V) in tracking temporal state dynamics. This real-world deployment offers a new human-centric framework that integrates visual, physiological, and motion tracking for physical human-robot interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19802v1
- Authors: Zhengji Liang, Guiyin Tian, Sijin Qu, Hainan Liu, Shiyan Hu
- Published: 2026-09-17T07:14:18Z
- Age days: 0

</details>
