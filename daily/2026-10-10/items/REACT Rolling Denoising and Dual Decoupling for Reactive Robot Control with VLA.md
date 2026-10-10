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
url: "https://arxiv.org/abs/2610.12007v1"
published: "2026-10-08T14:09:46Z"
age_days: 1
score: 38
created: 2026-10-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> REACT 不再每次丢掉旧计划、重新生成整段动作，而是保留一个持续修正的动作缓冲区。未来动作在逐渐接近执行时多次吸收新观测，兼顾长段运动的连贯性和及时纠正。

## 问题

长动作段执行平滑，但段内新观测难以及时影响剩余动作；频繁重规划虽更新快，却容易在新旧计划切换时抖动。异步计算能隐藏等待时间，仍可能使用过时画面；RTC 用已承诺前缀约束后续动作，也未完全解决观测更新和动作输出吞吐的绑定 [S5](https://arxiv.org/html/2610.12007v1#S1.p1.1) [S6](https://arxiv.org/html/2610.12007v1#S1.p2.1) [S11](https://arxiv.org/html/2610.12007v1#S2.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：输入画面和“把杯子放到移动托盘上”；缓冲区保存未来伸手与放置动作。托盘移动后，新画面修正尚未执行的块，前端块执行、尾端补噪声，输出连续更新的动作流；这不代表任意突变都能及时处理。

## 创新点或方法

标准流式 VLA 用一张观测完成整段多步去噪；REACT 把动作段分成噪声程度不同的块，每次用最新观测对整个缓冲区做一步去噪，执行最前面的干净块，其余前移，尾部补噪声 [S13](https://arxiv.org/html/2610.12007v1#S3.SS1.p1.1)。训练也让不同位置对应不同流时间，匹配这个阶梯式调度，而不是全段共享一个随机时间 [S15](https://arxiv.org/html/2610.12007v1#S3.SS3.SSS0.Px1.p1.1) [S16](https://arxiv.org/html/2610.12007v1#S3.E5) [S17](https://arxiv.org/html/2610.12007v1#S3.SS3.SSS0.Px1.p1.2) [S18](https://arxiv.org/html/2610.12007v1#S3.SS3.SSS0.Px1.p2.1)。部署的双解耦把感知、视觉语言编码、动作去噪和执行分开调度；该调度不改模型权重，但完整方法包含新的动作专家训练方式 [S8](https://arxiv.org/html/2610.12007v1#S1.p4.1) [S35](https://arxiv.org/html/2610.12007v1#A3.SS2.p1.1)。

### 方法如何工作

1. 把长动作时域分成多个块，前端接近干净、尾端噪声更多，为逐步输出建立固定次序。
2. 每次读取最新可用观测，对完整缓冲区更新一步，使保留的未来计划吸收变化。
3. 执行前端块，其余前移并在尾部补噪声，让同一块跨多次更新后才执行。
4. 训练按相同位置分配噪声时间，减少训练与滚动推理的输入差异。
5. 分开调度编码、去噪和执行，降低彼此等待；具体并发实现未在所给节选展开。

### 必要术语

- 滚动去噪：保留部分生成结果，边修正边输出；本文用于持续更新未来动作。
- 阶梯流时间：不同动作位置处于不同噪声程度；本文训练与部署都使用这种布局。
- jerk：加速度变化的快慢；本文以关节轨迹 jerk 衡量成功执行中的运动平滑度。

## 证据

实验都基于 π₀.₅：RoboTwin 2.0 七项仿真任务含 Clean／Randomized，另有 ARX X5 和 Franka R3 真机六个平台任务组合 [S20](https://arxiv.org/html/2610.12007v1#S4.SS1.p1.1) [S21](https://arxiv.org/html/2610.12007v1#S4.SS1.p2.1)。不含双解耦的滚动版本仿真成功率49.71%／20.86%，长段基线37.43%／11.43%；真机总体65.7%对58.7% [S27](https://arxiv.org/html/2610.12007v1#S4.SS2.p2.1) [S28](https://arxiv.org/html/2610.12007v1#S4.SS2.p3.1)。仿真 jerk 为1064.7，低于频繁重规划的1463.7，却高于长段基线658.9。它支持更好的反应与平滑折中，并非全面最平滑。节选没有完整 REACT 的成绩、反应延迟和吞吐数值，不能拿上述数字代替。

## 局限

作者明确只验证 π₀.₅，策略按固定块数与块长训练，未验证零样本切换调度；也没有独立训练种子 [S34](https://arxiv.org/html/2610.12007v1#S6.p1.1)。平滑度只统计成功轨迹 [S21](https://arxiv.org/html/2610.12007v1#S4.SS1.p2.1)，不同方法进入统计的样本可能不同。我的待核查问题是编码更新滞后时实际使用了多新的观测，以及双解耦各部分贡献多少。

- **判断**：值得读到缓冲更新和线程调度实现：机制清楚且能直接启发闭环设计，但换骨干或调度需要重新验证。

## 研究关联

值得借鉴的是保留未执行计划的中间状态，让新观测逐步修改它，而不是每次重新抽样整段动作。同时，实时控制应分别检查新信息进入频率和动作输出频率，单次推理耗时无法描述整个闭环。

### 下一步读哪里

结合 [S14](https://arxiv.org/html/2610.12007v1#S3.SS1.p3.2) [S20](https://arxiv.org/html/2610.12007v1#S4.SS1.p1.1) [S35](https://arxiv.org/html/2610.12007v1#A3.SS2.p1.1) 检查预热、块长、块数和每块实际经历的更新次数；核查未提供的双解耦线程、缓存时间戳和延迟指标。再看完整方法与无双解耦版本的比较，避免把训练变化和纯推理调度收益混为一谈。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.12007v1
- 获取时间：2026-10-10T00:24:47.807020+00:00
- [S1] [REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models · 正文段落 1](https://arxiv.org/html/2610.12007v1#abstract1.1)
- [S2] [REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models · 正文段落 2](https://arxiv.org/html/2610.12007v1#S0.F1)
- [S3] [REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models · 正文段落 3](https://arxiv.org/html/2610.12007v1#p2.1.1)
- [S4] [REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models · 正文段落 4](https://arxiv.org/html/2610.12007v1#p3.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.12007v1#S1.p1.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.12007v1#S1.p2.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.12007v1#S1.p3.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.12007v1#S1.p4.1)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.12007v1#S1.I1.i3)
- [S10] [2 Related Work · 正文段落 12](https://arxiv.org/html/2610.12007v1#S2.p1.1)
- [S11] [2 Related Work · 正文段落 13](https://arxiv.org/html/2610.12007v1#S2.p2.1)
- [S12] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.12007v1#S2.p3.1)
- [S13] [3.1 Rolling Denoising for Flow-Based VLAs · 正文段落 15](https://arxiv.org/html/2610.12007v1#S3.SS1.p1.1)
- [S14] [3.1 Rolling Denoising for Flow-Based VLAs · 正文段落 23](https://arxiv.org/html/2610.12007v1#S3.SS1.p3.2)
- [S15] [Staircase training procedure. · 正文段落 28](https://arxiv.org/html/2610.12007v1#S3.SS3.SSS0.Px1.p1.1)
- [S16] [Staircase training procedure. · 正文段落 29](https://arxiv.org/html/2610.12007v1#S3.E5)
- [S17] [Staircase training procedure. · 正文段落 30](https://arxiv.org/html/2610.12007v1#S3.SS3.SSS0.Px1.p1.2)
- [S18] [Staircase training procedure. · 正文段落 31](https://arxiv.org/html/2610.12007v1#S3.SS3.SSS0.Px1.p2.1)
- [S19] [4 Experiments · 正文段落 32](https://arxiv.org/html/2610.12007v1#S4.p1.1)
- [S20] [4.1 Experimental Setup · 正文段落 33](https://arxiv.org/html/2610.12007v1#S4.SS1.p1.1)
- [S21] [4.1 Experimental Setup · 正文段落 34](https://arxiv.org/html/2610.12007v1#S4.SS1.p2.1)
- [S22] [4.2 General Task Results · 正文段落 35](https://arxiv.org/html/2610.12007v1#S4.F2)
- [S23] [4.2 General Task Results · 正文段落 36](https://arxiv.org/html/2610.12007v1#S4.SS2.p1.1)
- [S24] [4.2 General Task Results · 正文段落 37](https://arxiv.org/html/2610.12007v1#S4.T1)
- [S25] [4.2 General Task Results · 正文段落 39](https://arxiv.org/html/2610.12007v1#S4.T2)
- [S26] [4.2 General Task Results · 正文段落 41](https://arxiv.org/html/2610.12007v1#S4.F3)
- [S27] [4.2 General Task Results · 正文段落 42](https://arxiv.org/html/2610.12007v1#S4.SS2.p2.1)
- [S28] [4.2 General Task Results · 正文段落 43](https://arxiv.org/html/2610.12007v1#S4.SS2.p3.1)
- [S29] [4.4 Training Efficiency Analysis · 正文段落 52](https://arxiv.org/html/2610.12007v1#S4.F5.2.1)
- [S30] [4.4 Training Efficiency Analysis · 正文段落 53](https://arxiv.org/html/2610.12007v1#S4.F5.3.1)
- [S31] [4.4 Training Efficiency Analysis · 正文段落 54](https://arxiv.org/html/2610.12007v1#S4.F5)
- [S32] [4.4 Training Efficiency Analysis · 正文段落 55](https://arxiv.org/html/2610.12007v1#S4.SS4.p1.1)
- [S33] [4.4 Training Efficiency Analysis · 正文段落 56](https://arxiv.org/html/2610.12007v1#S4.SS4.p2.1)
- [S34] [6 Limitations · 正文段落 58](https://arxiv.org/html/2610.12007v1#S6.p1.1)
- [S35] [C.2 Model Architecture · 正文段落 106](https://arxiv.org/html/2610.12007v1#A3.SS2.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/REACT Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, whereas frequent replanning improves reactivity at the cost of action discontinuities. We introduce REACT, a rolling-denoising framework that makes flow-based VLAs more reactive while preserving long-horizon context. Instead of regenerating entire action chunks from scratch, REACT maintains a persistent action buffer with staggered flow timesteps. At each control step, the full horizon is denoised using the latest observation, the cleanest action block is executed, partially refined future blocks are shifted forward, and fresh noise is appended to the tail. As a result, each executed action block is refined across multiple recent observations before deployment. To support real-time control, we further introduce dual decoupling, which separates sensing, VLM encoding, DiT denoising, and action execution, enabling high-frequency observation updates and action streaming under practical compute constraints. Across the RoboTwin 2.0 simulation benchmark and real-world tasks spanning bimanual manipulation and dynamic control on multiple robot platforms, REACT improves task success and reduces reaction latency while producing smoother trajectories than frequent-replanning and asynchronous baselines.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12007v1
- Authors: Houlong Xiong, Zhenqi Qiu, Zechen Wang, Suohang Zhang, Yiyu Ren, Wanting Xu, Hongfei Niu, Chengyang He, Ge Sun, Ran Cheng, Qian Zhu
- Published: 2026-10-08T14:09:46Z
- Age days: 1

</details>
