---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24511v1"
published: "2026-09-21T12:51:29Z"
age_days: 1
score: 32
created: 2026-09-23
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality

> [!summary] 先说人话（基于摘要）
> InsertAnything让机器人只在仿真中学会精密插入，再直接用于真实零件。策略结合目标位姿与指尖三维力反馈，一边寻找对准位置，一边修正插入动作。

## 问题

小间隙插入对定位误差敏感，容易碰撞或卡住；零件形状和间隙变化又让策略难以复用。

## 创新点或方法

采用纯仿真RL，利用解耦门控奖励协调对准和插入，并以力信号平滑及不依赖状态的标准差稳定学习；部署不使用真实示范或策略微调。

## 证据

真实实验最小名义间隙为0.02毫米，孔位误差下成功率改善且接触峰值力降低。ManipulationNet人在环协议下达20/20，插入动作全自主；仅用仿真六边形任务训练的单策略，在8项未见真实插入任务上总成功率95.0%。

## 局限

20/20属于人在环协议，需核查人工参与边界及目标位姿来源；0.02毫米是名义间隙，不能直接当作感知或定位精度。

- **判断**：值得精读真实实验协议与跨几何测试，精密接触迁移的证据较具体。

## 研究关联

对机器人学习和Sim2Real，展示了以紧凑力反馈支撑精密接触迁移与跨几何复用的路径；它不直接验证学习式世界模型。

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/InsertAnything Generalizable Contact-Rich Precision Insertion from Simulation to.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Contact-rich precision insertion is a key manipulation skill in robotic assembly. Tight clearances make insertion more sensitive to alignment errors and prone to collisions and jamming, while variations in geometry and clearance across parts further complicate policy reuse. We present a reinforcement learning framework that trains insertion policies entirely in simulation for direct deployment without real-world demonstrations or policy fine-tuning. By combining target poses with compact three-dimensional fingertip force feedback, the policy learns to search for alignment and correct its motion despite errors in the estimated hole position. A decoupled gated reward coordinates alignment and insertion. Force-signal smoothing and state-independent standard deviations stabilize the learning process. The resulting policies perform real-world insertion across multiple hole geometries with a minimum nominal clearance of 0.02 mm and improve success while reducing peak contact forces under hole-position errors. Cross-clearance and cross-geometry evaluations further confirm policy generalization. The system achieved the first perfect score of 20/20 on ManipulationNet's peg-in-hole benchmark under its Human-in-the-Loop protocol, with fully autonomous insertion motions. A single policy trained only on a simulated hexagonal insertion task achieved an overall success rate of 95.0% across eight unseen real-world insertion tasks. These results show that learning entirely in simulation can yield precision insertion skills that can be deployed directly and reused across real-world tasks. The project website (https://mzhsoul.github.io/InsertAnything/) provides open-source simulation and real-robot experiment scripts, assets, and trained checkpoints.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24511v1
- Authors: Zhenghua Ma, Xinpan Meng, Zeyu Liu, Muyuan Ma, Hengdi Zhang, Houcheng Li, Long Cheng
- Published: 2026-09-21T12:51:29Z
- Age days: 1

</details>
