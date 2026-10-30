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
url: "https://arxiv.org/abs/2606.03385"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 27
created: 2026-10-30
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> GTP-FA 先选抓法，再按抓法规划后续动作，并学习判断失败更可能来自哪里。它用诊断结果分别调整抓取选择和规划训练，减少修错模块的试错。

## 问题

长程操作中，物体中途掉落可能是最初没抓稳，也可能是后续动作太危险；抓取与规划互相影响，失败表象不能直接指明原因。若不区分来源就一起调，可能反复训练规划器，却始终受制于不适合任务的抓法。

### 用一个例子理解

理解用例（非论文实验）：输入“抓起长柄勺并放入窄筒”和场景观测；系统先选抓取位置，再规划插入动作。若勺子无法进入筒口，归因结果可指导检查抓法是否妨碍插入，或针对该起始姿态补充规划训练。

## 创新点或方法

本文将操作分成抓取候选生成和以选定抓法为条件的运动规划，再学习从失败轨迹输出各失败模式的概率分布。训练和优化时，抓取侧把任务先验、风险惩罚加入候选评分与优化；规划侧围绕高风险初始状态采集数据并微调。执行时按抓取后规划的顺序操作。摘要未说明归因标签来源、诊断模型结构，以及部署时是否每次都调用归因模型。

### 方法如何工作

1. 生成抓取候选并选定抓法，给后续规划提供明确的持物起始条件。
2. 以选定抓法规划并执行任务，得到成功结果或可用于诊断的失败轨迹。
3. 将失败轨迹送入归因模型，得到失败模式分布，为优化方向提供依据。
4. 依据诊断修正抓取评分，或采集高风险起始状态的数据微调规划器，使两侧改动对准相应问题。

### 必要术语

- 失败归因：判断失败可能由哪些模式造成；在本文中用概率分布指导优化。
- 任务先验：关于什么抓法有利于完成后续任务的知识；在本文中参与抓取评分。
- 条件规划：根据已选抓法规划后续动作；在本文中连接抓取阶段与运动阶段。

## 证据

摘要报告仿真和真机实验，并称在 RL、IL、扩散策略和 VLA 设置中提高相应基础学习器的整体任务成功率，同时报告归因模型可适用于未见抓法。未给任务清单、机器人平台、基线名称、成功率数值及归因准确率，无法据此量化跨方法收益或判断诊断本身有多可靠。

## 局限

抓法和规划可以共同导致失败，概率分布是否准确表达这种耦合值得核查。模型给出的归因是诊断预测，不能仅凭名称认定为因果识别；仿真与真机各覆盖哪些任务、是否分别获得收益，摘要也未展开。

- **判断**：值得读到归因标签和干预实验，因为只有诊断能指导有效修正，两阶段拆分才真正减少试错。

## 研究关联

这篇提醒我们，失败数据的用途不只是继续训练整个策略。若系统存在明确的前后依赖，可以先判断哪个环节让后续问题变得困难，再把采样和优化预算投到相应环节；但前提是诊断足够可信。

### 下一步读哪里

先核查失败模式如何定义和标注，再看固定抓法只改规划、固定规划只改抓法的实验是否支持归因；随后检查未见抓法测试的划分方式及真机结果。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/Grasp-Then-Plan with Failure Attribution A Closed Two-Stage Framework for Precis.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.03385v2 Announce Type: replace-cross Abstract: In robotic manipulation, the tight coupling between grasping and motion planning often obscures the true source of failure, leading to inefficient trial-and-error. To enable efficient long-horizon manipulation, we propose GTP-FA (Grasp-Then-Plan with Failure Attribution), a task-oriented two-stage 'grasp-then-plan' framework that generates grasp candidates and performs downstream motion planning conditioned on the selected grasp. Given a failed manipulation trajectory, we learn a failure attribution model that generalizes to unseen grasps and produces a stable distribution over failure modes for diagnosis-guided optimization. Based on these attribution results, we then optimize both modules in a diagnosis-driven manner: on the grasping side, we inject task-level priors and risk penalties into grasp candidate scoring and optimization to suppress unstable or task-incompatible grasps; on the planning side, we target high-risk initial states through data collection and fine-tuning to address genuine planning bottlenecks. We evaluate the proposed framework in both simulation and real-robot experiments, and show that GTP-FA improves the corresponding base learners across RL, IL, diffusion-policy, and VLA-based settings, achieving substantially higher overall task success rates.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.03385
- Authors: Jiahao Xu, Peiyuan Wang, Hanzhuo Zhang, Zihao Yu, Tianyu Fu, Hao Chen, Xuanhao Xiang, Zixuan Li, Jianbo Yu, Chenchen Fu, Wanyuan Wang
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
