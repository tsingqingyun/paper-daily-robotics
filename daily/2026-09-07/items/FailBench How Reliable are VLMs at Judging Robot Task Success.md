---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03611v1"
published: "2026-09-03T09:58:55Z"
age_days: 3
score: 31
created: 2026-09-07
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# FailBench: How Reliable are VLMs at Judging Robot Task Success?

> [!summary] 先说人话（基于摘要）
> FailBench 用跨14个公开来源的2,197次操作尝试检验VLM能否判定机器人成功，结果显示最佳模型也只有0.77平衡准确率，接触密集任务更接近随机。

## 这篇到底在做什么

- **卡在哪里**：VLM正被当作机器人评测器，但现有基准对跨来源泛化证据不足；如果视觉证据含糊或任务依赖接触状态，模型可能系统性误判成功。
- **关键解法**：基准汇集真实与仿真中的自然失败，评测13个VLM检测器，并按所需视觉证据分析错误；还测试了增加推理投入及裁剪结果相关区域两种干预。
- **拿什么证明**：共2,197次尝试、14个来源，其中12个真实、2个仿真，75%失败自然发生。最佳平均平衡准确率0.77；接触密集装配低于0.60，微调失败检测器持续差于通用VLM及其预训练基线。模型在模糊证据下偏向判成功，增加推理仍存在；相关区域定位裁剪令最佳模型提高2.4个百分点。

## 值不值得读

- **和你的研究有什么关系**：它直接警告具身评测研究者：不能未经验证就用VLM替代人工裁判，并提供了跨域、按失败证据类型拆分的压力测试。
- **先别急着信**：需核查人工标签定义、视频视角和不同来源权重；0.77均值可能掩盖具体模型与域之间的巨大差异。
- **判断**：强烈建议所有使用VLM自动评测的人精读；它是对当前评测基础设施可靠性的关键审计。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/FailBench How Reliable are VLMs at Judging Robot Task Success.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language Models (VLMs) are increasingly used to evaluate robot manipulation outcomes, but existing benchmarks offer limited evidence of cross-domain generalization. We introduce FailBench, a benchmark for robot failure detection comprising 2,197 manipulation attempts across 14 public sources (12 real-world, 2 simulated). In FailBench, 75% of failures occur naturally, and six real-world sources come from non-failure-detection datasets. Evaluating 13 VLM-based detectors, we find the best model achieves only 0.77 mean balanced accuracy. Notably, models fine-tuned for failure detection consistently underperform general-purpose VLMs and their own pretrained baselines. Performance depends heavily on required visual evidence: models approach saturation when outcomes depend on observable object motion, but degrade to near-chance (<0.60 balanced accuracy) on contact-intensive assembly tasks. Error analysis reveals a systematic bias toward predicting success under ambiguous evidence, which persists even with increased reasoning effort. Finally, we show that input-level intervention--spatially localizing and cropping outcome-relevant regions--improves the top detector by 2.4 percentage points without extra training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03611v1
- Authors: Zaruhi Navasardyan, Tatul Danielyan, Hrant Davtyan
- Published: 2026-09-03T09:58:55Z
- Age days: 3

</details>
