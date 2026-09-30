---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.36851v1"
published: "2026-09-29T06:59:50Z"
age_days: 0
score: 34
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts

> [!summary] 先说人话（基于摘要）
> RoXDrive 用视频世界模型训练驾驶策略，但先筛掉那些画面没有忠实响应车辆动作的模拟轨迹。它通过逆动力学评估动作与视觉是否一致，再用可信轨迹做闭环强化学习。

## 问题

模仿学习策略未经历自身动作后果，闭环部署容易出现因果混淆。重建式模拟器的反事实交互有限，合成模拟器存在现实差距，而视频世界模型虽能生成逼真未来，却可能不遵循输入动作。

## 创新点或方法

预训练策略的同时，结合几何感知的辅助轨迹监督训练 Action-Vision Faithfulness Evaluator，以逆动力学估计检查长轨迹的动作忠实性。后训练时保留通过评估的世界模型轨迹，进行密集安全评分和场景级闭环 RL。

## 证据

在 nuScenes 和包含超过 13 万训练场景的内部数据集上获得跨规划器收益。DiffusionDrive 在 nuScenes 的安全违规减少 27.6%，Qwen3-VL 在内部数据上的安全违规减少 33.7%。

## 局限

需核查忠实性评估器如何验证、筛选是否改变场景分布，以及安全违规的定义；摘要没有报告真实道路部署结果。

- **判断**：世界模型用于策略后训练的研究者值得精读，重点评估逆动力学筛选能否真正识别错误的动作后果。

## 研究关联

对世界模型与机器人 RL，核心价值是把动作条件可信度变成训练数据筛选条件，避免策略从不响应动作的模拟中学习错误因果关系。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/RoXDrive Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving vi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

End-to-end autonomous driving policies are commonly trained via imitation learning on logged demonstrations without observing the consequences of their own actions, leading to causal confusion in closed-loop real-world deployment. To address this issue, reinforcement learning (RL) post-training offers a promising alternative by leveraging world models as interactive training environments to enable future scene generation for policy improvement. Nevertheless, existing approaches either rely on reconstruction-based simulators, offering limited counterfactual interaction, or adopt synthetic simulators to enable long-horizon closed-loop interaction at the cost of a substantial sim-to-real gap. Recently, video world models have exhibited the ability to generate realistic multi-step future rollouts but may not faithfully reflect action conditions, resulting in action-vision mismatch. In this paper, we introduce RoXDrive, a plug-and-play closed-loop RL framework that enables reliable policy optimization by identifying action-faithful world-model rollouts, consisting of two stages: 1) Model pre-training: In addition to imitation-based policy pre-training, we devise an Action-Vision Faithfulness Evaluator for inverse dynamics estimation with our geometry-aware auxiliary trajectory supervision, enabling long-horizon assessment of whether visual dynamics faithfully reflect the conditioning ego actions. 2) Action-faithful RL post-training: Agents iteratively interact with world models to form long-horizon scene rollouts, retaining only action-faithful ones for dense safety-aware scoring and scene-level closed-loop RL post-training. Extensive experiments on nuScenes and an in-house dataset with over 130K training scenarios demonstrate consistent gains across planners, reducing safety violations by 27.6% with DiffusionDrive on nuScenes and 33.7% with Qwen3-VL on the internal data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.36851v1
- Authors: Hongbin Lin, Chaoda Zheng, Yiming Yang, Xiangyu Li, Shijia Chen, Jinhao Deng, Kangjie Chen, Dongbin Zhang, Jie Feng, Yu Zhang, Xianming Liu, Shuguang Cui, Boyang Wang, Zhen Li
- Published: 2026-09-29T06:59:50Z
- Age days: 0

</details>
