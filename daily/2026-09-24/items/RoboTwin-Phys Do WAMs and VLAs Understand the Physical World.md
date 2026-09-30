---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.26292v1"
published: "2026-09-22T12:04:52Z"
age_days: 1
score: 33
created: 2026-09-24
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?

> [!summary] 先说人话（基于摘要）
> RoboTwin-Phys 把物体质量、摩擦和关节动力学等物理变化纳入机器人评测，检查策略是否只能应付画面变化，却无法应付真实交互条件变化。

## 问题

现有操作基准大量改变外观、布局和观测，却通常固定底层物理参数，因此遗漏了影响动作结果的重要变化来源。

## 创新点或方法

在物理合理范围内连续改变 13 项物理属性，并提供带真实物理参数标注的专家示范。由此统一支持策略鲁棒性评测、属性估计和以物理条件为输入的模型训练。

## 证据

发布超过 5,000 条专家示范。对代表性 WAM 和 VLA 的评测发现，能应对视觉和布局随机化的模型，在物理条件变化下仍会明显退化；摘要未给出退化幅度。

## 局限

需核查 13 项属性的范围、组合方式和训练测试划分；性能下降本身还不能解释模型究竟缺少属性识别、在线适应还是控制能力。

- **判断**：值得细读评测协议并考虑纳入鲁棒性测试，核心价值是补足物理变化这一长期被固定的变量。

## 研究关联

对世界模型、VLA 和机器人学习研究者，这能区分视觉泛化与交互动力学泛化，并为物理条件建模提供明确监督。

- **概念**：世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/RoboTwin-Phys Do WAMs and VLAs Understand the Physical World.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physical-condition diversity is largely missing from current benchmarks for robot manipulation. While large-scale simulation benchmarks increasingly incorporate variations in object appearance, scene layout, and visual observations, they typically keep the underlying physical parameters fixed. As a result, important sources of real-world variability, such as changes in mass, friction, and joint dynamics, remain largely untested. We introduce RoboTwin-Phys, a physics-diverse benchmark that treats physical-condition diversity as an explicit dimension of robot manipulation evaluation. The benchmark continuously varies 13 physical attributes within physically plausible ranges, providing a unified setting for evaluating policies across diverse physical operating conditions. We further release more than 5,000 expert demonstrations with ground-truth physical parameters, enabling physical-attribute estimation, condition-aware modeling, and physics-conditioned policy training. Evaluations of representative WAMs and VLAs reveal a substantial robustness gap: models that remain effective under existing visual and layout randomization can degrade markedly under changes in physical conditions. RoboTwin-Phys provides the benchmark, data, and evaluation protocol needed to systematically measure and improve robustness to physical-condition diversity in robot manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.26292v1
- Authors: Jiaqi Zhang, Feng Ye, Mingjia Yang, Zhihong Chen, Mingkang Xiang, Xinglin Yao, Yanbin Li, Siwei Ma, Chuanmin Jia
- Published: 2026-09-22T12:04:52Z
- Age days: 1

</details>
