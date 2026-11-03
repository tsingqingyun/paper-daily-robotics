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
url: "https://arxiv.org/abs/2610.40799v1"
published: "2026-10-29T18:01:07Z"
age_days: 4
score: 41
created: 2026-11-03
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> CaPtain 让小视觉语言模型自己写代码完成抓取和放置，而不是只调用现成抓取技能。关键是训练时让一个能读取仿真物理状态的评价器，判断每次调用是否让任务更接近成功；部署时则只保留看图、写代码和读取执行回执的模型。

## 问题

任务是从相机图像和语言指令出发，决定抓哪里、怎样接近、何时闭合夹爪。调用大模型成本高；调用冻结 VLA 或高层技能，又把具体操作能力限制在技能内部。改用低层接口后，一次任务有几十次请求，很多只是观察，最终成败很难说明究竟哪个动作做对了。[S4](https://arxiv.org/html/2610.40799v1#S1.p2.1) [S5](https://arxiv.org/html/2610.40799v1#S1.p3.1)

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放到盘子中央”和桌面图像；模型调用感知接口定位杯子，测量位置，再写移动和夹爪代码；若回执显示接触后停止，就重新观察并修正接近方向，最终输出一串完成搬运的可执行调用。

## 创新点或方法

旧做法把最终结果分给整串调用，本文改为估计每次请求前后成功机会的变化。先用 GPT-6 Astra 生成同一执行环境内的轨迹做 SFT，教会接口；再用多轮 RL 学操作和纠错。评价器读取物体位姿、抓取状态等隐藏物理信息，但策略始终看不到它们。比较价值时固定时间索引，避免把“又花了一轮”误算成观察动作的负面效果；推理时移除评价器。[S6](https://arxiv.org/html/2610.40799v1#S1.p4.1) [S25](https://arxiv.org/html/2610.40799v1#S4.SS5.SSS0.Px2.p1.1)

### 方法如何工作

1. 先提供统一低层 API 和结构化回执，让模型得到动作后果，形成可反复观察和修正的闭环。
2. 用环境内合成轨迹做 SFT，使模型学会正确调用接口，避免把 RL 预算耗在接口误用上。
3. 在仿真中执行多轮请求，让物理评价器估计请求引起的成功机会变化，为延迟后果分配训练信号。
4. 据此更新写代码的策略；部署时删除评价器，继续仅凭图像和回执完成操作。

### 必要术语

- Code-as-Policy：把策略输出写成调用机器人接口的程序；本文让模型决定具体操作细节。
- 非对称 actor-critic：行动者与评价者获得不同信息；本文只有训练评价器读取隐藏物理状态。
- 信用分配：判断最终成败应归功或归咎于哪些早期决策；本文细化到每次请求。

## 证据

在留出的 LIBERO 初始状态上，240 回合的 host 成功率由 SFT 的55.4%升至73.8%，strict 成功率由52.1%升至67.5%。LIBERO-PRO 三套测试为78.5%，全部四套为68.6%，二者不能混用。[S22](https://arxiv.org/html/2610.40799v1#S4.T1.15) 对几种扰动仍有增益，支持其超出训练初始布局的适应能力；但这些任务家族的成绩不等于任意机器人迁移。真机完成任务仅有定性描述，节选未给回合数和成功率。[S7](https://arxiv.org/html/2610.40799v1#S1.p5.1)

## 局限

作者已报告 RoboTwin 2.0 和 RoboDojo 迁移成功率仅22.6%和0.8%，双臂协调及陌生运动学仍是明显障碍。[S7](https://arxiv.org/html/2610.40799v1#S1.p5.1) RL 同时使用了更宽布局和视觉扰动；仅凭主结果不能把全部收益归因于物理评价器。还需检查对应消融，以及 host 与 strict 判定差异。

- **判断**：值得深入读信用分配和评价器输入设计：它最有借鉴性的地方，是怎样避免把长过程中的观察、耗时和真正物理进展混为一谈。

## 研究关联

值得借鉴的是把“决策时能看见什么”和“训练时怎样判断进展”分开。只要仿真物理状态可靠，就可以用它教会基于图像的策略，而不必让部署系统依赖这些隐藏信息。

### 下一步读哪里

先看[S6](https://arxiv.org/html/2610.40799v1#S1.p4.1) [S25](https://arxiv.org/html/2610.40799v1#S4.SS5.SSS0.Px2.p1.1)的固定时间价值差与输入限制，再核查价值目标、优势计算和评价器消融；用[S22](https://arxiv.org/html/2610.40799v1#S4.T1.15)区分不同测试套件及两种成功标准。[S18](https://arxiv.org/html/2610.40799v1#S3.SS3.SSS0.Px5.p1.2)还提示实现成本：大批量梯度累积可能是复现的重要条件。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：41
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.40799v1
- 获取时间：2026-11-03T00:10:21.843574+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.40799v1#p1.2)
- [S2] [CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents · 正文段落 2](https://arxiv.org/html/2610.40799v1#abstract1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.40799v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.40799v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.40799v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.40799v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.40799v1#S1.p5.1)
- [S8] [Contributions. · 正文段落 8](https://arxiv.org/html/2610.40799v1#S1.I1.i1)
- [S9] [Contributions. · 正文段落 11](https://arxiv.org/html/2610.40799v1#S1.I1.i4)
- [S10] [Code-as-policy robot agents. · 正文段落 12](https://arxiv.org/html/2610.40799v1#S2.SS0.SSS0.Px1.p1.1)
- [S11] [End-to-end robot policies. · 正文段落 13](https://arxiv.org/html/2610.40799v1#S2.SS0.SSS0.Px2.p1.1)
- [S12] [Credit assignment and privileged critics. · 正文段落 14](https://arxiv.org/html/2610.40799v1#S2.SS0.SSS0.Px3.p1.1)
- [S13] [3 CaPtain · 正文段落 15](https://arxiv.org/html/2610.40799v1#S3.p1.1)
- [S14] [3 CaPtain · 正文段落 16](https://arxiv.org/html/2610.40799v1#S3.F1)
- [S15] [A ReAct loop over requests. · 正文段落 17](https://arxiv.org/html/2610.40799v1#S3.SS1.SSS0.Px1.p1.1)
- [S16] [Policy update. · 正文段落 51](https://arxiv.org/html/2610.40799v1#S3.SS3.SSS0.Px5.p1.1)
- [S17] [Policy update. · 正文段落 52](https://arxiv.org/html/2610.40799v1#S3.E8)
- [S18] [Policy update. · 正文段落 53](https://arxiv.org/html/2610.40799v1#S3.SS3.SSS0.Px5.p1.2)
- [S19] [Training distribution. · 正文段落 54](https://arxiv.org/html/2610.40799v1#S3.SS3.SSS0.Px6.p1.1)
- [S20] [Training distribution. · 正文段落 55](https://arxiv.org/html/2610.40799v1#alg1)
- [S21] [4.1 Main results · 正文段落 59](https://arxiv.org/html/2610.40799v1#S4.T1)
- [S22] [4.1 Main results · 正文段落 60](https://arxiv.org/html/2610.40799v1#S4.T1.15)
- [S23] [4.1 Main results · 正文段落 61](https://arxiv.org/html/2610.40799v1#S4.F2)
- [S24] [4.1 Main results · 正文段落 62](https://arxiv.org/html/2610.40799v1#S4.SS1.p1.1)
- [S25] [Why policy-side features and LM hidden states are excluded. · 正文段落 90](https://arxiv.org/html/2610.40799v1#S4.SS5.SSS0.Px2.p1.1)
- [S26] [6 Conclusion · 正文段落 94](https://arxiv.org/html/2610.40799v1#S6.p1.1)
- [S27] [A.1 Policy and harness · 正文段落 95](https://arxiv.org/html/2610.40799v1#A1.F6)
- [S28] [Policy. · 正文段落 96](https://arxiv.org/html/2610.40799v1#A1.SS1.SSS0.Px1.p1.1)
- [S29] [Returns and costs. · 正文段落 120](https://arxiv.org/html/2610.40799v1#A1.I3.i1)
- [S30] [Training distribution. · 正文段落 132](https://arxiv.org/html/2610.40799v1#A1.I5.i1)
- [S31] [Training distribution. · 正文段落 133](https://arxiv.org/html/2610.40799v1#A1.I5.i2)
- [S32] [Appendix I Host and strict success late in RL · 正文段落 167](https://arxiv.org/html/2610.40799v1#A9.I1.i1)
- [S33] [Appendix K Additional LIBERO results · 正文段落 180](https://arxiv.org/html/2610.40799v1#A11.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/CaPtain A Pipeline for Post-Training Code-as-Policy Robot Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-as-policy (CaP) casts robot manipulation in the same form, as the policy writes code against robot APIs and reads back the results, so the same recipe should apply. Yet existing CaP agents sidestep training: they either prompt closed frontier models or delegate manipulation to pre-trained vision-language-action models (VLAs) and high-level skills, while small open vision-language models (VLMs) fail outright. We present CaPtain, an open post-training pipeline that turns a small open VLM into a capable CaP agent, with no VLA, frontier model, or privileged state at test time. CaPtain trains and deploys the policy inside CaPtain-Harness, which exposes low-level perception, geometry, and guarded-motion primitives across simulation and real hardware. We first align the base model via SFT on synthetic trajectories generated with GPT-6 Astra, then apply multi-turn RL. Multi-turn RL must credit tens of agent requests, whose physical effects often surface turns later, from a single end-of-episode outcome. We therefore introduce a physical critic that reads privileged simulator state, never seen by the policy, and credits each request by how much it changes the predicted chance of success. Starting from Qwen3.5-4B (0% zero-shot), CaPtain-4B reaches 55.4% held-out LIBERO success after SFT and 73.8% after RL. On LIBERO-PRO, it reaches 78.5%, surpassing several frontier-model agents, and its RL gains persist across three perturbation suites (+17.6 to +21.2 points). Without target-domain training, it attains 83.3% on SimplerEnv WidowX, exceeds frontier models on CaP-Bench, and runs on a real robot after simulation-only adaptation. We release all code, data, and model weights.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.40799v1
- Authors: Yijia Fan, Xilin He, Yilei Jiang, Dongming Wu, Jiaxu Wang, Xiangyu Yue
- Published: 2026-10-29T18:01:07Z
- Age days: 4

</details>
