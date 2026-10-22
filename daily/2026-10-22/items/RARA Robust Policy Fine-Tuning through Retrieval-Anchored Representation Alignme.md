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
url: "https://arxiv.org/abs/2610.13578"
published: "Wed, 21 Oct 2026 00:00:00 -0400"
age_days: 0
score: 42
created: 2026-10-22
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> RARA 要解决的是：机器人用少量新示范学会任务时，别把预训练时学到的本领改坏。它先找相近旧示范来对齐内部表征，再在学习新动作时限制这些旧示范的表征变化。

## 问题

任务是给预训练机器人策略做少样本适配。直接微调可能在熟悉条件下表现不错，却改变原有表征，使模型遇到分布外变化时更容易失败。瓶颈因此不只是新动作学得够不够，而是新学习是否破坏了已有知识的组织方式。

### 用一个例子理解

理解用例（非论文实验）：输入几段“把杯子放上架子”的新示范，RARA 找到意图和运动相近的旧示范，先对齐表征，再约束微调。输出是适配后的策略，供机器人根据当前观测生成放杯动作。

## 创新点或方法

旧做法直接用目标示范更新策略；RARA 在动作学习前增加对齐，并在动作学习中增加保留约束。第一阶段检索任务意图与运动相近的预训练示范，让目标示范的表征向检索示范的预训练表征对齐；第二阶段在目标示范上微调，同时限制检索示范的表征漂移。前者减少适配起点的错位，后者限制后续改动。摘要将检索用于适配，未说明执行时是否还需检索。

### 方法如何工作

1. 读取目标示范，检索意图和运动相近的旧示范，为适配找到有关联的参照。
2. 对齐目标表征与旧示范的预训练表征，减少动作学习开始前的表征错位。
3. 用目标示范学习动作，同时约束旧示范表征的变化，限制不必要的知识漂移。
4. 用适配后的策略执行任务；推理时是否保留检索组件，摘要未说明。

### 必要术语

- 表征：模型内部编码的信息；RARA 直接约束它在适配中如何变化。
- 检索锚点：选出的相关旧示范及其表征；为对齐和保留提供参照。
- 分布外：测试条件偏离适配数据；用于检查新学习之后能否应对变化。

## 证据

据摘要，实验使用 Diffusion Policy 和 GR00T，覆盖 RoboTwin、RoboCasa 及真实机器人，共 13 个任务。相对微调，分布内平均成功率提高 9.5 个百分点，分布外提高 13.6 个百分点，并超过所有参与比较的基线。输入未列基线名称、绝对成功率、任务分项及误差范围，因此能支持所测设置下的平均收益，不能推出每个任务都同幅改善。

## 局限

摘要同时包含仿真和真机结果，但没有分开报数。我的待核查问题是收益有多少来自两阶段设计、有多少来自额外旧数据，以及检索不准或找不到相近动作时是否仍有效；现有输入不足以判断这些边界。

- **判断**：值得优先读方法和消融，因为两阶段各自解决什么问题很清楚，而实用性主要取决于检索条件及额外成本。

## 研究关联

值得借鉴的是把“保留旧知识”变成局部约束：挑与新任务有关的旧经验作为参照，再限制它们如何变化。若能访问预训练示范及对应表征，这比笼统要求模型少遗忘更容易落实到训练目标。

### 下一步读哪里

核查相似性怎样计算、对齐哪些层、两阶段分别更新哪些参数；再看单阶段消融、分布外变化类型、真机分项和预训练数据访问要求。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-22/RARA Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignme.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.13578v2 Announce Type: replace-cross Abstract: Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging. Directly fine-tuning a pre-trained policy often achieves strong in-distribution performance, yet it can distort the representations learned during pre-training and weaken the model's generalization ability under out-of-distribution shifts. We propose Retrieval-Anchored Representation Alignment (RARA), a two-stage adaptation method, to address this issue. First, RARA retrieves representation features from pretraining with similar task intent and motion, and aligns the policy's representations of the target demonstrations with the pre-trained representations of the retrieved demonstrations. Second, RARA fine-tunes the policy on the target demonstrations while limiting how much its representations of the retrieved demonstrations change during fine-tuning. By reducing the representation mismatch before action learning and preserving pre-trained knowledge during adaptation, RARA limits unnecessary representation drift during fine-tuning. Experiments with Diffusion Policy and GR00T on 13 tasks in RoboTwin, RoboCasa, and on a real robot show that RARA improves the average success of fine-tuning by 9.5 points in-distribution and 13.6 points out-of-distribution, and outperforms all compared baselines. Project page: https://shua-kang.github.io/RARA_robot/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.13578
- Authors: Xuhui Kang, Sung-Wook Lee, Yan Zhuang, Tianle Zhong, Yen-Ling Kuo
- Published: Wed, 21 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
