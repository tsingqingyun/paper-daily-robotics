---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13672v1"
published: "2026-06-11T17:59:15Z"
age_days: 1
score: 46
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# $\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> We apply $\texttt{WEAVER}$ in robotic hardware, demonstrating its effectiveness at policy evaluation ($ρ$=0.870 correlation with real- world success rate), policy improvement (real-world success rate improvement of $38\%$ on top of the $π_{0.5}$ robot foundat…

## 关键点

- **问题**：The potential impacts of world models (WMs, i.e., learned simulators) on robotics are far-reaching -- policy evaluation, policy improvement, and test-time planning -- all with limited real-world interaction.
- **创新点 / 方法**：We propose $\texttt{WEAVER}$ (World Estimation Across Views for Embodied Reasoning): a WM architecture that simultaneously achieves all three desiderata, providing state-of-the- art results on robotic manipulation tasks.
- **证据**：We apply $\texttt{WEAVER}$ in robotic hardware, demonstrating its effectiveness at policy evaluation ($ρ$=0.870 correlation with real- world success rate), policy improvement (real-world success rate improvement of $38\%$ on top of the $π_{0.5}$ robot foundation model), and test-time planning (real-world success rate…
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：46
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The potential impacts of world models (WMs, i.e., learned simulators) on robotics are
far-reaching -- policy evaluation, policy improvement, and test-time planning -- all
with limited real-world interaction. To unlock these downstream capabilities, a WM needs
to jointly satisfy three desiderata: $\textit{(i)}$ fidelity (i.e., producing simulated
trajectories that correlate with reality), $\textit{(ii)}$ consistency (i.e., producing
simulated trajectories that are coherent over long horizons), and $\textit{(iii)}$
efficiency (i.e., producing simulated trajectories quickly). We propose
$\texttt{WEAVER}$ (World Estimation Across Views for Embodied Reasoning): a WM
architecture that simultaneously achieves all three desiderata, providing state-of-the-
art results on robotic manipulation tasks. $\texttt{WEAVER}$ is a multi-view WM trained
to predict future latents and reward values via a flow-matching loss. We distill the key
design decisions across model architecture, memory, and prediction objectives required
to unlock the kinds of long-horizon dynamic manipulation tasks that have confounded
prior world modeling approaches. We apply $\texttt{WEAVER}$ in robotic hardware,
demonstrating its effectiveness at policy evaluation ($ρ$=0.870 correlation with real-
world success rate), policy improvement (real-world success rate improvement of $38\%$
on top of the $π_{0.5}$ robot foundation model), and test-time planning (real-world
success rate improvement of $14\%$ with a $5-10\times$ speedup over prior WMs).
$\texttt{WEAVER}$ also demonstrates better performance than prior WMs when evaluated on
out-of-distribution scenarios. Code, models, and videos at:
https://arnavkj1995.github.io/WEAVER/ .

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13672v1
- Authors: Arnav Kumar Jain, Yilin Wu, Jesse Farebrother, Gokul Swamy, Andrea Bajcsy
- Published: 2026-06-11T17:59:15Z
- Age days: 1

</details>
