---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03276v1"
published: "2026-09-03T02:08:16Z"
age_days: 3
score: 35
created: 2026-09-07
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# R2S-Eval: Robot Evaluation with Real-to-Sim Calibration via Vision-Language Models

> [!summary] 先说人话（基于摘要）
> R2S-Eval 先把真实评测场景校准到仿真并生成滚动视频，再让VLM成对比较完整行为质量，汇总为策略排名。

## 问题

真实机器人评测需要反复试验、人工复位和监看，结果还可能不稳定；单一成功率只能告诉任务是否完成，无法反映执行质量。

## 创新点或方法

输入是校准仿真中的策略滚动视频，VLM输出成对偏好，再聚合成排名；配套协议检验这些排名能否形成经验证且稳定的策略结论。与传统方法相比，它减少硬件重复执行，并以行为比较代替单纯二元计数。

## 证据

仿真和真实实验表明，R2S-Eval能产生可靠、稳定的策略结论，与人类偏好一致，减少重复硬件操作，并发现成功标签遗漏的行为质量差异；摘要未给一致率、节省比例或样本规模。


## 局限

最需核查的是仿真校准误差会否改变策略排序，以及VLM评价是否在不同任务、视角和失败类型上保持可靠。

- **判断**：值得读评测协议和真实—仿真一致性分析；在没有量化细节前，不宜把它直接当作真实评测替代品。

## 研究关联

它为VLA和机器人基准提供了成本更低、信息更丰富的评测管线，尤其适合需要频繁比较策略版本的团队。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/R2S-Eval Robot Evaluation with Real-to-Sim Calibration via Vision-Language Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Evaluating robot manipulation policies is becoming increasingly important as generalist models, particularly vision-language-action (VLA) models, are deployed on physical robots. However, conventional real-world evaluation remains labor-intensive, unstable, and insufficiently informative. It requires repeated hardware trials, manual scene resets, and continuous operator monitoring, may produce different policy rankings across repeated evaluations, and primarily relies on success-rate metrics that provide limited information about execution quality. In contrast, humans assess robot performance by observing and comparing complete behaviors rather than relying solely on binary success outcomes. To this end, we propose R2S-Eval, an evaluation pipeline that combines real-to-sim calibration with vision-language model (VLM) preference evaluation. The real-to-sim component efficiently generates rollout videos in a simulator calibrated to the real-world evaluation setting, thereby reducing the need for repeated hardware trials. The VLM evaluator assesses the execution quality of rollout videos and produces pairwise preferences, which are subsequently aggregated into policy rankings. We further introduce a protocol to assess whether the proposed evaluation pipeline yields validated policy conclusions while mitigating the key challenges of conventional real-world evaluation. Experiments in both simulation and real-world settings demonstrate that R2S-Eval produces reliable and stable policy conclusions, achieves agreement with human preferences, substantially reduces repeated hardware-operation effort, and reveals behavior-quality differences that are not captured by binary success labels. In general, R2S-Eval advances robot evaluation from manual success counting toward automated, statistically stable, and quality-aware evaluation of robot behavior. Project page: https://r2s-eval.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03276v1
- Authors: Yidi Wang, Feixiang Ruan, Ruoqu Chen, Jie Yin, Yang Yu, Mengdi Xu, Kaifeng Zhang
- Published: 2026-09-03T02:08:16Z
- Age days: 3

</details>
