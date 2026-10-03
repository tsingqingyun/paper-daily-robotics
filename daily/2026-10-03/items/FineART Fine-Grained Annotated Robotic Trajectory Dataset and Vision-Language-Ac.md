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
url: "https://arxiv.org/abs/2609.36416"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 41
created: 2026-10-03
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# FineART: Fine-Grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> FineART 为长程双臂操作补上密集的子任务标注，FineART-VLA 则学习先判断下一步子任务，再据此行动。它把整段示范里的中间步骤变成可学习的监督，使模型更容易知道当前该做哪一步。

## 问题

任务是复杂、多步骤的双臂操作。瓶颈是监督太粗：大量单臂轨迹通常每回合只有一句总指令，已有带子任务标签的双臂数据又只标注部分录制时长。只有最终目标时，学习者难以直接获得每个阶段应做什么的信息，尤其是在长任务和空间指令中。

### 用一个例子理解

理解用例（非论文实验）：输入“把礼物装进盒子并盖好”；模型结合画面先判断下一步是放入礼物，输出双臂动作；状态变化后再预测整理盒口、盖盖等步骤并行动。若每一步由人指定，则属于另一种信息条件，不能视作自主规划。

## 创新点或方法

本文把“整回合一个目标”改为密集标注子任务，并在中期训练中使用这些标注。FineART-VLA 学习预测自己的下一子任务，再用该预测指导动作。训练时明确可用的是人工标注的中间步骤；推理时存在两种需要分清的条件：模型自己预测步骤，以及人逐步提供子任务指导。摘要没有说明子任务预测与动作如何连接、标签何时切换，也未交代完整训练配方。

### 方法如何工作

1. 给双臂示范密集标注子任务，把一段长轨迹变成带阶段信息的训练样本。
2. 在中期训练中使用这些标注，让模型学习观测、指令与当前步骤之间的关系；具体目标摘要未说明。
3. 推理时预测下一子任务，用它指导动作，把总体目标落实为当前操作。
4. 随着操作推进继续选择步骤；摘要未说明如何检测完成、切换步骤或恢复失败。

### 必要术语

- 子任务标注：给整段任务中的具体步骤加标签；本文把它作为中间监督。
- 中期训练：在后续任务适应前增加的一段训练；本文在此阶段使用 FineART 子任务数据。
- 逐步人工指导：人按阶段告诉模型下一步做什么；本文长程任务的一组结果依赖此条件。
- 零样本任务泛化：未为某个测试任务单独训练也能执行；本文的新硬件结果仍以先做硬件微调为前提。

## 证据

摘要给出数据规模：40,543 回合、1,718 小时、533,913 个子任务，覆盖 151 项任务。使用子任务标注进行中期训练后，空间指令成功率从 32.0% 到 100.0%；在逐步人工指导下，未见长程任务成功率从 16.0% 到 76.0%。后者不能解释为自主完成率。新机器人上少量微调后，所需数据为没有这种中期训练的基线的十分之一，并对新硬件未见任务零样本泛化；摘要未给绝对数据量、任务数或误差。

## 局限

逐步人工指导为测试提供了额外信息，不能与模型自己选步骤混为一谈。这里的零样本是对新硬件上的未见任务而言，模型已经在新机器人上微调过，并非完全没有接触新硬件。100.0% 也只对应所报告的空间指令测试条件，不能外推到所有空间操作。

- **判断**：值得细读标注规则与自主、人工指导两组实验，因为它们决定密集子任务监督究竟改善了步骤选择还是执行能力。

## 研究关联

可借鉴的是标注示范中的“此刻在做哪个步骤”，让策略学习中间决策，而不只拟合动作。若长任务失败主要来自步骤选择，这种监督值得尝试；如果失败主要来自低层接触控制，摘要尚不能证明它同样有效。

### 下一步读哪里

先核查子任务边界、标签内容和预测触发方式；再看空间指令实验的样本规模、长程任务自主版本的表现，以及新机器人上十分之一数据的绝对数量和基线条件。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：41
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/FineART Fine-Grained Annotated Robotic Trajectory Dataset and Vision-Language-Ac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.36416v2 Announce Type: replace Abstract: Robots operating in real-world environments must often execute complex, multi-step bimanual tasks over long horizons rather than single, isolated actions. Current manipulation datasets struggle to support this capability: although single-arm datasets reach hundreds of thousands of trajectories, they typically provide only one high-level instruction per episode, while existing bimanual datasets with subtask labels annotate only part of their recorded hours. We present FineART, a densely annotated bimanual manipulation dataset comprising 40,543 episodes (1,718 hours) and 533,913 subtasks across 151 tasks. We also introduce FineART-VLA, a vision-language-action policy that predicts its own next subtask to guide its actions. Mid-training on FineART's subtask annotations raises FineART-VLA's success at following spatial instructions from 32.0% to 100.0%. With step-by-step human subtask guidance, it also raises success on unseen long-horizon tasks from 16.0% to 76.0%. Furthermore, after minimal fine-tuning on a new robot, the policy requires only one-tenth of the data needed by baselines without this mid-training and generalizes zero-shot to tasks unseen on the new hardware. We open-source the full dataset, model weights, and training code.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.36416
- Authors: Jade Choghari, Pepijn Kooijmans, Mansi Agarwal, Yusuf Umut Ciftci, Aseem Doriwala, Catherine Weaver, Mouli Sivapurapu, Kai Yang, Thomas Wolf, Jackson Lee, Pragna Mannam
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
