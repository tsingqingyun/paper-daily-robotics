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
url: "https://arxiv.org/abs/2610.11505v1"
published: "2026-10-08T08:42:45Z"
age_days: 2
score: 26
created: 2026-10-11
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# DAMP: Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Priors

> [!summary] 这篇论文到底做了什么（基于摘要）
> DAMP 想让人形机器人在没有环境感知信息的条件下走过复杂地形。摘要明确的机制是用循环网络积累历史，推断当前输入里看不到、但行走需要的信息，再让这些表示服务于控制目标。

## 问题

任务是复杂地形上的稳定、自然行走，限制是不能依靠环境感知。机器人身体结构允许跨越地形，却不意味着控制器知道下一步如何落脚。摘要指出这一困难，但没有具体解释已有方法怎样失效，也没有明确“无感知信息”包括哪些传感器。

### 用一个例子理解

理解用例（非论文实验）：机器人走上轻微不平地面；若策略允许读取关节与身体运动历史，循环网络据此更新隐藏状态，策略再输出下一步控制动作。这里假设的输入只是解释历史推断的作用，并非摘要确认的配置。

## 创新点或方法

从只看当前输入的控制思路出发，DAMP 把时间历史交给循环网络，让隐藏状态隐式推断特权信息及其他任务相关变量，再将表示学习对齐行走目标。训练使用强化学习，摘要称可从仿真迁移到真机；部署时历史表示参与策略控制。标题提到去噪信念学习和对抗运动先验，但摘要没有交代二者如何训练、怎样连接策略，不能补写具体损失或网络结构。

### 方法如何工作

1. 将连续时间的可用输入交给循环网络，保留当前瞬间无法表达的历史线索；具体输入未说明。
2. 由历史形成隐藏表示，隐式推断特权及任务相关信息，为控制提供额外状态判断。
3. 使表示学习与行走目标对齐，帮助策略利用这些判断选择动作；对齐方式摘要未说明。
4. 通过强化学习训练并迁移到真机运行；去噪和运动先验的具体参与方式，摘要只说明到此。

### 必要术语

- 循环网络：处理当前输入时保留过去信息的网络；本文用于形成历史相关表示。
- 特权信息：训练阶段可获得、部署时通常难以直接获取的信息；本文试图隐式推断它，具体内容未说明。
- 对抗运动先验：通常用判别器提供接近参考运动的训练信号；这是术语解释，DAMP 的具体实现需核查。

## 证据

摘要称在挑战性地形实现稳健、自然的行走，并展示仿真到现实迁移及真机演示。它没有给地形类别、机器人型号、对比方法、成功率、跌倒次数或自然性指标。因此现有材料支持作者报告了真机迁移演示，尚不足以量化鲁棒性、泛化范围或各模块的贡献；演示链接内容未在输入中提供。

## 局限

首先要核查“无感知”的准确范围，它不应被直接解释成没有任何传感器。还需确认训练时特权信息如何使用、部署时是否移除，以及所谓自然行走如何测量。摘要没有提供这些答案，也没有明确列出作者局限。

- **判断**：值得先读输入定义和训练目标，确认去噪与运动先验真正做了什么，再决定是否深入；目前摘要不足以复述完整 DAMP。

## 研究关联

可借鉴的是：当前缺少的状态信息，有时能从连续动作及其后果中推断。若可用历史确实包含接触或身体响应的线索，就值得检查它能否替代一部分环境输入；但不能由此推断机器人能提前知道尚未接触的地形。

### 下一步读哪里

我会先核查策略观测清单和特权信息清单，再查去噪目标、对抗运动先验的数据来源与作用位置；最后看真机地形、跌倒统计，以及去掉各模块的对照实验是否支持机制解释。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-11/DAMP Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Pri.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid robots possess the structural capability to traverse complex terrains. However, achieving stable t raversal without relying on perceived information remains challenging, particularly in complex environments. This paper introduces DAMP, a reinforcement learning framework aimed at achieving robust and naturalistic humanoid locomotion over challenging terrains, with the assumption that no perceived information is available. The framework leverages recurrent neural networks to capture temporal dependencies and implicitly infer privileged and other task-relevant latent information. By aligning the learned representations with the task objective, the method enables robust and goal-consistent policy learning. This end-to-end framework achieves transfer learning from simulation to real-world environments, demonstrating the proposed method's robustness and generalization capabilities. The video of the real-world demonstration can be found at the following link: https://youtu.be/AkI7TZB2DDM.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.11505v1
- Authors: Puying Shen, Wenhao Cui, Huaxing Huang, Bangyu Qin, Shengtao Li, Ziyang Dong, Guoteng Zhang
- Published: 2026-10-08T08:42:45Z
- Age days: 2

</details>
