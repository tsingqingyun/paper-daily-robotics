---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37165v1"
published: "2026-09-29T09:56:17Z"
age_days: 0
score: 32
created: 2026-09-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Disentangling Spurious Correlations in Vision-Language-Action Models via Predicting Domain-Invariant Latent Lookahead

> [!summary] 先说人话（基于摘要）
> DILL 让 VLA 预测与任务相关、尽量不受外观域变化影响的未来表示，减少靠背景或风格线索选动作。它先分离任务信息与域信息，再把这种表示用于策略训练。

## 问题

VLA 在视觉分布变化下容易失效，因为策略可能利用域特有的偶然相关性，而非真正决定任务的结构。表面视觉线索一变，原有动作选择就不再可靠。

## 创新点或方法

利用经过域变换的轨迹训练 Task-Domain Encoder，通过对比目标和高斯解耦正则分离任务与域因素。编码器提供未来潜变量，策略通过前瞻预测与域解耦监督学习，强化任务一致的表示。

## 证据

LIBERO-Plus 平均成功率为 69.1%，比最强基线高 11.4 个百分点。反事实任务—视角评测显示捷径依赖减少；真实操作和潜空间诊断分别支持实际适用性及任务结构保留，但摘要未给出对应数字。

## 局限

需核查域变换是否保持任务与动作语义，以及反事实评测如何区分捷径减少和一般数据增强收益。

- **判断**：值得细读表示解耦目标与反事实评测，基准增益明确，但机制解释需靠全文实验支撑。

## 研究关联

对鲁棒 VLA，提供了从表示监督入手处理视觉捷径的方案。它与世界模型的关联在未来潜表示预测，摘要未证明可用于完整环境模拟或规划。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Disentangling Spurious Correlations in Vision-Language-Action Models via Predict.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models remain brittle under visual distribution shifts, often relying on spurious correlations tied to domain-specific factors rather than task-relevant structure. We propose Domain-Invariant Latent Lookahead (DILL), a representation-learning framework that mitigates shortcut learning in VLA policies. Our key idea is to supervise policies with domain-invariant future latents learned from domain-transformed trajectory data. A Task-Domain Encoder is trained with contrastive objectives and Gaussian disentanglement regularization to separate task-relevant structure from domain-specific visual variation. The learned encoder then provides future latents for VLA policy learning through lookahead prediction and domain disentanglement, encouraging the policy to focus on task-relevant structure rather than incidental visual factors. Counterfactual task-view evaluations show that DILL reduces shortcut reliance, while LIBERO-Plus evaluations demonstrate improved visual robustness, with 69.1% average success, 11.4 percentage points above the strongest baseline. Real-world manipulation experiments further support DILL's applicability beyond controlled simulation. Complementary latent-space diagnostics show that these behavioral gains are accompanied by representations that better preserve task-consistent structure while suppressing domain-specific variation. Our project page is available at https://dill-vla.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37165v1
- Authors: Junghyun Kim, Ngseo Kim, ChungWoo Lee, Seoyeon Lee, Woo-Jeong Baek, Adam Zhou, Chip Huyen, Jun-Ki Lee, Gi-Cheon Kang, Byoung-Tak Zhang
- Published: 2026-09-29T09:56:17Z
- Age days: 0

</details>
