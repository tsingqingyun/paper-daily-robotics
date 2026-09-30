---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25689v1"
published: "2026-09-22T04:47:02Z"
age_days: 1
score: 29
created: 2026-09-24
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts

> [!summary] 先说人话（基于摘要）
> MotionForge 让机器人在物体持续运动、多个环境因素同时变化的条件下完成长任务，并把推理耗时真正计入执行过程。

## 问题

现有策略多在静态或近静态环境评估；已有动态基准又偏短时程、简单运动，对联合域变化和实时执行支持有限，因此可能高估实际动态操作能力。

## 创新点或方法

提供动态任务与数据生成流水线，分别测试单因素和联合域变化。解耦且考虑延迟的执行协议让环境独立于策略推理持续演化，使模型不能靠环境等待推理来完成任务。

## 证据

包含 40 个动态交互任务、11 种运动模式，其中专门支持 17 个长时程任务。代表性通用策略在联合域变化下暴露明显局限，摘要未给出可核查的性能数字。

## 局限

需核查延迟测量与硬件设置如何标准化，以及长时程、动态运动和域变化各自造成多大退化。

- **判断**：值得精读实时执行协议，尤其适合研究动态操作；具体模型强弱需查看完整评测结果。

## 研究关联

对具身智能体、世界模型和评测研究者，它把预测、控制与推理时延放在同一动态条件下检查，能检验静态成功率未覆盖的执行能力。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/MotionForge A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent advances in learning-based robot policies have demonstrated promising progress, yet they are predom- inantly evaluated in static or quasi-static environments. In dynamic manipulation, objects and scenes continuously evolve while the robot perceives, reasons, and acts. However, recent dynamic simulation benchmarks largely focus on short-horizon, reactive interactions with simple motion patterns and offer limited support for both systematic evaluation under domain shifts and model-agnostic real-time execution protocols. To bridge these gaps, we introduce MotionForge, the first large- scale simulation benchmark and data-generation pipeline tailored to jointly evaluate domain shifts and long-horizon interaction in dynamic manipulation. MotionForge comprises 40 dynamic interaction tasks spanning 11 distinct motion patterns, with dedicated support for 17 long-horizon tasks. Our benchmark introduces two key novelties: (1) a systematic evaluation protocol for assessing policy robustness under both single-factor (e.g., only backgrounds shift) and joint domain shifts (e.g., simultaneous shifts of objects, backgrounds, lighting, and speed); and (2) a decoupled, latency-aware execution protocol where the environ- ment continuously evolves independently of policy inference time. Extensive evaluations of representative general-purpose robot policies on our benchmark reveal substantial limitations under joint domain shifts. These findings expose a critical gap between current policy capabilities and the requirements of robust long- horizon manipulation of dynamic objects under domain shifts, establishing MotionForge as a comprehensive testbed for future research in embodied AI.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25689v1
- Authors: Mohan Liu, Dengchen Mei, Haotian Xian, Ruyang Han, Jiayi Sun, Xuanyu Chen, Haitian Zhang, Luxi Li, Kaimin Mao, Lin Wang
- Published: 2026-09-22T04:47:02Z
- Age days: 1

</details>
