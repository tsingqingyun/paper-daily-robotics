---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27158v1"
published: "2026-08-27T14:10:39Z"
age_days: 2
score: 27
created: 2026-08-30
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation

> [!summary] 先说人话（基于摘要）
> PDPO用扩散策略一次生成五步避障动作块，再以滚动时域执行；先离线学示范，后把去噪过程视作内部决策过程，用 PPO 在线优化。

## 问题

密集动态人群中存在多种合理短期避让方式，而传统强化学习每步只输出一个反应动作，难表达多模态策略。常用基准还允许机器人越界绕开人群，造成虚高结果。

## 创新点或方法

先在避碰示范上预训练扩散策略，再用 PPO微调去噪过程；执行时生成五步动作块并滚动重规划。同时把边界违规计作碰撞，修正原评测漏洞。

## 证据

摘要称 PDPO相较强基线提高成功率，消融显示动作块在加入边界约束的基准上尤其重要；未给出具体成功率或提升数字。


## 局限

需核查改进来自扩散分布建模、动作块还是在线 PPO，以及五步开环执行在快速变化人群中的安全代价。

- **判断**：做拥挤导航者应精读，尤其要采用其边界修正；泛机器人读者看评测漏洞与动作块消融即可。

## 研究关联

对机器人学习和具身评测者，价值一半在短时程多模态规划，一半在揭示“越界绕行”这一会扭曲导航结论的评测漏洞。与多模态基础模型关联不强。

- **概念**：多模态基础模型 智能体 Agent 机器人学习 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot crowd navigation requires safe and efficient decision-making under dense, dynamic, and multimodal human--robot interactions. Existing reinforcement-learning methods typically output a single reactive action at each timestep, which limits their ability to represent diverse short-term avoidance strategies. We propose Planning Diffusion Policy Optimization (PDPO), an offline-to-online reinforcement-learning framework that uses a diffusion policy to generate short-horizon action chunks for crowd navigation. PDPO is first pretrained on collision-avoidance demonstrations and then fine-tuned online with PPO by treating the denoising process as an internal decision process. During execution, the policy generates a five-step action chunk and applies it in a receding-horizon manner. Furthermore, we observe an evaluation artifact in common crowd-navigation benchmarks: without explicit boundary constraints, learned agents may leave the valid domain and bypass dense crowds. To address this, we introduce a setting in which boundary violations are treated as collisions. Experiments show that PDPO obtains an improved success rate over strong baselines, and ablations demonstrate that action chunks are especially important for the modified bounded benchmark.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27158v1
- Authors: Wendong Li, Jochen Garcke
- Published: 2026-08-27T14:10:39Z
- Age days: 2

</details>
