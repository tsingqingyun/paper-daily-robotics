---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10137v1"
published: "2026-09-09T13:17:34Z"
age_days: 1
score: 24
created: 2026-09-11
concepts: ["世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Assembling Two Parts in One Hand

> [!summary] 先说人话（基于摘要）
> We present a reinforcement learning formulation to solve this problem in a unified framework, which is driven by a goal relative pose between the two parts.

## 这篇到底在做什么

- **卡在哪里**：A hallmark of human dexterity is the cooperative use of fingers, where different fingers take on distinct yet coordinated roles to accomplish fine manipu- lation, such as capping a pen with the hand that holds it.
- **关键解法**：We present a reinforcement learning formulation to solve this problem in a unified framework, which is driven by a goal relative pose between the two parts.
- **拿什么证明**：摘要未报告明确实验结论；需阅读全文核查。

## 值不值得读

- **和你的研究有什么关系**：需结合研究方向判断；规则式回退未做语义评审。
- **先别急着信**：摘要未明确说明；需阅读全文核查。
- **判断**：仅完成摘要摘取，建议等待语义讲解或阅读全文。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-11/Assembling Two Parts in One Hand.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

A hallmark of human dexterity is the cooperative use of fingers, where different fingers take on distinct yet coordinated roles to accomplish fine manipu- lation, such as capping a pen with the hand that holds it. We study this finger-level coordination through in-hand assembly: mating two rigid objects within a single dexterous hand, with no second arm and no fixture. We present a reinforcement learning formulation to solve this problem in a unified framework, which is driven by a goal relative pose between the two parts. Finger coordination is shaped by a function-based auxiliary reward and regularized toward a single human reference pose, while domain randomization and a fusion of historical proprioception and object observation confer robustness to occlusion-induced estimation noise. The same recipe solves three different assembly tasks (Bottle, Syringe, and Marker). Trained purely in simulation, the policies transfer zero-shot to hardware with a single camera, demonstrating robustness to state-estimation errors caused by oc- clusion. Our experiments also reveal that in-hand assembly places demands on hand morphology and can serve as a benchmark for modern robotic hand systems. Videos and code are available at https://ltbgbird.github.io/in-hand-assembly-page/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10137v1
- Authors: Liuao Pei, Tianyue Wu, Hui Zhang, Ping Luo, Jie Song
- Published: 2026-09-09T13:17:34Z
- Age days: 1

</details>
