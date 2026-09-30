---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11445v1"
published: "2026-09-10T12:14:37Z"
age_days: 1
score: 30
created: 2026-09-12
concepts: ["世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model

> [!summary] 先说人话（基于摘要）
> FARM从冻结机器人世界模型的内部预测状态中读出失败风险，只训练一个很小的监督读出器。它检验已有预测表征能否兼做在线监控。

## 这篇到底在做什么

- **卡在哪里**：机器人需要在执行过程中识别失败，但现有监控常依赖代理风险信号或专门训练监测组件；世界模型内部是否已有可直接利用的失败信息尚需验证。
- **关键解法**：冻结VLA-JEPA预测骨干，在其状态上训练33,985参数的读出器，输出逐步失败分数及仅依赖已发生历史的轨迹风险；通过固定读出器迁移和仅适配读出器测试部署变化。
- **拿什么证明**：七项源任务的五折折外评估汇总AUROC/AUPRC为85.68/88.59；十任务基准的Seen设置优于15个匹配基线。测试覆盖PIPER X、SO-101和Franka上的四组真实机器人部署条件；冻结状态已可用时，平均新增CUDA延迟0.2256 ms。

## 值不值得读

- **和你的研究有什么关系**：为世界模型提供执行监控这一复用方向，也让VLA系统能研究冻结表征上的轻量失败检测。
- **先别急着信**：延迟不含生成冻结状态的成本；摘要未量化跨部署迁移表现。基于历史的因果风险计算也不等于识别失败原因。
- **判断**：值得精读数据划分、失败标签和迁移结果，轻量监控思路有价值但需谨慎理解部署收益。

## 研究关联

- **概念**：[[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/FARM Reading Failure Signals from the Internal Predictive States of a Frozen Rob.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reliable robot deployment requires online failure monitoring, yet existing monitors mainly derive risk from proxy signals or train dedicated monitoring components. We ask whether the internal predictive states of a frozen pretrained robotic world model already contain directly decodable failure information. Failure-Aware Readout from World Models (FARM) trains only a 33,985-parameter supervised readout over frozen VLA-JEPA predictive states, producing step-wise failure scores and causal trajectory risk. Five-fold out-of-fold evaluation across seven source tasks reaches 85.68/88.59 pooled AUROC/AUPRC, and FARM gives the best Seen performance among 15 matched baselines on the 10-task benchmark. Across four real-robot populations on PIPER X, SO-101, and Franka, fixed-readout transfer and readout-only adaptation test deployment shifts without updating the predictive backbone. FARM also discriminates failures from partial causal histories and adds 0.2256 ms mean CUDA latency once the frozen state is available. These results support frozen predictive world-model states as reusable features for causal, transferable, and low-overhead execution monitoring.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11445v1
- Authors: Haoran Pei, Mingrui Luo, Senbao Wang, Haoran Lv, Jie Guo, Sheng Zhong, Ruixi Ci
- Published: 2026-09-10T12:14:37Z
- Age days: 1

</details>
