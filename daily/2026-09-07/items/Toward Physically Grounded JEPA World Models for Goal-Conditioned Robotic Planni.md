---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03565v1"
published: "2026-09-03T09:11:13Z"
age_days: 3
score: 25
created: 2026-09-07
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planning

> [!summary] 先说人话（基于摘要）
> 该JEPA世界模型在潜在未来预测之外加入逆动力学和状态对齐，让隐表示既能反映动作，也锚定机器人的物理构型与运动，从而改善目标条件规划。

## 这篇到底在做什么

- **卡在哪里**：动作条件JEPA无需重建像素即可规划，但只预测潜变量并不保证表示保留控制所需信息，可能发生坍塌或学到与物理状态脱节的变化。
- **关键解法**：模型端到端预测动作条件潜在转移；IDM要求表示能解释产生转移的动作，SA则把相邻表示与对应物理配置和运动对齐。与只加IDM或纯潜预测相比，它显式注入动作可辨识性和物理落地约束。
- **拿什么证明**：四项任务中TwoRoom成功率100%、PushT 98%、OGBench-Cube 87%，Reacher与LeWorldModel相当。SA相对仅IDM在四项任务上均提高规划成功率；其有效转移维度高于LeWorldModel，但后者在OGBench-Cube平均straightening指标更高。

## 值不值得读

- **和你的研究有什么关系**：对机器人世界模型研究者，它给出一种不回到像素重建、又能增强控制相关物理信息的JEPA训练办法，并配有规划和表示空间证据。
- **先别急着信**：更高有效转移维度并不自动等于更好的因果或物理表征；且在一项指标上主基线仍占优，需要核查评价权重和状态监督需求。
- **判断**：值得精读损失设计与转移子空间分析；这是把JEPA从预测表征推向可规划物理表征的扎实工作。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planni.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Action-conditioned JEPA world models enable planning toward visually specified goals without reconstructing future pixels, yet latent prediction alone does not explicitly encourage the learned representations to retain information relevant to robotic control. We introduce an end-to-end JEPA world model that augments latent prediction with inverse dynamics (IDM) and state alignment (SA). While inverse dynamics discourages latent collapse and makes latent transitions informative of the actions that produced them, state alignment grounds consecutive representations in their associated physical configuration and motion. Across four benchmark tasks, our model attains the highest success rates on TwoRoom (100%), PushT (98%), and OGBench-Cube (87%), while performing comparably to LeWorldModel on Reacher. Our ablation further shows that adding state alignment consistently improves planning success over IDM alone across all four tasks. Although LeWorldModel, our primary baseline, attains higher average straightening on OGBench-Cube, transition-subspace analysis shows that its transition energy is concentrated in a substantially lower-dimensional subspace. Our state-aligned model exhibits a higher effective transition dimension than LeWorldModel and improves planning over IDM alone, supporting state alignment as an effective complement to inverse dynamics for robotic planning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03565v1
- Authors: Muyuan Liu, Yue Huang, Zheng Liang, Xiang Gao
- Published: 2026-09-03T09:11:13Z
- Age days: 3

</details>
