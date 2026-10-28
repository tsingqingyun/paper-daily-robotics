---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.35075v1"
published: "2026-10-26T09:20:31Z"
age_days: 1
score: 36
created: 2026-10-28
concepts: ["智能体 Agent", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data

> [!summary] 这篇论文到底做了什么（基于摘要）
> Zero-HLM 用手机采集真实环境，在仿真里修正场景和全身动作，生成可执行的示范，再训练人形机器人。巧处在于场景和动作一起改，避免得到看着像真的环境却跑不通的动作。

## 问题

人形移动操作需要边移动身体边接触物体，真实示范昂贵。仿真可以扩大数据量，但既要重建视觉外观和物理属性，又要让全身动作在该环境中实际执行；只解决其中一项，训练数据仍可能失效。

### 用一个例子理解

理解用例（非论文实验）：输入是手机拍摄的柜台和一段仿真取物动作；系统重建柜台，发现机器人伸手时身体碰撞，于是修正动作参考与交互几何；输出可执行示范，供策略学习走近并取物。

## 创新点或方法

相比直接依赖真实机器人示范，Zero-HLM 从手机采集和仿真源示范出发。高斯引导的智能体重建负责对齐场景外观与物理结构；随后用仿真执行反馈，同时修正全身动作参考和交互几何。训练阶段使用这些通过物理验证的示范训练 GR00T N1.7；部署阶段零样本迁移到 G1。摘要未说明在线是否继续适配，也未交代各项修正的优化细节。

### 方法如何工作

1. 用手机采集真实场景，提供仿真重建所需的环境信息。
2. 通过高斯引导重建对齐视觉和物理场景，使训练环境既能看也能交互。
3. 在场景中执行源示范，用失败反馈共同修正动作参考与交互几何，获得可执行数据。
4. 用验证后的示范训练策略，再迁移到真机；摘要未说明部署时的额外处理。

### 必要术语

- 移动操作：移动身体并操作物体；本文要求全身动作与环境接触协调。
- real-to-sim-to-real：从真实环境建仿真，再把仿真所学带回真机；本文用它组织数据生成。
- 动作—环境共同适配：根据执行反馈同时修改动作与交互几何；本文用它提高示范可执行性。

## 证据

摘要报告生成 4,800 条物理验证示范，用于 Unitree G1 的三个任务。仿真数据训练的 GR00T N1.7 平均完整任务成功率为 66.7%，真实数据训练为 46.7%；在泛化配置上，扩大仿真训练后，汇总成功率由基础真实数据策略的 23% 升至 69%，无需新增真实示范。摘要将其作为真机迁移结果，但未列任务、配置变化、试验次数和误差范围；两组比较也不能直接当成同一条件下的消融。

## 局限

“不用真实机器人数据”仍需要手机采集和仿真源示范，并不等于没有真实环境输入。尚需核查数据规模和训练预算是否匹配，以及成功率提高有多少来自数据扩充、多少来自共同修正机制。

- **判断**：值得细读数据生成与共同修正部分；摘要结果有吸引力，但要看清比较条件才能判断方法本身的收益。

## 研究关联

值得借鉴的是用“能否执行成功”反过来修正数据生成过程。需要扩大接触式全身动作数据时，重建质量应同时看外观、碰撞关系和动作可行性。

### 下一步读哪里

优先核查三个真机任务和泛化配置的定义、物理验证通过条件、场景与动作分别怎样修改，以及相同数据量下的消融。还需确认手机采集、源示范和人工修正的实际成本。

- **概念**：智能体 Agent 世界模型 机器人学习 Sim2Real 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/Zero-HLM Generalizable Humanoid Loco-Manipulation without Real Robot Data.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning generalizable humanoid loco-manipulation remains bottlenecked by costly real-world demonstrations. Simulation provides a scalable alternative, but requires visually faithful, physics-ready scenes and executable whole-body motions. We present Zero-HLM, a real-to-sim-to-real framework that transforms smartphone captures and simulated source demonstrations into scalable training data for humanoid loco-manipulation. Gaussian-guided agentic real-to-sim reconstruction aligns visual and physical scenes; motion-environment co-adaptation uses rollout feedback to correct whole-body references and interaction geometry. We generate 4,800 physically validated demonstrations for zero-shot transfer across three Unitree G1 tasks. Simulation-trained GR00T N1.7 achieves 66.7% mean full-task success, versus 46.7% with real-data training. On generalized configurations, expanded simulation training raises pooled success from 23% for base-trained real-data policies to 69%, without additional real demonstrations. Project page: https://young-bit.github.io/zero-hlm/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.35075v1
- Authors: Dianyi Yang, Mengya Liu, Zhumei Wang, Yu Liu, Xiaochen Zhang, Yixuan Li, Le Ma, Yuhang Yang, Weiqi Huang, Wei Liang, Baoxiong Jia, Siyuan Huang
- Published: 2026-10-26T09:20:31Z
- Age days: 1

</details>
