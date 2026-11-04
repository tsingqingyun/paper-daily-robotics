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
url: "https://arxiv.org/abs/2606.22174"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 38
created: 2026-11-04
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> OpenHLM 要让人形机器人看图、听指令后协调全身行动，关键是开放全身关节的示教接口，再结合已有 VLA 预训练和 HuMI 数据共同训练。它的主要贡献是一套逐项比较得出的实践配方。

## 问题

任务是同时完成移动和操作，例如改变身体高度时继续用手处理物体。摘要指出，常见系统把上下半身交给不同控制器，限制了整条运动链的协调；机器人虽然有人形身体，实际行为却接近带双臂的移动底盘。真正的问题是怎样采集、学习能使用全身自由度的动作。

### 用一个例子理解

理解用例（非论文实验）：输入“把低层架上的盒子放到高层架”和相机画面；策略结合盒子与架子位置生成全身动作，使腿、躯干和手臂配合取放；输出是一段覆盖全身关节的动作序列。

## 创新点或方法

旧做法把身体分开控制，或只向操作者开放部分自由度；本文改用基于关节的全身遥操作，并逐项研究示教接口、VLA 设计和异构数据共同训练。训练时利用静态及轮式双臂平台的预训练，并加入 HuMI 数据；推理目标是从语言和像素直接输出覆盖全身自由度的动作。摘要未说明动作编码、各类数据如何对齐，以及具体训练损失。

### 方法如何工作

1. 通过全关节遥操作采集协调动作，让训练数据包含上下身共同完成任务的示范。
2. 比较不同接口与模型选择，每次改变一个因素，以辨认配方中哪些选择有效。
3. 将已有双臂平台预训练与人形数据衔接，利用已学到的能力支持全身动作学习；衔接细节摘要未说明。
4. 加入 HuMI 数据共同训练，再由语言和视觉驱动全身动作，检验新对象与指令上的表现。

### 必要术语

- 全身自由度：机器人可独立控制的各个运动方向；本文希望策略能共同使用这些控制量。
- VLA：把视觉、语言映射为动作的模型；本文将输出范围扩展到人形全身。
- 异构共训：把不同来源或形态的数据一起训练；本文用它补充昂贵的全身示教。

## 证据

摘要报告：在一个覆盖较大垂直活动范围的长时任务中，OpenHLM 超过 GR00T N1.6 和 Ψ₀，总示教时间不到对比方案的一半。摘要还报告全关节遥操作优于部分自由度接口，以及 HuMI 共训可扩展到新物体和指令而无需这些目标的额外全身示教。但未提供成功率、试验次数、平台细节和差异幅度，因此支持的是该实验设置下的数据效率与协调收益。

## 局限

我会核查长时任务究竟要求哪些上下身协同动作，以及收益能否跨任务保持。摘要没有交代测试环境的仿真与真机构成，也没有列出作者明确承认的局限；不能据此把一个任务上的结果推广到整类人形操作。

- **判断**：值得读方法和逐项对照实验，重点看数据采集与共训如何落地；目前最有说服力的是配方思路，收益大小仍需实验细节。

## 研究关联

值得借鉴的是先检查示教接口有没有允许人展示目标行为：如果采集时身体就被分开控制，后续模型很难从数据中学到协调。另一条可尝试的路径是让较易采集的操作数据补充全身示教，但前提是确认动作空间与训练接口能有效衔接。

### 下一步读哪里

先查遥操作接口具体开放哪些关节，再看预训练动作如何迁移到人形动作空间，最后核对 HuMI 共训的数据比例、新物体划分及示教时间的统计口径。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/OpenHLM An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.22174v2 Announce Type: replace Abstract: Whole-body humanoid loco-manipulation requires coordinating the robot's entire kinematic chain. However, most existing systems typically decouple the upper and lower bodies into separate controllers, limiting such coordination and yielding behaviors similar to those of a wheeled dual-arm platform. In this paper, we ask what it takes to build a whole-body native vision-language-action (VLA) model that maps language and pixels directly to all of the humanoid's degrees of freedom. We conduct a systematic empirical study organized as a roadmap of one-variable-at-a-time experiments across three phases: whole-body teleoperation, VLA model design, and heterogeneous co-training. Our study yields several intriguing findings: a joint-based whole-body teleoperation interface outperforms alternatives that only partially expose the humanoid's degrees of freedom; a VLA pretrained on static and wheeled dual-arm platforms transfers surprisingly well to a humanoid's full action space; and co-training with HuMI, the humanoid analog of UMI, extends the policy to new objects and instructions without additional whole-body teleoperation on those targets. Following this roadmap yields OpenHLM, an open-source recipe for whole-body humanoid loco-manipulation. In a challenging long-horizon task that spans a wide vertical range of the humanoid, OpenHLM outperforms two state-of-the-art humanoid VLA baselines (GR00T N1.6 and $\Psi_0$) using less than half the total demonstration time. Our code, training data, and model checkpoints are available at [https://openhlm-project.github.io/].

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22174
- Authors: Yingdong Hu, Haodong Zhu, Boyuan Zheng, Yihang Hu, Tong Zhang, Zunhao Chen, Junming Zhao, Ruiqian Nai, Yang Gao
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
