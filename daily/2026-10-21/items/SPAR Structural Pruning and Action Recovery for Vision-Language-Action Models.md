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
url: "https://arxiv.org/abs/2610.26487v1"
published: "2026-10-19T14:28:51Z"
age_days: 1
score: 34
created: 2026-10-21
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> SPAR 先把 VLA 语言骨干中的隐藏维度和前馈中间维度大幅裁小，再用强化学习恢复操作能力。它把压缩和动作恢复分成两个相接的步骤，使模型变小后仍有机会重新学会完成任务。

## 问题

机器人机载算力有限，大型 VLA 的推理成本难以承担。但激进压缩会破坏操作策略，而且摘要指出，仅靠监督微调不足以恢复性能。具体问题因此是：怎样删掉大量计算结构，同时补回压缩造成的动作能力损失。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“把杯子放到盘子旁”；离线先裁小策略并用任务反馈训练，部署时由这个小策略处理图像和指令；输出机械臂动作。例子展示训练与推理的分工，不代表该具体任务已被验证。

## 创新点或方法

旧做法在压缩后依赖监督微调恢复行为；SPAR 先通过考虑剪枝的调优，同时裁剪语言骨干的隐藏维度和前馈中间维度，再应用强化学习恢复策略。前一步直接缩小网络结构，后一步让压缩策略根据任务反馈继续改进动作。训练包含剪枝相关调优和后续强化学习；部署推理使用压缩后的策略，不需要每次执行时再训练。摘要没有说明剪枝重要性指标、奖励设计、强化学习算法及训练成本。

### 方法如何工作

1. 以 π₀.₅ 为起点确定要缩减的语言骨干维度，使压缩直接改变网络规模。
2. 在考虑剪枝的调优中同时裁剪两类维度，得到参数更少、但可能损失操作能力的策略。
3. 对压缩策略进行强化学习，让任务反馈推动动作改善，补偿剪枝后的性能损失。
4. 部署恢复后的压缩策略并测量完整推理速度；具体训练算法和硬件设置，摘要只说明到此。

### 必要术语

- 结构剪枝：直接删除网络中的维度等结构；本文靠它缩小实际模型。
- 前馈中间维度：网络前馈层内部的表示宽度；它是本文裁剪的对象之一。
- 强化学习：通过奖励反馈改进行为；本文用于恢复剪枝后的操作成功率。

## 证据

在 π₀.₅ 上，语言骨干由 2.34B 缩至 0.09B 参数，完整模型由 3.37B 缩至 1.12B，分别删去约 96% 和 67% 的参数。该压缩程度下，强化学习将四个 LIBERO 套件的平均成功率从 84.55% 提至 93.45%，增加 8.90 个百分点；完整策略推理相对未剪枝模型加速 1.98 倍，均来自摘要。这里的成功率增益对应压缩后强化学习带来的恢复，不能解读为比原始模型高 8.90 个百分点。LIBERO 是仿真评测，摘要未给真机结果。

## 局限

语言骨干删去约 96% 参数，并不等于整套策略计算减少同样比例，摘要中的完整模型规模和实际加速已经体现了这一边界。我会核查恢复训练需要多少交互、未剪枝策略的成功率，以及加速测试的硬件和输入设置，才能判断部署收益是否覆盖训练代价。

- **判断**：值得细读压缩配置、恢复曲线和延迟测量；它给出了明确的体积与速度收益，但是否适合实际部署取决于恢复成本和硬件条件。

## 研究关联

可借鉴之处是把“删参数后模仿原有动作”扩展为“删参数后重新优化任务表现”。当小模型难以完整复制大模型行为、但能获得有效任务反馈时，强化学习可能为压缩后的策略找到可行的动作方式。

### 下一步读哪里

先看隐藏维度与前馈维度怎样联合选择，再核查 84.55% 对应的确切训练状态。实验应检查四个套件的分项表现、未剪枝基线、强化学习预算，以及 1.98 倍加速是否包含完整动作生成流程。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/SPAR Structural Pruning and Action Recovery for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The limited onboard computing resources of robots make the inference demands of vision-language-action (VLA) models costly to accommodate. Reducing these demands through aggressive compression, however, can degrade manipulation performance beyond what supervised fine-tuning alone recovers. We present SPAR (Structural Pruning and Action Recovery), which simultaneously prunes the hidden and feed-forward intermediate dimensions of the large language model (LLM) backbone through pruning-aware tuning, then applies reinforcement learning (RL) to recover policy performance. Applied to $π_{0.5}$, SPAR reduces the language backbone from 2.34B to 0.09B parameters and the full model from 3.37B to 1.12B, removing approximately 96% and 67% of their parameters, respectively. At this compression level, RL raises average success across the four LIBERO suites from 84.55% to 93.45%, an 8.90-percentage-point gain. The compressed policy achieves a $1.98\times$ full-policy inference speedup over the unpruned model. These results identify substantial intermediate-dimension redundancy and show that post-pruning RL can recover manipulation performance in compact policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.26487v1
- Authors: Shenli Zheng, Zhou Fang, Yuan Du, Yijiang Liu, Li Du
- Published: 2026-10-19T14:28:51Z
- Age days: 1

</details>
