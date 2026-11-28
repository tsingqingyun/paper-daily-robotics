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
url: "https://arxiv.org/abs/2611.34014v1"
published: "2026-11-25T09:03:48Z"
age_days: 2
score: 23
created: 2026-11-28
concepts: ["视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Hetero-Associative Visuomotor Memory: Soft Recall as a Base for Learned Residuals in Few-Demonstration Imitation

> [!summary] 这篇论文到底做了什么（基于摘要）
> HAVM 让机器人从多条相似示范中加权读出一段基础动作，再学会对它做修正。用少量且有变化的示范时，这个基础动作即使直接执行没有优势，修正后的成功率也可以更高。

## 问题

只有少量演示时，机器人常先检索最相似的一段动作，再用学习器修正。最近邻片段单独执行表现好，却可能在两条示范的匹配度接近时突然换动作。论文问的是，拿来直接执行的最佳动作片段，是否也最适合当学习器的起点。

### 用一个例子理解

理解用例（非论文实验）：机器人要夹取位于两条示范抓取点之间的方块。当前观测让两条示范得到相近权重，读出一段介于两条接近轨迹之间的动作。修正器再调整横向位移，输出本次执行的动作片段。

## 创新点或方法

原做法只取排名第一的片段。HAVM 给整库候选按匹配度做 softmax 加权，让检索分数接近时，读出的动作随权重连续变化。作者在动作感知的检索键和留一示范训练条件下研究这个起点，并离线训练修正器和检索温度 β。推理时先加权读出基础动作，再由修正器调整。摘要未说明检索键和修正器的具体结构。

### 方法如何工作

1. 用当前观测查询示范记忆，给每个候选动作片段算匹配分数。
2. 用学习到的温度把分数转成权重，加权得到基础动作，降低对第一名切换的敏感性。
3. 训练时留出整条示范来学习修正，执行时用修正器把基础动作调整为当前输出。

### 必要术语

- 软读出：按匹配程度混合多个记忆条目。在本文中，它产生交给修正器的基础动作。
- 检索温度：控制权重集中程度的参数。在本文中，温度 β 通过训练确定。
- 残差修正：学习对已有动作做多少调整。在本文中，它将检索读出转成最终动作。

## 证据

摘要称，ALOHA 方块转移用 40 条人类示范。固定检索键、候选和训练比较两种读出时，新编码器与新重置上的成功率优势为 22.4 个百分点，相比闭环调优的前一名修正器仍高 7.4 个百分点。robomimic Square 在表现较好的两位操作者数据上领先 7.9 个百分点，在等量无标签抽样上领先 6.7 个百分点。按 ALOHA 的 8 秒限制，HAVM 成功率为 74.6%，较 Diffusion Policy 高 6.5 个百分点。SO-101 真机结果展示了稳定的 30 Hz 控制。

## 局限

作者报告，优势在密集、脚本化或生成数据上减弱甚至略微反转，并明确以快速适应已有示范为取舍。平方块任务的受控对照支持读出方式在该设置下的作用。我会核查相互冲突的动作被混合时，修正器还能恢复多少。SO-101 的 30 Hz 衡量控制频率。

- **判断**：值得细读固定检索条件的对照，尤其是直接执行与修正后表现为何分开，以及优势在哪些数据上消失。

## 研究关联

有学习器接手时，选检索策略可以看修正后的成功率。平滑读出能减少相近观测在示范之间切换时的动作跳变，这个解释可通过固定检索键和候选、只换读出规则来检验。

### 下一步读哪里

先核对动作感知检索键用了哪些信息、留一示范时哪些邻近片段会被排除，再看直接执行与修正后的对照。比较 ALOHA 基线时，按同一时限核对成功率。

- **概念**：视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：23
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/Hetero-Associative Visuomotor Memory Soft Recall as a Base for Learned Residuals.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Retrieve-and-correct policies typically refine the nearest retrieved demonstration chunk, the readout that works best when executed directly. We study what a demonstration memory should supply to the corrector instead and find that a smooth, softmax-weighted recall over the whole memory is a much better base. On ALOHA cube transfer (40 human demonstrations), soft recall is no better to execute alone than the nearest chunk; however, with keys, candidates, and training fixed, correcting it raises success by 22.4 points on fresh resets with new encoders and by 7.4 against a closed-loop-tuned top-1 corrector. On robomimic Square, it leads by 7.9 points with the two better operators and by 6.7 on a label-free draw of equal size. This gain holds on sparse, varied demonstrations under an action-aware key and leave-one-demonstration-out training, and fades or slightly reverses on dense, scripted, or generated data. Building on this finding, our hetero-associative visuomotor memory (HAVM, 14M parameters) trains offline in about five minutes, including a learned retrieval temperature $β$, and runs in 1.1 ms. Across six fresh ALOHA encoders, it reaches 76.4% within 24 s, comparable to a 264M Diffusion Policy trained for 6.7 h (78.8%) and ahead of ACT (71.7%) and fine-tuned VLAs (65.2-75.2%), while leading every 40-demonstration baseline within the benchmark's 8 s limit (74.6%; +6.5 over Diffusion Policy, +15.1 over ACT). On LIBERO, one 40-task memory reaches 92.2% and loses far less than SmolVLA to rewording; on a real SO-101 arm, it sustains 30 Hz control without stalling. Unlike pretrained foundation policies aimed at zero-shot generalization to unseen tasks and workspaces, HAVM trades broad out-of-distribution generalization for rapid adaptation to the available demonstrations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34014v1
- Authors: Runcong Wang
- Published: 2026-11-25T09:03:48Z
- Age days: 2

</details>
