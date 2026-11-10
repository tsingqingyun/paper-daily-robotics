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
url: "https://arxiv.org/abs/2611.08946v1"
published: "2026-11-06T03:51:20Z"
age_days: 3
score: 28
created: 2026-11-10
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents

> [!summary] 这篇论文到底做了什么（基于摘要）
> Flex-RSI 测试智能体能否利用任务反馈，修改自己做事的流程，而不只是修答案。它让执行者改进解法、改进者修改包括自身在内的工作流程，并在固定预算下用隐藏测试集检查最终效果。

## 问题

智能体的表现不仅取决于模型，也取决于提示词、工具、记忆和控制循环。多数现有基准固定这些安排，只评最终答案，或关注大规模模型训练，因此难以回答：智能体能否从反馈中学会更有效地组织工作？

### 用一个例子理解

理解用例（非论文实验）：输入搭建稳定积木结构的任务；执行者生成方案，验证反馈暴露失败，改进者据此加入检查步骤；后续轮次继续改方案，最终在隐藏任务上输出并评分。反馈包含多少诊断信息需看具体设置。

## 创新点或方法

本文把固定工作流程改成可修改的对象。每轮先由执行者改进任务解法，只有独立验证数据上的得分更高才保留；随后改进者调整工作流程，执行者与改进者自身都可被修改。这里描述的是运行中的流程迭代，并未说明更新模型权重。最终隐藏测试用于检验迭代所得是否能超出验证数据本身。

### 方法如何工作

1. 从相同的通用工作流程出发，减少不同起点对结果的干扰。
2. 执行者改进解法并接受验证，只有得分提高才保留，避免直接用新版本替换更好解法。
3. 改进者根据反馈修改工作流程，包括自身，让下一轮的工作方式也发生变化。
4. 在固定预算内重复迭代，最后用隐藏测试数据评分，检查最终效果。

### 必要术语

- Harness：提示词、工具、记忆和控制循环组成的工作安排；本文允许智能体修改它。
- 递归自我改进：改进流程也能修改负责改进的部分；本文以多轮方式测试。
- 配对运行：在相互对应的实验条件下比较结果；用于辨认流程编辑的贡献。

## 证据

摘要报告对闭源和开放权重模型的评测，任务覆盖感知、推理、机器人动作、三维重建、视觉创作与基础设施。收益在智能体自行构建解法时最明显；仅提供成功或失败反馈会限制开放权重模型；物理稳定性或精确正确性检查严格的任务上，两类模型差距最大。配对运行还支持修改流程本身贡献了收益。摘要没有模型名单、预算、分数和配对控制细节，无法量化贡献大小。

## 局限

我会核查反复使用验证反馈是否导致针对验证集调节，以及配对运行是否控制了总调用成本。摘要中的机器人动作任务不能据此认定为真机实验；“递归自我改进”也不意味着无限持续进步。

- **判断**：值得先读评测协议与配对实验：这篇最有用的是如何识别流程修改的贡献，而非把总分上涨直接归因于自我改进。

## 研究关联

它提醒我们，把“多试几次”和“学会怎样试”分开评估。若要判断自动改提示词、工具或记忆是否有用，就应控制预算和起点，并用最终未参与迭代的数据检查结果。

### 下一步读哪里

下一步检查预算计算方式、可修改范围、验证与测试划分，以及配对运行具体关闭了什么；再看细粒度反馈与二元反馈如何比较。输入没有正文节选。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-10/Flex-RSI Benchmarking Recursive Self-Improvement of Frontier Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Frontier language models are increasingly deployed as agents, and how well an agent performs depends not only on its model but also on its harness: the prompts, tools, memory, and control loop through which the model acts. When an agent is applied to a new problem, a natural question is whether it can use the feedback of the task to improve the way it works, and not merely its answer. Most existing benchmarks keep the agent's harness fixed and score the solution it produces, or target large-scale model training. We introduce Flex-RSI, a benchmark for the recursive self-improvement of agents on vision and robotics tasks under a fixed budget. In each round, an executor improves the task solution, which is kept only if it scores higher on held-out validation data, and an improver then revises the harness, including the executor and itself. Every run starts from the same general-purpose harness, and the final solution is scored on hidden test data. Evaluating closed-source and open-weight models on tasks spanning perception, reasoning, robot action, 3D reconstruction, visual creation, and infrastructure, we find that self-improvement helps most when the agent builds its own solution, that feedback recording only success or failure holds back open-weight models, and that open-weight models fall furthest behind where outputs must pass strict checks of physical stability or exact correctness. Paired runs further show that editing the harness itself contributes to the gains.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08946v1
- Authors: Jingdong Zhang, Jionghao Wang, Zhengming Yu, Yancheng Cai, Wei Chow, Chris Choy, Zhiyang Dou, Hang Hua, Jiachen Li, Zhixuan Liu, Chen Wang, Songlin Wei, Siyuan Yang, Yu Yuan, Xiaohang Zhan, Yucheng Zhang, Shuhong Zheng, Xin Li, Lingjie Liu, Wojciech Matusik, Zhengzhong Tu, Wenping Wang
- Published: 2026-11-06T03:51:20Z
- Age days: 3

</details>
