---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29242v1"
published: "2026-08-29T12:55:15Z"
age_days: 2
score: 37
created: 2026-09-01
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization

> [!summary] 先说人话（基于摘要）
> AnyWorld 把一次人类第一视角交互分解为动作、相机和 embodiment，再独立重组为多种机器人原生视频—动作 rollout，无需成对人机示范。

## 问题

接触丰富的机器人经验昂贵且难以覆盖不同身体、视角和场景；人类第一视角视频虽多，但每段只呈现单一身体、相机轨迹和环境，不能直接填补机器人策略的数据缺口。

## 创新点或方法

输入单段人类交互及目标动作、相机和 embodiment 条件，输出保持交互动力学和物体作用关系的机器人域 rollout。模型先做人类交互预训练，再用混合 embodiment 微调；相比直接域迁移或只改动作，它允许身体、视角和场景独立重组，并同时校准动作与视觉。

## 证据

摘要称可控地重组 embodiment、视角和场景，生成数据能提升 RoboCasa GR1 桌面基准及真实 IRON 人形机器人的操作表现。受控干预纠正了虚假完成先验并学会语言条件空间目标选择，而仅动作反事实干预不能可靠学会后者；未给具体提升数字。


## 局限

需重点核查重组后视频—动作对是否保持真实接触动力学，以及策略提升在多大程度上来自目标化干预而非额外数据量。

- **判断**：值得精读建模分解和受控干预实验；“动作校准与视觉重组缺一不可”比单纯扩增视频更有研究价值。

## 研究关联

对世界模型和机器人学习，这是把海量非配对人类视频转成针对性机器人训练数据的具体机制，尤其适合诊断并补策略缺口。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/AnyWorld Factorized Egocentric World Models for Cross-Embodiment Generalization.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Collecting contact-rich robot experiences at scale remains a major bottleneck for generalizable manipulation. Beyond data quantity, robot learning also requires diverse experiences across embodiments, viewpoints, and scenes. Human egocentric videos provide abundant physical interactions, but each video captures only a narrow slice of experience under a single body, camera trajectory, and environment. We propose AnyWorld, a cross-embodiment world modeling framework that expands a single human interaction into diverse robot-native rollouts without paired human-robot demonstrations. Our model factorizes an interaction into action, camera, and embodiment: action controls capture the motion structure, camera controls specify viewpoint evolution, and the target embodiment context defines the acting body and its interaction geometry. This formulation enables independent recomposition of embodiment, viewpoint, and scene factors, allowing a single model to generate many robot-domain experiences while preserving the underlying dynamics and object interactions. We train the model with large-scale human interaction pretraining followed by mixed-embodiment fine-tuning. Experiments show that our model supports controllable recomposition across embodiments, viewpoints, and scenes, and we further demonstrate that the generated data can improve manipulation performance on the RoboCasa GR1 tabletop benchmark and a real IRON humanoid robot. Beyond aggregate gains, we test whether unpaired human experience can be recomposed into robot-native video-action pairs that target a policy gap. Controlled IRON interventions correct a spurious completion prior and establish language-grounded spatial target selection; an action-only counterfactual intervention fails to learn the latter reliably, showing that both action calibration and visual recomposition are necessary.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29242v1
- Authors: Cheng Chen, Jerry Bai, Jiacheng Wei, Boyu Chen, Xiaoji Zheng, Fan Wu, Minghao Yang, Tianrun Chen, Ruibo Li, Xiaoyu Yue, Xiaoyang Guo, Yixiao Ge, Guosheng Lin, Fayao Liu
- Published: 2026-08-29T12:55:15Z
- Age days: 2

</details>
