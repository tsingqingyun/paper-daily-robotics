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
url: "https://arxiv.org/abs/2610.31845v1"
published: "2026-10-22T19:28:43Z"
age_days: 4
score: 29
created: 2026-10-27
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions

> [!summary] 这篇论文到底做了什么（基于摘要）
> EgoForesight 想利用大量第一视角视频训练机器人，同时避免从视频重建出的错误动作标签拖累学习。它按来源可靠度调整动作监督，并让能看到真实未来画面的教师，把“动作最终改变了什么”教给学生。

## 问题

机器人示范的动作轨迹可靠，但采集昂贵；人的第一视角视频覆盖更广，却需要运动重建和动作重定向，因而带入噪声。瓶颈是数据量增加时，动作标签的可信度并不一起提高，直接混合监督会让模型学习不可靠的动作目标。

### 用一个例子理解

理解用例（非论文实验）：输入一段人打开抽屉的视频、估计动作和来源可靠度；训练降低对不可靠动作的依赖，同时让教师从打开后的画面提取变化信息；输出学到动作与结果联系的策略。部署时输入当前观测和任务，生成机器人动作，不提供真实未来画面。

## 创新点或方法

EgoForesight 一方面按来源可靠度分配动作监督的噪声水平，并对回归项加权；另一方面联合学习未来视觉表示和动作。训练时，指数移动平均教师看到当前场景及干净未来，其深层表示监督接收受扰未来的学生较早层，让结果画面补充动作标签。推理不能依赖真实未来；摘要未说明此时未来表示的初始化和生成顺序，不能据此补出完整执行流程。

### 方法如何工作

1. 混合机器人示范与第一视角数据，保留来源可靠度信息，以区分动作监督的可信程度。
2. 依据可靠度设置动作扰动和回归权重，调节不同来源对动作学习的影响。
3. 联合学习未来视觉表示预测与动作生成，让训练同时接触动作目标和结果信息。
4. 让看到干净未来的教师监督接收受扰未来的学生，把场景变化中的动作相关结构传过去；推理细节摘要只说明到此。

### 必要术语

- 动作重定向：把人的运动转换成机器人可执行的动作标签；它是本文处理的噪声来源之一。
- 联合视觉—动作流：耦合未来视觉表示预测与动作生成的学习机制；具体计算形式需读方法。
- 特权未来蒸馏：训练时让教师使用真实未来，再把表示传给学生；本文用它补充动作监督。
- 开环 MSE：不执行反馈修正时比较预测动作与目标动作的均方误差；它不能直接代表任务完成率。

## 证据

摘要称，在测试的数据规模范围内，其扩展曲线比基线更陡；使用 30,000 小时预训练数据时，真实世界开环动作 MSE 降低 20.5%，RoboCasa 少样本成功率提高 8.1 个百分点（摘要）。基线名称、绝对值和误差范围未给出。摘要另称后训练后在仿真和真机灵巧操作中表现强，但未给数字。开环误差与闭环成功率是不同证据，不能相互替代。

## 局限

我的待核查问题是来源可靠度如何确定，以及未来画面中的无关变化会不会被教师学进去。摘要没有给出各机制的独立贡献；不能据此断言全文缺少消融。更陡的扩展曲线也只在已测试范围成立。

- **判断**：值得深入读训练目标和消融，因为它直接处理扩大数据时监督质量下降的问题；是否值得复现，取决于可靠度设定和未来蒸馏的实现成本。

## 研究关联

这里值得借鉴的是把两种监督分开看待：动作标签可能错，结果画面仍可能说明任务发生了什么变化。当动作重建质量有限、结果画面又足够清晰时，可以考虑让结果信息补充动作学习。

### 下一步读哪里

先查可靠度条件如何对应噪声水平、回归权重怎样设置，再看教师与学生的层间监督及防止未来信息泄漏的方式。实验重点核查同数据量比较、两类监督的消融，以及闭环真机成功率。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-27/EgoForesight Effectively Scaling Policy Learning with Noisy Egocentric Actions.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Scaling policy learning requires broad experience and reliable supervision. Robot demonstrations provide high-quality trajectory supervision but are costly to collect. Egocentric videos broaden task and environment coverage, yet motion reconstruction and retargeting introduce noisy action labels. To address this challenge, we introduce EgoForesight, a vision-language-action framework that learns jointly from both sources by reducing the influence of unreliable action labels and exploiting demonstrated outcomes as complementary supervision. A joint vision-action flow couples future visual representation prediction with action generation, unifying reliability-aware action learning with outcome-informed representation transfer. Specifically, reliability-conditioned corruption allocates action supervision across noise levels according to source reliability, while reliability-weighted regression regulates each source's contribution. Complementing this treatment of noisy labels, privileged-future representation distillation draws supervision from demonstrated outcomes. An exponential-moving-average teacher observes the current scene and clean future to encode action-relevant structure from the resulting scene change. Its deeper representations supervise an earlier student layer receiving a corrupted future, providing outcome-informed structure beyond noisy action annotations. Together, these mechanisms support effective scaling with noisy egocentric actions. Over the tested range, EgoForesight exhibits steeper scaling slopes than the baseline, reducing real-world open-loop action MSE by 20.5% and improving RoboCasa few-shot success by 8.1 percentage points at 30,000 hours of pretraining data. After post-training, it also achieves strong absolute performance in both simulated and real-world dexterous manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.31845v1
- Authors: Chubin Zhang, Changyuan Wang, Yirui Wang, Ao Li, Shilin Ma, Yue Su, Cai Zhou, Xiuwei Xu, Tianle Zhang, Yansong Tang
- Published: 2026-10-22T19:28:43Z
- Age days: 4

</details>
