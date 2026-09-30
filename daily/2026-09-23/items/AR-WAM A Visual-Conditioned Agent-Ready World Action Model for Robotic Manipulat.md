---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23578v1"
published: "2026-09-20T11:55:26Z"
age_days: 2
score: 36
created: 2026-09-23
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# AR-WAM: A Visual-Conditioned Agent-Ready World Action Model for Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> AR-WAM让上层Agent用“目标框＋技能编号”指挥机器人，减少语言指令中的指代和空间歧义。底层模型同时预测场景变化和动作，把长期记忆与纠错交给Agent。

## 问题

自然语言接口会混合任务意图与执行细节，对已具备语言理解能力的Agent而言存在冗余，目标指代和空间描述也可能不够精确。

## 创新点或方法

0.5B模型使用冻结视觉编码器、不设语言编码器，以目标框和可学习操作token为条件，在紧凑潜在状态中预测场景演化并解码动作；兼容层提供detect、execute、query接口。

## 证据

在RoboTwin 2.0、RMBench及Astribot S1上评测；标准操作平均成功率87.2%，记忆依赖和真实长程任务提升分别报告为5.9%和36.7%，推理延迟14.1毫秒。

## 局限

长程收益来自Agent与策略组成的系统，需核查双方贡献；提升是否为百分点、14.1毫秒是否包含Agent开销，摘要未说明。

- **判断**：值得精读系统接口和长程对照实验，判断其可复用性比单看模型规模更重要。

## 研究关联

对Agent与机器人策略集成有直接价值：把目标选择、原子技能执行和进度查询变成明确接口，便于分开研究高层记忆与底层控制。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/AR-WAM A Visual-Conditioned Agent-Ready World Action Model for Robotic Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As AI agents become increasingly capable, agent-driven robotic control is emerging as a compelling paradigm. However, prevailing vision-language-action (VLA) models and world action models (WAMs) still rely on natural-language instructions to specify manipulation tasks, an ill-suited interface for agent-driven control: referentially ambiguous, spatially imprecise, redundant with the agent's inherent language understanding, and entangling intent with execution. We present AR-WAM, a visual-conditioned, agent-ready world action model that replaces language with two complementary conditions: a visual grounding prompt (a bounding box of the target) denoting the interaction object and location, and a learnable operation token dictating the atomic skill to execute. Our compact 0.5B-parameter model, with a frozen pretrained visual encoder and no language encoder, predicts scene evolution within compact latent states while decoding actions, exposing the policy's intent through explicit, supervisable reasoning signals. A model-agnostic compatibility layer provides three primitives (detect, execute, and query) so that local VLMs or online agent APIs can drive the policy directly, with long-horizon memory and closed-loop error recovery delegated to the agent side. On RoboTwin 2.0, RMBench, and a real Astribot S1 dual-arm platform, AR-WAM matches the strongest baselines on standard manipulation (87.2% average success) and outperforms them on memory-dependent and real-robot long-horizon tasks, improving success rates by 5.9% and 36.7%, respectively, while maintaining the lowest inference latency (14.1 ms).

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23578v1
- Authors: Yicheng Jiang, Zesen Gan, Xiaobo Wang, Tianlun He, Chenxu Zhao, Minghui Wu, Xinyue Wang, Jiaxu Wang, Junhao He, Jianan Wang, Qiming Shao
- Published: 2026-09-20T11:55:26Z
- Age days: 2

</details>
