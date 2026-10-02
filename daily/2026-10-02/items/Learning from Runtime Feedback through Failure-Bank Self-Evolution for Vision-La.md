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
url: "https://arxiv.org/abs/2609.39820"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 37
created: 2026-10-02
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> FailBank 把运行时发现的动作问题收集起来，筛选后用于更新 VLA，让策略逐渐减少需要纠正的行为。关键是纠错建议不全部照收，还保留原本成功的动作，避免改好接触问题却破坏任务能力。

## 问题

机器人既要完成操作，又要减少非预期接触。运行时安全模块可以临时改动作，但策略本身不变；它下一次仍可能提议相同动作，与安全模块反复冲突，导致任务迟迟无法推进。

### 用一个例子理解

理解用例（非论文实验）：输入是机械臂取杯时的画面和动作；旁观模块发现路径可能碰到旁边的瓶子，记录绕行建议。系统结合本次执行结果决定是否采用建议，并保留成功抓杯动作，更新后输出更合适的取杯动作。

## 创新点或方法

旧做法是在执行时拦截动作；FailBank 将反馈转为后续训练监督。收集阶段，固定的 CBF 模块只旁观，提出“若由我纠正会怎样”的建议，实际仍由原策略控制。随后结合执行结果筛选建议，生成纠正目标，并将成功且未被纠正的动作保留为稳定参照，通过带保护措施的 LoRA 更新策略。更新后的推理使用已改变的策略；是否还同时启用安全模块，摘要未说明。四阶段的完整划分也未展开。

### 方法如何工作

1. 让策略执行任务，同时让固定教师记录纠正建议，获得策略与教师分歧的位置。
2. 结合执行结果筛选建议，形成纠正目标，避免把所有分歧直接当作错误。
3. 保留成功且未纠正的动作，给更新提供维持原有能力的参照。
4. 通过受保护的 LoRA 更新吸收这些监督；具体保护条件摘要只说明到此。

### 必要术语

- 运行时防护：执行期间检查并修改动作；本文将其与学习后的策略比较。
- CBF：控制障碍函数，用约束描述动作是否越过安全边界；本文据此生成纠正建议。
- 反事实纠正：没有实际执行的替代动作建议；本文筛选它们作为监督。
- LoRA：只训练少量附加参数来调整模型；本文用于吸收运行反馈。

## 证据

摘要报告在 VLA-Arena 的两个难度、两种 VLA 骨干上评估。相对基础策略，两种骨干的成功率分别增加8.5、6.9个百分点，策略引起的累计代价分别下降35.6%、23.8%。相对运行时防护，成功率分别增加25.4、9.5个百分点，同时保持相近累计代价。这支持在该基准上改善成功与代价的折中；摘要未给代价公式、绝对成功率、重复次数，也未报告真机结果。

## 局限

需要核查结果筛选如何判断一条反事实建议值得学习：实际执行的是原动作，建议动作的效果并不会自动被观测到。累计代价下降也不能直接解释为每次执行都有安全保证，尤其收集时教师并不接管动作。

- **判断**：值得深入读样本准入和更新保护规则；它们决定 FailBank 是可靠地积累改进，还是把未经验证的纠错固化进策略。

## 研究关联

有用的启示是把外部纠错当成需要验证的训练建议，而非天然正确的标签。当纠错会阻碍任务推进时，应同时学习“哪里要改”和“哪些成功行为要保留”。

### 下一步读哪里

优先核查纠正建议的准入条件、成功参照样本的权重，以及“带保护”的更新如何决定接受或回退。还应查看代价定义、测试时是否有防护，以及连续多轮更新是否稳定。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-La.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.39820v1 Announce Type: new Abstract: Vision-language-action (VLA) models generalize broadly across robotic manipulation tasks, but complex environments require balancing task success with unintended contact. Runtime shields can correct individual actions, but they leave the underlying policy unchanged, so repeated disagreements may create a persistent policy-shield mismatch that blocks task progress. To address this challenge, we introduce FailBank, a four-stage self-evolving framework that converts runtime feedback into persistent policy improvement. During collection, a fixed CBF-based safety module serves as an observe-only teacher, producing counterfactual corrections while the policy remains in control. Outcome-aware admission then converts useful proposals into corrective targets and retains successful uncorrected actions as quiet anchors for guarded LoRA updates. We evaluate FailBank on the VLA-Arena benchmark across two difficulty levels and two VLA backbones. Compared with the base policies, FailBank improves the joint success-cost operating point. Across the two backbones, FailBank improves task success rate by 8.5 and 6.9 percentage points, while reducing policy-induced cumulative cost by 35.6\% and 23.8\%, respectively. Compared with runtime shielding, FailBank raises task success rate by 25.4 and 9.5 percentage points, while maintaining comparable policy-induced cumulative cost. These results show that runtime feedback can serve as persistent policy supervision rather than only as a temporary action constraint.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.39820
- Authors: Mingyue Cui, Zheyuan Liu, Yihan Zhu, Zheyuan Zhang, Meng Jiang
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
