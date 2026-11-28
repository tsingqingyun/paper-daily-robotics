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
url: "https://arxiv.org/abs/2611.33733v1"
published: "2026-11-25T03:53:49Z"
age_days: 3
score: 24
created: 2026-11-28
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# PROVE: Predict-to-Specify and Observe-to-Verify for Human-Aligned Evaluation of Mobile Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> PROVE 先把机器人指令写成一组可以核验的成功条件，再用真实执行结果逐项判断。生成的目标图只帮助写条件，最终判定依据是执行观测。

## 问题

移动操作任务里，物体位置、柜门结构和合理终态都会随场景变。同一句指令可能有多个有效结果。固定的仿真判据与人类判断有偏差，直接让视觉语言模型评价整段执行也会判断错。PROVE 要把两个容易混在一起的问题拆开：任务到底要求什么，以及机器人实际做到了什么。

### 用一个例子理解

理解用例（非论文实验）。输入“把蓝杯放进柜子并关门”、初始画面、杯子参考图和生成目标图。系统据此写出“蓝杯在柜内”和“柜门关闭”两项条件。若执行观测能看到杯子已经放进柜内，而终态柜门仍开着，评估输出可标出第一项满足、第二项未满足，并判整项任务失败。

## 创新点或方法

PROVE 把指令、初始场景、目标物体参考图和生成的目标图用于细化成功条件。目标图帮助描述预期结果，之后由执行观测提供核验依据。为减少训练时的评估成本，作者把 PROVE 蒸馏成 4B 的 PROVE-Lite。Lite 推理时无需参考图，一次前向就给出整体成败和每项条件的终态判断。做 PPO 后训练时，团队再把这些逐项诊断映射为考虑失败严重程度的奖励。摘要未详述蒸馏样本或奖励映射。

### 方法如何工作

1. 根据指令和初始场景定位需要完成的操作，借助物体参考图确认对象。
2. 借助生成目标图细化成功条件，得到用于核验的规格。
3. 用执行观测判断各条件是否满足，据此给出整体结果。
4. 把评估能力蒸馏进 PROVE-Lite，需要训练策略时再把逐项诊断转成奖励。

### 必要术语

- 仿真判据：用模拟器状态判断任务是否完成的规则；本文用它作人类一致率的对照。
- 蒸馏：让较小模型学习较大系统的判断；本文借此训练运行更快的 PROVE-Lite。
- 严重程度感知奖励：按失败条件及其重要程度给反馈；本文把它用于 PPO 后训练。

## 证据

摘要报告，在 RoboCasa365 上，基于覆盖 65 种原子动作的 6,500 条人类标注轨迹，PROVE 与人类判断一致率为 96.83%，仿真判据为 69.09%，前沿视觉语言模型判定器为 86.12%。PROVE-Lite 一致率为 91.20%，运行速度约为 PROVE 的 38 倍。作者还报告，PROVE 给开源策略评出的成功率更低并改变排名，逐项诊断奖励在 PPO 后训练中优于仿真奖励和二元奖励。摘要未给出后两项的具体分数。这些一致率衡量评估器与人类判断的吻合程度。

## 局限

当前一致率来自仿真基准上的人类标注轨迹。真实场景中的遮挡和视角变化是否降低判定一致性，仍待核查。还需要看生成目标图是否会让规格过度贴合某一种合法终态，以及人类标注有分歧时如何处理。

- **判断**：值得读成功条件的构造与核验细节，再读 PPO 对照，区分判分准确性和奖励设计各自回答了什么问题。

## 研究关联

评估器逐项交代条件是否满足，既能解释为什么一次操作算失败，也让奖励有机会区分失败程度。例如，物体放对但柜门没关，与从头取错物体，可以收到不同反馈。

### 下一步读哪里

先查允许哪些成功条件以及核验时能看到终帧、多帧还是额外观测，再看人类一致率按动作类型有没有明显差异。若关心训练，核对严重程度如何映射成奖励、PPO 对照是否使用同等训练预算，以及策略提升用什么评估器复核。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：24
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/PROVE Predict-to-Specify and Observe-to-Verify for Human-Aligned Evaluation of M.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Judging open-world robot manipulation is hard because layouts, articulated fixtures, and valid goal configurations vary widely. On RoboCasa365, simulator predicates agree with human judgments on only 69.09\% of rollouts, and a frontier VLM judge on 86.12\%. We present \textbf{PROVE} (Predict-to-Specify, Observe-to-Verify), which first specifies what success should look like and then checks the outcome. PROVE refines success conditions from the instruction, the initial scene, a target-object reference image, and a generated goal image. The goal image only sharpens the conditions and never serves as evidence. On 6,500 human-annotated rollouts over 65 atomic actions, PROVE reaches \textbf{96.83\%} agreement. Applied to open-source policies, it reports far lower success than native checks and changes their ranking. To reduce evaluation overhead in policy learning, we distill PROVE into \textbf{PROVE-Lite}, a 4B evaluator that needs no reference images. In one forward pass, PROVE-Lite predicts the outcome and the terminal state of each task condition. It reaches \textbf{91.20\%} agreement while running about 38$\times$ faster than PROVE. Mapped to a severity-aware reward, its diagnoses improve PPO post-training over both simulator and binary rewards.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33733v1
- Authors: Bowen Lyu, Yunan Liu, Liaoyuan Fan, Qinchuan Cheng, Jiafei Duan, Cheston Tan, Shijie Li
- Published: 2026-11-25T03:53:49Z
- Age days: 3

</details>
