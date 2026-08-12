---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01651v1"
published: "2026-07-02T03:23:40Z"
age_days: 1
score: 33
created: 2026-07-03
concepts: ["机器人学习", "具身智能评测与基准"]
---

# One Demonstration Is Enough for Real-World Robotic Reinforcement Learning

> [!summary] 一句话结论（基于摘要）
> AutoSERL consistently outperforms SERL initialized with 20 demonstrations, behavior cloning, and MILES -- a dedicated one-shot imitation learning baseline -- across all tasks while matching HIL-SERL, achieves 100% success rate on insertion tasks, and demonstr…

## 关键点

- **问题**：Learning effective robot control policies on physical hardware is challenging due to costly data collection and the difficulty of reward specification.
- **创新点 / 方法**：To address these limitations, we present AutoSERL, a framework that leverages a single demonstration to fully automate the intervention process in real-world robot RL.
- **证据**：AutoSERL consistently outperforms SERL initialized with 20 demonstrations, behavior cloning, and MILES -- a dedicated one-shot imitation learning baseline -- across all tasks while matching HIL-SERL, achieves 100% success rate on insertion tasks, and demonstrates improved robustness to positional variations, all from…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning effective robot control policies on physical hardware is challenging due to
costly data collection and the difficulty of reward specification. Prior work has
incorporated demonstrations into reinforcement learning (RL), yet existing approaches
either require large numbers of demonstrations or depend on continuous human
intervention during training. To address these limitations, we present AutoSERL, a
framework that leverages a single demonstration to fully automate the intervention
process in real-world robot RL. The framework includes three complementary mechanisms to
accomplish certain tasks: a sliding window intervention mechanism that continuously
guides exploration to prevent local optima and unsafe deviations, a safety recovery
mechanism that detects and corrects failure states via predefined trajectory recovery
points, and an intervention termination criterion that automatically disables guidance
once the policy can independently complete the task, preserving its exploration
advantage. We evaluate AutoSERL on six contact-intensive manipulation tasks across two
robot platforms, spanning insertion, hanging, and hinge-based tasks. AutoSERL
consistently outperforms SERL initialized with 20 demonstrations, behavior cloning, and
MILES -- a dedicated one-shot imitation learning baseline -- across all tasks while
matching HIL-SERL, achieves 100% success rate on insertion tasks, and demonstrates
improved robustness to positional variations, all from a single demonstration. Code and
videos are available on our project website: https://autoserl.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01651v1
- Authors: Yuwan Liu, Hongze Yu, Song Liu, Yuhan Wang, Junge Zhang, Yaodong Yang, Yuanpei Chen, Ceyao Zhang
- Published: 2026-07-02T03:23:40Z
- Age days: 1

</details>
