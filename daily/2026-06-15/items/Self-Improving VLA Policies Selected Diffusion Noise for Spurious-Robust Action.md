---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14084v1"
published: "2026-06-12T03:59:47Z"
age_days: 2
score: 41
created: 2026-06-15
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Self-Improving VLA Policies: Selected Diffusion Noise for Spurious-Robust Action Smoothing

> [!summary] 一句话结论（基于摘要）
> SDN consistently improves success rates by +8% in simulation and +10% in real-world settings, while producing smoother and more stable actions.

## 关键点

- **问题**：Diffusion-based Vision-Language-Action (VLA) policies enable strong generalization in robotic manipulation, but remain sensitive to spurious visual correlations and noisy action generation, leading to brittle behavior under perturbations.
- **创新点 / 方法**：We introduce Selected Diffusion Noise (SDN), a simple, training-free test-time method that improves both robustness and success rate by leveraging the diffusion noise space as a controllable degree of freedom.
- **证据**：SDN consistently improves success rates by +8% in simulation and +10% in real-world settings, while producing smoother and more stable actions.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Diffusion-based Vision-Language-Action (VLA) policies enable strong generalization in
robotic manipulation, but remain sensitive to spurious visual correlations and noisy
action generation, leading to brittle behavior under perturbations. We introduce
Selected Diffusion Noise (SDN), a simple, training-free test-time method that improves
both robustness and success rate by leveraging the diffusion noise space as a
controllable degree of freedom. SDN dynamically samples noise vectors that are maximally
separated from a reference set to mitigate reliance on spurious cues, while selecting
candidates that yield more coherent action trajectories. This dual objective encourages
stable behavior even under object-masked observations and reduces action jitter without
modifying model parameters. We evaluate SDN on two simulation benchmarks (Google Robot,
Widow-X) and two real-world robotic datasets across multiple VLA policies, including
pi_0, Groot-N1.5, and Groot-N1.6. SDN consistently improves success rates by +8% in
simulation and +10% in real-world settings, while producing smoother and more stable
actions. Our results highlight that diffusion noise selection can serve as an effective
and general mechanism for enhancing VLA policies at test time.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14084v1
- Authors: Duc Minh Nguyen, Bao-Ngoc Dao, Tung M. Luu, Binh Gia Nguyen, Vinh Tong, Anji Liu, Vu N. Duong, Dung D. Le, Daniel Sonntag, Trung Le, Ngan Le, Jan Peter, An Thai Le, Minh Nhat Vu, Mathias Niepert, Khoa D. Doan, Duy M. H. Nguyen, Vien Anh Ngo
- Published: 2026-06-12T03:59:47Z
- Age days: 2

</details>
