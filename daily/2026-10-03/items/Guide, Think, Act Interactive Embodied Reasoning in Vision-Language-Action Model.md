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
url: "https://arxiv.org/abs/2605.13632"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-10-03
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> GTA-VLA 给机器人一个可接收人类视觉纠正的接口：用户可以点位置、画框或轨迹，模型据此重新推理，再生成动作。它让“你应该操作这里”成为策略可用的明确输入。

## 问题

直接从观察生成动作的 VLA 在分布外视觉变化下容易失误，失败后也难以纠正。已有具身思维链虽然展示中间推理，却缺少接收人的空间指引的机制；当目标相似或位置含糊时，展示推理本身不能解决歧义。

### 用一个例子理解

理解用例（非论文实验）：桌上有两个相似杯子，机器人选错目标；用户框出右侧杯子。模型把框与取杯指令一起用于推理，再由动作头输出朝右杯接近和抓取的动作。

## 创新点或方法

旧做法由模型自行解释画面并行动，本文允许用户额外提供操作点、框或轨迹。推理模块将这些空间线索与内部任务计划合成空间—视觉思维链，再连接轻量反应式动作头执行。希望通过明确目标位置减少误解，同时控制动作计算成本。推理时指导是可选输入；摘要未说明训练样本如何构造、指导如何编码，以及两个模块如何训练。

### 方法如何工作

1. 接收画面、任务与可选视觉指导，使目标位置或操作路径变成显式输入。
2. 生成结合指导与任务规划的空间—视觉思维链，把人的指向转为行动依据。
3. 将推理结果连接轻量动作头，生成可执行动作，降低执行阶段的计算负担。
4. 发生歧义或错误时加入一次视觉交互，再据指导行动；摘要未说明具体恢复触发和停止规则。

### 必要术语

- 空间先验：提前给出的点、区域或路径提示；本文用它约束目标与操作位置。
- 具身思维链：行动前的中间推理；本文让它同时使用空间指导和任务计划。
- 分布外变化：测试条件偏离训练条件；本文据此考察视觉变化下的交互纠错。

## 证据

摘要报告，在分布内的 SimplerEnv WidowX 基准上成功率为 81.2%，并称达到最高水平；这是仿真基准结果。在分布外视觉变化和空间歧义条件下，单次视觉交互明显改善成功率。未提供后者的具体数值、基线名称、交互成本或真机结果，不能把 81.2% 用作分布外恢复成功率。

## 局限

摘要未列出明确局限。我会核查是谁提供指导、是否知道正确答案，以及错误或不精确的标注会怎样影响执行。有人介入后的成功率衡量的是交互系统能力，不能直接等同于完全自主能力。

- **判断**：值得读交互协议和分布外实验，判断一次视觉纠正解决了哪类错误、需要多少人力。

## 研究关联

值得借鉴的是把纠正做成模型能直接使用的空间输入。当失败源于“到底指哪个物体或位置”时，明确指向目标可能比继续补充自然语言描述更直接。

### 下一步读哪里

先核查点、框、轨迹分别如何进入推理，以及思维链怎样连接动作头。再检查无指导与有指导是否使用相同模型、交互何时触发，以及分布外收益是否来自更明确的目标信息。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/Guide, Think, Act Interactive Embodied Reasoning in Vision-Language-Action Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2605.13632v3 Announce Type: replace Abstract: In this paper, we propose GTA-VLA(Guide, Think, Act), an interactive Vision-Language-Action (VLA) framework that enables spatially steerable embodied reasoning by allowing users to guide robot policies with explicit visual cues. Existing VLA models learn a direct "Sense-to-Act" mapping from multimodal observations to robot actions. While effective within the training distribution, such tightly coupled policies are brittle under out-of-domain (OOD) shifts and difficult to correct when failures occur. Although recent embodied Chain-of-Thought (CoT) approaches expose intermediate reasoning, they still lack a mechanism for incorporating human spatial guidance, limiting their ability to resolve visual ambiguities or recover from mistakes. To address this gap, our framework allows users to optionally guide the policy with spatial priors, such as affordance points, boxes, and traces, which the subsequent reasoning process can directly condition on. Based on these inputs, the model generates a unified spatial-visual Chain-of-Thought that integrates external guidance with internal task planning, aligning human visual intent with autonomous decision-making. For practical deployment, we further couple the reasoning module with a lightweight reactive action head for efficient action execution. Extensive experiments demonstrate the effectiveness of our approach. On the in-domain SimplerEnv WidowX benchmark, our framework achieves a state-of-the-art 81.2% success rate. Under OOD visual shifts and spatial ambiguities, a single visual interaction substantially improves task success over existing methods, highlighting the value of interactive reasoning for failure recovery in embodied control. More details of the project can be found here: https://github.com/FutianLabs/GTA-VLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13632
- Authors: Yiran Ling, Qing Lian, Jinghang Li, Qing Jiang, Tianming Zhang, Xiaoke Jiang, Chuanxiu Liu, Jie Liu, Lei Zhang
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
