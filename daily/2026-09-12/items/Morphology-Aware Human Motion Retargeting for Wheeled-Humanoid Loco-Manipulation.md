---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11357v1"
published: "2026-09-10T10:40:31Z"
age_days: 1
score: 29
created: 2026-09-12
concepts: ["智能体 Agent"]
---

# Morphology-Aware Human Motion Retargeting for Wheeled-Humanoid Loco-Manipulation

> [!summary] 先说人话（基于摘要）
> 这套流程把人类动作转换为轮式人形机器人的移动与操作行为。关键是把人类腿部动作重新分配给轮式底盘和躯干，同时保住手臂的操作几何。

## 问题

已有重定向主要面向有腿人形机器人；R1 Pro没有腿关节，人类下肢运动无法直接映射，且底盘移动必须与躯干和双臂协调。

## 创新点或方法

输入多数据集SMPLX动作，经体型规范化、底盘归一化、形态感知微分逆运动学、肩部层级映射及躯干替代生成参考运动；规划层输出受连续性和执行器限制约束的轮命令，再于Isaac Lab训练21维BaseDecode策略。

## 证据

摘要描述了从人体动作到物理跟踪的完整流程，但未给出可核查的结果数字，并明确将定量策略比较留待后续版本。


## 局限

缺少定量比较，无法据摘要判断跟踪精度、失败边界或真实硬件执行效果。

- **判断**：有R1 Pro或类似形态需求可读实现细节，否则等待定量结果更合适。

## 研究关联

对轮式人形机器人学习有直接数据转化价值；与research_links中的通用Agent关联较弱，核心贡献是具身映射与控制。

- **概念**：智能体 Agent
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/Morphology-Aware Human Motion Retargeting for Wheeled-Humanoid Loco-Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human-to-humanoid retargeting has largely been studied on legged platforms, while comparatively few wheeled-humanoid systems support coupled locomotion and manipulation from general human motion. Building on GMR's configurable general-motion retargeting and BeyondMimic's physically simulated R1 Pro learning framework, we present a reproducible pipeline that converts multi-dataset SMPLX motion into executable loco-manipulation behavior for the Galaxea R1 Pro wheeled humanoid. The robot has a planar three-wheel base, a serial torso, and two arms but no leg joints, so human lower-body motion must be redistributed across base motion and torso posture without sacrificing manipulation-relevant arm geometry. Our pipeline combines canonical body-shape preprocessing, planar-base normalization, morphology-aware differential inverse kinematics, shoulder-rooted hierarchical arm retargeting, and continuous torso substitution for bending and squatting. A reference-twist-driven planning layer then decodes planar base motion into continuous three-wheel steering and rolling commands subject to hysteresis, kinematic continuity, acceleration, and actuator-rate limits. Finally, a 21-dimensional BaseDecode policy is trained in Isaac Lab with directional joint-limit scaling, focused upper-body tracking, and a staged wheel-contact reward. The resulting system provides a complete bridge from human motion data to physically trackable wheeled-humanoid loco-manipulation rather than a visualization-only retargeter; quantitative policy comparisons remain scheduled for a later revision.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11357v1
- Authors: Chenbo Xia, Chao Ye
- Published: 2026-09-10T10:40:31Z
- Age days: 1

</details>
