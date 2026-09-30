---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30249v1"
published: "2026-09-24T17:58:21Z"
age_days: 3
score: 29
created: 2026-09-28
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# RAPID: Robot Agentic Programming from Demonstrations

> [!summary] 先说人话（基于摘要）
> RAPID 从一段人类视觉示范中推断任务判据、动作原语和验证环境，再让编程智能体反复生成、测试与修正机器人程序。程序保留物体之间的操作关系，以便适应新场景。

## 问题

把编程智能体用于机器人，需要可测试的任务规格、可执行动作原语和交互验证环境。单次示范还带有特定几何与运动细节，直接复用这些细节会限制泛化。

## 创新点或方法

自动从示范推断上述三个要素，通过执行验证闭环修正代码。动作原语表示为实现物体级运动效果的轨迹优化程序，再用运行时关系约束组合，以适配当前场景几何。

## 证据

仿真评估包含八个接触密集非抓取任务和 LIBERO-Pro 抓取任务；真实 Franka 上评估了全部八个非抓取任务。摘要报告对物体位姿、形状、材料和环境的泛化，但未给出可核查的结果数字。

## 局限

需核查自动推断的任务规格和验证环境是否准确，以及单次视觉示范之外需要哪些既有模型与系统配置。

- **判断**：值得读完整系统流程和失败案例，定量对照清楚前不宜仅凭“强泛化”判断效果。

## 研究关联

对机器人智能体与示范学习研究者，它提供了从视觉示范通向可执行程序和自动验证的路线，特别适合考察策略结构而非具体轨迹的复用。

- **概念**：智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/RAPID Robot Agentic Programming from Demonstrations.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Coding agents have demonstrated enormous success in solving complex programming problems. To leverage their potential for robot systems, this work introduces Robot Agentic Programming from Demonstrations (RAPID), which automatically generates, verifies, and refines robot programs, given a single visual human demonstration. The iterative agentic loop of code refinement requires several key ingredients: (i) a testable task specification, (ii) action primitives for robot execution, and (iii) an interactive environment for program execution and verification. RAPID infers all three from the demonstration automatically. To make the resulting program reusable beyond the demonstration setting, RAPID uses an object-centric relational program representation that focuses on the underlying structure of the demonstrated strategy rather than the specific motion per se: it expresses the action primitives as trajectory-optimization programs that realize object-level motion effects, while composing them through relational constraints that capture scene-specific geometry at run time. We evaluated RAPID in simulation on eight challenging contact-rich nonprehensile manipulation tasks as well as general prehensile manipulation tasks in the LIBERO-Pro benchmark. We also successfully deployed it on a real Franka arm and evaluated on all eight nonprehensile tasks. In all experiments, RAPID demonstrated strong performance, with generalization over object pose, shape, material, and environment. Website: https://yuyaoliu.me/projects/rapid.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30249v1
- Authors: Yuyao Liu, Jiayuan Mao, David Hsu, Leslie Pack Kaelbling, Tomás Lozano-Pérez
- Published: 2026-09-24T17:58:21Z
- Age days: 3

</details>
