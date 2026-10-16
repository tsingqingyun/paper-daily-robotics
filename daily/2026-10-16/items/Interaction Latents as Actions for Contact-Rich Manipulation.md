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
url: "https://arxiv.org/abs/2610.18855"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 36
created: 2026-10-16
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Interaction Latents as Actions for Contact-Rich Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> ILA（Interaction Latents as Actions）让机器人学习的动作同时包含“怎么移动”和“接触、用力怎样变化”，再把这种紧凑表示解码成可执行动作。关键改动是把接触过程写进动作学习目标，而不只是把触觉交给模型作为输入。

## 问题

接触密集操作需要协调运动、接触和施力过程。摘要指出，常见策略主要把运动轨迹当动作，触觉只是输入或辅助预测目标；这样即使模型感受到了接触，训练目标也未明确要求它表达完整的接触演变。真正瓶颈是动作表示没有充分承载任务所需的交互信息。

### 用一个例子理解

理解用例（非论文实验）：输入相机画面、任务指令和可用的触觉观测，要求将插头插入插座。策略生成同时描述移动与接触变化的潜变量，解码器输出执行动作。这个用例说明表示的用途，不代表论文验证了插头任务或特定施力策略。

## 创新点或方法

旧做法直接预测动作；ILA 先学习一种可解码的交互潜变量。训练时，模型结合视觉，通过联合重建动作与触觉，把两者随时间的变化压进同一表示，解码器接收时间条件。随后用流匹配学习生成这些潜变量，可用于预训练 VLA、WAM 的后训练，也可从头训练策略。推理时先生成潜变量，再由共享解码器转成动作。另一个离线改进阶段从专家示范学习触觉条件下的参考模型：成功轨迹按专家一致性加权学习，失败轨迹中的低奖励预测则借助与观测相容的专家参考修正。修正的具体计算方式未说明。

### 方法如何工作

1. 将示范中的动作和触觉联合编码，得到描述一次交互过程的潜变量，使训练目标包含接触变化。
2. 通过视觉条件下的联合重建训练表示与解码器，让潜变量保留可还原的动作和触觉信息。
3. 训练流匹配策略生成潜变量，执行时再解码成动作，连接交互表示与机器人控制。
4. 用专家参考为成功数据加权、为失败预测提供修正方向，让同一表示继续服务离线改进。

### 必要术语

- 交互潜变量：压缩后的交互表示；本文用它共同承载运动、接触和施力变化。
- 流匹配：学习从简单分布逐步生成目标样本的方法；本文生成的目标是交互潜变量。
- 专家一致性奖励：衡量预测与专家参考符合程度的信号；本文用它指导离线加权与修正。

## 证据

摘要报告：在三类策略、四项真机任务上，相比以触觉为条件的直接动作基线，平均成功率提高 21.0—36.5 个百分点。摘要还称消融支持把接触演变编码进动作目标的收益。这个对照比单纯比较“有无触觉”更贴近核心主张；但任务名称、各基线绝对成功率、试验次数及不确定性未提供，不能据此判断所有接触操作都会获益。

## 局限

我会核查动作与触觉的时间对齐、传感器配置，以及共享解码器是否能跨物体或硬件使用。专家一致性只是离线学习的指导信号，与真实成功不能直接画等号；摘要未给出两者关系的细节，也未说明部署时需要哪些触觉输入。

- **判断**：值得深入读表示学习目标和消融实验：它明确改动了动作学习目标，并用触觉条件基线检验了这一改动。

## 研究关联

值得借鉴的是：传感器信息重要时，除了增加输入，还应检查输出目标是否表达了它所约束的过程。当任务成败依赖接触如何建立、维持和释放时，把这些变化纳入动作表示，可能比只让模型读取触觉更有效。

### 下一步读哪里

先核查联合重建的损失、潜变量时间跨度和时间条件解码器，再看直接动作基线是否使用相同数据与触觉。最后检查离线改进如何匹配专家参考，以及表示改动和离线改进各自贡献多少。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/Interaction Latents as Actions for Contact-Rich Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.18855v2 Announce Type: replace Abstract: Contact-rich manipulation requires robots to coordinate not only where to move, but also how contact and force should evolve throughout an interaction. Yet most robot policies represent actions primarily as motion trajectories, using tactile signals as inputs or auxiliary prediction targets without explicitly encoding contact dynamics in the action representation. We propose ILA (Interaction Latents as Actions), which uses decodable interaction latents that jointly capture the evolution of motion, contact, and force application as policy action units, providing a shared representation for action generation, evaluation, and offline improvement. We learn these latents through visually conditioned joint action-tactile reconstruction with a time-conditioned implicit decoder. Using them as flow-matching generation targets supports post-training of pretrained vision-language-action models (VLAs) and world action models (WAMs), as well as training flow-matching policies from scratch. A shared decoder maps generated latents to executable actions. For offline improvement, we learn a tactile-conditioned expert reference model from interaction latents encoded from expert demonstrations. The resulting expert-consistency rewards guide weighted learning from successful rollouts, while observation-compatible expert references guide correction of low-reward predictions from failed rollouts. Across three policy families, ILA improves success rates averaged over four real-world tasks by 21.0-36.5 percentage points relative to tactile-conditioned direct-action baselines. Ablations highlight the benefit of encoding contact evolution in action targets beyond tactile conditioning, while the same latent space supports expert-guided offline improvement. Project website: https://mrsecant.github.io/ILA/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.18855
- Authors: Yuhang Zheng, Yujie Zang, Yuchen Liu, Yupeng Zheng, Zhennan Jiang, Zebin Xing, Shuai Tian, Songen Gu, Jingxiang Guo, Chen Gao, Zhongpu Xia, Shuicheng Yan
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
