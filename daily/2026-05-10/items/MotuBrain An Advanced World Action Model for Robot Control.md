---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2604.27792v2"
published: "2026-04-30T12:34:44Z"
age_days: 
score: 36
created: 2026-05-10
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# MotuBrain: An Advanced World Action Model for Robot Control

> [!summary] 一句话结论（基于摘要）
> Experimentally, MotuBrain achieves 95.8% and 96.1% average success on RoboTwin 2.0 under clean and randomized settings, respectively, attains the strongest reported EWMScore in our WorldArena comparison, and adapts to new humanoid embodiments with only 50--10…

## 关键点

- **问题**：Vision-Language-Action (VLA) models generalize semantically well but often lack fine- grained modeling of world dynamics.
- **创新点 / 方法**：We present MotuBrain, a unified World Action Model that jointly models video and action under a UniDiffuser formulation with a three-stream Mixture-of-Transformers architecture.
- **证据**：Experimentally, MotuBrain achieves 95.8% and 96.1% average success on RoboTwin 2.0 under clean and randomized settings, respectively, attains the strongest reported EWMScore in our WorldArena comparison, and adapts to new humanoid embodiments with only 50--100 trajectories.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-10/MotuBrain An Advanced World Action Model for Robot Control.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models generalize semantically well but often lack fine-
grained modeling of world dynamics. We present MotuBrain, a unified World Action Model
that jointly models video and action under a UniDiffuser formulation with a three-stream
Mixture-of-Transformers architecture. A single model supports policy learning, world
modeling, video generation, inverse dynamics, and joint video-action prediction, while
scaling to heterogeneous multimodal data such as video-only, task-agnostic, and cross-
embodiment robot data. Building on Motus, MotuBrain further introduces unified multiview
modeling, an independent text stream for stronger language-action coupling, a shared
cross-embodiment action representation, and an efficient post-training and deployment
recipe for long-horizon real-world control. Our inference stack combines step reduction,
compilation, FP8 quantization, DiT caching, V2A-style action-only inference, and real-
time chunked closed-loop execution, achieving over 50x speedup over a naive baseline and
up to 11 Hz inference. Experimentally, MotuBrain achieves 95.8% and 96.1% average
success on RoboTwin 2.0 under clean and randomized settings, respectively, attains the
strongest reported EWMScore in our WorldArena comparison, and adapts to new humanoid
embodiments with only 50--100 trajectories. These results show that unified world action
models can scale in generality, predictive accuracy, and real-world deployability.

### 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2604.27792v2
- Authors: MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan, Hongzhe Bi, James Li, Jiabao Liu, Jingrui Pang, Kiro Jing, Louis Liu, Mengchen Cai, Rongxu Cui, Ruowen Zhao, Runqing Wang, Shuhe Huang, Yao Feng, Yinze Rong, Zeyuan Wang, Jun Zhu
- Published: 2026-04-30T12:34:44Z
- Age days: 

</details>
