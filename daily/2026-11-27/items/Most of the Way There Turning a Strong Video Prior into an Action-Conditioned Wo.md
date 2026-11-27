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
url: "https://arxiv.org/abs/2611.34435v1"
published: "2026-11-25T14:19:27Z"
age_days: 1
score: 28
created: 2026-11-27
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# Most of the Way There: Turning a Strong Video Prior into an Action-Conditioned World Model

> [!summary] 这篇论文到底做了什么（基于摘要）
> Dianjing 把预训练视频模型改成能预测指定机器人动作后果的世界模型。它冻结主干、加入物理动作与历史条件，并把训练集中在去噪中较早决定运动和布局的高噪声阶段。

## 问题

视频模型看到机械臂和杯子，可以生成一段自然的移动画面。但如果给定一条具体控制命令，例如向左推，它必须预报这条命令对应的结果。用于评估机器人策略时，只要模型把不同动作的后果混在一起，画面再逼真也无法据此选动作。

### 用一个例子理解

理解用例（非论文实验）。输入是机械臂靠近杯子的历史画面，以及随后向左推的动作。历史交代手和杯子的位置，动作条件在生成过程中约束运动。输出是一段预测视频，可以拿来和实际执行左推动作的录像比对。

## 创新点或方法

Dianjing 保留 MiniMax H3 已有的视频生成能力，用统一的物理动作条件指定接下来要执行什么，并利用模型原有的历史条件能力提供此前发生的事。训练集中在高噪声阶段，作者的理由是运动和布局在这里形成，所以动作信号应当在这时就影响未来。推理时，模型根据历史和给定动作预测视频。动作如何统一编码、历史提供多长，摘要未说明。

### 方法如何工作

1. 冻结预训练视频主干，复用它已学到的画面与运动表征。
2. 提供历史与物理动作条件，让预测同时知道当前局面和将要施加的控制。
3. 将适配训练集中到高噪声阶段，使动作能在运动与布局形成时影响预测。
4. 推理时生成给定动作下的未来视频，用同一动作的真实执行作参照检验预测。

### 必要术语

- 视频先验：预训练模型学到的画面和运动规律；本文以它作为预测未来的起点。
- 动作条件：告诉模型接下来要执行的控制命令；本文用它约束未来随指定动作变化。
- 高噪声阶段：去噪生成中离清晰视频较远的阶段；作者把训练集中到这里，以影响运动和布局。

## 证据

据摘要，基座为 33B 参数的 MiniMax H3，冻结主干，仅训练 0.34% 的参数，使用约 65 小时、覆盖两种机器人本体的视频。WorldOracle 将预测与配对的真实执行比较。Dianjing 在五条评测赛道中四条得分最佳，在 AgiBot-Long 排第二。受控消融显示，在所测设置里，训练分布在哪些噪声阶段，比动作如何接入网络更影响结果。摘要未展开逐赛道指标、具体分差和基线名单。

## 局限

作者报告的边界包括 AgiBot-Long 排名第二，以及适配数据来自两种本体。我会核查长序列里误差怎样积累，以及预测分数能否保留真实执行中的动作优劣排序。配对真机验证衡量的是预测与执行结果的对应程度，尚不能据此判断用该模型优化策略会怎样。

- **判断**：值得细读噪声阶段的受控消融与 WorldOracle 的计分方式，前者解释训练资源该放在哪里，后者决定排行榜能说明多少动作预测能力。

## 研究关联

把生成模型改成动作模拟器时，可以先查动作在哪个生成阶段开始改变预测。若物体移动方向在早期已经形成，只在后期强化条件可能更容易修到纹理，难以改掉错误的运动。这也给了消融一个具体方向：固定动作输入方式，单独调整训练覆盖的噪声阶段。

### 下一步读哪里

先查物理动作如何跨本体编码、历史如何接入，以及高噪声训练所覆盖的区间。再查消融是否控制训练预算，并核对 WorldOracle 的指标对方向错误和长时误差有多敏感。

- **概念**：多模态基础模型 世界模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/Most of the Way There Turning a Strong Video Prior into an Action-Conditioned Wo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Modern video generators excel at producing visually plausible futures guided by text and image prompts. Yet their emphasis on semantic plausibility does not guarantee fidelity to the physical consequences of specific actions. Action-conditioned world models (ACWMs), in contrast, aim to simulate how the world responds to robot actions, enabling scalable policy evaluation and improvement without costly real-world rollouts. The challenge is not merely to generate a plausible future, but to predict what follows from a specific physical action. As video priors grow stronger, we ask how little adaptation is truly needed to bridge this gap. We introduce Dianjing, a minimal recipe that preserves and unlocks the capabilities of strong video priors through unified physical action conditioning, training concentrated at the high noise levels where motion and layout, and thus the consequences of actions, are decided, and native history conditioning. Built upon MiniMax H3, a 33B video foundation model, Dianjing freezes the pretrained backbone and trains only 0.34% of its parameters using approximately 65 hours of robot video across two embodiments, without additional robot-specific pretraining or camera calibration. Controlled ablations show that where training is allocated across noise levels matters more than how actions enter the network. On WorldOracle, which evaluates predictions against paired real-world executions, Dianjing achieves the best scores on four of the five evaluation tracks and ranks second on AgiBot-Long. Our findings suggest that strong video priors already bring us most of the way to world modeling; lightweight physical action grounding can unlock their potential for real-world prediction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34435v1
- Authors: Zanyi Wang, Xia Chen, Liu Liu, Xianglong Guo, Dengyang Jiang, Haodong Li, Tingyang Xiao, Wenhao Hu, Zhizhong Su
- Published: 2026-11-25T14:19:27Z
- Age days: 1

</details>
