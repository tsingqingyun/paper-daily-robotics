---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19441v1"
published: "2026-09-16T21:25:37Z"
age_days: 1
score: 27
created: 2026-09-18
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Predict Before You Deploy: Offline Prediction of Quantization-Induced Task Degradation for World Action Models

> [!summary] 先说人话（基于摘要）
> PreDE先用少量闭环结果校准离线动作偏差，再筛选世界动作模型的量化配置；证据不足时明确暂缓判断，减少逐个上机器人测试的负担。

## 问题

量化配置由位宽、分组和量化器共同决定，穷举闭环测试成本高。仅凭位宽或跨策略统一的动作偏差阈值，无法可靠判断任务性能是否受损。

## 创新点或方法

用小型开发集的闭环标签校准两个阈值，在固定观测日志上评估新配置的动作偏差。基于同设置内的标签排序假设，仅在所有与开发标签一致的阈值都同意时接受或拒绝，否则暂缓。

## 证据

研究覆盖5个WAM和4种基准设置。两种策略的28个留出配置中，提前判定21个，覆盖率75%，均与后来闭环标签一致。450次Franka Research 3试验中，预先划定的高偏差组均显著退化；低偏差比较未发现显著退化。实机W4A4动作查询加速1.37倍、峰值内存约降44%。

## 局限

判定依赖同设置内的排序假设；21个判定全对不是任意配置的保证，低偏差组未显著退化也不等于已证明无损。

- **判断**：值得优先精读校准假设、留出划分和暂缓规则，对量化部署有直接价值，也明确保留了闭环验证的必要位置。

## 研究关联

对生成式动作模型部署与具身评测，提供把昂贵闭环实验集中到不确定配置上的筛选工具，并强调校准必须针对具体策略。

- **概念**：视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/Predict Before You Deploy Offline Prediction of Quantization-Induced Task Degrad.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World action models (WAMs) rely on video-generation backbones, requiring substantial memory and compute for deployment. Post-training quantization reduces memory and can accelerate inference, but bit width, grouping, and quantizer choice define a large configuration space. Identifying configurations that preserve task performance through exhaustive closed-loop evaluation is costly. We propose PreDE (Predict Before You Deploy), a policy-calibrated framework for predicting quantization-induced task degradation from offline action deviations. Using closed-loop outcomes from a small development set, PreDE calibrates two thresholds and accepts, rejects, or defers new configurations using a fixed observation log. Under a within-setting label-ordering hypothesis, the rule issues decisions where all thresholds consistent with the development labels agree. Across five WAMs and four benchmark settings, quantization produces configuration-dependent task losses that cannot be explained by bit width alone or a shared deviation threshold. Across 28 held-out configurations from two policies, PreDE issued 21 decisions before observing closed-loop outcomes (75% coverage), all matching the observed acceptable or degraded labels. Deferred candidates included both acceptable outcomes and a 33-percentage-point loss. In 450 Franka Research 3 trials across two independently fine-tuned policies, all configurations assigned to high-deviation groups before testing showed significant degradation, while low-deviation comparisons showed no statistically significant degradation. On the real robot, W4A4 achieved a 1.37x action-query speedup and approximately 44% lower peak memory. These results support policy-specific behavioral calibration for quantization configuration selection while identifying candidates that require closed-loop evaluation. The code is available at https://github.com/jiuyixu25/PreDE.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19441v1
- Authors: Jiuyi Xu, Jinjia Guo, Meida Chen, Jing Du, Yangming Shi
- Published: 2026-09-16T21:25:37Z
- Age days: 1

</details>
