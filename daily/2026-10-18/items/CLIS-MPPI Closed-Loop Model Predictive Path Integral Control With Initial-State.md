---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.21239v1"
published: "2026-10-15T04:37:31Z"
age_days: 2
score: 27
created: 2026-10-18
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# CLIS-MPPI: Closed-Loop Model Predictive Path Integral Control With Initial-State Sampling Under Execution Delay

> [!summary] 这篇论文到底做了什么（基于摘要）
> CLIS-MPPI 处理一个实际问题：规划算完时，机器人已经不在计算开始的位置了。它从多个可能的执行时刻状态出发规划，并在执行时用局部反馈修正动作，减少计划与真实运动的错位。

## 问题

任务是在有障碍的狭窄通道里移动机械臂并到达目标。标准 MPPI 通过采样候选控制并模拟后果来选动作，但计算需要时间；若仍从计算开始的状态预测，执行时整条预测就可能偏移。通道越窄，这种偏移越可能导致碰撞。

### 用一个例子理解

理解用例（非论文实验）：输入是机械臂当前状态、障碍和目标；计算期间机械臂仍在运动，控制器估计执行时的多个可能状态，从这些起点模拟候选动作，再按实际反馈修正；输出是通过窄缝的控制命令。

## 创新点或方法

旧做法的预测起点与实际执行状态可能不一致；CLIS-MPPI 把规划延迟对应的执行状态表示成一个分布，采样多个起点后进行轨迹优化，使动作考虑可能出现的状态偏差。执行期间，再利用基于模拟轨迹的局部反馈纠正控制。这是在线控制方法，摘要没有描述需要离线学习的模型；状态分布如何估计、反馈律怎样计算以及额外算力开销，均未说明。

### 方法如何工作

1. 把规划延迟转成执行时可能出现的状态范围，避免只依赖已经过时的当前状态。
2. 从该分布采样初始状态，模拟候选控制的运动后果，让优化覆盖起点偏差。
3. 依据模拟结果优化控制，选出面向这些可能状态的动作。
4. 执行时用基于模拟轨迹的局部反馈修正命令，进一步缩小预测与实际运动的差异。

### 必要术语

- MPPI：通过采样控制、模拟结果和评价代价来求动作的控制方法；它是本文改进的基础。
- 初始状态采样：从多个可能起点进行预测；本文用它表示执行延迟造成的状态不确定性。
- 局部反馈：根据实际状态偏差调整动作；本文用它在执行期间修正控制。

## 证据

摘要报告，UR5e 六自由度机械臂在同一真实窄通道任务各运行 5 次：标准 MPPI 碰撞 2 次，CLIS-MPPI 为 0 次。分别对无碰撞运行取平均，完成时间由 25.4 秒降到 24.4 秒，末端路径由 0.456 米降到 0.425 米；两组样本分别为 3 次和 5 次。摘要还报告关节位置、速度 RMSE 从 0.100 弧度、0.108 弧度/秒降至 0.017 弧度、0.011 弧度/秒，但未交代误差参照与统计范围。结果支持该任务中的改善。

## 局限

五次无碰撞不构成安全保证，且只验证一个任务。完成时间和路径长度比较筛选了各自成功运行，不能代表全部尝试的平均代价。我的待核查问题是两项改动各贡献多少，以及延迟更大时是否仍有效。

- **判断**：值得读控制公式和延迟实验；思路直接可用，但现有实机样本只足以支持有限范围的可靠性判断。

## 研究关联

值得借鉴的是把“执行时从哪里开始”也视为不确定量。已有采样控制器在实机上表现差时，除了检查动力学预测，还应检查计算延迟是否让规划起点失效。

### 下一步读哪里

先核查初始状态分布如何由延迟产生，再查局部反馈的推导和实时计算预算。实验应重点找不同延迟、通道宽度及分别移除两项改动的对照，并确认 RMSE 的参考轨迹。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-18/CLIS-MPPI Closed-Loop Model Predictive Path Integral Control With Initial-State.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Sampling-based motion planning such as Model Predictive Path Integral (MPPI) control has become attractive for robotics due to its ability to handle nonlinear dynamics and non-smooth objectives without gradient information, while leveraging parallel rollout computation for real-time performance. However, in real-world robotic systems, the optimized control input is often applied after a non-negligible planning delay, causing a mismatch between the state used in forward simulation and the actual state at control execution, which can significantly degrade planning accuracy and may even lead to unsafe behavior such as collisions. This paper proposes Closed-Loop MPPI with Initial-State Sampling (CLIS-MPPI), which explicitly addresses execution-time state mismatch by modeling planning delay as a distribution over plausible execution-time initial states, performing rollout optimization from sampled initial states, and applying a rollout-based local feedback correction during control execution. The proposed method is validated through real-world experiments on a 6-DoF UR5e manipulator in a narrow-passage task involving obstacle avoidance and end-effector target reaching. Across 5 real-world runs of the same task, standard MPPI collided in 2 runs, whereas CLIS-MPPI remained collision-free in all 5 runs. Averaged over all collision-free runs for each method (3 for MPPI and 5 for CLIS-MPPI), CLIS-MPPI reduced the average task completion time from 25.4s to 24.4s and the average end-effector path length from 0.456 m to 0.425 m. It also reduced the overall joint-position and joint-velocity root mean square errors (RMSEs) from 0.100 rad and 0.108 rad/s to 0.017 rad and 0.011 rad/s, respectively. These results demonstrate improved safety, planning-execution consistency, and motion smoothness.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21239v1
- Authors: Zidong Liu, Xu Chen
- Published: 2026-10-15T04:37:31Z
- Age days: 2

</details>
