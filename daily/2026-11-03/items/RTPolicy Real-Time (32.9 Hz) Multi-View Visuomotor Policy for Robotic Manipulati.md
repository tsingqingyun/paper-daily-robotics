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
url: "https://arxiv.org/abs/2610.41625v1"
published: "2026-10-30T12:01:49Z"
age_days: 3
score: 26
created: 2026-11-03
concepts: ["具身智能评测与基准"]
---

# RTPolicy: Real-Time (32.9 Hz) Multi-View Visuomotor Policy for Robotic Manipulation on Edge Devices

> [!summary] 这篇论文到底做了什么（基于摘要）
> RTPolicy 把多台相机提供的信息先融合、压缩，再交给动作生成器，以降低边缘设备上的控制延迟。它希望保留操作需要的视觉线索，同时让新动作块更快生成，及时纠正执行偏差。

## 问题

机器人异步执行动作块时，一边执行旧动作，一边计算新动作；计算越慢，偏差就越久得不到修正。现有视觉运动策略的昂贵视觉骨干带来推理延迟和部署负担，因此瓶颈不只是动作预测准确率，还包括视觉处理与动作生成能否及时完成。

### 用一个例子理解

理解用例（非论文实验）：双臂机器人把杯子放到托盘上；输入多相机图像和机器人状态，融合压缩后生成下一段动作；执行期间新观测触发后续动作计算，用更新的动作块纠正杯子位置偏差。

## 创新点或方法

相对于昂贵的视觉处理流程，RTPolicy 用考虑相机视角的特征融合与视觉压缩，把互补信息变成紧凑 token，再结合机器人状态和流时间，输入流匹配动作生成器。减少条件表示的规模，有望降低后续生成成本。训练使用何种示范、损失配置及采样过程，摘要未说明；推理则输出动作块，并在真实平台上以异步流式方式更新。流时间是生成过程的变量，不能直接当作机器人执行时间。

### 方法如何工作

1. 提取多相机视觉特征，并考虑视角进行融合，以汇集互补的操作线索。
2. 把融合信息压缩成紧凑 token，减少动作生成器需要处理的视觉输入。
3. 结合机器人状态与流时间，用流匹配生成动作块；具体生成步数摘要未说明。
4. 在执行动作时异步计算更新，让新动作块能够及时修正偏差；交接规则需查正文。

### 必要术语

- token：供网络处理的特征单元；本文压缩其表示以降低计算负担。
- 流匹配：学习连续变换来生成目标样本的方法；本文用于动作生成。
- 异步动作块推理：执行一段动作时并行计算后续动作；本文关注更新延迟。
- INT16：以 16 位整数进行计算的表示方式；摘要中的设备速度在此条件下测得。

## 证据

摘要报告：RoboTwin 2.0 的 50 项单任务 clean 评测中，平均成功率为 52.26%，高于最强榜单基线 π₀ 的 46.4%。真实双臂平台异步评测平均成功率为 72.0%；INT16 下，RDK S600 推理耗时 30.35 ms、32.9 Hz，S100 为 149.72 ms、6.7 Hz。结果支持指定评测与设备上的表现；32.9 Hz 不能外推到所有边缘设备，也不等于完整控制闭环频率。

## 局限

我的待核查问题是各阶段耗时、动作块长度、异步更新规则，以及真实任务的数量和对照。摘要的成功率与延迟同时良好，尚不足以单独证明“降低延迟导致成功率提高”；还需要控制其他差异的实验。

- **判断**：值得读到融合压缩消融和设备计时细节，因为它给出了明确部署结果，但不同设备间的速度差异决定了实际使用条件。

## 研究关联

可借鉴的是先整合多视角互补信息，再控制表示规模：相机增加不必意味着下游始终处理同样多的信息。值得尝试的条件是视觉计算确为主要瓶颈，并且压缩后仍能保住决定接触和定位的细节。

### 下一步读哪里

先核查视角信息怎样参与融合、压缩保留多少 token，再看同等训练条件下的消融；设备部分应检查计时范围、INT16 精度影响、动作块交接和真实任务成功判据。输入未提供这些正文细节。

- **概念**：具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/RTPolicy Real-Time (32.9 Hz) Multi-View Visuomotor Policy for Robotic Manipulati.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Low inference latency is critical for closed-loop robotic manipulation, especially under asynchronous inference, where action chunks must be updated promptly to correct accumulated deviations. However, existing visuomotor policies rely on computationally expensive visual backbones, resulting in high inference latency and deployment overhead. In this paper, we propose RTPolicy, a multi-view visuomotor policy that attains accurate manipulation with high inference efficiency. Its core design combines view-aware feature fusion with visual compression to aggregate complementary information across camera views into a compact token representation. The representation conditions a flow-matching action generator with the robot state and flow time, reducing the cost of action generation. Extensive experiments demonstrate that this design reduces the computational cost of visual representation and action generation while preserving visual information required for manipulation. On the RoboTwin~2.0 single-task clean evaluation across 50 tasks, RTPolicy attains a mean success rate of 52.26\%, outperforming the strongest leaderboard baseline $π_0$ (46.4\%). We further evaluate RTPolicy under asynchronous streaming inference on a real bimanual platform, where RTPolicy attains a mean success rate of 72.0\% and sustains real-time inference at 30.35 ms (32.9 Hz) on the RDK S600 and 149.72 ms (6.7 Hz) on the RDK S100, both in INT16. Project Page: https://d-robotics-ai-lab.github.io/RTPolicy.project.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.41625v1
- Authors: Xianbao Hou, Zehao Ni, Yonghao He, Lingfeng Qian, Xin Shi, Hu Su, Wei Sui, Cong Yang
- Published: 2026-10-30T12:01:49Z
- Age days: 3

</details>
