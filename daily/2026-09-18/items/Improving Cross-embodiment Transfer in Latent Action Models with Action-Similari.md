---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19846v1"
published: "2026-09-17T07:55:35Z"
age_days: 0
score: 32
created: 2026-09-18
concepts: ["视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Improving Cross-embodiment Transfer in Latent Action Models with Action-Similarity Supervision

> [!summary] 先说人话（基于摘要）
> 这项工作用“两个动作有多相似”监督潜动作，而不要求潜动作还原某台机器人的具体控制命令，让不同机器人的相似运动更容易对齐。

## 问题

从无动作标签视频学习的潜动作模型容易受背景干扰，还可能把不同机器人执行的相同运动编码成不同潜变量。用动作预测辅助损失虽能引入监督，却又把潜空间绑定到本体特定动作。

## 创新点或方法

训练任意两个潜动作的相似度匹配其真实动作序列的相似度，不要求LAM输出真实动作。研究比较了末端运动与关节运动定义的相似度，以及是否跨机器人配对监督。

## 证据

在RoboTwin 2.0的两种双臂机器人互斥任务集上，固定策略架构、超参数、数据和评估协议；预测潜动作相较直接预测真实动作使跨本体成功率超过翻倍。相似性监督优于动作预测辅助损失，跨机器人比较末端运动相似性的方案最佳。

## 局限

需区分“潜动作优于真实动作”的翻倍结果与“相似性监督优于辅助预测”的收益，摘要未给出后者的绝对幅度。

- **判断**：值得精读损失定义和受控对照，研究问题清晰，尤其适合正在设计跨本体动作表示的团队。

## 研究关联

对跨本体VLA与机器人学习，提供了重新利用既有动作标签的方法：监督共享运动关系，同时减少对具体控制接口的绑定。

- **概念**：[[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/Improving Cross-embodiment Transfer in Latent Action Models with Action-Similari.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As generalist robot policies gain vision and language from web-scale pretraining, demonstrations remain costly to collect and tied to the robot that recorded them. Latent action models (LAMs) address both by learning latent actions from action-free videos that can be shared across embodiments, however, in practice, LAMs are sensitive to background visual noise, and the same motion from two different robots may be encoded with different latents. One solution to the background visual noise is to add an auxiliary loss predicting the robot action from the latent action, further associating the latent action space to the embodiment specific robot action space. We study a different use of the same labels, through action-similarity supervision. The similarity between any two latent actions is trained to match the similarity of the two ground-truth robot action sequences. The ground-truth actions are never predicted by the LAM, so the latent action does not need to encode embodiment specifics. We evaluate cross-embodiment transfer on RoboTwin 2.0 in a controlled setup, two bimanual robots demonstrate disjoint task sets, a policy is trained on all the demonstrations, and each robot is evaluated closed-loop on the tasks only the other demonstrated. With the policy architecture and its hyperparameters, the dataset, and the evaluation protocol fixed, predicting latent actions instead of ground-truth actions more than doubles cross-embodiment success. Given the same ground-truth actions, similarity supervision transfers better than an auxiliary loss that predicts the ground-truth action during the LAM training. Computing the similarities on end-effector motion rather than joint-space motion, and letting the loss compare latent actions across the two robots, gives the best approach of the study.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19846v1
- Authors: Maxime Alvarez, Renzo Caballero, Tatsuya Matsushima, Yusuke Iwasawa, Yutaka Matsuo
- Published: 2026-09-17T07:55:35Z
- Age days: 0

</details>
