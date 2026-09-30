---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03611"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 31
created: 2026-09-05
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# FailBench: How Reliable are VLMs at Judging Robot Task Success?

> [!summary] 先说人话（基于摘要）
> FailBench 用跨14个来源的2,197次操作尝试检验 VLM 能否可靠判定机器人失败。结论很直接：最佳模型也只有0.77平衡准确率，接触密集任务接近随机，而且专门微调反而普遍退化。

## 问题

VLM 越来越常被当作机器人成功判定器，但现有基准缺少跨领域证据。可见物体运动容易判断，装配接触等结果证据模糊时，模型可能系统性把失败误判为成功。

## 创新点或方法

基准汇集12个真实和2个仿真来源，其中75%的失败自然发生；作者评测13种 VLM 检测器，按所需视觉证据分析错误，并测试将结果相关区域定位、裁剪后再判断的输入干预。

## 证据

最佳模型平均平衡准确率0.77；接触密集装配任务低于0.60。失败检测微调模型持续落后于通用 VLM 及其预训练基线；歧义场景存在偏向成功的系统误差，增加推理强度仍未消失。空间裁剪使最佳检测器提升2.4个百分点。


## 局限

需核查标注定义、视频时长与输入协议是否公平，以及0.77平均值在不同来源间是否存在巨大波动。

- **判断**：强烈建议做机器人自动评测或 VLM 奖励模型的人精读；它给出了明确的失败边界和简单但有效的改进方向。

## 研究关联

它提醒使用 VLM 自动评测 VLA 或真实机器人时，不能把单一模型判决当真值；基准也为失败检测、奖励建模和主动取证提供了更困难的测试集。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/FailBench How Reliable are VLMs at Judging Robot Task Success.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.03611v1 Announce Type: new Abstract: Vision-Language Models (VLMs) are increasingly used to evaluate robot manipulation outcomes, but existing benchmarks offer limited evidence of cross-domain generalization. We introduce FailBench, a benchmark for robot failure detection comprising 2,197 manipulation attempts across 14 public sources (12 real-world, 2 simulated). In FailBench, 75% of failures occur naturally, and six real-world sources come from non-failure-detection datasets. Evaluating 13 VLM-based detectors, we find the best model achieves only 0.77 mean balanced accuracy. Notably, models fine-tuned for failure detection consistently underperform general-purpose VLMs and their own pretrained baselines. Performance depends heavily on required visual evidence: models approach saturation when outcomes depend on observable object motion, but degrade to near-chance (<0.60 balanced accuracy) on contact-intensive assembly tasks. Error analysis reveals a systematic bias toward predicting success under ambiguous evidence, which persists even with increased reasoning effort. Finally, we show that input-level intervention--spatially localizing and cropping outcome-relevant regions--improves the top detector by 2.4 percentage points without extra training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03611
- Authors: Zaruhi Navasardyan, Tatul Danielyan, Hrant Davtyan
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
