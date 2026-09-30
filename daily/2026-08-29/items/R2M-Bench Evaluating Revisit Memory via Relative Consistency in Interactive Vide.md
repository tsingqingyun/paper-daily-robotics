---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27328"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 21
created: 2026-08-29
concepts: ["世界模型", "具身智能评测与基准"]
---

# R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models

> [!summary] 先说人话（基于摘要）
> R2M-Bench不再只看“回来后画面像不像”，而是把重访相似度与同一轨迹中的普通时间稳定性、短程一致性对照，借MG和NMR隔离真正的重访记忆。

## 问题

首访与重访画面相似，可能只是模型几乎没移动或内容重复，并不代表记住场景。绝对重访分数因此容易被渲染稳定、慢动作和失败运动抬高。

## 创新点或方法

对每次检测到的返回，构造间隔匹配的非重访对照与短距离对照。MemoryGain衡量重访相对普通时间基线的优势，NMR再按短程到基线的动态范围归一化；评测外观、身份、局部几何和持久状态。

## 证据

100个参考场景各配3条离开—返回轨迹，共300个实例，覆盖7个动作条件视频世界模型。Overall NMR与人工一致性判断的Spearman相关为0.547，95%置信区间[0.45,0.63]；其模型内与生成运动的相关绝对值为0.072，而原始重访相似度为0.207。


## 局限

人工相关度仍属中等，且需核查返回检测、对照配对和不同运动幅度下NMR的稳定性；300个实例的覆盖边界也应看全文。

- **判断**：世界模型评测研究者应精读，尤其值得复用相对校准思想；它比单纯公布最佳模型排名更有方法论价值。

## 研究关联

它为世界模型长期空间记忆提供更抗慢动作捷径的评测，可帮助研究者区分“稳定地不动”和“离开后仍能恢复场景”。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/R2M-Bench Evaluating Revisit Memory via Relative Consistency in Interactive Vide.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.27328v1 Announce Type: new Abstract: High similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene; the intervening rollout may simply have changed very little. This ambiguity makes absolute revisit scores sensitive to rendering stability, repetitive content, and failed motion. We introduce \emph{R2M-Bench} (\textbf{R}elative \textbf{R}evisit \textbf{M}emory Benchmark), a benchmark of observable revisit-selective consistency. For every detected return, R2M-Bench compares the revisit pair with two controls from the same rollout: a gap-matched non-revisit pair that measures generic temporal stability and a short-range pair that estimates short-horizon consistency. These comparisons produce \emph{MemoryGain} (MG), the revisit advantage over the temporal baseline, and the \emph{Normalized Memory Ratio} (NMR), which normalizes this advantage by the short-to-baseline dynamic range. R2M-Bench combines 100 reference scenes with three leave-and-return trajectories to form 300 instances and evaluates appearance fidelity, scene and object identity, local geometry, and persistent state. Across seven action-conditioned video world models, Overall NMR correlates with human consistency judgments at Spearman's $\rho=0.547$ (95\% CI $[0.45,0.63]$). Its within-model correlation magnitude with generated motion is $0.072$, compared with $0.207$ for raw revisit similarity, indicating that relative calibration substantially reduces the slow-motion shortcut. DreamX-World-Memo achieves the highest Overall NMR among the evaluated video models. Together, these results support same-rollout relative calibration as a practical way to distinguish revisit-specific consistency from generic temporal stability.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27328
- Authors: Qiwen Gu, Bingjie Gao, Rui Chen, Geng Li, Jifan Li, Qishuai Wen, Li Niu, Jing Tang, Xiangxiang Chu, Junqiao Zhao
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
