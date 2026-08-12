---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.12702v1"
published: "2026-07-14T12:27:58Z"
age_days: 2
score: 32
created: 2026-07-17
concepts: ["机器人学习"]
---

# Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning

> [!summary] 一句话结论（基于摘要）
> The learned policy achieves 100% success in nominal target-driven dribbling and 96% success with a single static obstacle, while reaching 46% success against an actively moving ball-attacker opponent.

## 关键点

- **问题**：Recent advances in humanoid robotics have highlighted the importance of deployable loco- manipulation skills.
- **创新点 / 方法**：We propose an integrated approach in which a temporal depth encoder is embedded into a reinforcement learning policy through a task- specific projection layer.
- **证据**：The learned policy achieves 100% success in nominal target-driven dribbling and 96% success with a single static obstacle, while reaching 46% success against an actively moving ball-attacker opponent.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-17/Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learnin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent advances in humanoid robotics have highlighted the importance of deployable loco-
manipulation skills. Dribbling a soccer ball while evading active opponents requires
simultaneous balance, precise ball control, and awareness of a dynamic adversary under
onboard sensing and real-time constraints. Existing approaches typically separate
perception and motion, which can be effective in controlled settings but may fail under
occlusions, fast ball movements, and complex opponent interactions, since perception is
not directly optimized for control. We propose an integrated approach in which a
temporal depth encoder is embedded into a reinforcement learning policy through a task-
specific projection layer. We apply this framework to a simulated Booster T1 humanoid
robot and show that it is possible to learn vision-based, opponent-aware dribbling
directly from depth observations, without explicit state estimation or privileged scene
information. The learned policy achieves 100% success in nominal target-driven dribbling
and 96% success with a single static obstacle, while reaching 46% success against an
actively moving ball-attacker opponent. These results demonstrate that the proposed
framework supports robust vision-based dribbling in nominal and moderately dynamic
settings, and provides a strong foundation for handling more challenging moving-
adversary scenarios.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.12702v1
- Authors: Flavio Maiorana, Valerio Spagnoli, Eugenio Bugli, Flavio Volpi, Daniele Affinita, Vincenzo Suriani, Daniele Nardi, Luca Iocchi
- Published: 2026-07-14T12:27:58Z
- Age days: 2

</details>
