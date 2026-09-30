---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26645v1"
published: "2026-08-27T05:58:06Z"
age_days: 2
score: 32
created: 2026-08-30
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> FLARE用“Retry + Reset”给 VLA 加恢复能力：轻微偏差由带扰动和桥接段的策略自行重试，破坏任务状态的严重失败则由监控器调用专门复位技能。

## 这篇到底在做什么

- **卡在哪里**：VLA多从单调、无失败的完美轨迹学习，遇到漏抓、掉落或碰撞便偏离训练分布；普通策略既缺少局部纠偏经验，也不会把已破坏环境恢复到可继续执行的状态。
- **关键解法**：Retry在演示中加入扰动及解耦机器人位姿与环境状态的桥接段；Reset先由 MLLM 离线分析视频定位 OOD 状态，再针对性采集少量物体中心复位技能。推理时在线 MLLM 在主任务与复位技能间仲裁。
- **拿什么证明**：摘要称接触丰富的困难任务实验中，成功率与鲁棒性显著提高；没有给出任务数、成功率或复位数据量等可核查数字。

## 值不值得读

- **和你的研究有什么关系**：对 VLA 和 Agent 系统，价值在于把故障按可继续纠偏与必须恢复环境两级处理，比单纯重规划更贴近真实机器人运行。
- **先别急着信**：最需核查在线 MLLM 的故障检测准确率、延迟和误触发代价，以及“少量”复位技能能覆盖多大故障空间。
- **判断**：概念很实用，建议读系统设计；是否值得复现，要等全文的恢复成功率和监控器误判数据。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/FLARE A Failure-Aware Framework for Autonomous Correction and Recovery in Visual.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action Models~(VLAs) have demonstrated significant promise in generalizing to complex, long-horizon robotic manipulation tasks. However, their performance remains brittle, as they are typically trained on trajectory-monotonic, failure-free demonstrations. This reliance on ``perfect" data leaves them unable to recover from common execution errors, such as a missed grasp, a dropped object, or an unexpected collision. In this paper, we propose FLARE, a novel framework that endows VLAs with robust error recovery capabilities through a ``Retry" and ``Reset" paradigm. First, we introduce a ``Retry" mechanism by injecting perturbation and bridging segments that decouple robot pose from environment state into demonstrations, enabling the policy to autonomously handle execution deviations. Second, to address critical, state-breaking (OOD) failures, we introduce a ``Reset" pipeline. We leverage an MLLM for offline failure analysis to automatically identify OOD states from execution videos. This analysis enables the efficient, targeted collection of a small library of object-centric ``Reset" skills, which are trained to restore the environment to a task-valid state. Our full framework integrates these learned policies. At inference, an online MLLM monitor arbitrates between task execution and ``Reset" skills. Experiments on challenging, contact-rich manipulation tasks show our approach significantly improves task success and robustness.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26645v1
- Authors: Ganlong Zhao, Zijia Tang, Xingping Chen, Zhanghui Kuang, Ye Tian, Guanbin Li
- Published: 2026-08-27T05:58:06Z
- Age days: 2

</details>
