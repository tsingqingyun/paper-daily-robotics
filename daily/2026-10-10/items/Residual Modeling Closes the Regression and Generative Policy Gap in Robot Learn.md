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
url: "https://arxiv.org/abs/2610.12231v1"
published: "2026-10-08T16:16:09Z"
age_days: 1
score: 32
created: 2026-10-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> HT-Policies 重新检查了直接动作回归为何常输给生成式策略：问题可能也出在少数大误差样本占用了过多训练梯度。它用随输入变化的 Student-t 误差模型减轻这种影响，仍然一次前向就输出一段动作。

## 问题

任务是从示范学习机器人动作。MSE 回归常不如扩散或 flow matching，这通常被解释为示范存在多种正确动作。本文检查另一处瓶颈：不同状态的动作误差尺度不同，而且大误差出现得比高斯假设预期更多，MSE 会把更强的更新压力分配给这些样本。

### 用一个例子理解

理解用例（非论文实验）：输入抓取前的图像和状态；训练中，某些遮挡状态对应较分散的示范动作，模型学习其较大的残差尺度，避免个别巨大误差压过其他样本；部署时直接输出一段抓取动作。学习尺度不等于已经得到可靠的安全置信度。

## 创新点或方法

旧做法用平方误差统一惩罚动作残差；HT-Policies 改用异方差 Student-t 回归，同时学习输入相关的误差尺度，并降低重尾残差对训练的支配。摘要指出 MSE 与 Flow-Policies 都有重尾残差，但训练梯度行为不同。训练时优化这种误差模型，推理时单次前向预测动作块，还可复用预训练 flow matching 网络作骨干。具体尺度参数化和网络转换方式未说明。

### 方法如何工作

1. 分析示范动作与策略预测的差值，识别状态相关尺度变化和重尾现象。
2. 检查这些残差如何进入训练梯度，定位 MSE 对大残差样本的过度关注。
3. 训练动作预测及输入相关尺度，用 Student-t 目标减轻极端残差的影响。
4. 推理时一次前向输出动作块，避免逐步生成动作带来的开销；预训练骨干的适配细节摘要只说明到此。

### 必要术语

- 残差：预测动作与示范动作的差；本文从它解释优化差异。
- 异方差：不同输入的误差尺度不同；本文让模型学习这种变化。
- Student-t 分布：比高斯更容纳大偏差的分布；本文用它减少极端误差的训练影响。
- 动作块：一次预测的一段连续动作；本文以单次前向输出它。

## 证据

摘要报告真实机器人示范数据中的状态相关残差尺度和重尾现象，并在四个仿真基准及真机上评估。无论从头训练，还是从预训练 VLA、世界—动作模型出发，成功率都可与生成式基线竞争，训练和推理更快。未给基准名称、成功率、速度数值或统计误差，因此不能说所有任务都打平，也不能量化节省。

## 局限

这些结果支持残差建模是实际差距的一部分原因，不能排除多模态动作本身的重要性。我的待核查问题是下调大残差的影响会不会忽略稀有但关键的动作，以及 Student-t 与输入相关尺度分别贡献多少；摘要没有给出足以分离这些因素的实验细节。

- **判断**：值得读到损失公式和消融，因为这是一个能直接检验现有回归训练是否失衡的具体改动。

## 研究关联

它提醒我们：换模型家族之前，可以先检查误差分布和样本对梯度的贡献。若大误差样本长期主导训练，且误差尺度随状态变化，修改回归目标可能比增加生成步骤更直接。

### 下一步读哪里

核查 Student-t 的自由度和尺度怎样设置、动作块各维度如何建模；重点找固定尺度、仅改变分布、同时学习尺度的对照，并确认与生成式策略比较时骨干、数据和动作时域一致。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learn.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning from demonstration has enabled impressive robot behaviors. A common choice for policy learning is to use diffusion or flow matching (Flow-Policies), which often outperforms direct action regression trained with mean squared error (MSE-Policies). This gap is commonly attributed to multimodal demonstrations. We revisit this gap from the perspective of statistical modeling: how action-prediction residuals shape policy optimization. Our analysis of real-world robot demonstration data reveals substantial state-dependent variation in residual scales and heavier-than-Gaussian tails. While both MSE-Policies and Flow-Policies exhibit heavy-tailed action residuals, their training gradients behave differently: MSE allocates more gradient magnitude to observations with large action residuals, which hurts optimization. Motivated by these findings, we introduce heteroscedastic Student-t action regression (HT-Policies), which learns input-dependent residual scales and reduces the influence of heavy tails. HT-Policies predict action chunks with a single feed-forward pass and can reuse pretrained flow-matching-based policy networks as the backbone. Across four simulation benchmarks and real-robot evaluations, HT-Policies achieves success rates competitive with generative policy baselines, both when trained from scratch and from pretrained vision-language-action and world-action models, despite being faster in training and inference. Together, these findings shed light on the practical advantages of generative objectives in robot learning from demonstrations and offer an efficient direct-regression alternative for a range of architectures and tasks. Project page: https://the-labone.github.io/regression-policy-project/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12231v1
- Authors: Yuchen Zhou, Jiacheng You, Weikang Wan, Weijun Dong, Yang Gao, Jiayuan Mao
- Published: 2026-10-08T16:16:09Z
- Age days: 1

</details>
