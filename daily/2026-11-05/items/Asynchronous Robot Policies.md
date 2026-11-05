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
url: "https://arxiv.org/abs/2611.05155v1"
published: "2026-11-03T16:30:27Z"
age_days: 1
score: 43
created: 2026-11-05
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Asynchronous Robot Policies

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> ARP 让大模型慢慢理解任务，小模型持续看最新画面并控制机器人，两者不必互相等待。巧处是训练时就让快控制器练习使用过期语义，并处理动作算出来时机器人已经前进的问题。

## 问题

目标是既听懂复杂指令，又能在物体突然移动时及时改动作。同步 VLA 把语义计算和动作生成串在主循环里，大模型越慢，机器人重新观察并纠偏的间隔越长；仅把动作预先算成一长段，也不能及时应对中途变化。

### 用一个例子理解

理解用例（非论文实验）：输入“拿起红杯”，慢循环留下目标语义；杯子随后被推开，快循环用最新腕部画面和旧语义重新定位红杯，输出修正后的抓取轨迹，不必等待大模型再次理解指令。

## 创新点或方法

同步等待完整 VLM 推理，改为两个独立进程：慢循环发布固定宽度语义记忆，快循环读取最新图像、机器人状态和最近可用记忆。训练把当前画面配上同一示范中较早画面产生的记忆，并显式输入记忆年龄和采样的执行延迟；动作前缀条件帮助新规划接上正在执行的动作。推理时快循环持续更新，不等慢循环。记忆压缩和前缀处理的完整结构未在节选中展开。[S6](https://arxiv.org/html/2611.05155v1#S1.p4.1) [S12](https://arxiv.org/html/2611.05155v1#S3.I1.i1) [S13](https://arxiv.org/html/2611.05155v1#S3.I1.i2) [S14](https://arxiv.org/html/2611.05155v1#S3.SS1.p1.1) [S15](https://arxiv.org/html/2611.05155v1#S3.SS1.p2.1) [S16](https://arxiv.org/html/2611.05155v1#S3.SS4.SSS0.Px1.p1.1) [S17](https://arxiv.org/html/2611.05155v1#S3.SS4.SSS0.Px1.p2.1) [S18](https://arxiv.org/html/2611.05155v1#S3.E3) [S19](https://arxiv.org/html/2611.05155v1#S3.SS4.SSS0.Px1.p2.2)

### 方法如何工作

1. 慢循环把图像和指令压成语义记忆，保留动作选择需要的任务信息。
2. 快循环结合最新感知与已有记忆生成动作，使纠偏速度不受每次 VLM 推理限制。
3. 训练时故意错配新画面与旧记忆，并告知延迟，让策略学会区分两者的时效。
4. 重规划时加入动作前缀条件，使新轨迹接续当前执行；具体实现仍需核查。

### 必要术语

- 语义记忆：慢模型提供的紧凑任务表征；本文用它连接两个循环，并非已经验证的长期记忆库。
- 记忆过期程度：语义所依据的观测距现在多久；本文将其作为控制条件。
- 动作前缀条件：生成后续动作时参考已有动作开头；本文用它支持连续重规划。

## 证据

LIBERO 中 ARP-1B 平均成功率 84.8%，复现的 π₀-1B 为 80.2%；但原始 π₀ 报告值为 94.2%，所以不能概括为全面领先 [S30](https://arxiv.org/html/2611.05155v1#S4.T1.6)。目标中途位移 5 cm 的仿真中，两者为 51.5% 与 9.5% [S26](https://arxiv.org/html/2611.05155v1#S4.SS1.SSS0.Px2.p1.1) [S38](https://arxiv.org/html/2611.05155v1#S4.SS3.p1.1)。更关键的训练消融是：VLM 以 0.5 Hz 更新时，只用同步记忆训练为 2.0%，默认较宽过期范围训练为 81.8% [S44](https://arxiv.org/html/2611.05155v1#S4.T4.4.1)。真机覆盖三任务；20% 更短平均回合长度的具体陈述来自 RoboLab 仿真评估 [S28](https://arxiv.org/html/2611.05155v1#S4.SS1.SSS0.Px4.p1.1) [S35](https://arxiv.org/html/2611.05155v1#S4.SS2.SSS0.Px2.p2.1)。

## 局限

作者明确把进程通信和长任务持久记忆列为待解决问题 [S46](https://arxiv.org/html/2611.05155v1#S5.p2.1)。动态收益主要在仿真验证；训练过期消融支持该训练设计有效，但主结果不能单独归因于并行执行。摘要“提高18%”的具体计算口径仍需核查。

- **判断**：值得细读时序训练与消融：证据最有说服力的部分，是展示了为什么异步控制必须连同信息过期一起训练。

## 研究关联

当任务含义变化慢、物体位置变化快时，两类信息无需同频更新。可借鉴的不只是拆进程，而是把部署中的信息年龄显式带进训练，否则旧语义可能让快循环做出错误反应。

### 下一步读哪里

先读 [S16](https://arxiv.org/html/2611.05155v1#S3.SS4.SSS0.Px1.p1.1) [S17](https://arxiv.org/html/2611.05155v1#S3.SS4.SSS0.Px1.p2.1) [S18](https://arxiv.org/html/2611.05155v1#S3.E3) [S19](https://arxiv.org/html/2611.05155v1#S3.SS4.SSS0.Px1.p2.2) [S44](https://arxiv.org/html/2611.05155v1#S4.T4.4.1)，核查过期时间单位、部署延迟是否落在训练范围；再检查动作前缀如何避免跳变，以及 [S35](https://arxiv.org/html/2611.05155v1#S4.SS2.SSS0.Px2.p2.1) 真机比较的试验次数和任务完成指标。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：43
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.05155v1
- 获取时间：2026-11-05T00:11:39.455703+00:00
- [S1] [Asynchronous Robot Policies · 正文段落 1](https://arxiv.org/html/2611.05155v1#abstract1.1)
- [S2] [Asynchronous Robot Policies · 正文段落 2](https://arxiv.org/html/2611.05155v1#abstract1.2)
- [S3] [Asynchronous Robot Policies · 正文段落 3](https://arxiv.org/html/2611.05155v1#S0.F1.sf1)
- [S4] [Asynchronous Robot Policies · 正文段落 4](https://arxiv.org/html/2611.05155v1#S0.F1.sf2)
- [S5] [Asynchronous Robot Policies · 正文段落 5](https://arxiv.org/html/2611.05155v1#S0.F1)
- [S6] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.05155v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 11](https://arxiv.org/html/2611.05155v1#S1.p6.1)
- [S8] [2.1 Generalist Robot Policies · 正文段落 12](https://arxiv.org/html/2611.05155v1#S2.SS1.p1.1)
- [S9] [2.2 Asynchronous Systems · 正文段落 13](https://arxiv.org/html/2611.05155v1#S2.SS2.p1.1)
- [S10] [2.2 Asynchronous Systems · 正文段落 14](https://arxiv.org/html/2611.05155v1#S2.SS2.p2.1)
- [S11] [3 Method · 正文段落 15](https://arxiv.org/html/2611.05155v1#S3.p1.1)
- [S12] [3 Method · 正文段落 16](https://arxiv.org/html/2611.05155v1#S3.I1.i1)
- [S13] [3 Method · 正文段落 17](https://arxiv.org/html/2611.05155v1#S3.I1.i2)
- [S14] [3.1 Problem Formulation and System Overview · 正文段落 18](https://arxiv.org/html/2611.05155v1#S3.SS1.p1.1)
- [S15] [3.1 Problem Formulation and System Overview · 正文段落 19](https://arxiv.org/html/2611.05155v1#S3.SS1.p2.1)
- [S16] [Training with Stale Semantic Memory. · 正文段落 33](https://arxiv.org/html/2611.05155v1#S3.SS4.SSS0.Px1.p1.1)
- [S17] [Training with Stale Semantic Memory. · 正文段落 34](https://arxiv.org/html/2611.05155v1#S3.SS4.SSS0.Px1.p2.1)
- [S18] [Training with Stale Semantic Memory. · 正文段落 35](https://arxiv.org/html/2611.05155v1#S3.E3)
- [S19] [Training with Stale Semantic Memory. · 正文段落 36](https://arxiv.org/html/2611.05155v1#S3.SS4.SSS0.Px1.p2.2)
- [S20] [4 Experiments and Results · 正文段落 37](https://arxiv.org/html/2611.05155v1#S4.p1.1)
- [S21] [4 Experiments and Results · 正文段落 38](https://arxiv.org/html/2611.05155v1#S4.I1.i1)
- [S22] [4 Experiments and Results · 正文段落 39](https://arxiv.org/html/2611.05155v1#S4.I1.i2)
- [S23] [4 Experiments and Results · 正文段落 40](https://arxiv.org/html/2611.05155v1#S4.I1.i3)
- [S24] [4 Experiments and Results · 正文段落 41](https://arxiv.org/html/2611.05155v1#S4.I1.i4)
- [S25] [LIBERO Simulation Benchmark · 正文段落 42](https://arxiv.org/html/2611.05155v1#S4.SS1.SSS0.Px1.p1.1)
- [S26] [LIBERO-Perturb · 正文段落 43](https://arxiv.org/html/2611.05155v1#S4.SS1.SSS0.Px2.p1.1)
- [S27] [Dynamic Bump Benchmark · 正文段落 44](https://arxiv.org/html/2611.05155v1#S4.SS1.SSS0.Px3.p1.1)
- [S28] [DROID Dataset & RoboLab Evaluation · 正文段落 45](https://arxiv.org/html/2611.05155v1#S4.SS1.SSS0.Px4.p1.1)
- [S29] [LIBERO Results · 正文段落 46](https://arxiv.org/html/2611.05155v1#S4.T1)
- [S30] [LIBERO Results · 正文段落 47](https://arxiv.org/html/2611.05155v1#S4.T1.6)
- [S31] [LIBERO Results · 正文段落 48](https://arxiv.org/html/2611.05155v1#S4.SS2.SSS0.Px1.p1.1)
- [S32] [LIBERO Results · 正文段落 49](https://arxiv.org/html/2611.05155v1#S4.SS2.SSS0.Px1.p2.1)
- [S33] [Franka-DROID Results · 正文段落 50](https://arxiv.org/html/2611.05155v1#S4.SS2.SSS0.Px2.p1.1)
- [S34] [Franka-DROID Results · 正文段落 51](https://arxiv.org/html/2611.05155v1#S4.F3)
- [S35] [Franka-DROID Results · 正文段落 52](https://arxiv.org/html/2611.05155v1#S4.SS2.SSS0.Px2.p2.1)
- [S36] [4.3 Dynamic Tasks (RQ2) · 正文段落 54](https://arxiv.org/html/2611.05155v1#S4.T3.fig1.3)
- [S37] [4.3 Dynamic Tasks (RQ2) · 正文段落 56](https://arxiv.org/html/2611.05155v1#S4.T3.fig2.3)
- [S38] [4.3 Dynamic Tasks (RQ2) · 正文段落 58](https://arxiv.org/html/2611.05155v1#S4.SS3.p1.1)
- [S39] [4.3 Dynamic Tasks (RQ2) · 正文段落 59](https://arxiv.org/html/2611.05155v1#S4.SS3.p2.1)
- [S40] [4.4 Robustness to Compute Budget and ASYNCHRONY (RQ3) · 正文段落 61](https://arxiv.org/html/2611.05155v1#S4.F6)
- [S41] [4.4 Robustness to Compute Budget and ASYNCHRONY (RQ3) · 正文段落 62](https://arxiv.org/html/2611.05155v1#S4.SS4.p1.1)
- [S42] [4.4 Robustness to Compute Budget and ASYNCHRONY (RQ3) · 正文段落 63](https://arxiv.org/html/2611.05155v1#S4.SS4.p2.1)
- [S43] [4.5 Ablation Study (RQ4) · 正文段落 64](https://arxiv.org/html/2611.05155v1#S4.T4)
- [S44] [4.5 Ablation Study (RQ4) · 正文段落 65](https://arxiv.org/html/2611.05155v1#S4.T4.4.1)
- [S45] [5 Discussion and Conclusions · 正文段落 71](https://arxiv.org/html/2611.05155v1#S5.p1.1)
- [S46] [5 Discussion and Conclusions · 正文段落 72](https://arxiv.org/html/2611.05155v1#S5.p2.1)
- [S47] [D.2 Real World Evaluations · 正文段落 108](https://arxiv.org/html/2611.05155v1#A4.SS2.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-05/Asynchronous Robot Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Scaling vision-language foundation models has significantly advanced generalist robot manipulation, but the increased model scale introduces computational latency that degrades real-time physical reactivity. Existing Vision-Language-Action (VLA) architectures execute high-level semantic reasoning and action ex- ecution sequentially within the primary control loop, creating a fundamental tension between semantic-reasoning capability and robot agility. To address this, we propose Asynchronous Robot Policy (ARP), an architectural framework that decouples semantic reasoning from low-level action generation using asynchronous processes operating at independent frequencies. In ARP, a high-capacity Vision-Language Model (VLM) asynchronously updates a semantic memory at low fre- quency, while a lightweight Vision-Action Expert, conditioned on this semantic memory, generates robot actions at a much higher control frequency. Such a formulation, enables having a fast perception-action loop without compromising on the semantic capability. To overcome asynchronous memory staleness, ARP trains the vision-action expert on the semantic staleness and execution delay, with temporally mismatched observation across processes. On Franka manipulation tasks, ARP achieves an 18% higher success rate and 20% less time need for execution in quasi-static setups, while 3-5 times baseline performance in dynamic simulation environments. Furthermore, ARP enables operating the VLM at 10 times lower than its nominal frequency with no significant performance loss making it much more efficient than the baseline. These results highlight the architectural advantages of modeling robot policies as asynchronous processes, enabling real-world reactive deployment without sacrificing the scale of foundation models.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.05155v1
- Authors: Sombit Dey, Luc Van Gool, Danda Pani Paudel
- Published: 2026-11-03T16:30:27Z
- Age days: 1

</details>
