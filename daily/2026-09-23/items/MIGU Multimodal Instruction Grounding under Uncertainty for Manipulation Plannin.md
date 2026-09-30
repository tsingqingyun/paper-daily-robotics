---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24995v1"
published: "2026-09-21T17:58:22Z"
age_days: 1
score: 31
created: 2026-09-23
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# MIGU: Multimodal Instruction Grounding under Uncertainty for Manipulation Planning

> [!summary] 先说人话（基于摘要）
> MIGU把人说的话和指向手势合起来判断操作目标，同时保留“不确定有多大”。证据足够时继续规划，不足时请求澄清。

## 问题

语言和手势可互补，但都存在歧义和估计误差；机器人需要把这种不确定性传递到目标选择与操作规划，摘要未逐项说明已有基线的机制缺陷。

## 创新点或方法

将视线方向、深度与手方向误差经眼—手指几何传播成三维似然；VLM提供候选物体和区域的语义先验，经贝叶斯启发的融合得到目标信念，再决定执行或澄清。

## 证据

真实基准上优于全部受测基线，消融支持显式多模态不确定性建模的作用；摘要未给出可核查的结果数字。

## 局限

需核查几何误差假设、融合后置信度是否校准，以及澄清触发阈值如何影响交互成本和成功率。

- **判断**：做语言加手势交互值得读方法，性能判断需依赖全文的量化与澄清协议。

## 研究关联

对人机交互与具身Agent，提供了将目标理解置信度连接到澄清行为的路径，可用于移动操作和桌面任务—运动规划。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/MIGU Multimodal Instruction Grounding under Uncertainty for Manipulation Plannin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Understanding natural human instructions is crucial for deploying robots in human-centric environments. We study multimodal instruction grounding, where language and gesture provide complementary but uncertain cues. We present MIGU, a modular framework that combines semantic and geometric evidence into a unified grounding belief and connects it to manipulation planning. MIGU constructs a 3D geometric likelihood by propagating viewing-direction and depth uncertainty through eye-finger geometry while accounting for hand-direction estimation error. A vision-language model (VLM) provides semantic priors over candidate objects and regions, which are combined with the geometric likelihood through Bayes-inspired fusion. The resulting belief supports behavior planning to either proceed directly to downstream planning or request clarification. Grounded targets then define goals for mobile manipulation and tabletop task-and-motion planning. On a real-world benchmark, MIGU outperforms all evaluated baselines, while ablations support the benefit of explicit multimodal uncertainty modeling. Project website: multimodal-instruction.github.io

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24995v1
- Authors: Mingke Lu, Anxing Xiao, David Hsu
- Published: 2026-09-21T17:58:22Z
- Age days: 1

</details>
