---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.08448"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 40
created: 2026-09-04
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents

> [!summary] 先说人话（基于摘要）
> Harness VLA不微调原VLA，而把冻结VLA当作可重试的接触操作原语，再由带记忆的智能体组合少量解析原语并处理重规划。它用执行轨迹、成功规则和失败模型学习各原语的可用边界。

## 这篇到底在做什么

- **卡在哪里**：端到端VLA擅长局部视觉运动控制，却容易在语义重定向、目标重绑定、布局变化和接触不稳定时失效；纯LLM式解析原语又难处理不规则抓取、受限放置和关节物体交互。
- **关键解法**：规划器负责语义重新落地、非接触运动和VLA重新就位，冻结VLA只处理局部接触密集阶段；固定的解析原语库承担定位、预备、搬运、导航和释放。记忆由任务执行记录、全局成功规则及失败模型组成，用于决定重试和组合，而不是不断扩充技能库。
- **拿什么证明**：相对最强相关基线，LIBERO-Pro和RoboCasa365分别提升38.6和25.4个百分点；在RoboTwin C2R达到58.4%。

## 值不值得读

- **和你的研究有什么关系**：它为VLA部署提供一种成本较低的系统路线：保留预训练接触技能，同时用Agent层吸收长时程推理和分布偏移。对研究技能编排、失败恢复和无需微调扩展能力的人尤其有价值。
- **先别急着信**：摘要只给出总体增益，未说明记忆、失败模型、重试机制各自贡献，也未交代额外规划开销；这些是判断可靠性来源时最需核查的内容。
- **判断**：值得精读系统分工、记忆形成和失败恢复实验；若目标是纯端到端策略学习，则主要读其强基线与失效案例。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/Harness VLA Steering Frozen VLAs into Reliable Manipulation Primitives via Memor.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2607.08448v4 Announce Type: replace Abstract: Language-conditioned manipulation requires both precise contact-rich control and robust reasoning over language, scenes, and long horizons. End-to-end Vision-Language-Action (VLA) models provide strong local visuomotor skills, but they are trained on in-distribution task trajectories and often fail under deployment perturbations such as semantic retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts. LLM coding agents provide complementary semantic and compositional reasoning, but purely analytic primitives struggle with irregular grasping, constrained placement, and articulated-object interaction. We present Harness VLA, a memory-augmented agentic framework that exposes a frozen VLA as a retryable contact-rich primitive and composes it with a small fixed library of analytic primitives for grounding, staging, transport, navigation, and release. Rather than expanding the skill library, the harness learns the operating range of these fixed primitives from task-specific execution traces, global success rules, and failure models. By lifting semantic re-grounding, non-contact execution, and VLA re-staging to the planner while reserving the frozen VLA for local contact-rich phases, Harness VLA extends pretrained VLAs beyond their original trajectory distribution without finetuning. Across perturbed tabletop, household kitchen, and clean-to-randomized bimanual manipulation, Harness VLA improves over the strongest relevant baselines by 38.6 and 25.4 percentage points on LIBERO-Pro and RoboCasa365, respectively, and reaches 58.4% on RoboTwin C2R. Code is available at https://github.com/RLinf/RPent.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.08448
- Authors: Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Chunyang Zhu, Jiaxing Qiu, Yuchen Yan, Jiyuan Liu, Wenhao Tang, Zhengru Fang, Yi Nie, Changxu Wei, Yu Wang, Wenbo Ding, Chao Yu
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
