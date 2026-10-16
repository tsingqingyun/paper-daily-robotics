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
url: "https://arxiv.org/abs/2610.19656"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-10-16
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Accelerating VLA Inference with Perturbation Informed Execution

> [!summary] 这篇论文到底做了什么（基于摘要）
> PICES 不重新训练 VLA，而是让它一次生成多组动作及各自的小扰动版本，再根据动作变化决定选哪组、连续执行多久。它试图在预测较稳定时少调用模型，在敏感时更早重新观察和计算。

## 问题

动作块模型会预测未来一串动作，固定执行长度却只使用其中一段。执行得短，需要频繁调用昂贵策略；统一执行得长，又会减少纠错机会。真正要解决的是每个时刻该信任当前预测多远，而不是为全部任务选一个固定长度。

### 用一个例子理解

理解用例（非论文实验）：输入图像和“把积木移到盒内”；若候选对在接近盒沿时明显分歧，PICES 可选择较短执行段，让机器人较早获得新图像，再输出下一段动作。

## 创新点或方法

旧做法固定选取动作块前缀；PICES 在一次策略调用内，复用相同条件特征，从多个初始噪声及其局部扰动版本批量生成动作块。随后比较每对动作在对应时刻的差异，为候选块选择执行长度，再选出实际执行的原始块。这里的直觉是用局部扰动敏感性辅助决定执行跨度，但摘要没有给出阈值、评分公式，也未证明差异就是校准后的风险。方法无需额外训练，新增计算发生在推理阶段。

### 方法如何工作

1. 复用当前图像和语言条件特征，生成多个噪声起点及其扰动对，减少重复条件编码。
2. 批量生成配对动作块，得到同一条件下对局部噪声变化的响应。
3. 比较对应动作的差异，为每个候选决定执行跨度，并据此选择原始动作块；具体规则未说明。
4. 执行所选长度后再次调用策略，用可变调用间隔平衡计算成本与纠错机会。

### 必要术语

- 动作块：一次预测的一串未来动作；本文决定实际使用其中多长的一段。
- 执行时域：重新调用策略前连续执行的动作数量；越长通常越少重算。
- 局部扰动：对初始噪声做小幅改动；本文利用输出差异辅助选择执行长度。

## 证据

摘要称在仿真基准和真机操作中，PICES 相对固定执行长度基线，在 Jetson Orin 与 Thor 上将墙钟策略推理时间最多加速 2.3 倍，同时提高成功率。没有给出任务名称、基线执行长度、成功率数值和平均加速，因而只能确认作者报告了这些设置下的最佳加速与成功率改善，不能推成每项任务均有 2.3 倍收益，也不能等同于完整任务耗时下降。

## 局限

对噪声扰动稳定，只说明模型局部输出相近；模型也可能稳定地给出错误动作。环境突然变化能否及时打断长执行段，需要另外核查。候选批次会增加单次计算与内存需求，净收益取决于硬件和任务。

- **判断**：值得读选择规则和完整计时实验；它的吸引力是无需训练即可改执行策略，但效果取决于扰动差异能否可靠指示何时该重算。

## 研究关联

值得借鉴的是把重新计算的时机也当成决策变量：已有动作块未必每次都只能用固定长度。若硬件能较高效地批量生成候选，用额外并行计算换取更少串行策略调用，是可检验的部署思路。

### 下一步读哪里

下一步核查噪声扰动幅度、候选数、差异到执行长度的映射，以及选择动作块的准则；再看是否计入候选生成全部开销、固定长度基线是否充分调优，以及动态扰动测试。输入没有正文节选。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/Accelerating VLA Inference with Perturbation Informed Execution.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.19656v2 Announce Type: new Abstract: Action-chunking vision-language-action (VLA) models predict sequences of future robot actions. Under fixed-horizon execution, the robot executes a fixedlength prefix of each predicted chunk before invoking the policy again, leaving the remaining predictions unused. For a given number of executed actions, short execution horizons require more policy calls. Extending the execution horizon amortizes policy inference cost over more actions. However, uniformly applying long horizons across episodes can limit opportunities for precise corrections. To address this limitation, we propose PICES (Perturbation-Informed Chunk and Execution Horizon Selection), a training-free method that jointly selects an action chunk and the number of actions executed before the next policy call. Within a single policy call, the action expert generates a batch of action chunks from multiple initial noise samples and their locally perturbed counterparts, using the same conditioning features across all samples. PICES exploits differences between corresponding actions in each nominal chunk and its counterpart to determine candidate-specific execution horizons and select a nominal chunk for execution. Experiments on simulation benchmarks and real-world manipulation tasks demonstrate that PICES achieves speedup by up to 2.3x in wall-clock policy inference time on Jetson Orin and Thor relative to fixed horizon baselines while improving the success rate.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.19656
- Authors: Jehun Lee, Hajun Lee, Jimin Ryu, Youhan Lee, Beomseok Kang, Jonghyun Choi, Jae-Joon Kim
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
