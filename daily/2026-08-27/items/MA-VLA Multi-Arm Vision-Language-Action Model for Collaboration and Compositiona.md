---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.25864v1"
published: "2026-08-26T14:38:04Z"
age_days: 0
score: 43
created: 2026-08-27
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Compositional Generalization

> [!summary] 先说人话（基于摘要）
> MA-VLA 用“原子动作分配”把协作任务拆成中层子目标并分别交给各机械臂；Arm Shuffle 在训练时置换各臂的观测、状态和提示，迫使策略学会与角色无关的组合执行。

## 问题

多数VLA只接收一条全局指令，没有显式描述每条手臂该做什么，因此容易记住固定角色和训练中的协作模板，面对未见过的分工组合时难以迁移。

## 创新点或方法

框架将协作行为分解为可复用的原子提示，并为每条手臂分配子目标；训练时同步置换每臂的观测、状态和原子提示，使策略依据分配内容而非臂的固定身份行动。输出是多臂协同动作。

## 证据

作者构建了测试协作模式不出现在训练集中的基准；摘要称在仿真和真实评测中，既有先进VLA大多失败，而MA-VLA持续成功，但未给出可核查的结果数字。


## 局限

原子提示由谁生成、粒度如何选择及错误分解会怎样传播，摘要均未说明；“持续成功”也缺少数字支撑。

- **判断**：值得读方法与新基准设计，尤其适合研究多臂组合泛化的人；性能结论应等全文数据后再定。

## 研究关联

它把多臂VLA的泛化问题改写为任务分解与行为重组问题，对双臂、人形机器人及多智能体式操作都有实际价值。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/MA-VLA Multi-Arm Vision-Language-Action Model for Collaboration and Compositiona.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multi-arm collaboration is becoming a core capability in embodied manipulation. Recent vision-language-action (VLA) models integrate perception, language, and control, but most represent language as a single global instruction and do not provide an explicit mechanism for assigning and composing arm-specific behaviors. This design limits transfer to collaboration patterns that differ from those observed during training. We present MA-VLA, a unified framework for multi-arm collaboration via atomic action assignment. MA-VLA decomposes cooperative behavior into mid-level atomic prompts and allocates them to individual arms, enabling explicit subgoal specification and compositional reuse across tasks. To reduce reliance on fixed execution roles, we introduce Arm Shuffle, a training-time permutation of the observation, state, and assigned atomic prompts for each arm. This permutation enforces role-agnostic instruction following and supports recomposition into unseen coordination patterns, which we term multi-arm compositional generalization. We also construct a benchmark in which test-time collaboration patterns are absent in training set. Across simulation and real-world evaluations, prior state-of-the-art VLAs largely fail under these unseen collaborations, while MA-VLA consistently succeeds. These results indicate that structured, per-arm atomic action assignment offers a practical route to scalable generalization in multi-arm embodied systems. Code, models, and data are available at https://github.com/zhangzaibin/future-robots

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.25864v1
- Authors: Zaibin Zhang, Junlan Xiao, Zhongbo Zhang, Yifan Wang, Li Kang, Yiran Qin, Changxing Xia, Heng Zhou, Talas Fu, Enshen Zhou, Ruimao Zhang, Zhenfei Yin, Huchuan Lu, Lijun Wang
- Published: 2026-08-26T14:38:04Z
- Age days: 0

</details>
