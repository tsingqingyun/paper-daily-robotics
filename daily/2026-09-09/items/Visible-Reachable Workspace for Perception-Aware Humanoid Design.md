---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08905v1"
published: "2026-09-08T15:40:05Z"
age_days: 0
score: 34
created: 2026-09-09
concepts: ["具身智能评测与基准"]
---

# Visible-Reachable Workspace for Perception-Aware Humanoid Design

> [!summary] 先说人话（基于摘要）
> VRW衡量机器人在真正伸手操作的姿态下，目标是否也能被看见。论文用可独立转动的相机扩大“看得见且够得着”的区域，并减少为看清目标而产生的身体运动。

## 问题

传统工作空间只衡量末端可达性，但某个可达目标在实际到达姿态下可能被遮挡，迫使机器人转动传感器或身体；单看可达范围无法反映视觉引导操作的成本。

## 创新点或方法

在可行到达构型下计算可见性，并扩展为多个分离工作区域的同时可见性指标。用搭载独立驱动RGB-D相机的31自由度人形机器人验证相机布局与驱动方式。

## 证据

相机可动使可见可达覆盖率从38%升至97%；第二台相机使成对覆盖率从0.45升至0.95，第三台仅升至0.97。同机固定相机对照下，双目标任务平均耗时减少17%、机械能耗减少19%；硬件展示无需躯干转向的前后及左右目标操作。


## 局限

覆盖率与收益依赖目标分布和构型约束，双目标测试的17%与19%收益不应直接外推到全部操作任务。

- **判断**：值得精读指标定义和同机对照，设计变量与任务收益之间的证据链较清楚。

## 研究关联

对具身评测的价值是把感知构型纳入能力度量，帮助区分策略失败与硬件视野限制，也能指导相机数量和布局选择。

- **概念**：具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/Visible-Reachable Workspace for Perception-Aware Humanoid Design.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Workspace analysis measures where a robot can place its end effector. For visually guided manipulation, reachability alone is insufficient: a kinematically reachable target may not be visible in the specific pose required to reach it. The robot must then redirect its sensing or move its body to acquire a view, turning a perception limitation into additional motion. Existing humanoids largely inherit this limitation when copying human form factors. We introduce the visible-reachable workspace (VRW), a design-stage measure that conditions visibility on feasible reaching configurations and extends it to concurrent visibility of spatially separated work regions. We apply VRW by building a 31-DoF humanoid with independently actuated RGB-D cameras. On the same robot, camera articulation increases visible-reachable coverage from 38% to 97%. With actuated camera layouts, a second camera raises pairwise coverage from 0.45 to 0.95, while a third changes it only to 0.97. In a controlled two-target reach-and-grasp benchmark, our dual-actuated design reduces mean completion time by 17% and mechanical energy by 19% relative to the same robot with its cameras fixed. Hardware experiments demonstrate simultaneous observation and manipulation of front/back and left/right target pairs without torso reorientation. The results suggest that reachability becomes a more informative design quantity for perception-driven humanoid manipulation when it is evaluated together with the sensing configurations that make the reachable space observable. We will open-source all software and the humanoid hardware design. Our website is https://generalroboticslab.com/DukeHumanoidv2

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08905v1
- Authors: Boxi Xia, Zijiang Yang, Ryan Shin, Bokuan Li, Eric Wun-Hao Lu, Jacob Lee, Jiaxun Liu, Boyuan Chen
- Published: 2026-09-08T15:40:05Z
- Age days: 0

</details>
