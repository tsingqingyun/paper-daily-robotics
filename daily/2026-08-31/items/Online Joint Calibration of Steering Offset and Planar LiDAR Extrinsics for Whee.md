---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26789v1"
published: "2026-08-27T08:19:06Z"
age_days: 3
score: 23
created: 2026-08-31
concepts: ["具身智能评测与基准"]
---

# Online Joint Calibration of Steering Offset and Planar LiDAR Extrinsics for Wheeled Mobile Robots

> [!summary] 先说人话（基于摘要）
> 该方法用 EKF 在机器人运行过程中联合估计转向零偏和二维 LiDAR—车体外参，替代手动“看起来走直”和长期信任 CAD 外参的做法。

## 这篇到底在做什么

- **卡在哪里**：仓储移动机器人的转向偏置或 LiDAR 外参漂移会造成蛇形、摆动和横向误差；人工设零与静态 CAD 标定在维护后容易失效，且不适合安全关键运行。
- **关键解法**：在自行车运动学模型中，把转向偏置和 LiDAR 平面外参纳入 EKF 状态，根据在线观测联合更新，输出持续校正的标定参数，区别于一次性离线或人工标定。
- **拿什么证明**：摘要称真实数据实验中，修正转向偏置显著降低横向跟踪误差，但没有给出误差数值、数据规模或外参估计精度；摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对仓储机器人部署与评测，它能减少维护后标定漂移导致的控制退化；对 VLA、世界模型或学习算法研究的直接价值有限。
- **先别急着信**：标题强调联合标定，但摘要只明确报告转向偏置对 CTE 的改善；LiDAR 外参的可观测性和定量精度最需全文核查。
- **判断**：移动机器人标定工程者可读，其他人浏览即可；问题实用，但摘要证据不足以证明“联合”部分的完整效果。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/Online Joint Calibration of Steering Offset and Planar LiDAR Extrinsics for Whee.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Accurate steering sensing and LiDAR-to-vehicle extrinsics are crucial for reliable path tracking in warehouse mobile robots (WMRs); miscalibration often leads to snaking, weaving, and elevated cross-track error (CTE). In practice, steering ``zero'' is commonly set manually (e.g., eyeballing straightness via a PS4 joystick), while LiDAR extrinsics are assumed from CAD and may drift after maintenance. Such static, manual procedures frequently cause miscalibration in safety-critical environments. This paper presents an Extended Kalman Filter (EKF)--based method for online estimation of steering offset and planar LiDAR extrinsics within a bicycle-kinematics model, providing a principled alternative to manual calibration. Experiments on real datasets show that correcting steering offset reduces CTE substantially, validating the effectiveness of the proposed approach.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26789v1
- Authors: Subodh Mishra, Arindam Dhar, Suprotim Majumdar, Naveen Arulselvan
- Published: 2026-08-27T08:19:06Z
- Age days: 3

</details>
