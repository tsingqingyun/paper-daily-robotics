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
url: "https://arxiv.org/abs/2611.08407v1"
published: "2026-11-05T18:14:06Z"
age_days: 1
score: 30
created: 2026-11-07
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Social Humanoid: Socially Responsive Human-Humanoid Interaction

> [!summary] 这篇论文到底做了什么（基于摘要）
> Social Humanoid让人形机器人根据人的动作生成配合动作，再由底层控制器执行。关键不只是学动作序列，还包括把双人动作数据改造成符合人机体型、可达范围和接触关系的训练数据。

## 问题

任务是人与人形机器人的全身互动：机器人需要随伙伴动作调整自身，而不是独自完成预设动作。独立训练的策略缺少这种相互配合经验；直接套用双人动作也会遇到人体与机器人比例、关节和触及范围不同的问题。

### 用一个例子理解

理解用例（非论文实验）：输入伙伴伸手准备击掌的动作，高层生成机器人抬臂迎合的动作序列；短暂遮挡时估计伙伴后续运动，底层输出关节控制，使机器人执行该序列。

## 创新点或方法

旧做法把机器人当单独行动者；本文用分层系统连接互动动作生成与物理执行。训练数据先经过两阶段自适应重定向：一方转换为机器人动作，同时调整另一方的身体形态，尽量保留接触、可达性与相对尺度。高层用共享的离散表示学习人与机器人动作序列；执行时根据人类动作生成反应，遮挡时预测伙伴运动，底层跟踪控制器把生成动作落到机器人上。

### 方法如何工作

1. 读取双人动作捕捉数据，将其中一方转换到机器人身体，使动作符合机器人结构。
2. 同时调整另一方的身体形态，尽量保住原互动中的接触位置和双方可达关系。
3. 用共享离散表示学习双方动作序列，让高层根据伙伴动作生成反应，并在遮挡时预测其运动。
4. 由底层全身跟踪控制器执行生成序列，将动作预测转为真实机器人运动。

### 必要术语

- 动作重定向：把一种身体的动作转换到另一种身体；本文还需保留双方互动关系。
- 共享离散表示：把人与机器人的动作编码成共同使用的离散单元；供高层建模序列。
- 全身跟踪控制器：驱动多个关节跟随目标动作的控制器；负责执行高层输出。

## 证据

摘要报告将五个动作捕捉数据集处理为260小时的HHI人机互动基准，并在29自由度Unitree G1上实现系统，展示仿真和真机中的多类协调互动。没有给互动任务名称、对比基线、协调指标、成功率或消融结果。数据时长说明训练资源规模，但不能单独证明动作协调质量或遮挡预测准确性。

## 局限

我的待核查问题是：调整伙伴身体形态后的数据，与真实人体动作之间有多大差异；遮挡预测错误时，底层控制器怎样处理不合适的目标。摘要报告了真机展示，但不足以判断面对未见伙伴和突发动作的稳定性。

- **判断**：值得重点读双人动作重定向，再看高层预测；数据是否保住接触关系，是理解这篇方法有效范围的关键。

## 研究关联

这里值得借鉴的是把互动关系作为数据转换的约束。迁移动作时，如果只让机器人单独摆出相似姿态，原本双方能接触的位置可能已经错开；同时调整双方关系，才有机会保留配合所依赖的条件。

### 下一步读哪里

下一步检查两阶段重定向各自优化什么、接触约束如何表达，以及共享动作表示怎样适配不同身体。实验上应核查未见互动、遮挡长度、预测误差和真机跟踪误差；摘要未提供这些细节。

- **概念**：智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/Social Humanoid Socially Responsive Human-Humanoid Interaction.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid robots are typically trained as solitary agents, leaving them unable to coordinate physically with human partners who naturally anticipate and adjust to one another. To bridge this gap, we present Social Humanoid, a hierarchical system that generates and executes socially responsive whole-body motion on a 29-DoF Unitree G1 conditioned on a human partner's motion. Its high-level policy performs flexible sequence modeling of human and humanoid motion through a shared tokenized representation, generating reactive humanoid motion and anticipating the partner's motion when they are occluded, while a low-level whole-body tracking controller executes the generated motion on the robot. To train the system, we introduce a two-phase adaptive retargeting procedure that retargets one interaction partner to the robot while morphing the other partner to preserve contact dynamics, reachability, and relative body scale. We apply this procedure across five motion-capture datasets to produce a new Human-Humanoid Interaction (HHI) benchmark of 260 hours of human-humanoid interactions. Our results demonstrate that Social Humanoid produces coordinated, human-aligned behavior across diverse interaction types in simulation and the real world. Project page: https://von31.github.io/social-humanoid/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08407v1
- Authors: Vongani H. Maluleke, James Ni, Kie Horiuchi, Lea Wilken, Jiahui Lei, Evonne Ng, Roei Herzig, Jitendra Malik, Trevor Darrell, Angjoo Kanazawa
- Published: 2026-11-05T18:14:06Z
- Age days: 1

</details>
