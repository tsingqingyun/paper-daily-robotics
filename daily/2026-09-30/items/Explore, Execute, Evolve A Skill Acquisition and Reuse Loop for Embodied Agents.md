---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37810v1"
published: "2026-09-29T15:25:43Z"
age_days: 0
score: 43
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents

> [!summary] 先说人话（基于摘要）
> RoboSkill 让机器人把做过的任务变成下次能直接调用的技能，减少每次重新探索和推理的开销。关键是 Explore、Execute、Evolve 闭环，并用触觉和可复用代码提高执行效率。

## 问题

VLA 和世界动作模型面对未见任务仍难泛化；通用多模态智能体虽能零样本解题，却常从头理解、探索物理环境，导致执行成本高。任务完成记录尚未充分转化为后续可复用能力。

## 创新点或方法

智能体先收集任务信息，再根据反馈执行，把执行记录更新进技能库，供下一轮探索与行动调用。触觉补充视觉以减少接触不确定性，代码补充文本技能说明以减少重复推理。

## 证据

在 LIBERO-10 的四种智能体上，首回合成功率提高 12.5–25.0 个百分点，平均运行时间减少 7.6–72.4%。真实机器人成功率提高 8.3 个百分点，成功试验的平均运行时间至少减少 14.4%。

## 局限

需核查首回合测试前技能库已有何种经验，以及真实机器人耗时统计为何仅覆盖成功试验；这决定效率与迁移收益应如何解释。

- **判断**：值得细读技能生成、检索和更新规则，摘要同时给出跨智能体的成功率与耗时收益，具有明确复现价值。

## 研究关联

对具身 Agent 研究者，价值在于把经验积累落实为可执行技能库，并同时衡量成功率与运行成本。它也提供了在 VLA 外层组织探索、触觉反馈和技能调用的思路。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Explore, Execute, Evolve A Skill Acquisition and Reuse Loop for Embodied Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action and world-action models have demonstrated impressive capabilities in robotics, yet generalization to unseen tasks remains challenging. More recently, general-purpose multimodal agents have shown great potential for zero-shot robotic task solving. However, they often incur high execution costs by reasoning and exploring the physical world from scratch. To reduce these costs, we introduce RoboSkill, a framework that connects skill acquisition and reuse through an Explore, Execute, Evolve loop. Within this loop, the agent explores to gather task-relevant information, executes tasks while adapting to feedback, and evolves its skill library based on execution records. It then reuses these skills to guide exploration and execution in the next cycle, closing the loop. To improve loop efficiency, we complement vision with tactile feedback to reduce uncertainty during physical interaction. We further augment textual guidance with reusable code to reduce reasoning overhead during skill reuse. On LIBERO-10, RoboSkill improves first-episode success rates by 12.5--25.0 percentage points and reduces average runtime by 7.6--72.4% across four agents. On real robots, it improves success rates by 8.3 percentage points and reduces average runtime for successful trials by at least 14.4%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37810v1
- Authors: Sicheng Xie, Yitong Chen, Haidong Cao, Shunlin Lu, Zuxuan Wu, Yu-Gang Jiang
- Published: 2026-09-29T15:25:43Z
- Age days: 0

</details>
