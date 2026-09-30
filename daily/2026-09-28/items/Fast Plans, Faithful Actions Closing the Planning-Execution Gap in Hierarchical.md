---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30833v1"
published: "2026-09-25T05:22:23Z"
age_days: 3
score: 28
created: 2026-09-28
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> 这项工作同时修补分层 VLA 的两个问题：规划太慢，以及动作专家实际上很少使用规划。Block-AR 按路点块解码提速，NGM 加强路点对动作生成的影响。

## 问题

在一个改自 π₀.₅ 的路点层级系统中，Token-AR 需要 57 次昂贵 VLM 前向计算，但擦除路点终点对成功率影响很小。瓶颈既有规划粒度过细，也有执行器没有有效利用目标条件。

## 创新点或方法

Block-AR 以路点对齐的块替代逐 token 自回归生成；NGM 建立逐层目标调制路径，通过阶段门控与反捷径训练，使路点参与动作生成，同时保留其他输入信号。

## 证据

LIBERO 上最多 VLM 前向次数从 57 降至 8，含一次前缀预填充；真机规划延迟降低 8.7 倍。加入 NGM 与反捷径训练后，Block-AR 在 LIBERO-Long 从 91.0% 提升至 96.2%，四套件均值从 95.85% 提升至 98.45%；三个真机双臂任务成功率相近。

## 局限

诊断来自特定改造的层级流水线，不能推广到所有分层 VLA；真机证据支持提速，但未显示成功率明显提高。

- **判断**：值得精读诊断实验与反捷径训练，是今天最适合转化为自身系统检查项的工作之一。

## 研究关联

对分层 VLA 与机器人智能体研究者，最有价值的是同时检查规划成本和规划的实际控制作用。擦除规划的干预也提供了检验模块是否被使用的直接思路。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/Fast Plans, Faithful Actions Closing the Planning-Execution Gap in Hierarchical.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Hierarchical vision-language-action (VLA) systems consist of a high-level vision-language planner and a low-level action expert that generates continuous actions. This hierarchical design has practical value only if the planner can generate plans fast enough to meet real-time control requirements, and the resulting plans actually contribute to the generation of action. We study one such system, a waypoint hierarchy pipeline adapted from $π_{0.5}$, and find that neither requirement is satisfied. This baseline relies on token-level autoregressive decoding (Token-AR) to generate a waypoint plan, requiring 57 very expensive vision-language model (VLM) forward passes. However, we find that erasing the waypoint endpoints has little effect on task success. Two findings reveal the misalignment of planner-executor: the planner generates outputs at an excessively fine granularity, and the executor underuses plans as a control condition. We address the latency issue with waypoint-aligned block-autoregressive decoding (Block-AR), and plan underuse issue with normalized goal modulation (NGM), a layer-wise goal path constrained by phase gating and anti-shortcut training so that the waypoint influences action generation maintaining other signals. Our method reduces the maximum number of VLM forward passes from 57 to 8 on LIBERO, including one prefix prefill, and achieves an $8.7\times$ reduction in planning latency on a Rokae dual-arm robot. With normalized goal modulation and anti-shortcut training, Block-AR's success rate on LIBERO-Long increases from 91.0% to 96.2%, while its average success rate across the four suites increases from 95.85% to 98.45%. On three bimanual tasks with this robot, success rates remain comparable across methods.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30833v1
- Authors: Chuanliang Xie, Boyu Ma, Gen Li, Yizhou Liu, Houwang Chen, Xinyu Zhou, Jianfei Yang
- Published: 2026-09-25T05:22:23Z
- Age days: 3

</details>
