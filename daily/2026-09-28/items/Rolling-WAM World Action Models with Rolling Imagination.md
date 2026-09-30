---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30247v1"
published: "2026-09-24T17:58:03Z"
age_days: 3
score: 28
created: 2026-09-28
concepts: ["智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Rolling-WAM: World Action Models with Rolling Imagination

> [!summary] 先说人话（基于摘要）
> Rolling-WAM 不在每次重规划时从头生成整段未来，而是保留尚未完成去噪的视频动作预测，边执行边继续细化。最近要执行的动作优先完成，远期预测分摊到后续周期。

## 问题

联合预测视频与动作的 WAM 每轮都完成全预测窗口去噪，会拖慢动作更新，限制闭环响应。瓶颈在跨重规划周期重复承担完整生成成本。

## 创新点或方法

维护不同噪声水平的视频动作块滑动窗口，用滚动噪声调度完全去噪临近动作、部分细化远期块。新相机观测到来后窗口前移，保留的未来块继续去噪，同时携带跨动作块的预测上下文。

## 证据

在 LIBERO、RoboTwin 和真实 Unitree G1 人形机器人上评估，摘要报告操作性能有竞争力；相对标准联合 WAM，稳态重规划速度提高 4.5 倍。未给出具体成功率。

## 局限

4.5 倍是稳态重规划提速，不能直接解释为启动延迟或整项任务耗时改善；需核查突发观测变化时，保留预测如何被纠正。

- **判断**：值得精读调度实现与动态变化实验，适合已有联合视频动作模型、受重规划延迟限制的团队。

## 研究关联

对世界动作模型和机器人智能体研究者，提供了直接改变推理调度、复用未来预测计算的机制，适合研究生成式策略的闭环响应效率。

- **概念**：智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/Rolling-WAM World Action Models with Rolling Imagination.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) couple action generation with future visual prediction for robotic manipulation. However, completing the joint video-action denoising process at each replanning cycle incurs substantial latency, delaying action updates and limiting closed-loop responsiveness. We present Rolling-WAM, a formulation that distributes joint denoising across successive replanning cycles. Our method maintains a sliding window of video-action chunks at staggered noise levels. At each step, a rolling noise schedule fully denoises the imminent action chunk for execution, while partially refining farther-future chunks. As the window advances with new camera observations, the retained future chunks continue their denoising process. This distributes the computational cost over time while carrying an evolving visual-action context across chunk boundaries. Evaluations on LIBERO, RoboTwin, and a real-world Unitree G1 humanoid show that Rolling-WAM achieves competitive manipulation performance. By removing the need to denoise the entire prediction horizon from scratch, it delivers a 4.5x steady-state replanning speedup over standard joint WAMs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30247v1
- Authors: Yinghua Zhou, Junjie Ye, Yiqi Zhao, Hao Dong, Celina Shiyu Wang, Ruohai Ge, Tingyi Yang, Basile Van Hoorick, Gaurav Sukhatme, Vitor Guizilini, Yue Wang
- Published: 2026-09-24T17:58:03Z
- Age days: 3

</details>
