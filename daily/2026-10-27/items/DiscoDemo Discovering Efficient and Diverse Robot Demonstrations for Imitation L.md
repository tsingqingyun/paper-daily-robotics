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
url: "https://arxiv.org/abs/2610.32093v1"
published: "2026-10-23T02:55:17Z"
age_days: 3
score: 47
created: 2026-10-27
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> DiscoDemo 让强化学习先探索同一任务的多种成功做法，再把这些行为收集成示范，供视觉动作策略模仿。关键是只有成功得到保障时才鼓励行为多样，避免为了“不同”而生成无用数据。

## 问题

任务是用示范训练机器人操作策略。真正的瓶颈不只是示范数量少，而是反复展示同一种做法，容易只覆盖狭窄的成功轨迹；行为克隆遇到训练中少见的状态就可能失手。人工收集更多样且成功的示范又很贵，因此作者研究让 RL 负责生产数据，而非直接部署为控制器。

### 用一个例子理解

理解用例（非论文实验）：输入“把积木放进盒子”和初始场景；生成器在不同潜变量条件下尝试不同接近路径，保留成功且通过安全检查的轨迹；输出多种示范，训练视觉策略面对偏移的积木仍能选出可行动作。

## 创新点或方法

旧做法重复采集一种成功解；本文训练带潜变量条件的 RL 生成器，让不同条件对应不同成功行为，并结合并行反向课程和成功门控的多样性目标。巧处在于把探索多样性放到数据生产阶段，下游仍可使用静态数据训练。训练生成器时使用特权信息；生成轨迹经过安全过滤后，再用于预训练 flow-matching VLA 的模仿学习。部署时运行下游视觉动作策略。摘要未说明特权信息内容、课程推进规则和多样性具体怎么算。

### 方法如何工作

1. 给 RL 生成器任务条件和特权信息，使它先能找到成功行为；具体观测未说明。
2. 加入潜变量条件、并行反向课程和成功门控目标，寻找多个成功模式；摘要只说明到此。
3. 让生成器闭环执行并过滤不安全轨迹，得到可供学习的静态示范集。
4. 用示范训练下游视觉动作策略，再通过仿真和真机闭环成功率检查数据是否有用。

### 必要术语

- 行为克隆：根据示范中的观察与动作学习控制；本文是最终使用数据的学习方式。
- 潜变量条件：额外输入的隐藏行为条件；本文用它支持生成不同成功做法。
- 特权信息：训练时可获得、部署时未必可用的信息；本文供 RL 数据生成器使用。
- 成功门控：让多样性奖励受任务成功约束；本文借此避免只追求行为不同。

## 证据

摘要报告四项操作任务：下游策略平均成功率在仿真中由最强基线的 40% 升至 62%，真机由 39% 升至 78%；还报告成功状态覆盖更广，并称该做法能与纠正性数据采集互补。这支持所测任务和该预训练 VLA 下的数据收益。摘要没有给出任务名称、基线身份、数据量配平、试验次数或波动范围，尚不能量化多样性本身贡献了多少。

## 局限

目前仅有摘要，无法判断作者完整讨论了哪些局限。我的待核查问题是：收益是否仍存在于相同数据量和生成预算下，以及安全过滤会不会删掉某些有用模式。真机结果证明下游策略实际受益，但摘要没有交代生成数据如何跨越仿真与现实。

- **判断**：值得读到数据生成目标和配平实验：最有用的部分是如何让“成功且不同”成为可执行的采集标准。

## 研究关联

可以借鉴的是改变采集目标：先问数据里有几种可靠的解法，再问一共有多少条轨迹。当同一任务允许不同接近方向、动作顺序或运动路径，且能可靠判断成功时，这种采集思路值得尝试。

### 下一步读哪里

优先核查成功门控如何影响奖励、潜变量如何区分行为、反向课程从哪些状态开始；再看是否固定示范数量，以及多样性与纠正数据如何组合。输入未提供正文，不能进一步指定实验位置。

- **概念**：世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：47
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：URLError: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-27/DiscoDemo Discovering Efficient and Diverse Robot Demonstrations for Imitation L.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Behavior cloning for robotic manipulation is highly sensitive to the coverage of its training data, yet collecting diverse successful demonstrations remains costly. We study reinforcement learning (RL) not as a deployable controller, but as a data generator for downstream visuomotor imitation learning. Our key premise is that multiple successful solution modes cover a broader range of successful trajectories than repeatedly collecting a single narrow solution. We introduce DiscoDemo, which trains a privileged latent-conditioned RL generator with a parallel reverse curriculum and a success-gated diversity objective to discover diverse solutions while preserving task success. The trained generator produces multiple successful closed-loop behaviors, which are safety-filtered and exported as a static dataset for downstream imitation learning. Across four manipulation tasks, DiscoDemo produces broader successful-state coverage and improves downstream visuomotor policies in both simulation and the real world. Averaged across tasks, downstream success increases to 62% from 40% for the strongest baseline in simulation, and to 78% from 39% on the real robot, respectively. These results suggest that successful solution diversity improves imitation learning for a pretrained flow-matching VLA and remains complementary to corrective data collection. Project page: https://davian-robotics.github.io/DiscoDemo

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.32093v1
- Authors: Minho Park, Kinam Kim, Donghu Kim, Byungkun Lee, Dongyoon Hwang, Yongjae Shin, Junha Hyung, Hojoon Lee, Jaegul Choo
- Published: 2026-10-23T02:55:17Z
- Age days: 3

</details>
