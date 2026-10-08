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
url: "https://arxiv.org/abs/2610.09369v1"
published: "2026-10-07T03:22:26Z"
age_days: 0
score: 34
created: 2026-10-08
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# Immiscible Diffusion Policy: Preserving Multimodal Robot Actions through Label-Free Noise Assignment

> [!summary] 这篇论文到底做了什么（基于摘要）
> Immiscible Diffusion Policy 处理扩散策略学会一种动作、却丢掉其他有效动作的问题。它只改训练时动作与噪声的配对，让通向不同动作的去噪路线较少混在一起，网络和推理流程都不用改。

## 问题

同一观测可能对应多种合理动作，但扩散策略即使看到数量平衡、批次内严格对称的数据，也可能只输出其中一种。作者分析认为，独立动作—噪声配对会增加扩散路径的混合和交叉，使去噪响应趋向平均，压制不同动作方式；密集、低维的机器人动作空间尤其容易出现这一问题。

### 用一个例子理解

理解用例（非论文实验）：同一场景里，夹爪可以从左侧或右侧绕过障碍抓杯子。训练输入包含这两种动作和噪声，分配机制减少两条路线混合；推理输入当前观测与随机噪声，输出其中一条动作路线。这个用例仅解释多解问题。

## 创新点或方法

原来为动作独立配噪声，可能让相近去噪区域同时承担不同动作方向；本文通过动作—噪声分配，保留相对分离的噪声到动作路线。这样有望减少训练目标之间的混淆，而不需要给动作方式贴类别标签。改动只发生在训练配对阶段，推理仍按原扩散策略生成动作；分配的代价函数、求解范围和计算开销未说明。

### 方法如何工作

1. 取训练动作与噪声，识别原始独立配对可能造成的路线混合问题。
2. 重新分配动作与噪声，让不同目标尽量保留相对独立的去噪路线；具体分配规则摘要未说明。
3. 使用重新配对的数据训练原策略，不增加动作类别标签或修改网络。
4. 按原流程采样动作，并检查各示范模式是否仍出现，同时独立衡量任务表现。

### 必要术语

- 动作多模态：同一条件有多种合理动作方式；本文希望保留这些不同解。
- 模式坍缩：输出集中于一种方式、其他方式消失；是本文要缓解的现象。
- 动作—噪声分配：决定每个训练动作配哪份噪声；是本文唯一明确改动的训练环节。

## 证据

摘要报告五个仿真任务和两个真实世界人形机器人操作任务，覆盖状态、RGB 与点云观测。相比原始策略，三个双模式任务中的非主导模式占比增至 6.0—14.6 倍；两个四模式任务中，恢复了原策略执行时完全未出现的示范模式。摘要还称保持较强任务表现，但未给成功率、各任务模式占比或统计波动，因此不能把模式恢复直接等同于成功率提升。

## 局限

倍数大并不说明少数模式最终占比已经充分，需要看原始占比和目标分布。我的待核查问题是路径混合的解释有怎样的对照支持、模式如何识别，以及对更多连续动作差异是否仍有效。真实任务结果也不能替所有机器人类型背书。

- **判断**：值得深入读配对算法和受控实验：改动小、机制明确，但应先确认它恢复的是有效动作方式，而不只是增加输出变化。

## 研究关联

这篇改变的是排查动作多样性丢失的顺序：数据平衡之后，还应检查噪声如何与训练目标配对。若同一状态确实存在多个有效解，先检查这个训练环节，可能比扩大网络更直接。

### 下一步读哪里

先核查动作—噪声匹配准则和训练成本，再看数据严格平衡时的对照、模式判定方式及完整占比分布；同时确认真实任务的成功率是否随模式保留而变化。

- **概念**：多模态基础模型 智能体 Agent 机器人学习
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/Immiscible Diffusion Policy Preserving Multimodal Robot Actions through Label-Fr.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

When diffusion policies were first introduced, they were expected to recover multi-modal action distributions. However, we find this expectation does not always hold, as diffusion policies often collapse to a single modality even when we guarantee the balance of dataset modalities and exact within-batch symmetry. Our analysis indicates that independent action-noise pairing contributes to this failure by increasing mixing and crossing among diffusion paths, which can produce averaged denoising responses and suppress modality-specific behavior. This issue is especially severe in robot planning, where action spaces are dense and low-dimensional, significantly increasing such mixing and crossing. To alleviate this problem, we propose Immiscible Diffusion Policy, a label-free training-time add-on to diffusion policy that uses action-noise assignment to preserve relatively distinct noise-to-action routes without modifying the policy architecture or inference procedure. Across five simulated and two real-world humanoid manipulation tasks spanning state, RGB, and point-cloud observations, our method significantly improves the policy's preservation of action modalities while maintaining strong task performance. It increases the proportion of the non-dominant modality by 6.0x-14.6x across three two-modality tasks and recovers demonstrated modalities that are entirely absent from vanilla policy rollouts on both four-modality tasks. These results demonstrate that Immiscible Diffusion Policy provides a simple yet robust approach to preserving action multi-modality in general robot learning tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09369v1
- Authors: Xiao Zhang, Yuxin Chen, Zhixuan Liang, Guojian Zhan, Chenran Li, Chenfeng Xu, Masayoshi Tomizuka, Yiheng Li
- Published: 2026-10-07T03:22:26Z
- Age days: 0

</details>
