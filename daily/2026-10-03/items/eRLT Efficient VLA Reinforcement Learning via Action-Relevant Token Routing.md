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
url: "https://arxiv.org/abs/2610.00913"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-10-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# eRLT: Efficient VLA Reinforcement Learning via Action-Relevant Token Routing

> [!summary] 这篇论文到底做了什么（基于摘要）
> eRLT 冻结已有 VLA，让一个小模块从不同层、不同 token 中挑出当前任务最需要的信息，再交给强化学习模块。这个选择器先学习专家动作相关特征，再根据在线交互的价值反馈继续调整。

## 问题

任务是用在线强化学习适配机器人操作能力。瓶颈在于 actor 和 critic 看到了什么状态信息：独立视觉编码器可能没有利用 VLA 已学到的知识，固定压缩内部特征又不会针对任务选择动作相关内容。这会使动作改进和价值估计需要更多交互。

### 用一个例子理解

理解用例（非论文实验）：输入插头附近的图像和插入指令；路由模块从冻结 VLA 中汇集与接近、对齐有关的特征，合成 RL token；强化学习模块据此选择调整动作，交互反馈再帮助更新信息选择方式。

## 创新点或方法

旧做法使用外部编码器或固定压缩，eRLT 改为学习如何取信息。路由 token 在 VLA 多个深度汇集视觉语言特征，层路由器再把这些摘要合成固定维度的 RL token。训练时先用专家示范初始化，使表示包含能预测专家动作的信息，再用在线 critic 反馈调整它，使表示服务于价值估计；VLA 保持冻结。使用时 RL 模块读取该表示进行动作决策，具体如何修正基础 VLA 动作，摘要未说明。

### 方法如何工作

1. 让冻结 VLA 处理观察和指令，得到多个层的视觉语言特征，保留已有行为知识。
2. 用学习到的路由 token 汇集各层内容，再组合成固定维度表示，供强化学习模块使用。
3. 用专家示范初始化路由模块，使表示先包含与专家动作相关的信息。
4. 在线交互后用 critic 反馈细化路由，使后续表示更有利于估计动作价值和改进行为。

### 必要术语

- Token：模型内部的信息单元；本文从这些单元中汇集任务相关内容。
- Actor／critic：分别负责选动作和估计动作价值的模块；它们使用路由后的状态表示。
- 学习曲线 AUC：整个学习过程表现曲线下的面积；本文用它衡量学习期间的总体表现。

## 证据

摘要报告，在 LIBERO 和 RoboTwin 的七个任务上，相比代表性基线，平均归一化学习曲线 AUC 的提升最高为 23.7%。真机 USB 接头插入和主板排线插入，相比最强基线的 AUC 分别提升 108.9% 和 46.7%。这些是学习曲线面积的相对提升，不能读成成功率增加相同百分点；摘要未提供基线名称、交互预算和误差范围。

## 局限

摘要没有明确列出局限。我会核查专家示范数量、路由模块计算开销，以及比较是否使用相同数据预算。两项真机结果支持精细插入任务中的适用性，尚不能推出所有操作任务都能获得同样幅度的收益。

- **判断**：值得细读表示构造与预算对齐实验，因为它给出了具体、可检验的样本效率改进路径。

## 研究关联

可借鉴之处是，把“冻结模型后怎样适配”中的状态表示也当成可学习对象。专家动作提供初始筛选标准，在线价值反馈再纠正筛选方向，适合尝试于基础模型已有能力、但下游学习仍耗费大量交互的情形。

### 下一步读哪里

下一步检查专家初始化的监督目标、critic 梯度如何更新路由器，以及只选 token、只选层、固定压缩之间的对比；核查 AUC 的归一化方式和所有方法的交互预算。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/eRLT Efficient VLA Reinforcement Learning via Action-Relevant Token Routing.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.00913v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models provide strong behavioral priors for robotic manipulation, yet efficiently adapting them to downstream tasks remains challenging. Recent work addresses this challenge by adapting frozen VLAs through online reinforcement learning (RL), whose sample efficiency depends on the quality of the state representation used by the actor and critic. Existing methods construct such representations either with VLA-independent visual encoders or through fixed compression of internal VLA representations. Neither design explicitly extracts the task-specific action-relevant VLA features most useful for downstream action refinement and action-value estimation, therefore limiting sample efficiency. To address this limitation, we introduce eRLT, which constructs an effective state representation by routing task-specific action-relevant information across both tokens and layers of the frozen VLA. Specifically, learned routing tokens dynamically aggregate visual-language features at multiple depths, while a lightweight layer router combines these summaries into a fixed-dimensional RL token. The routing module is initialized using expert demonstrations to capture features predictive of expert actions and then refined using critic feedback from online interactions for action-value estimation. Across seven LIBERO and RoboTwin tasks, eRLT improves mean normalized learning-curve AUC by up to 23.7% over representative baselines. Real-robot experiments on USB connector insertion and motherboard ribbon-cable insertion further show AUC improvements of 108.9% and 46.7%, respectively, over the strongest baseline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.00913
- Authors: Dehao Huang, Jianbang Liu, Jianpan Gao, Chao Tang, Zilang Cen, Zedong Dan, Jiaheng Wang, Tingguang Li, Yue Wang, Hong Zhang
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
