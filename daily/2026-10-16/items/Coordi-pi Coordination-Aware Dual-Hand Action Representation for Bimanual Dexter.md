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
url: "https://arxiv.org/abs/2610.19753"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 36
created: 2026-10-16
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> Coordi-π 把双手动作从“左右拼成一大串数字”，改成按左右手交错排列的动作 token。它另外标明“属于哪只手”和“属于哪个控制时刻”，让模型更容易处理两手同时协作。

## 问题

双臂加灵巧手的动作维度高，而且两侧动作存在配合关系。现有双手 VLA 常在每个时刻拼接两侧动作，跨手关系藏在一个大向量内部。模型既要学习每侧如何运动，又要自行识别左右手之间的时序与协作结构。

### 用一个例子理解

理解用例（非论文实验）：输入画面与“左手扶盒子、右手放入物体”；模型处理左右手交错的动作表示，同一控制时刻的两侧 token 共享时间标记，最终还原成两侧臂手控制指令。

## 创新点或方法

本文把左右两侧臂手动作各自表示成 token，再交错组织。可学习的手身份嵌入说明动作属于哪一侧；分解式 RoPE 同时保留序列位置和控制时刻，因此同一时刻的左右动作虽然前后排列，仍共享时间坐标。训练中模型接触这种结构，推理输出也采用相应表示；具体训练损失、动作生成器及两侧是否同时解码，摘要未说明。

### 方法如何工作

1. 把每个控制时刻的左右臂手动作拆成独立 token，使两侧动作成为可分别处理的单位。
2. 交错排列并加入手身份嵌入，让模型区分两侧，同时在序列中接触跨手关系。
3. 分别编码序列位置与控制时刻，避免前后排列掩盖两侧动作本应同步的关系。
4. 学习并生成这种动作序列，再转换为双手控制；具体生成与转换细节摘要只说明到此。

### 必要术语

- 动作 token：供模型处理的动作表示单位；本文把左右臂手分别表示。
- 手身份嵌入：可学习的左右侧标记；防止模型混淆动作归属。
- RoPE：把位置信息加入模型计算的编码方式；本文分开表达序列顺序与控制时间。

## 证据

摘要报告，在 DexJoCo 全部五项双手灵巧操作任务中，两种随机化设置均达到作者所称最佳表现。相对 π₀.₅，rand-obj 平均成功率从 31.9% 到 51.3%，rand-full 从 18.3% 到 32.3%。四项真机任务也均优于 π₀.₅，但未提供数值。证据支持这些任务中的表示收益，尚不能拆分各项设计的独立贡献。

## 局限

摘要未定义两种随机化的具体范围，不能自行把它们解释为某类完整泛化能力。还需核查收益是否在训练数据、计算量相当时成立，以及增加 token 后的推理延迟；这些是待查问题，不是已知缺陷。

- **判断**：值得细读动作布局和位置编码消融；改动集中、机制清楚，但要靠对照实验确认收益究竟来自哪种结构信息。

## 研究关联

它提醒我们，动作怎么排给模型看，本身就是学习条件。对于多个执行部件必须同步的任务，可以尝试分别表达“谁在动作”和“何时动作”，减少模型从扁平向量中自行恢复结构的负担。

### 下一步读哪里

先核查 token 对应的动作范围及解码方式，再看手身份嵌入、交错排列、分解式 RoPE 各自消融；最后检查随机化定义和真机逐任务结果。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/Coordi-pi Coordination-Aware Dual-Hand Action Representation for Bimanual Dexter.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.19753v1 Announce Type: new Abstract: Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-dimensional and structured action space. Existing bimanual VLA policies commonly concatenate right- and left-side arm--hand actions at each control timestep, leaving cross-hand interactions implicit within a single action vector. We introduce Coordi-$\pi$, a structured action representation for bimanual dexterous manipulation. Coordi-$\pi$ represents the right- and left-side arm--hand actions as individual action tokens and organizes them into an interleaved sequence, explicitly exposing the two sides within the action sequence. To explicitly encode hand identity and temporal synchronization in this interleaved representation, a learnable hand-identity embedding distinguishes the two sides, while sequence--control-timestep factorized rotary positional encoding (RoPE) separates sequence position from control timestep, allowing actions at the same control timestep to share a temporal coordinate while retaining distinct sequence positions. Across all five bimanual dexterous manipulation tasks in DexJoCo, Coordi-$\pi$ achieves state-of-the-art performance under both \textit{rand-obj} and \textit{rand-full}, improving the average success rate over $\pi_{0.5}$ from 31.9\% to 51.3\% and from 18.3\% to 32.3\%, respectively. Coordi-$\pi$ also consistently outperforms $\pi_{0.5}$ across four real-world bimanual dexterous manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.19753
- Authors: Yiming Meng, Yanming Shao, Weijie Shen, Kunyang Lin, Jiayu Sun, Ping Luo, Yao Mu
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
