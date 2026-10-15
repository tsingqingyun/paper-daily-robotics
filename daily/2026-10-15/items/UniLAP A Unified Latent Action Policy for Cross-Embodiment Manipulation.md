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
url: "https://arxiv.org/abs/2610.16969"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 46
created: 2026-10-15
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# UniLAP: A Unified Latent Action Policy for Cross-Embodiment Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> UniLAP 把从无动作标签视频中学到的运动知识，变成推理时可以直接使用的连续潜在动作策略。关键是向 LAM 教师学习动作表征，同时保留多种可行动作，并尽量把真正的运动与无关画面变化分开。

## 问题

任务是从多来源视频学习操作规律，再适配不同身体或机器人。离散潜在动作像有限的动作词表，可能表达不出精细差别；已有连续方案虽然缓解这一点，却常服务于世界预测，还要额外规划才能得到可执行动作。

### 用一个例子理解

理解用例（非论文实验）：输入机械臂当前看到的杯子及取杯目标，策略生成一个连续潜在动作，再经平台适配得到控制指令。若杯子有多种可行抓法，理想情况下可保留这些选择；输入未说明任务目标实际采用何种编码。

## 创新点或方法

UniLAP 将“先预测或利用未来，再规划动作”改成学习连续潜在动作策略。训练时用 flow-adaptive 目标蒸馏 LAM 教师，并用流匹配建模动作分布，目标是继承动作知识而不把多种合理行为压成一种。另提取无需标签的运动目标，削弱外观变化的干扰。推理时不依赖未来帧；新平台怎样把潜在动作转换成具体控制量、需要多少适配数据，摘要未说明。

### 方法如何工作

1. 从多来源视频学习 LAM 教师的动作表征，为缺少控制标签的数据建立可迁移的运动描述；教师细节未说明。
2. 提取无标签运动目标，使训练更关注运动线索，减少无关外观变化进入潜在动作。
3. 用 flow-adaptive 目标蒸馏教师，并通过流匹配学习连续动作分布，以表达精细变化和多种可行行为。
4. 推理时直接产生潜在动作，再适配到具体平台；潜在动作到执行指令的结构，摘要只说明到此。

### 必要术语

- 潜在动作：用内部向量表示动作变化；它不一定直接等于关节指令。
- 流匹配：学习连续变换以生成目标分布中的样本；本文用它建模连续潜在动作。
- 蒸馏：让学生学习教师已有的表征或行为；本文用来继承 LAM 的动作知识。

## 证据

摘要称模型以 1.1B 参数在多来源视频上预训练，并在手部姿态预测、单臂操作、人形机器人操作和真机部署中超过先进潜在动作与 VLA 基线。但没有提供基线名称、数据量、指标数值或适配预算。现有证据只能支持作者报告了跨任务优势，无法判断优势大小，也不能据此断定新平台适配成本低。

## 局限

“与身体无关”的潜在空间是作者的方法主张，不意味着无需适配就能控制任意机器人。我会核查运动目标是否也保留了任务无关运动，以及跨平台实验是否控制了新增数据量。摘要没有给出足以回答这些问题的结果。

- **判断**：值得深入读蒸馏目标、运动目标构造和平台适配接口；能否把视频知识稳定转成精细控制，是比总榜成绩更关键的判断点。

## 研究关联

这里值得借鉴的是将“视频中有什么在动”与“画面长什么样”分开学习。若希望多个身体共享运动知识，减少背景、纹理等信息进入动作表征，可能比单纯扩大视频预训练更切中迁移障碍；是否有效仍需消融验证。

### 下一步读哪里

优先核查教师如何从视频定义动作、flow-adaptive 目标如何保留多种行为，以及无标签运动目标的提取算法。再查各平台适配的数据和参数预算，并确认推理时是否仍有其他规划或解码开销。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- **筛选分数**：46
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/UniLAP A Unified Latent Action Policy for Cross-Embodiment Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.16969v1 Announce Type: new Abstract: Latent Action Models (LAMs) can capture manipulation priors from action-free videos, but discrete latents usually impose a granularity bottleneck, limiting their ability to represent fine-grained action. Recent continuous alternatives mitigate this, but they are typically used as proxies for world modeling and require a further planning step to produce executable actions. We thus introduce UniLAP, a unified continuous latent-action policy that models the latent space via flow matching and bypasses reliance on future frames during inference. By distilling a LAM teacher with a flow-adaptive objective, UniLAP inherits the teacher's action representation while retaining the multimodal distribution of feasible behaviors. To decouple latent representations from task-irrelevant appearance, we extract a label-free motion target to isolate relevant kinematic cues from spurious visual dynamics. With the established embodiment-agnostic latent manifold, UniLAP can be easily adapted to novel platforms. Pretrained on multi-source videos at a compact 1.1B parameter scale, UniLAP outperforms state-of-the-art latent-action and Vision-Language-Action (VLA) baselines across hand pose forecasting, single-arm and humanoid manipulation, and real-world deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.16969
- Authors: Lei Yao, Qiao Feng, Mutian Tong, Qihao Yun, Lap-Pui Chau, Lingjie Liu
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
