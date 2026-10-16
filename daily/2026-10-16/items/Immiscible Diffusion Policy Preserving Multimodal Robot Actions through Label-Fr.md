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
url: "https://arxiv.org/abs/2610.09369"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 34
created: 2026-10-16
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# Immiscible Diffusion Policy: Preserving Multimodal Robot Actions through Label-Free Noise Assignment

> [!summary] 这篇论文到底做了什么（基于摘要）
> Immiscible Diffusion Policy 处理扩散策略总偏向一种动作解法的问题。它只改训练时动作与噪声的分配，让不同解法保留相对分离的去噪路线，不改网络和推理过程。

## 问题

一个任务可能有几种合理动作，但扩散策略即使看到数量均衡、批次内严格对称的数据，执行时仍可能只用其中一种。作者分析认为，独立的动作—噪声配对使去噪路径混杂、交叉，容易学出平均响应，压制各解法特有的动作；低维且密集的机器人动作空间会加重这个问题。

### 用一个例子理解

理解用例（非论文实验）：输入绕障抓物的演示，其中有从左侧和右侧接近两种动作；训练时重新分配动作与噪声，减少两条路线的混杂；部署时照常去噪生成动作，检查两种成功路线是否都能出现。

## 创新点或方法

普通训练独立配对动作和噪声，本文改用无需动作类别标签的分配方式，让噪声到不同动作的路线保持相对区分。这样希望减少训练目标之间的混杂，而不是要求策略事先知道每种解法的名称。改动仅发生在训练时；推理仍沿用原扩散策略。具体分配目标、求解算法与额外训练开销，摘要未说明。

### 方法如何工作

1. 收集含多种动作解法的示范，明确要保留的是动作差异，而非不同传感器输入。
2. 训练时分配动作与噪声，使对应不同动作的去噪路线相对分离；摘要只说明到此，未给求解细节。
3. 沿用原策略结构学习去噪，减少混杂监督对特定动作解法的压制。
4. 推理时沿用原采样流程，分别统计动作模态出现情况和任务表现，验证多样性是否保留下来。

### 必要术语

- 动作模态：完成任务的一类不同动作解法；本文关注多种解法能否都被策略生成。
- 去噪：从噪声逐步生成动作的过程；本文试图让不同解法对应的生成路线少混杂。
- 无标签分配：无需人工标注每条动作属于哪种解法就进行配对；这是本文训练改动的特征。

## 证据

摘要报告五项仿真、两项真实世界人形机器人操作任务，观察输入覆盖状态、RGB 和点云。在三项双模态任务中，非主导动作模态的占比提高 6.0—14.6 倍；两项四模态任务中，恢复了普通策略执行时完全未出现的示范模态。结果支持更好保留多种动作解法，但未给各任务名称、占比绝对值、成功率数字或统计误差，不能据倍数判断最终是否均衡。

## 局限

作者的路径混杂分析提供了机制解释，但仅凭摘要还无法判断它在各种策略中的因果证据强度。还需核查新增模态是否同样成功、稳定，以及在不同初始条件下是否适用；多样性增加本身不保证任务完成更好。

- **判断**：若关注动作多样性，值得细读分配算法和受控实验，因为它给出了一个无需改推理流程、可以直接检验的训练改动。

## 研究关联

如果数据中明明有多种解法，策略却只执行一种，值得检查训练样本如何与噪声组成监督，而不只检查数据比例或增大网络。这里把一个行为问题追溯到了训练配对过程。

### 下一步读哪里

优先核查分配依据是什么、是否引入其他偏差，再对照普通策略查看各模态的绝对占比、任务成功率及随机种子结果；确认哪些结果来自真机。

- **概念**：多模态基础模型 智能体 Agent 机器人学习
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/Immiscible Diffusion Policy Preserving Multimodal Robot Actions through Label-Fr.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.09369v2 Announce Type: replace Abstract: When diffusion policies were first introduced, they were expected to recover multi-modal action distributions. However, we find this expectation does not always hold, as diffusion policies often collapse to a single modality even when we guarantee the balance of dataset modalities and exact within-batch symmetry. Our analysis indicates that independent action-noise pairing contributes to this failure by increasing mixing and crossing among diffusion paths, which can produce averaged denoising responses and suppress modality-specific behavior. This issue is especially severe in robot planning, where action spaces are dense and low-dimensional, significantly increasing such mixing and crossing. To alleviate this problem, we propose Immiscible Diffusion Policy, a label-free training-time add-on to diffusion policy that uses action-noise assignment to preserve relatively distinct noise-to-action routes without modifying the policy architecture or inference procedure. Across five simulated and two real-world humanoid manipulation tasks spanning state, RGB, and point-cloud observations, our method significantly improves the policy's preservation of action modalities while maintaining strong task performance. It increases the proportion of the non-dominant modality by 6.0x-14.6x across three two-modality tasks and recovers demonstrated modalities that are entirely absent from vanilla policy rollouts on both four-modality tasks. These results demonstrate that Immiscible Diffusion Policy provides a simple yet robust approach to preserving action multi-modality in general robot learning tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09369
- Authors: Xiao Zhang, Yuxin Chen, Zhixuan Liang, Guojian Zhan, Chenran Li, Chenfeng Xu, Masayoshi Tomizuka, Yiheng Li
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
