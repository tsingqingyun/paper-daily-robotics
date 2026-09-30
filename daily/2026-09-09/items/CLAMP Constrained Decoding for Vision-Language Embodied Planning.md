---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08602v1"
published: "2026-09-08T11:38:09Z"
age_days: 0
score: 31
created: 2026-09-09
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CLAMP: Constrained Decoding for Vision-Language Embodied Planning

> [!summary] 先说人话（基于摘要）
> CLAMP在冻结VLM生成计划时，直接屏蔽不符合场景或动作规则的词元，并用状态前瞻偏向可达目标的方案。它把“计划是否可执行”变成解码过程中的约束。

## 这篇到底在做什么

- **卡在哪里**：VLM生成的流畅计划可能引用未观察到的物体、选择缺少可供性的动作，或违反语法和动作约束，导致具身规划不可执行。
- **关键解法**：从初始观察提取允许引用的场景对象，结合外部提供的符号动作模型约束状态转移与目标。硬掩码删除非法候选，HMM世界状态前瞻按前置条件和目标可达性重加权；测试时用冻结VLM采样的无标签续写适配HMM。
- **拿什么证明**：在VLABench、SafeAgentBench和TaPA上，场景约束改善对象落地与安全性；剩余失败主要源于感知错误和约束规格不匹配。摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对具身Agent提供无需更新规划器的可执行性约束方案；与VLA的关联主要在高层规划接口，而非底层动作策略训练。
- **先别急着信**：其保障依赖场景识别和符号动作模型的正确性；初始观察形成的约束如何应对后续场景变化，需要全文核查。
- **判断**：具身规划方向值得精读约束构造与失败分析，不能将受约束解码直接理解为现实执行安全保证。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/CLAMP Constrained Decoding for Vision-Language Embodied Planning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied planning increasingly relies on vision-language models (VLMs) to translate instructions and visual observations into executable action sequences. However, fluent plans are not always executable. A VLM may refer to objects that are not visually observed, select actions whose required affordances are unavailable, or violate syntax and action constraints. We introduce CLAMP, a multimodal constraint-grounding framework that turns scene evidence into decoding-time constraints for a frozen VLM planner. CLAMP uses the initial observation to restrict object references to those supported by the scene, while a provided symbolic action model specifies state transitions and goals. During decoding, hard masks eliminate invalid next-token candidates, while a Hidden Markov Model (HMM)-based world-state lookahead module reweights the probabilities of the remaining feasible candidates based on action preconditions and goal reachability. This allows the planner to retain the VLM's language prior while preventing visually unsupported, unsafe, or infeasible candidates from entering the plan. For unseen tasks and environments, CLAMP adapts the HMM at test time using label-free continuations sampled from the frozen VLM. Experiments on VLABench, SafeAgentBench, and TaPA show that scene-grounded constraints improve object grounding and safety, while most remaining failures stem from perception errors or misaligned constraint specifications.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08602v1
- Authors: Tianyi Ma, Parisa Kordjamshidi
- Published: 2026-09-08T11:38:09Z
- Age days: 0

</details>
