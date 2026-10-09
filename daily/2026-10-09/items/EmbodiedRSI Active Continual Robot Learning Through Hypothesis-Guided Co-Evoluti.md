---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.10498v1"
published: "2026-10-07T17:48:02Z"
age_days: 1
score: 40
created: 2026-10-09
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> EmbodiedRSI 不改机器人基础模型，而是改围绕它运行的代码、技能和记忆。关键是每次试验先问“这次能分清哪些改进是否有效”，再按信息收益与成本决定试什么。

## 问题

任务是物体位置、指令或技能组合变化后的操作。重新训练底层模型需要昂贵数据；现有执行层自我修改又容易反复尝试相似方案，代码与技能各改各的，记忆只堆积而不检验后续用途 [S4](https://arxiv.org/html/2610.10498v1#S1.p1.1) [S5](https://arxiv.org/html/2610.10498v1#S1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放进柜子”和场景观察；系统怀疑失败来自开门顺序或抓取技能，分别及联合测试；输出经证据支持的新执行程序与技能搭配。

## 创新点或方法

旧做法是提出修改后试运行；本文先保留竞争假设，再选能减少疑问的配对实验。相同初始状态下分别测代码修改、技能修改及二者组合，减少把环境差异误认成改进的风险。快系统更新假设和可执行方案；慢系统整理记忆，其管理策略用 PPO 按后续成功、疑问减少和试验成本学习。底层机器人模型始终冻结；演化在仿真完成，再零样本转到真机，评估时是否继续更新执行层，节选未说明 [S8](https://arxiv.org/html/2610.10498v1#S1.p5.1) [S20](https://arxiv.org/html/2610.10498v1#S3.SS2.p3.1) [S25](https://arxiv.org/html/2610.10498v1#S3.SS3.p3.1) [S26](https://arxiv.org/html/2610.10498v1#S3.SS3.p4.1) [S27](https://arxiv.org/html/2610.10498v1#S3.SS3.p4.2)。

### 方法如何工作

1. 把轨迹和成败转成代码、技能假设，并保留修订关系，让下一轮知道修改依据。
2. 估计候选实验能减少多少不确定性，再除以执行成本，优先做更能回答问题的试验 [S19](https://arxiv.org/html/2610.10498v1#S3.SS2.p2.2)。
3. 同起点比较单项与联合修改，更新支持度并保留有效搭配。
4. 将原始经历、假设和归纳知识分层保存，按对后续试验的作用学习如何整理记忆。

### 必要术语

- 执行层：组织底层策略调用的代码与技能；本文主要修改这里。
- 信息价值：一次试验预计能消除多少疑问；本文用它与成本之比排序。
- 配对试验：尽量保持起点和其他调用一致的对照；用于判断修改效果。

## 证据

RoboCasa365 仿真总体成功率为 77.0%，Harness VLA 为 63.6%；未见组合任务为 71.3% 对 40.1%，后者不是基线总体成绩 [S43](https://arxiv.org/html/2610.10498v1#S4.T1.4.1)。演化和评估使用互不重叠种子 [S29](https://arxiv.org/html/2610.10498v1#S4.SS1.p1.1)。LIBERO-Pro 为 86.8%，真机为 71.3% [S8](https://arxiv.org/html/2610.10498v1#S1.p5.1)，但节选缺少对应完整比较及真机试验数量。成绩支持执行层适应有效；学习效率表只有标题，不能据此量化节省多少试验。

## 局限

作者明确指出冻结模型也限制了改进层次 [S49](https://arxiv.org/html/2610.10498v1#S5.p2.1)。我的待核查问题是：候选实验的结果概率估计是否可靠，复位和大模型计算是否完整计入成本；组合成绩领先也不能单独证明每个组件都必要。

- **判断**：值得读到选实验规则和消融结果，因为真正有用的贡献是试验分配与归因，而不只是成功率。

## 研究关联

可借鉴的是把失败后的修改写成可区分的假设，并用同起点对照检验。试错昂贵、候选改动相互影响时，这比凭一次成功保留修改更可靠。

### 下一步读哪里

先看 [S15](https://arxiv.org/html/2610.10498v1#S3.SS2.p1.1) [S18](https://arxiv.org/html/2610.10498v1#S3.SS2.p2.1) [S19](https://arxiv.org/html/2610.10498v1#S3.SS2.p2.2) [S20](https://arxiv.org/html/2610.10498v1#S3.SS2.p3.1) [S21](https://arxiv.org/html/2610.10498v1#S3.SS2.p3.2)，再核查附录 D 的结果概率、成本权重，以及学习效率表和真机协议；这些内容未完整提供。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.10498v1
- 获取时间：2026-10-09T00:15:43.699637+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.10498v1#p1.2)
- [S2] [EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution · 正文段落 2](https://arxiv.org/html/2610.10498v1#abstract1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.10498v1#S1.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.10498v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.10498v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.10498v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.10498v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.10498v1#S1.p5.1)
- [S9] [2 Related Work · 正文段落 9](https://arxiv.org/html/2610.10498v1#S2.p1.1)
- [S10] [2 Related Work · 正文段落 10](https://arxiv.org/html/2610.10498v1#S2.p2.1)
- [S11] [3 Method · 正文段落 12](https://arxiv.org/html/2610.10498v1#S3.F2)
- [S12] [3.1 Problem Formulation · 正文段落 14](https://arxiv.org/html/2610.10498v1#S3.SS1.p2.1)
- [S13] [3.1 Problem Formulation · 正文段落 16](https://arxiv.org/html/2610.10498v1#S3.SS1.p2.2)
- [S14] [3.1 Problem Formulation · 正文段落 19](https://arxiv.org/html/2610.10498v1#S3.SS1.p3.1)
- [S15] [3.2 Fast System: Rapid Code-Skill Co-Evolution · 正文段落 21](https://arxiv.org/html/2610.10498v1#S3.SS2.p1.1)
- [S16] [3.2 Fast System: Rapid Code-Skill Co-Evolution · 正文段落 23](https://arxiv.org/html/2610.10498v1#S3.SS2.p1.2)
- [S17] [3.2 Fast System: Rapid Code-Skill Co-Evolution · 正文段落 25](https://arxiv.org/html/2610.10498v1#S3.SS2.p1.3)
- [S18] [3.2 Fast System: Rapid Code-Skill Co-Evolution · 正文段落 26](https://arxiv.org/html/2610.10498v1#S3.SS2.p2.1)
- [S19] [3.2 Fast System: Rapid Code-Skill Co-Evolution · 正文段落 28](https://arxiv.org/html/2610.10498v1#S3.SS2.p2.2)
- [S20] [3.2 Fast System: Rapid Code-Skill Co-Evolution · 正文段落 29](https://arxiv.org/html/2610.10498v1#S3.SS2.p3.1)
- [S21] [3.2 Fast System: Rapid Code-Skill Co-Evolution · 正文段落 31](https://arxiv.org/html/2610.10498v1#S3.SS2.p3.2)
- [S22] [3.2 Fast System: Rapid Code-Skill Co-Evolution · 正文段落 32](https://arxiv.org/html/2610.10498v1#S3.F3)
- [S23] [3.3 Slow System: Hierarchical Memory and Reward-Grounded Memory Learning · 正文段落 33](https://arxiv.org/html/2610.10498v1#S3.SS3.p1.1)
- [S24] [3.3 Slow System: Hierarchical Memory and Reward-Grounded Memory Learning · 正文段落 38](https://arxiv.org/html/2610.10498v1#S3.SS3.p2.3)
- [S25] [3.3 Slow System: Hierarchical Memory and Reward-Grounded Memory Learning · 正文段落 39](https://arxiv.org/html/2610.10498v1#S3.SS3.p3.1)
- [S26] [3.3 Slow System: Hierarchical Memory and Reward-Grounded Memory Learning · 正文段落 40](https://arxiv.org/html/2610.10498v1#S3.SS3.p4.1)
- [S27] [3.3 Slow System: Hierarchical Memory and Reward-Grounded Memory Learning · 正文段落 42](https://arxiv.org/html/2610.10498v1#S3.SS3.p4.2)
- [S28] [4 Experiments · 正文段落 43](https://arxiv.org/html/2610.10498v1#S4.p1.1)
- [S29] [4.1 Experimental Setup · 正文段落 44](https://arxiv.org/html/2610.10498v1#S4.SS1.p1.1)
- [S30] [4.1 Experimental Setup · 正文段落 45](https://arxiv.org/html/2610.10498v1#S4.SS1.p2.1)
- [S31] [4.1 Experimental Setup · 正文段落 46](https://arxiv.org/html/2610.10498v1#S4.SS1.p3.1)
- [S32] [4.1 Experimental Setup · 正文段落 47](https://arxiv.org/html/2610.10498v1#S4.F4.2.1.1)
- [S33] [4.1 Experimental Setup · 正文段落 48](https://arxiv.org/html/2610.10498v1#S4.F4.2.2.1)
- [S34] [4.1 Experimental Setup · 正文段落 49](https://arxiv.org/html/2610.10498v1#S4.F4.2.3)
- [S35] [4.1 Experimental Setup · 正文段落 50](https://arxiv.org/html/2610.10498v1#S4.F4.3.1.1)
- [S36] [4.1 Experimental Setup · 正文段落 51](https://arxiv.org/html/2610.10498v1#S4.F4.3.2.1)
- [S37] [4.1 Experimental Setup · 正文段落 52](https://arxiv.org/html/2610.10498v1#S4.F4.3.3)
- [S38] [4.1 Experimental Setup · 正文段落 53](https://arxiv.org/html/2610.10498v1#S4.F4.4.1.1)
- [S39] [4.1 Experimental Setup · 正文段落 54](https://arxiv.org/html/2610.10498v1#S4.F4.4.2.1)
- [S40] [4.1 Experimental Setup · 正文段落 55](https://arxiv.org/html/2610.10498v1#S4.F4.4.3)
- [S41] [4.1 Experimental Setup · 正文段落 56](https://arxiv.org/html/2610.10498v1#S4.F4)
- [S42] [4.1 Experimental Setup · 正文段落 57](https://arxiv.org/html/2610.10498v1#S4.T1)
- [S43] [4.1 Experimental Setup · 正文段落 58](https://arxiv.org/html/2610.10498v1#S4.T1.4.1)
- [S44] [4.2 Generalization on RoboCasa365 and LIBERO-Pro · 正文段落 59](https://arxiv.org/html/2610.10498v1#S4.SS2.p1.1)
- [S45] [4.2 Generalization on RoboCasa365 and LIBERO-Pro · 正文段落 60](https://arxiv.org/html/2610.10498v1#S4.SS2.p2.1)
- [S46] [4.2 Generalization on RoboCasa365 and LIBERO-Pro · 正文段落 62](https://arxiv.org/html/2610.10498v1#S4.T2)
- [S47] [4.4 Ablation Study · 正文段落 74](https://arxiv.org/html/2610.10498v1#S4.F6.fig1)
- [S48] [4.4 Ablation Study · 正文段落 76](https://arxiv.org/html/2610.10498v1#S4.T4)
- [S49] [5 Conclusion · 正文段落 83](https://arxiv.org/html/2610.10498v1#S5.p2.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-09/EmbodiedRSI Active Continual Robot Learning Through Hypothesis-Guided Co-Evoluti.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolving harnesses use robot trials inefficiently when deciding which code and skill changes to pursue. We introduce EmbodiedRSI, a self-evolving agentic harness that autonomously decides where to explore next and turns the resulting physical interaction into improved code and skills. EmbodiedRSI realizes this through a Fast-Slow Dual-System Architecture, in which competing code and skill hypotheses are maintained in a Hypothesis Graph. Value-of-Information Experiment Selection chooses physical experiments that can distinguish these hypotheses. Their outcomes guide Code-Skill Co-Evolution. The Slow System builds Hierarchical Memory, and Reward-Grounded Memory Learning selects effective memory according to their value for later Fast-System improvement. On RoboCasa365, EmbodiedRSI reaches 77.0% overall success and 71.3% on Composite-Unseen, compared with 40.1% for the best baseline. EmbodiedRSI also reaches 86.8% overall success on LIBERO-Pro. Beyond benchmark performance, EmbodiedRSI transfers zero-shot to real-world robot, achieving 71.3% overall success across multiple challenging tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10498v1
- Authors: Python Song, Zhixuan Liang, Kelsey Fu, Mengdi Wang, Junfeng Yang, Shilong Liu
- Published: 2026-10-07T17:48:02Z
- Age days: 1

</details>
