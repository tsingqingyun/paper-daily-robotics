---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.27042v1"
published: "2026-11-20T03:14:26Z"
age_days: 3
score: 37
created: 2026-11-24
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RoboColiseum: Co-evolution of Simulation, Evaluation, and Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RoboColiseum 把真机命令回放到仿真里，检查机器人和物体是否呈现相近的反应。它也把机器人评测拆成不同能力赛道，记录系统完成了多少、用了多少执行额度。

## 问题

仿真里关节跟得准，可能只是控制器纠偏强，接触、负载和抓取结果仍可能与真机不同。刚体和软物体还需要不同的物理表示。与此同时，排行榜总分容易掩盖系统在哪类操作上失败，以及成功靠了多少次动作调用。[S2](https://arxiv.org/html/2611.27042v1#S1.p1.1) [S3](https://arxiv.org/html/2611.27042v1#S1.p2.1) [S4](https://arxiv.org/html/2611.27042v1#S1.p3.1)[S15](https://arxiv.org/html/2611.27042v1#S2.SS3.p2.1)

### 用一个例子理解

理解用例（非论文实验）——评估机械臂把海绵放入窄槽。输入真机的关节命令和海绵观测，在仿真中回放并检查末端位置、海绵变形和是否放入。随后让待测策略运行，输出对准与放入的阶段得分、动作额度和最终完成情况。

## 创新点或方法

作者先用录下的真机命令做校准回放，分阶段估计摩擦、惯量等参数，把位置、力矩和任务结果分别检查。仿真运行时，物理后端发布位姿、时间和变形几何，渲染器据此生成模型所见的画面。执行评测时，任务检查器分别记录中间进度、动作预算和最终完成。Agent2Act 接收语言模型生成的控制命令，VLA 则先做混合任务监督微调再执行评测。[S6](https://arxiv.org/html/2611.27042v1#S2.SS2.p2.1)[S15](https://arxiv.org/html/2611.27042v1#S2.SS3.p2.1)[S19](https://arxiv.org/html/2611.27042v1#S3.p1.1) [S20](https://arxiv.org/html/2611.27042v1#S3.SS1.p1.1) [S21](https://arxiv.org/html/2611.27042v1#S3.SS1.p2.1)[S35](https://arxiv.org/html/2611.27042v1#S4.SS5.p1.1) [S36](https://arxiv.org/html/2611.27042v1#S4.SS5.p1.2) [S37](https://arxiv.org/html/2611.27042v1#S4.SS5.p2.1)[S45](https://arxiv.org/html/2611.27042v1#S5.SS3.p2.1)

### 方法如何工作

1. 记录真机命令和传感观测，再在仿真里执行同一串命令，把比较锚定到相同输入。
2. 用不同运动辨识不同物理参数，并同时检查位置、力矩、任务完成，避免只看跟踪误差。
3. 把物理状态和变形几何传给渲染器，生成与仿真时刻对应的观测供系统执行。
4. 对每条赛道记录检查点和预算内完成情况，再按具体能力解释分数差异。

### 必要术语

- 系统辨识：从机器人对给定命令的反应估计物理参数；本文用它校准仿真动力学。
- 命令回放：在仿真中重发真机记录的控制命令；用于对比同一输入下的运动和交互结果。
- 预算计分：把动作资源限制纳入阶段与完成评价；用于区分效率和任务进度。

## 证据

22 组同机器人、同任务的真机与仿真配对分数，皮尔逊相关系数为 0.9686，表明这些配置的分数有很强的线性关联。[S1](https://arxiv.org/html/2611.27042v1#abstract1.1)[S39](https://arxiv.org/html/2611.27042v1#S5.F8) 第一季选列的 12 个策略中，Prime-0 总分最高，为 77.54，空间推理领先的却是总分 76.92 的 HiDream-O1-Embodied。[S40](https://arxiv.org/html/2611.27042v1#S5.SS2.p1.1) [S41](https://arxiv.org/html/2611.27042v1#S5.T2) [S42](https://arxiv.org/html/2611.27042v1#S5.T2.2) [S43](https://arxiv.org/html/2611.27042v1#S5.T2.3) [S44](https://arxiv.org/html/2611.27042v1#S5.SS2.p2.1) 第二季覆盖全部 11 个公开系统，但训练、任务覆盖和资源统计存在差异。[S1](https://arxiv.org/html/2611.27042v1#abstract1.1)[S46](https://arxiv.org/html/2611.27042v1#S5.SS3.p3.1)

## 局限

作者指出公开榜单缺少完整的逐案例分母、推理调用数和独立重复的不确定性。[S48](https://arxiv.org/html/2611.27042v1#S6.p2.1) 对配对实验，我会核查不同机器人组各自的分数偏差及组内排序。整体高相关本身无法回答绝对分差有多大，也无法隔离校准步骤的因果贡献。

- **判断**：值得细读校准验证和执行计分协议，榜单适合按目标赛道查阅，因为总分会掩盖能力差异。

## 研究关联

当仿真用于筛选候选机器人方案时，可以先问关键物理交互的真机与仿真差多少，再看各赛道的分数。这样既能发现模拟接触偏差，也能避免用综合排名挑错擅长特定操作的系统。

### 下一步读哪里

先看 [S15](https://arxiv.org/html/2611.27042v1#S2.SS3.p2.1) [S16](https://arxiv.org/html/2611.27042v1#S2.SS3.p3.1) [S17](https://arxiv.org/html/2611.27042v1#S2.SS3.p4.fig1) [S18](https://arxiv.org/html/2611.27042v1#S2.F5) 如何分别检查轨迹误差和任务完成，再看 [S39](https://arxiv.org/html/2611.27042v1#S5.F8) 图 8 的拟合线与等值线。解释榜单前用 [S35](https://arxiv.org/html/2611.27042v1#S4.SS5.p1.1) [S36](https://arxiv.org/html/2611.27042v1#S4.SS5.p1.2) [S37](https://arxiv.org/html/2611.27042v1#S4.SS5.p2.1)[S46](https://arxiv.org/html/2611.27042v1#S5.SS3.p3.1)[S48](https://arxiv.org/html/2611.27042v1#S6.p2.1) 核对预算和统计口径。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.27042v1
- 获取时间：2026-11-24T01:58:55.568956+00:00
- [S1] [RoboColiseum: Co-evolution of Simulation, Evaluation, and ModelsThanks: *These authors contributed equally. †Corresponding authors. · 正文段落 1](https://arxiv.org/html/2611.27042v1#abstract1.1)
- [S2] [I Introduction · 正文段落 2](https://arxiv.org/html/2611.27042v1#S1.p1.1)
- [S3] [I Introduction · 正文段落 3](https://arxiv.org/html/2611.27042v1#S1.p2.1)
- [S4] [I Introduction · 正文段落 4](https://arxiv.org/html/2611.27042v1#S1.p3.1)
- [S5] [I Introduction · 正文段落 5](https://arxiv.org/html/2611.27042v1#S1.p4.1)
- [S6] [II-B System Identification · 正文段落 15](https://arxiv.org/html/2611.27042v1#S2.SS2.p2.1)
- [S7] [II-B System Identification · 正文段落 21](https://arxiv.org/html/2611.27042v1#S2.E5)
- [S8] [II-B System Identification · 正文段落 22](https://arxiv.org/html/2611.27042v1#S2.SS2.p3.3)
- [S9] [II-B System Identification · 正文段落 23](https://arxiv.org/html/2611.27042v1#S2.SS2.p4.1)
- [S10] [II-B System Identification · 正文段落 24](https://arxiv.org/html/2611.27042v1#S2.SS2.p5.fig1.1)
- [S11] [II-B System Identification · 正文段落 25](https://arxiv.org/html/2611.27042v1#S2.SS2.p5.fig1)
- [S12] [II-C Simulation Calibration and Validation · 正文段落 26](https://arxiv.org/html/2611.27042v1#S2.SS3.p1.1)
- [S13] [II-C Simulation Calibration and Validation · 正文段落 27](https://arxiv.org/html/2611.27042v1#S2.E6)
- [S14] [II-C Simulation Calibration and Validation · 正文段落 28](https://arxiv.org/html/2611.27042v1#S2.SS3.p1.2)
- [S15] [II-C Simulation Calibration and Validation · 正文段落 29](https://arxiv.org/html/2611.27042v1#S2.SS3.p2.1)
- [S16] [II-C Simulation Calibration and Validation · 正文段落 30](https://arxiv.org/html/2611.27042v1#S2.SS3.p3.1)
- [S17] [II-C Simulation Calibration and Validation · 正文段落 31](https://arxiv.org/html/2611.27042v1#S2.SS3.p4.fig1)
- [S18] [II-C Simulation Calibration and Validation · 正文段落 32](https://arxiv.org/html/2611.27042v1#S2.F5)
- [S19] [III Composable Physics and Rendering · 正文段落 33](https://arxiv.org/html/2611.27042v1#S3.p1.1)
- [S20] [III-A Decoupled Architecture and RoboColiseum Protocol · 正文段落 34](https://arxiv.org/html/2611.27042v1#S3.SS1.p1.1)
- [S21] [III-A Decoupled Architecture and RoboColiseum Protocol · 正文段落 35](https://arxiv.org/html/2611.27042v1#S3.SS1.p2.1)
- [S22] [III-A Decoupled Architecture and RoboColiseum Protocol · 正文段落 36](https://arxiv.org/html/2611.27042v1#S3.SS1.p3.fig1)
- [S23] [IV-A Season I: Foundational Tracks · 正文段落 45](https://arxiv.org/html/2611.27042v1#S4.SS1.p3.1)
- [S24] [IV-B Season II: Task Design · 正文段落 49](https://arxiv.org/html/2611.27042v1#S4.SS2.p1.1)
- [S25] [IV-B Season II: Task Design · 正文段落 50](https://arxiv.org/html/2611.27042v1#S4.T1)
- [S26] [IV-B Season II: Task Design · 正文段落 54](https://arxiv.org/html/2611.27042v1#S4.SS2.p4.1)
- [S27] [IV-B1 Dexterous Manipulation · 正文段落 56](https://arxiv.org/html/2611.27042v1#S4.SS2.SSS1.p2.1)
- [S28] [IV-B2 Whole-Body Coordination · 正文段落 59](https://arxiv.org/html/2611.27042v1#S4.SS2.SSS2.p1.1)
- [S29] [IV-B4 Cross-Embodiment Transfer · 正文段落 68](https://arxiv.org/html/2611.27042v1#S4.SS2.SSS4.p3.1)
- [S30] [IV-C Task Authoring, Initialization, and Controlled Variation · 正文段落 69](https://arxiv.org/html/2611.27042v1#S4.SS3.p1.1)
- [S31] [IV-C Task Authoring, Initialization, and Controlled Variation · 正文段落 70](https://arxiv.org/html/2611.27042v1#S4.SS3.p2.1)
- [S32] [IV-C Task Authoring, Initialization, and Controlled Variation · 正文段落 71](https://arxiv.org/html/2611.27042v1#S4.SS3.p3.1)
- [S33] [IV-D Leaderboard Protocol and Evaluation Integrity · 正文段落 72](https://arxiv.org/html/2611.27042v1#S4.SS4.p1.1)
- [S34] [IV-D Leaderboard Protocol and Evaluation Integrity · 正文段落 74](https://arxiv.org/html/2611.27042v1#S4.SS4.p3.1)
- [S35] [IV-E Scoring and Execution Budgets · 正文段落 75](https://arxiv.org/html/2611.27042v1#S4.SS5.p1.1)
- [S36] [IV-E Scoring and Execution Budgets · 正文段落 77](https://arxiv.org/html/2611.27042v1#S4.SS5.p1.2)
- [S37] [IV-E Scoring and Execution Budgets · 正文段落 78](https://arxiv.org/html/2611.27042v1#S4.SS5.p2.1)
- [S38] [V-A System Identification and Real2Sim Evaluation · 正文段落 89](https://arxiv.org/html/2611.27042v1#S5.F7)
- [S39] [V-A System Identification and Real2Sim Evaluation · 正文段落 90](https://arxiv.org/html/2611.27042v1#S5.F8)
- [S40] [V-B Season I: Public Policy Leaderboard · 正文段落 91](https://arxiv.org/html/2611.27042v1#S5.SS2.p1.1)
- [S41] [V-B Season I: Public Policy Leaderboard · 正文段落 92](https://arxiv.org/html/2611.27042v1#S5.T2)
- [S42] [V-B Season I: Public Policy Leaderboard · 正文段落 93](https://arxiv.org/html/2611.27042v1#S5.T2.2)
- [S43] [V-B Season I: Public Policy Leaderboard · 正文段落 94](https://arxiv.org/html/2611.27042v1#S5.T2.3)
- [S44] [V-B Season I: Public Policy Leaderboard · 正文段落 95](https://arxiv.org/html/2611.27042v1#S5.SS2.p2.1)
- [S45] [V-C Season II Evaluation Setup · 正文段落 97](https://arxiv.org/html/2611.27042v1#S5.SS3.p2.1)
- [S46] [V-C Season II Evaluation Setup · 正文段落 98](https://arxiv.org/html/2611.27042v1#S5.SS3.p3.1)
- [S47] [V-C Season II Evaluation Setup · 正文段落 102](https://arxiv.org/html/2611.27042v1#S5.T4)
- [S48] [VI Limitations and Future Directions · 正文段落 108](https://arxiv.org/html/2611.27042v1#S6.p2.1)
- [S49] [VI Limitations and Future Directions · 正文段落 109](https://arxiv.org/html/2611.27042v1#S6.p3.1)
- [S50] [VII Conclusion · 正文段落 110](https://arxiv.org/html/2611.27042v1#S7.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/RoboColiseum Co-evolution of Simulation, Evaluation, and Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Simulation-based evaluation of embodied models requires calibrated interactions, diverse tasks, and explicit execution constraints. We present RoboColiseum, a platform combining system identification, composable physics and rendering, and multidimensional benchmarking. Recorded-command replay characterizes robot dynamics and object interactions, while a shared interface connects rigid and deformable simulation to rendering. Across 22 paired real--simulation robot--task configurations, task scores have a reported Pearson correlation of 0.9686. Eight evaluation tracks span instruction following, spatial reasoning, general manipulation, robustness, dexterous manipulation, precision manipulation, whole-body coordination, and execution across robot embodiments. Budget-aware scoring combines task progress, resource use, and completion rewards. We report 12 selected Season~I policies and all 11 systems on the public Season~II leaderboard, comprising eight Agent systems and three VLA policies. Agent2Act connects language models to robot-control execution; the VLA study uses mixed-task supervised fine-tuning. The results reveal substantial variation across tracks within each evaluation category. RoboColiseum connects simulation development with capability-oriented evaluation and provides a foundation for extending robot interactions and model assessment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.27042v1
- Authors: Chenghao Yin, Da Huang, Di Yang, Jichao Wang, Junhui Wu, Nanshu Zhao, Tong Ran, Zhijun Li, Gang Zhao, Linting Guo, Rui Feng, Sheng Zhang, Tianyu Jiang, Wenjun Sun, Yongxin Su, Zhaobo Liu, Zheyuan Xing, Sukai Wang, Yue Zhou, Qihan Jiang, Jianhua Jiang, Chuang Men, Yuxiang Yan, Daizhen Lv, Kunyu Yu, Yongjian Shen, Tianxiang Zhu, Siying Zhang, Wenhao Wang, Jun Zhao, Bowen Jiang, Zhi Zeng, Maoqing Yao, Qian Wang
- Published: 2026-11-20T03:14:26Z
- Age days: 3

</details>
