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
url: "https://arxiv.org/abs/2610.32431v1"
published: "2026-10-23T09:56:27Z"
age_days: 3
score: 30
created: 2026-10-27
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> MART-GRPO 处理失败轨迹中的“连坐”：任务失败，不代表每个动作都该受罚。它用 VLM 找到最后一次可见且未观察到恢复的错误，保留到该错误区间的失败反馈，去掉之后的反馈。

## 问题

VLA 强化学习中的 GRPO 会把一个轨迹级优势分给整段动作。失败轨迹里的错误、后续纠错尝试因此可能一起受到负向更新；瓶颈是反馈没有区分哪些动作仍应为最终失败负责。

### 用一个例子理解

理解用例（非论文实验）：机器人插装失败后继续调整。训练时输入完整视频，VLM 标出最后一个未恢复错误区间，输出反馈截断位置；该位置之后不再施加这次失败的反馈。这不等于把后续动作标成正确。

## 创新点或方法

旧做法整段施加同一个优势；本文按事件截断失败反馈，成功轨迹损失项与原始归一化保持不变。先用标注数据和 LoRA 微调 VLM，再冻结它分析完整轨迹视频、选择边界，并据此训练动作策略。这个判断发生在训练反馈处理中，摘要没有说明部署执行时需要调用 VLM。

### 方法如何工作

1. 采集一组 VLA 轨迹并计算 GRPO 反馈，得到原本会分配给整段动作的优势。
2. 用标注数据微调 VLM 后冻结，使其能够识别错误与恢复事件。
3. 让 VLM 查看完整失败视频，定位最后一个可见且未观察到恢复的错误区间。
4. 保留到所选错误区间的失败反馈，移除其后部分，同时保留成功项和原始归一化。
5. 更新策略并比较任务成功率，检验减少后段惩罚是否帮助学习。

### 必要术语

- GRPO：利用同组轨迹的相对表现更新策略；本文针对其轨迹级反馈分配。
- 鞅：给定已有信息后，下一步条件期望保持当前值的随机过程；用于推导理想停止条件。
- 回溯边界：看完完整轨迹后再选择的截断位置；它与仅依据当时信息的停止条件有区别。

## 证据

理论部分给出理想停止条件：被移除梯度在保留信息下的条件期望为零，因此保留参考 GRPO 组梯度估计器的期望，并可能降低协方差。实验使用 RoboTwin 2.0 中的 OpenVLA-OFT，多任务成功率优于整轨迹 GRPO；摘要未给任务名单、提升数值、试验次数或显著性。这是仿真证据。

## 局限

理想停止时刻与看完整视频后回溯选边界不同。作者明确分析了回溯边界偏离理想条件时的期望和方差变化，因此不能把无偏保证直接套到 VLM 截断上；视觉错误也未必意味着成功概率已为零。

- **判断**：值得精读理论条件和边界消融：核心判断是实际 VLM 选点在多大程度上保留了理论收益。

## 研究关联

可借鉴的是重新检查失败反馈的作用范围。若任务已经无法成功，后续动作仍不断接收同一失败惩罚，就可能引入无助于学习的更新；先定位责任边界，可能比直接放大终局奖励更有效。

### 下一步读哪里

核查理想停止所允许的信息、回溯选点的偏差分析，以及 VLM 标注规范；再看边界误差、简单固定截断和额外标注成本的对照。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-27/When to Stop Penalizing Actions Martingale GRPO for VLA Reinforcement Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A failed vision-language-action (VLA) rollout does not imply that every action contributed to failure. Yet in group-relative policy optimization (GRPO), a single trajectory-level advantage is assigned to all actions in a rollout. Potentially useful recovery attempts can thus be penalized alongside the errors they aim to correct. Ideal stopping conditions for failure feedback are characterized using success-probability and policy-score martingales. At these stops, the removed gradient contribution has zero conditional expectation given the retained information. Truncation therefore preserves the expectation of a reference GRPO group-gradient estimator and can reduce its covariance. One such stop occurs when the conditional probability of success is zero, motivating error and recovery cues for selecting candidate feedback boundaries. Martingale GRPO (MART-GRPO) is introduced with a vision-language model (VLM) for event-guided truncation. The VLM is fine-tuned on our annotated training set using low-rank adaptation (LoRA). The last visible error without observed recovery is localized by the frozen VLM in complete rollout videos. Failure feedback is retained through the selected error interval and removed afterward, while successful-rollout loss terms and original loss normalization are preserved. For retrospective boundaries, changes in expectation and variance are analyzed to assess departures from ideal stopping. Experiments with OpenVLA-OFT on RoboTwin 2.0 show that MART-GRPO improves success rates over full-trajectory GRPO across multiple tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.32431v1
- Authors: Zongyao Zhao, Cheng-Jie Zhao, Ruihang Jiang, Bing Zheng, Zhaolin Wang, Yuanwei Liu
- Published: 2026-10-23T09:56:27Z
- Age days: 3

</details>
