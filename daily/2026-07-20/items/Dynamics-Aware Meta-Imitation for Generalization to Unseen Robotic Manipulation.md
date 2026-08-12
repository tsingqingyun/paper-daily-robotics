---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15880v1"
published: "2026-07-17T11:50:03Z"
age_days: 2
score: 34
created: 2026-07-20
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习"]
---

# Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation

> [!summary] 一句话结论（基于摘要）
> Extensive experiments in both simulation and real-world settings demonstrate that our approach outperforms state-of-the-art baselines regarding direct inference on seen tasks and adaptation to unseen tasks via few-shot fine-tuning.

## 关键点

- **问题**：The existing methods predominantly focus on imitation from in-domain tasks and consequently struggle with generalization to unseen tasks.
- **创新点 / 方法**：To bridge this generalization gap, we propose the \textbf{D}ynamics-\textbf{A}ware \textbf{M}eta-\textbf{I}mitation (DAMI) framework.
- **证据**：Extensive experiments in both simulation and real-world settings demonstrate that our approach outperforms state-of-the-art baselines regarding direct inference on seen tasks and adaptation to unseen tasks via few-shot fine-tuning.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-20/Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Imitation Learning aims to learn skills from extensive observations and demonstrations
for robots, so it suffers from data scarcity and environment generalization. The
existing methods predominantly focus on imitation from in-domain tasks and consequently
struggle with generalization to unseen tasks. To bridge this generalization gap, we
propose the \textbf{D}ynamics-\textbf{A}ware \textbf{M}eta-\textbf{I}mitation (DAMI)
framework. By integrating meta-learning to construct a shared skill space, DAMI equips
agents for rapid adaptation to novel tasks. We introduce the Visual-Motor Trajectory
(VMT) module to capture complex spatio-temporal dynamics within the task latent space.
Furthermore, we propose the Unpaired Unified Task (U2T) block to fuse unstructured
multimodal observations. To coordinate these representations, we integrate a Task-
Conditioned Feature Modulation (TCFM) mechanism customized for modulating low-level 3D
features. By capturing intrinsic dynamics from a random complete reference
demonstration, our framework learns the underlying task logic rather than memorizing
static cues, ensuring effective generalization. Extensive experiments in both simulation
and real-world settings demonstrate that our approach outperforms state-of-the-art
baselines regarding direct inference on seen tasks and adaptation to unseen tasks via
few-shot fine-tuning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15880v1
- Authors: Zhenduo Shang, Xiyao Liu, Bohan Li, Xudong Wang, Teng Ren, Lianqing Liu, Zhi Han
- Published: 2026-07-17T11:50:03Z
- Age days: 2

</details>
