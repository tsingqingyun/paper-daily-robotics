---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.24877v1"
published: "2026-08-25T17:56:54Z"
age_days: 1
score: 30
created: 2026-08-27
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# From Seeing to Acting: Smart Glasses as First-Person Intelligence Platforms

> [!summary] 先说人话（基于摘要）
> 这篇综述把智能眼镜视为持续运行的第一人称感知—状态—交互—行动闭环，而非单独的拍摄或问答设备，并提出L0-L5能力等级与部署、证据评估框架。

## 问题

智能眼镜研究分散在AR、自我中心视觉、多模态模型、交互和具身智能等领域，设备、任务与基准难比较；核心难点是整个闭环能否长期保持时效、可纠错和可治理。

## 创新点或方法

论文形式化第一人称数据流与受限任务效用，按8个可验证硬件轴刻画设备，以7项基础能力组织文献，并用L0-L5描述从采集到具身耦合；另覆盖9类应用、9维部署框架和分层证据协议。

## 证据

这是综述与框架论文；摘要未报告新的受控实验或可核查性能数字，仅陈述覆盖的能力轴、应用场景和评估层级。


## 局限

“首篇”及框架覆盖是否完整不能由摘要验证；分类体系的可操作性和不同设备间一致性需看正文与资料选择方法。

- **判断**：做可穿戴多模态系统或评测者值得通读；机器人策略研究者读框架与证据梯度章节即可。

## 研究关联

对多模态具身系统研究者，它提供了从模型指标走向持续上下文、隐私、反馈和治理的系统评测视角；对机器人核心控制算法的直接价值有限。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/From Seeing to Acting Smart Glasses as First-Person Intelligence Platforms.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Smart glasses are evolving from capture and display accessories into first-person intelligence platforms that connect human perception, persistent context, and digital or physical action. Their on-body viewpoint aligns with the wearer's vision, audition, motion, and hand-object interaction, but must operate under tight energy, thermal, privacy, and feedback constraints. Despite rapid progress in augmented reality, egocentric vision, multimodal models, human-computer interaction, and embodied intelligence, the literature remains fragmented across devices, tasks, and benchmarks. \textit{The key challenge is not whether a model can recognize, answer, remember, or act in isolation, but whether a complete system can sustain a reliable, temporally valid, correctable, and governable perception-state-interaction-action loop.} This survey is \textit{the \textbf{first} to systematically study smart glasses through such a unified framework}. We formalize first-person data flow and constrained task utility, characterize devices along eight verifiable hardware capability axes, organize the literature around seven interdependent foundational capabilities, and introduce an L0-L5 framework spanning capture, reactive perception, contextual assistance, persistent state, governed action, and embodied coupling. Across nine application scenes, we connect tasks with datasets, systems, products, stakeholders, failure consequences, and evidence gaps. We further present a nine-dimensional deployment framework, a claim-conditioned evaluation protocol, and an evidence ladder from controlled measurement to longitudinal field validation and audit. Together, these elements make smart glasses more comparable, deployable, and reproducibly evaluated, while outlining a roadmap toward trustworthy first-person intelligence.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.24877v1
- Authors: Jiangning Zhang, Haojun Chen, Yong Liu
- Published: 2026-08-25T17:56:54Z
- Age days: 1

</details>
