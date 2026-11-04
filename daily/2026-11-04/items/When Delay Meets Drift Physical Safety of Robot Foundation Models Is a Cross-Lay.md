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
url: "https://arxiv.org/abs/2611.02101"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 36
created: 2026-11-04
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem

> [!summary] 这篇论文到底做了什么（基于摘要）
> Delay Meets Drift 说明，相机视角变化与推理延迟同时出现时，安全风险可能远超过分别测试两者所得的预期。论文用跨层变化传播来描述这种现象，并用交互对比量化额外风险。

## 问题

任务是评估机器人基础模型在闭环执行中的物理安全。摘要指出，鲁棒性测试通常改变场景却假设推理即时完成，实时执行研究则常在正常场景里研究延迟；这两种分开测试的方法无法识别环境变化与计算延迟相互放大的危险。

### 用一个例子理解

理解用例（非论文实验）：输入偏转视角下的桌面画面与“将杯子放到托盘”；策略耗时后输出动作，执行时场景已经继续变化。将这次闭环结果与仅偏转、仅延迟和两者都无的条件比较，就能估计联合风险是否额外增大。

## 创新点或方法

旧做法分别测环境扰动或推理延迟；本文把环境、模型、计算平台和执行作为相互影响的系统层，比较不同变化单独和共同出现时的风险。关键量是联合变化的风险是否超过两项单独效应相加的预期。这里是在分析已有 pi0.5 的闭环表现，摘要没有描述重新训练策略，也未给出已实现的在线自适应控制器；调节计算、功耗与控制属于后续研究方向。

### 方法如何工作

1. 分别设置正常与变化环境，并施加不同延迟，使两类因素能够交叉比较。
2. 让同一策略闭环执行，记录安全违规，而非仅检查离线动作预测。
3. 计算各变化的单独风险效应，再与联合条件对比，识别超过相加预期的部分。
4. 据此讨论如何预测风险并调整系统资源；具体自适应方案摘要只说明到研究议程。

### 必要术语

- 闭环：机器人执行后继续观察并决定下一步；延迟会影响这个持续反馈过程。
- 交互效应：两个变化共同造成的影响超出单独影响相加的部分；本文用它衡量额外风险。
- 配对回合：将可比较的执行回合对应起来；有助于比较条件变化带来的差异。

## 证据

摘要报告在 LIBERO 上进行 4,000 个配对闭环回合，模型为 pi0.5。在训练视角下，400 毫秒推理延迟使安全违规率增加 3.5 个百分点；相机偏转 60 度时，同样延迟增加 37 个百分点。额外交互效应为 33.5 个百分点，95% 置信区间为 25—43。结果支持该模型、基准和变化设置下存在明显交互效应；摘要未提供安全违规定义、各条件绝对违规率或真机结果。

## 局限

这些数值来自 LIBERO 基准闭环实验，不能直接当作真机事故概率。配对与联合干预支持测试条件下的交互判断，但摘要没有揭示风险放大的具体内部原因；不能进一步断言一定是视觉误差、动作过期或某个网络模块造成。

- **判断**：值得先读实验设计和风险指标，再看机制分析；它提供了明确的评测警示，但还没有给出可直接部署的安全解决方案。

## 研究关联

具体启示是安全测试应把延迟与场景变化交叉组合。一个在常见视角下看似可接受的延迟预算，换到另一种观测条件可能已经不合适；只分别报告视觉鲁棒性和推理速度，会遗漏这种风险。

### 下一步读哪里

先核查安全违规的操作性定义、配对回合如何控制其他因素，以及四类条件的绝对风险；再检查置信区间计算方式、延迟注入位置与任务间差异。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/When Delay Meets Drift Physical Safety of Robot Foundation Models Is a Cross-Lay.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2611.02101v1 Announce Type: new Abstract: Robot foundation models now act in a closed loop, yet their safety is evaluated one variation at a time: robustness benchmarks perturb the scene while assuming instantaneous inference, and real-time execution methods study inference delay in nominal scenes. We argue that physical safety is not a property of the model alone, but emerges from how variations in the physical environment, the model, the computing platform, and execution interact in closed loop. We formalize this as cross-layer variation propagation across these system layers and use an interaction contrast to measure when joint variation creates more risk than the sum of its parts. In 4,000 paired closed-loop episodes of the pi0.5 vision-language-action model on LIBERO, a 400 ms inference delay raises the safety-violation rate by 3.5 percentage points under the training viewpoint but by 37 percentage points under a 60-degree camera shift: 33.5 percentage points (95% CI: 25-43) more than the two effects combined. We close with a research agenda toward predictable physical intelligence: predicting when variation becomes risk, and adapting compute, power, and control accordingly.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.02101
- Authors: Liangkai Liu, Bimal Thapa Magar
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
