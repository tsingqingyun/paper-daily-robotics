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
url: "https://arxiv.org/abs/2610.08133v1"
published: "2026-10-06T10:47:43Z"
age_days: 0
score: 36
created: 2026-10-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> VLA-ACL 学一个小型选择器，让 VLA 每次只看部分视觉 token，从而减少计算。它判断哪些信息能删的依据是：删完之后，机器人预测的动作还能不能接近完整画面下的动作。

## 问题

VLA 每个控制步都要处理长序列，视觉图像块占了大量输入，拖慢实时执行。已有剪枝方法用注意力分数、运动阈值等间接线索判断重要性，未必对应控制需要；另一条路线微调整个 VLA，训练成本又高。瓶颈是便宜地找到可以删除、又不会破坏动作的信息。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放到托盘上”和相机画面；选择器保留足够支持该动作的图像块，VLA 用缩短后的序列输出抓取与放置动作。背景墙可能被删，但具体保留区域由学习决定，不能预先认定只留下杯子。

## 创新点或方法

旧做法凭视觉启发式删 token；VLA-ACL 冻结基础 VLA，只训练轻量视觉选择策略。训练时，完整视觉上下文产生教师动作，剪枝上下文产生另一组动作，目标是让两者一致，并以真实动作作为辅助监督。因此选择器学的是信息删除对控制输出的影响。推理时使用学到的选择策略和保留的 token。选择器结构、离散选择如何训练，以及一致性损失怎样定义，摘要未说明。

### 方法如何工作

1. 用冻结 VLA 处理完整画面，得到教师动作，作为保留控制行为的参照。
2. 由轻量策略选择视觉 token，再交给同一冻结 VLA，得到剪枝后的动作。
3. 比较两种动作并加入真实动作辅助监督，训练选择器识别哪些删除会损害控制。
4. 推理时按学到的策略缩短视觉输入，减少基础 VLA 处理的序列长度。

### 必要术语

- 视觉 token：图像分块后形成的模型输入单元；本文主要删减对象。
- 动作一致性：完整输入与删减输入产生的动作尽量接近；本文用它监督选择器。
- 冻结模型：训练中保持基础模型参数不变；本文把学习成本集中在轻量剪枝策略上。

## 证据

摘要报告在 LIBERO 仿真基准及真机操作任务上，最多删除 87.5% 的视觉 token，计算量最多减少 75%，推理加速 1.5 倍，同时保持有竞争力的任务表现。作者称其效果与效率取舍优于已有冻结 VLA 的剪枝方法，但摘要未给出基线名称、成功率、硬件和分任务结果。几个最大收益也不能默认来自同一配置；现有信息支持可行性，不能精确判断在哪种部署条件下最划算。

## 局限

动作接近教师，只能说明保住了教师当时的行为，教师原有错误仍可能被保留；真实动作辅助监督如何缓解这一点需要核查。还应检查细小目标、遮挡和长任务上的剪枝表现，以及选择器自身开销是否计入加速。摘要没有给出这些细分结果，不能推断全文未测。

- **判断**：值得读到训练目标和实际延迟测量，因为动作监督的思路清楚，而部署收益取决于剪枝成本和成功率损失。

## 研究关联

最可借鉴的是用最终动作来监督中间信息选择。一个图像块视觉上显眼，并不代表它影响抓取；反过来，小物体也可能决定动作。若想给已有控制模型减负，可以先尝试学习选择输入，避免把全部成本放在重训基础模型上。

### 下一步读哪里

核查教师与真实动作两项监督的权重、剪枝比例如何控制，以及完整模型、启发式剪枝和 VLA-ACL 在同一硬件上的成功率与端到端延迟。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-07/VLA-ACL Action-Consistent Visual Token Pruning for Efficient Vision-Language-Act.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models achieve strong robotic manipulation performance but incur high computational costs from processing long token sequences at every control step, limiting real-time deployment. Visual token pruning offers a direct solution, as visual patches dominate the input sequence and contain considerable redundancy. Existing approaches, however, either rely on indirect training-free heuristics, such as attention scores and motion thresholds, or require costly fine-tuning of the base VLA model. We introduce VLA-ACL (Action Consistency Learning), which learns a lightweight visual token pruning policy through action-level supervision while keeping the base VLA model entirely frozen. The training objective encourages actions produced from pruned visual contexts to remain consistent with the full-context teacher, with ground-truth actions as auxiliary supervision. This directly ties token selection to its effect on the downstream control output. Experiments on LIBERO and real-world manipulation tasks show that VLA-ACL prunes up to 87.5% of visual tokens while retaining competitive performance, reduces computation by up to 75%, and achieves a 1.5x inference speedup. These results establish a stronger performance-efficiency trade-off than existing frozen-VLA pruning methods and demonstrate the value of action-level supervision for visual token selection. Code is available at https://github.com/du-owen/VLA-ACL.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.08133v1
- Authors: Owen Du, Yang Yue, Jie Zhang, Jiaqi Pi, Chi Bene Chen, Gao Huang
- Published: 2026-10-06T10:47:43Z
- Age days: 0

</details>
