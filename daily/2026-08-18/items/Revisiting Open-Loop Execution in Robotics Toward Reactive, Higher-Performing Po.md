---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15938v1"
published: "2026-08-16T21:49:07Z"
age_days: 1
score: 32
created: 2026-08-18
concepts: ["世界模型", "机器人学习"]
---

# Revisiting Open-Loop Execution in Robotics: Toward Reactive, Higher-Performing Policies

> [!summary] 一句话结论（基于摘要）
> Across four simulation and two real-world tasks, we show that expert non-Markovianity strongly shapes the relationship between task success and open-loop execution horizon.

## 关键点

- **问题**：However, executing long open-loop prefixes reduces reactivity, limiting policies' ability to correct for errors.
- **创新点 / 方法**：Action chunking --- the practice of predicting a sequence of actions and executing a prefix open-loop --- has emerged as a key enabler of recent progress in imitation learning for robotic manipulation.
- **证据**：Across four simulation and two real-world tasks, we show that expert non-Markovianity strongly shapes the relationship between task success and open-loop execution horizon.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/Revisiting Open-Loop Execution in Robotics Toward Reactive, Higher-Performing Po.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Action chunking --- the practice of predicting a sequence of actions and executing a prefix open-loop --- has emerged as a key enabler of recent progress in imitation learning for robotic manipulation. However, executing long open-loop prefixes reduces reactivity, limiting policies' ability to correct for errors. Further, the mechanisms underlying these performance benefits remain poorly understood: prior works cite mitigating compounding errors, absorbing inference latency, or smoothing motions, but provide limited controlled evidence or guidance for preserving reactivity. In this work, we argue that long open-loop execution primarily helps short-context policies imitate "non-Markovian demonstrations". Across four simulation and two real-world tasks, we show that expert non-Markovianity strongly shapes the relationship between task success and open-loop execution horizon. Further, we investigate the impact of compounding errors --- the prevailing explanation for long open-loop execution in prior work --- and find that while they matter, expert non-Markovianity has a much stronger impact in our experimental setting. Finally, we show that when policies are provided with a sufficiently long context, open-loop execution is no longer beneficial and the most reactive, closed-loop policies perform best. While imitation learning has seen great success using long open-loop execution, our findings motivate long-context, reactive policies as a more principled and performant paradigm.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15938v1
- Authors: Michael Zeng, Abhinav Agarwal, Ajay Bati, Brian Lee, Siddharth Ancha, Russ Tedrake
- Published: 2026-08-16T21:49:07Z
- Age days: 1

</details>
