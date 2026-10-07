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
url: "https://arxiv.org/abs/2610.07946v1"
published: "2026-10-06T08:21:19Z"
age_days: 0
score: 33
created: 2026-10-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution

> [!summary] 这篇论文到底做了什么（基于摘要）
> SALT 用上一轮动作块中尚未执行的部分，监督当前 VLA 在画面受干扰后的预测。两轮计划覆盖同一段未来时间，因此旧计划可以暂时提供参照，并把修正沿后续重规划传下去。

## 问题

机器人执行途中可能突然遇到视觉干扰，既不知道类型，也不知道发生时刻。当前画面变化后，策略可能预测出错误动作，而执行现场没有专家动作可供纠正。SALT 要解决的是如何仅靠策略已有预测，在执行中获得时间对齐的适应信号。

### 用一个例子理解

理解用例（非论文实验）：机器人预测了一块抓杯动作，执行前几步后灯光突变；下一轮输入变暗画面，SALT 将新预测与旧块剩余部分在相同未来时段对齐，更新策略后重新输出动作块，再把新剩余动作留给下一轮。

## 创新点或方法

常规重规划用新画面生成下一块动作；SALT 额外保留上一块未执行的动作，取两块覆盖同一未来区间的部分作监督。干扰刚发生时，旧块可能形成于画面正常的时候，因此能把当前预测拉向干扰前计划。测试时更新后保留适应后的策略，并重新生成当前动作块，其剩余部分继续监督下一轮。门控只在正常轨迹上校准，决定何时开始更新。训练哪些参数、损失及更新次数未说明；适应不需要干扰标签或专家动作。

### 方法如何工作

1. 保存上一块未执行的动作，获得对未来控制区间的已有预测。
2. 将当前预测与剩余动作按时间对齐，确保监督的是同一时段。
3. 门控触发后用剩余动作更新策略，使干扰后的预测受到先前计划约束。
4. 重新生成动作块并保留适应参数，让新剩余轨迹继续提供下一轮监督，也因此需要检查错误传播。

### 必要术语

- 动作块：一次预测多步未来动作；本文利用其中未执行的部分。
- 测试时适应：执行任务时继续更新模型；本文不依赖现场专家标签。
- 过渡锚定：用干扰前形成的剩余计划约束干扰后预测；本文用于跨越视觉突变。
- 顺序修正传播：更新后的新计划继续监督后续重规划；本文借此延续适应效果。

## 证据

摘要报告，LIBERO-10 仿真中五种持续视觉污染下，SmolVLA 平均成功率由 43.9% 升至 53.2%，GR00T N1.7 由 58.7% 升至 66.0%，正常条件表现大体保留。真机上，数字与物理干扰平均任务进度由 0.49 升至 0.61。它支持受测持续干扰下的适应收益；任务进度不等于成功率，摘要未列干扰类型、各类结果、正常性能具体变化和额外延迟。

## 局限

旧计划可能本来就错，物体移动或接触改变也可能让它过时；自监督会有延续错误的风险。这是我需要核查的边界，摘要没有说明作者如何处理。已有证据针对视觉扰动，不能推广到动力学突变；五类平均收益也不能证明每种干扰都改善。

- **判断**：值得读到时间对齐、门控和误差传播消融，因为核心机制容易复述，真正决定可靠性的是何时该相信旧计划。

## 研究关联

可借鉴的是时间重叠本身能提供监督：系统过去对同一未来区间的判断，是当前预测的一个参照。这个办法尤其依赖干扰前计划仍然有效、相邻重规划间环境变化有限；它把动作块的剩余部分变成了适应资源。

### 下一步读哪里

核查动作块重叠的索引与实际执行时序、门控阈值和更新参数；再看旧计划错误、环境真实变化、干扰解除时的表现，以及测试时更新的控制延迟。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Exec.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual disruptions can arise while a robot is executing a task, leaving a vision-language-action (VLA) policy to respond without knowing the disruption type or timing. We introduce Self-supervised Adaptation from Leftover Trajectories (SALT), which uses the leftover trajectory, the unexecuted part of the previous action chunk, as self-supervision for test-time adaptation. Because consecutive chunks overlap in time, the leftover provides a temporally aligned target for the current prediction over the same future control interval. At the onset of a visual shift, the leftover can retain a plan formed before the corruption, so updating the policy toward it anchors the adaptation across the shift (Transition Anchoring). SALT keeps the adapted policy and regenerates the current chunk, whose leftover becomes the target at the next replan, carrying the correction forward along the execution trajectory (Sequential Correction Propagation). Supervision comes entirely from the policy's own predictions, requiring no disruption annotations, expert actions, or target-domain demonstrations, and a lightweight adaptation gate calibrated only on nominal trajectories decides when updates begin. On LIBERO-10, SALT increases average success across five persistent visual corruptions from 43.9% to 53.2% with SmolVLA and from 58.7% to 66.0% with GR00T N1.7, while largely preserving nominal performance. On a real robot, it raises task progress averaged over digital and physical disruptions from 0.49 to 0.61.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.07946v1
- Authors: Ahin Lee, Jinwoo Seo, Youngsoo Jang, Taesik Gong
- Published: 2026-10-06T08:21:19Z
- Age days: 0

</details>
