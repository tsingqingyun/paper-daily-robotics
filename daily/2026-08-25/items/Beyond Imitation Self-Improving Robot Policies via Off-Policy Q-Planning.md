---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.21204"
published: "Mon, 24 Aug 2026 00:00:00 -0400"
age_days: 0
score: 27
created: 2026-08-25
concepts: ["智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning

> [!summary] 一句话结论（基于摘要）
> On two contact-rich bimanual real-robot tasks, the same loop (BC frozen, no human intervention) improves purely from its own deployment rollouts: stack-cups 40% to 90% and insert-wallet 25% to 80% in five iterations, whereas SFT on successful rollouts alone s…

## 问题

arXiv:2608.21204v1 Announce Type: new Abstract: Behaviour Cloning (BC) has driven remarkable progress in robot manipulation, yet it is fundamentally limited by its inability to self-improve: a policy that fails cannot learn from that failure without additional human demonstrations.

## 创新点或方法

We propose Q-Planning, which equips a large visuomotor BC policy with a small off-policy Q-function.

## 证据

On two contact-rich bimanual real-robot tasks, the same loop (BC frozen, no human intervention) improves purely from its own deployment rollouts: stack-cups 40% to 90% and insert-wallet 25% to 80% in five iterations, whereas SFT on successful rollouts alone stalls at 55% and 30%.

## 局限

arXiv:2608.21204v1 Announce Type: new Abstract: Behaviour Cloning (BC) has driven remarkable progress in robot manipulation, yet it is fundamentally limited by its inability to self-improve: a policy that fails cannot learn from that failure without additional human demonstrations.


## 研究关联

- **概念**：智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-25/Beyond Imitation Self-Improving Robot Policies via Off-Policy Q-Planning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.21204v1 Announce Type: new Abstract: Behaviour Cloning (BC) has driven remarkable progress in robot manipulation, yet it is fundamentally limited by its inability to self-improve: a policy that fails cannot learn from that failure without additional human demonstrations. Reinforcement Learning fine-tuning offers a path to self-improvement but has proven difficult to scale to the multi-billion-parameter models underpinning modern robot policies. We propose Q-Planning, which equips a large visuomotor BC policy with a small off-policy Q-function. Because a Q-function estimates value rather than imitates actions, it can be trained on the same successful demonstrations as the BC policy and later absorb both successful and failed deployment rollouts, an asymmetry BC does not have. We exploit this asymmetry to enable value-guided action selection at inference (a single-step Q-weighted average over BC draws) and online self-improvement that fine-tunes only the Q-function, leaving the BC weights untouched. On LIBERO and bimanual RoboTwin, ten iterations of self-improvement lift every benchmark score we tested (LIBERO-10 93% to 99%, RoboTwin 83.8% to 91.4%) and shorten successful episodes on the near-ceiling suites (LIBERO-Object, LIBERO-Goal). On two contact-rich bimanual real-robot tasks, the same loop (BC frozen, no human intervention) improves purely from its own deployment rollouts: stack-cups 40% to 90% and insert-wallet 25% to 80% in five iterations, whereas SFT on successful rollouts alone stalls at 55% and 30%. Under an identical online budget Q-Planning is the only method, among Best-of-N, filtered SFT, IBRL, DSRL, and DAWR, that improves stably from failures without training an auxiliary actor.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.21204
- Authors: Varun Giridhar, Anant Khandelwal, Jeremy A. Collins, Ignat Georgiev, Animesh Garg
- Published: Mon, 24 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
