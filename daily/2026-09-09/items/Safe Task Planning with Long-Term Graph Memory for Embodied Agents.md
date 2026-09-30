---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08444v1"
published: "2026-09-08T08:49:50Z"
age_days: 0
score: 31
created: 2026-09-09
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Safe Task Planning with Long-Term Graph Memory for Embodied Agents

> [!summary] 先说人话（基于摘要）
> SafeMem把机器人过去看到的物体和关系存成长期图记忆，再让风险预测器据此检查候选动作。这样，暂时移出视野的危险也能参与重新规划。

## 这篇到底在做什么

- **卡在哪里**：部分可观测环境中，危险可能不在当前视野内，而现有LLM/VLM规划器缺少持续的物理风险认知，容易生成不安全的高层动作。
- **关键解法**：从第一视角观察增量构建动态环境的语义图，记录物体及关系；LLM风险预测器结合图记忆评估候选动作，并触发带风险解释、可调保守程度的重规划循环。
- **拿什么证明**：摘要报告在IS-Bench和真实机器人平台上，相较先进VLM规划器显著提高安全成功率；摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：为具身Agent记忆提供明确用途：支持视野之外的风险判断，而不仅是保存任务历史。适合研究记忆如何实际改变规划决策。
- **先别急着信**：动态环境中图记忆可能过时，需要核查更新和失效机制，以及保守程度变化对任务完成率的影响。
- **判断**：安全规划与长期记忆方向值得读方法和错误案例，量化收益需等待完整实验细节。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/Safe Task Planning with Long-Term Graph Memory for Embodied Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large language models (LLMs) and vision-language models (VLMs) have significantly advanced zero-shot task planning for embodied agents. However, most LLM- and VLM-driven methods struggle to generate safe high-level actions due to a lack of physical risk awareness, particularly under partial observability, where hazards lie outside the immediate field of view. To address this challenge, we propose a novel safe task-planning framework, SafeMem, which constructs and maintains a long-term semantic graph memory of the open and dynamic environment. Based on egocentric observations, the proposed framework incrementally accumulates knowledge about surrounding objects and their relationships with a graph. Then, an LLM-based risk predictor evaluates candidate actions using the graph memory, triggering a conservatism-modulated replanning loop with explanations for detected hazards. Extensive experiments on the IS-Bench benchmark and a real-world robot platform demonstrate that the SafeMem framework substantially improves safe success rates compared to state-of-the-art VLM-driven task planners. Video results are available on our webpage: https://sites.google.com/view/safemem.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08444v1
- Authors: Siyuan Li, Taiyan Lang, Aoqi Yan, Jia Yu, Feifan Liu, Yihan Du, Yu Zheng, Xun Wang, Peng Liu
- Published: 2026-09-08T08:49:50Z
- Age days: 0

</details>
