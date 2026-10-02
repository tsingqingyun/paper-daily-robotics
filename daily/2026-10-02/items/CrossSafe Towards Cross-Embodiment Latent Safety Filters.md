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
url: "https://arxiv.org/abs/2609.28984"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-02
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CrossSafe: Towards Cross-Embodiment Latent Safety Filters

> [!summary] 这篇论文到底做了什么（基于摘要）
> CrossSafe 想让不同机器人共用一个安全过滤器，同时让它知道当前机器人的身体长什么样、能怎么动。关键是在包含身体与环境信息的潜在表示里判断危险，并共享安全价值函数和避险策略。

## 问题

任务是双臂操作中的全身避碰。同样的末端移动，对短臂可能安全，对长臂却可能让肘部撞上障碍；只在共同末端动作空间里工作的通用策略，不能充分表达这种差别。真正难点是既复用跨机器人的避险知识，又保留身体结构决定的安全边界。

### 用一个例子理解

理解用例（非论文实验）：输入是双臂机器人、桌边障碍和向前取杯的动作；过滤器结合臂长与当前姿态判断肘部风险，输出避险动作。换一台机器人，即使末端目标相同，安全输出也可能不同。

## 创新点或方法

旧做法的问题在于：末端动作相同，背后的身体运动却不同。本文把机器人形态、运动学和环境纳入潜在表示，再直接在这个空间做 Hamilton–Jacobi 可达性分析，学习共享的安全价值函数及对应避险策略。训练覆盖多种机器人；推理时依据当前机器人的条件判断并干预原策略动作。摘要未说明过滤器何时触发、如何修改动作，也未交代潜在动力学的学习方式。

### 方法如何工作

1. 把机器人与环境编码到潜在空间，使共享模型能区分不同身体对应的危险。
2. 在潜在空间分析可达性，得到用于判断安全程度的价值函数；摘要未展开求解细节。
3. 学习对应的安全策略，让危险判断能转化为避险动作，而不只是风险分数。
4. 在未参与训练的机器人上按其身体条件使用过滤器，检验共享知识能否降低碰撞。

### 必要术语

- 具身条件化：判断时把机器人的身体条件作为依据；本文用它区分同一动作对不同机器人的风险。
- 潜在表示：把原始信息编码成内部变量；本文在这个空间中进行安全分析。
- Hamilton–Jacobi 可达性：分析系统演化能否进入危险区域；本文用它构造安全价值和避险策略。

## 证据

摘要报告在五种双臂机器人、五项操作任务上测试全身碰撞约束；单一策略在其中四种机器人和五项任务上联合训练，能零样本用于留出的第五种机器人，降低原策略碰撞率。增加训练机器人种类也改善泛化。未给碰撞率数值、任务成功率、安全基线或仿真与真机划分，因此支持的是所测范围内的迁移效果，不能据此推成任意机器人的安全保证。

## 局限

我的待核查问题是：潜在表示是否会丢掉决定碰撞的细节，以及学习误差下可达性分析还保留什么保证。碰撞率下降不等于绝不碰撞，也需检查是否通过过度保守、少完成任务换来。

- **判断**：值得读到表示构造与安全过滤规则，因为跨机器人共享安全能力是否成立，取决于这两处如何保留身体约束。

## 研究关联

值得借鉴的是把“共享判断”与“身体条件”同时建模：跨机器人共享控制知识时，不能只统一动作接口，还应让安全判断看到执行动作的身体。

### 下一步读哪里

先核查形态和运动学怎样编码，再看潜在空间中的安全集合、动力学与干预规则；实验重点找留出机器人如何选择，以及碰撞率、任务成功率和干预频率是否同时报告。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/CrossSafe Towards Cross-Embodiment Latent Safety Filters.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.28984v2 Announce Type: replace Abstract: Cross-embodiment learning has shown that a single model, such as a vision-language-action (VLA) model, can learn state representations and manipulation skills that can be applied across heterogeneous robots to accomplish various tasks. We hypothesize that the same holds for safety enforcement. The reasoning required to satisfy a safety constraint, such as detecting an obstacle, recognizing that it should be avoided, and selecting a safe abstract action, is largely shared across robots. What differs across embodiments is how the abstract safe action is realized: morphology, kinematics, and dynamics determine which actions are safe and feasible. Consequently, the same action can be safe for one robot and unsafe for another. This is especially important for generalist manipulation policies that operate in a common end-effector action space without explicitly capturing how safety depends on the robot's morphology and kinematics. We propose embodiment-conditioned safety filtering, in which a Hamilton-Jacobi reachability-based value function and its corresponding safety-maximizing policy are shared across robots. Using a morphology-aware latent representation of the robot and its environment, we perform Hamilton-Jacobi reachability analysis directly in latent space so that the learned safety concepts can generalize across embodiments while remaining explicitly conditioned on each robot's morphology and kinematics. We evaluate our approach across five bimanual robot embodiments and five manipulation tasks with whole-body collision-avoidance constraints. Our results show that a single policy, jointly trained across five manipulation tasks and four embodiments, exhibits zero-shot generalization to a held-out embodiment, reducing the nominal policy's collision rate. They also show that training using more embodiments improves generalization.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.28984
- Authors: Ihab Tabbara, Yuxuan Yang, Hussein Sibai
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
