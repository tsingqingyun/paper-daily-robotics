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
url: "https://arxiv.org/abs/2611.08895v1"
published: "2026-11-06T02:38:55Z"
age_days: 3
score: 31
created: 2026-11-10
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Localizing and Editing the Goal Representation of a Vision-Language-Action Model

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇研究发现，给 OpenVLA 加上“不要做 X”，在所测任务中并不能可靠阻止它做 X。作者进一步定位目标信息在网络中的作用位置，发现早层可以一次性干预，较深层则需要对每个生成的动作 token 持续干预。

## 问题

具体问题是机器人能否遵守语言禁令，以及内部究竟表示了哪个执行目标。LIBERO-Goal 的任务共享场景，便于区分一次执行实际朝哪个目标行动。仅检查指令文字不够：模型可能收到禁令，却仍按被禁止的目标生成动作。

### 用一个例子理解

理解用例（非论文实验）：输入“不要把碗放到炉子上”和当前图像；探针读出模型仍朝放碗目标行动，监测器将其与禁令比较，输出不合规信号；是否停止机器人还需另设执行机制。

## 创新点或方法

这不是训练一个新策略，而是诊断和编辑现有 OpenVLA。作者先用闭环执行检查禁令效果，再用线性探针读取目标、用激活替换和向量引导测试哪些位置真正影响动作，最后监测指令变化后的不合规。探针需要拟合；干预与监测发生在推理时。探针训练数据及目标改写的具体构造，摘要未说明。

### 方法如何工作

1. 在共享场景中执行普通和否定指令，标注实际目标，从行为上检验禁令是否生效。
2. 用探针读取各层目标信息，确定内部表征是否区分肯定与否定。
3. 替换激活或加入引导向量，观察动作是否改向，以检验表征位置的因果作用。
4. 比较一次性和逐动作干预，再将目标读出与当前约束比较，评估持续控制与监测的可行性。

### 必要术语

- 线性探针：从内部激活预测目标的小模型；可读出信息，但单独不能证明因果。
- 激活替换：把指定位置的内部数值换掉；用于测试该位置是否影响执行目标。
- 动作 token：编码动作的输出单元；本文深层有效干预需要覆盖每个生成位置。

## 证据

以下数字均来自摘要：在 LIBERO-Goal 中，否定指令下执行被禁任务的比例为 79%，普通任务完成率为 78%。第 8 层指令位置的固定向量改向成功 12/18；第 12—20 层固定向量或预填充替换为 0/158；第 24 层逐动作 token 替换为 15/18。这支持干预位置和时机影响效果，但不构成跨模型结论。第 32 层目标读出监测优于失败检测器，外部图像与指令探针表现相近，摘要未给监测指标。

## 局限

证据限于 OpenVLA 和这一组仿真任务，不能推出所有 VLA 都不理解否定。激活干预支持所测位置的因果作用，但仍需核查替换内容是否引入其他变化；目标监测也不等于能阻止违规。

- **判断**：值得细读干预实验，因为它把“模型知道什么”和“哪里能改变动作”分开检验，结论边界也较明确。

## 研究关联

这改变了一个容易混淆的判断：能从内部读出目标，不等于在该位置改一下就能改变行为。设计监测或控制时，需要分别验证信息可读性、干预有效性和持续时间。

### 下一步读哪里

先核查执行目标的标注规则，再看激活替换的来源与对照、逐 token 干预的时序，以及监测器的误报和漏报。还应确认指令中途变化时，各检测器获得的信息是否一致。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-10/Localizing and Editing the Goal Representation of a Vision-Language-Action Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Operators can state safety constraints for robots as prohibitions such as "do not put the bowl on the stove". We study whether OpenVLA follows such prohibitions and where it represents the goal it executes. The 10 tasks of LIBEROGoal share one scene, so we can label the goal that each rollout executes. We combine closed-loop rollouts with activation patching, linear probes, activation steering and runtime monitors. On LIBERO-Goal, negation had no detectable effect on which task OpenVLA executed. The model executed the forbidden task in 79% of negated rollouts and completed 78% of plain tasks. A goal probe gives similar read-outs under "not X" and "X". Activation patching shows that the first action depends mostly on the instruction tokens before layer 12 and on the last prompt token from layer 16 onward. A fixed steering vector at the instruction tokens at layer 8 redirected 12 of 18 rollouts. Fixed vectors and prefill patches at layers 12 to 20 redirected none of 158. From layer 16, only patches at every decoded action token redirected the robot (15 of 18 rollouts at layer 24). When the instruction changes during a rollout, the layer-32 goal read-out detects non-compliance better than failure detectors, and an external probe on image and instruction features performs comparably. These results support enforcing prohibitions outside the instruction and monitoring goal read-outs against the specification. Goal edits in OpenVLA should act before layer 12 or patch every action token.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08895v1
- Authors: Sudhanshu Srivastava, Faisal Aqlan
- Published: 2026-11-06T02:38:55Z
- Age days: 3

</details>
