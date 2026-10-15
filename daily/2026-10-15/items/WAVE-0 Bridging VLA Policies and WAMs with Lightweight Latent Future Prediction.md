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
url: "https://arxiv.org/abs/2610.18568"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 44
created: 2026-10-15
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction

> [!summary] 这篇论文到底做了什么（基于摘要）
> WAVE-0 在预训练 VLA 中加入一个轻量世界模型：先把潜在动作计划转成预测的未来表征，再让动作专家参考这个未来生成动作。它不必生成视频像素，也不需要为这个世界模型做大规模视频预训练。

## 问题

任务是让操作策略在出动作时考虑环境后果。摘要指出，普通 VLA 没有显式预测后果；许多 WAM 要付出视频生成成本，而部分潜在预测方法只把未来当训练辅助目标，或依赖昂贵的视频预训练和质量欠佳的视觉转变来推断动作。

### 用一个例子理解

理解用例（非论文实验）：输入抽屉图像和“拉开抽屉”，VLM 形成潜在动作计划，世界模型生成相应未来表征，动作专家据此输出控制动作。这个例子不意味着模型显式枚举多条轨迹或在线搜索；摘要没有描述这些操作。

## 创新点或方法

WAVE-0 将“直接由 VLA 生成动作”改成“潜在计划→预测未来表征→动作专家”。新增世界模型为 257M 参数，连接 VLM 生成的潜在动作计划与动作生成。训练直接使用真实机器人动作，并加入反事实排序目标，不要求重建像素；摘要未说明替代动作怎样构造、如何打分。推理时预测表征实际进入动作专家，因此未来预测不只是训练时的辅助任务。

### 方法如何工作

1. 由预训练 VLA 的视觉语言部分产生潜在动作计划，为未来预测提供执行意向。
2. 用 257M 世界模型把计划转成未来表征，提供预期后果而无需生成视频像素。
3. 训练时利用真实机器人动作和反事实排序目标约束世界模型；排序细节摘要只说明到此。
4. 推理时将预测表征送给动作专家，使最终动作同时参考当前信息与预期未来。

### 必要术语

- 潜在未来表征：用内部向量表示未来状态信息；本文用它替代像素级视频预测。
- 动作专家：负责输出机器人动作的模型部分；本文让它接收预测未来作为条件。
- 反事实排序：比较不同假设对应结果的相对优劣；本文将其用于训练，具体比较项未说明。

## 证据

摘要报告成功率：RoboTwin 2.0 为 91.47%，LIBERO 为 98.7%，LIBERO-Plus、Pro、Para 分别为 88.0%、61.4%、75.0%。真机任务中，π₀.₅ 从 38.3% 提高到 73.3%。这些结果支持所测操作任务上的效果，但摘要未给各仿真基线、试验次数、误差范围与推理延迟，也不能与其他论文中不同设置的数字直接排名。

## 局限

257M 是新增世界模型规模，不是整套系统规模；无需大规模视频预训练也不代表整个系统从零训练。成功率上升本身不能证明每次都预测对了后果。我会核查无未来输入、无排序目标等消融，以及错误预测对动作的影响。

- **判断**：值得优先读方法与消融：它把未来预测接入动作生成的路径很明确，真机增益也具体；复现前应核查排序目标和新增推理成本。

## 研究关联

可借鉴的是先问动作需要哪种未来信息，再决定是否必须生成完整视频。若紧凑表征足以指导动作，预测表征可能是利用后果信息的较省计算路线；仍需确认它学到的是可区分动作后果的动态，而不只是场景特征。

### 下一步读哪里

先查潜在计划与真实动作如何对应、未来表征的训练目标，以及反事实排序的样本构造。再查预测分支是否带来独立收益、额外延迟有多少，并确认真机两组结果的数据和控制条件是否一致。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：44
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/WAVE-0 Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.18568v1 Announce Type: new Abstract: Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences. World action models (WAMs) incorporate future prediction, yet most rely on costly video generation, while latent alternatives either use predicted futures only as auxiliary targets or infer latent actions from suboptimal visual transitions through costly large-scale video pretraining. We introduce WAVE-0 (World-model-Augmented VLA Execution), a framework that bridges VLAs and WAMs through a lightweight latent world model. By connecting the semantic understanding of pretrained VLAs with explicit future prediction, WAVE-0 allows anticipated action consequences to directly guide action generation. Built on a pretrained VLA, its 257M world model translates VLM-generated latent action plans into predicted future representations that condition the action expert, unifying latent planning, future prediction, and action generation. The world model is trained directly on ground-truth robot actions with a counterfactual ranking objective, requiring neither pixel reconstruction nor large-scale video pretraining. WAVE-0 achieves success rates of 91.47% on RoboTwin 2.0 and 98.7% on LIBERO, along with 88.0%, 61.4%, and 75.0% on LIBERO-Plus, LIBERO-Pro, and LIBERO-Para, respectively. On real-world tasks, it improves the success rate of $\pi_{0.5}$ from 38.3% to 73.3%. These results demonstrate strong manipulation performance and generalization across diverse distribution shifts.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.18568
- Authors: Haomin Wang, Anqiong Ji, Ke Wang, Zhongshan Liu, Ru Ying, Ran Zheng, Zhipeng Zhang
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
