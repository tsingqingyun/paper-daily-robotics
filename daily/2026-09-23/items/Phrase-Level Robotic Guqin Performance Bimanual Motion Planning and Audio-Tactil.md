---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24133v1"
published: "2026-09-21T05:39:04Z"
age_days: 1
score: 39
created: 2026-09-23
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Phrase-Level Robotic Guqin Performance: Bimanual Motion Planning and Audio-Tactile Interaction Monitoring

> [!summary] 先说人话（基于摘要）
> 这套古琴机器人把连续乐句拆成需要精确配合的双手接触事件，并结合触觉监测和声音校准完成演奏。难点不只是手臂不碰撞，还包括何时拨弦、何时按触以及发出什么声音。

## 问题

古琴弦距小，右手拨弦短促、左手泛音接触持续，要求不对称双臂协作；仅实现无碰轨迹无法保证时序和声学结果。

## 创新点或方法

将演奏建模为离散事件与连续运动的混合问题，分层协调手指分配、构型连续性、避障和接触时序，并加入视觉定位、触觉接触监测及听觉反馈驱动的拨弦参数校准。

## 证据

真实古琴上演奏含25个事件的乐句，覆盖散音和七徽泛音序列；重复试验报告两项事件正确率为93.6%和96.8%。

## 局限

结果范围是一个25事件乐句；事件正确率不等于整段演奏成功率，也不足以说明跨曲目泛化。

- **判断**：适合选读规划与监测细节，作为精细双臂系统案例，而非通用策略能力证据。

## 研究关联

对具身系统和评测有价值：把动作成功进一步约束为接触时序与声学结果，可借鉴其多模态监测设计；对通用VLA训练的直接贡献有限。

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/Phrase-Level Robotic Guqin Performance Bimanual Motion Planning and Audio-Tactil.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent advances in humanoid robotics and embodied intelligence have enabled robots to perform increasingly complex manipulation tasks. However, musical instrument performance remains a formidable benchmark, demanding not only collision-free trajectory execution but also precise contact timing, asymmetric bimanual coordination, and target acoustic outcomes on physical instruments. The guqin, a seven-string fretless zither, presents unique manipulation challenges due to its millimetric string spacing, transient right-hand plucking, and sustained left-hand harmonic contacts. In this work, we present a physical heterogeneous dual-arm robotic system for phrase-level autonomous guqin performance. We formulate guqin playing as a hybrid discrete--continuous execution problem and develop a hierarchical planning framework that coordinates working finger assignment, configuration continuity, obstacle avoidance, and tight bimanual contact schedules across consecutive musical events. The system integrates vision-guided instrument localization, tactile-based harmonic contact monitoring, and auditory feedback-informed plucking parameter calibration. Real-world experiments on a 25-event phrase demonstrate that the system reliably executes coordinated open-string and seventh-hui harmonic sequences on a physical guqin, achieving 93.6% and 96.8% event correctness across repeated trials.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24133v1
- Authors: Zhen Wang, Zhiheng Chen, Tianyuan Bao, Tianwei Zhang
- Published: 2026-09-21T05:39:04Z
- Age days: 1

</details>
