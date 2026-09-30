---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23968v1"
published: "2026-09-21T00:41:02Z"
age_days: 1
score: 41
created: 2026-09-23
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation

> [!summary] 先说人话（基于摘要）
> Opt2VLA让人形机器人不仅知道“往哪里动”，还知道“该用多大力”。VLA同时输出运动目标和接触力参考，再由全身控制器执行。

## 问题

接触密集任务中，相似轨迹可能需要不同用力方式，接触后视觉也可能失效；仅预测几何目标、依靠运动跟踪的系统缺少明确的力调节接口。

## 创新点或方法

单个多任务VLA联合预测运动目标与连续接触力，由任务专用RL全身控制器跟踪；使用带显式力参考的全身轨迹优化生成动力学可行、接触一致的监督。

## 证据

在3项人形接触任务上，显式力条件比纯运动控制具有更准确、一致的力调节；轨迹优化提供的力矩监督进一步改善跟踪与稳定性。仿真和硬件展示语言条件下的力调制；摘要未给出可核查的结果数字。

## 局限

底层控制器是任务专用的，需核查新增任务的控制器需求，以及轨迹优化监督对实际接触条件的覆盖。

- **判断**：做全身接触控制值得精读，重点看力命令如何生成、跟踪和验证。

## 研究关联

对接触型VLA和机器人学习，核心价值是明确语义策略与物理控制之间的力接口；摘要没有提供直接的世界模型贡献。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/Opt2VLA Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid robots are expected to perform diverse human-level tasks in daily environments, many of which require precise regulation of interaction forces. While recent vision-language-action (VLA) models have shown promise for semantic planning and visuomotor control, existing humanoid systems primarily represent actions through geometric motion goals and rely on whole-body controllers focused on motion tracking, with limited explicit reasoning or control of interaction forces. This limitation is particularly relevant in contact-rich tasks, where geometrically similar motions may require different force regimes depending on the task context and where visual observations may become unreliable after contact. In this work, we present Opt2VLA, a force-aware VLA framework that introduces explicit force commands at the VLA-to-control interface for humanoid whole-body manipulation. A single multi-task VLA policy jointly predicts both geometric motion goals and continuous contact-force references, which are tracked by task-specific reinforcement learning (RL)-based whole-body controllers. To provide scalable and physically grounded supervision, we generate dynamically feasible and contact-consistent training data via whole-body trajectory optimization (TO) with explicit force references. We evaluate Opt2VLA on three contact-rich humanoid tasks and show that explicit force conditioning enables more accurate and consistent force regulation than motion-only control, while physically grounded torque supervision from TO further improves force tracking accuracy and stability. Closed-loop evaluations further demonstrate language-conditioned force modulation with Opt2VLA in simulation and on humanoid hardware.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23968v1
- Authors: Fukang Liu, Yipu Chen, Jaehwi Jang, Danfei Xu, Zsolt Kira, Ye Zhao
- Published: 2026-09-21T00:41:02Z
- Age days: 1

</details>
