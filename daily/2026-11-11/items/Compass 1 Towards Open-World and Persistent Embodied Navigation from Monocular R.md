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
url: "https://arxiv.org/abs/2611.12087v1"
published: "2026-11-09T09:04:48Z"
age_days: 1
score: 39
created: 2026-11-11
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos

> [!summary] 这篇论文到底做了什么（基于摘要）
> Compass 1 让导航机器人利用较长时间前看过的场景，而不只盯着最近几帧。它用稀疏关键帧和显式历史地图保存线索，再通过三类问答监督训练模型使用这些线索。

## 问题

任务是在开放环境里持续导航，包括探索、判断任务进度和返回先前位置。摘要指出，现有架构通常只能有效利用少量近期帧，容易丢失长期空间上下文，进而影响长程执行稳定性。

### 用一个例子理解

理解用例（非论文实验）：输入“回到刚才经过的红门”及当前视频；模型从历史中找出红门画面，结合历史地图判断它与当前位置的关系；输出后续导航决策。

## 创新点或方法

从依赖近期画面，改为保留关键帧及 History Representation Map，并用 History Utilization 教模型回答任务阶段、探索一致性和时空目标检索问题。训练时，这些结构化问答提供“如何用历史”的监督；推理时，模型结合当前画面与历史进行导航。摘要称底层架构不变，并统一语言理解与视频生成，但未解释生成视频如何转成控制。

### 方法如何工作

1. 从单目视频保留稀疏关键帧，以较少画面保存较长历史。
2. 结合显式历史地图组织时空上下文，让旧画面有可检索的关系。
3. 训练中用三类问答要求模型定位阶段、检查探索和找回目标，使历史参与推理。
4. 执行时结合当前观察与历史作导航判断；具体控制输出方式，摘要只说明到此。

### 必要术语

- 单目 RGB：单个彩色相机的视频；是本文的视觉信息来源。
- 历史表示地图：显式保存历史时空上下文的表示；不能仅凭摘要认定它是精确几何地图。
- VQA 监督：用视觉问题和答案训练模型；本文用它训练历史信息的使用。
- 零样本执行：不针对评估任务额外训练便执行；具体划分仍需查协议。

## 证据

摘要报告：数据包含超过500小时真实交互和超过2,000小时标注网络视频；主要训练相机高度为1米，评估涉及0.35米轮式、0.5米四足、0.85米人形及1.5米无人机。开放世界总体成功率79.4%，最强基线17.8%；基础任务零样本执行超过90%，探索提升250%，历史回溯由0%到58%。这些数字均来自摘要；基线名称、样本量及探索指标定义未提供，不能把总体成绩当作每种机体的成绩。

## 局限

近两分钟是摘要声称的视觉历史回溯范围，不代表无限期记忆。跨高度结果值得关注，但各机体性能、环境重叠和失败分布仍待核查；目前也无法分开判断地图、监督与数据规模的贡献。

- **判断**：值得重点读历史表示和监督设计；大幅成功率差距需要结合评估协议与消融才能解释。

## 研究关联

可借鉴之处是：保存历史与使用历史需要分别训练。给模型更长输入未必足够；明确要求它找回旧目标、检查探索进度，可能更直接地训练出导航需要的记忆操作。

### 下一步读哪里

检查历史地图具体存什么、如何更新与检索；再查三类问答的构造、各项消融，以及回溯成功和探索提升的定义。还需核查视频生成与实际动作接口。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-11/Compass 1 Towards Open-World and Persistent Embodied Navigation from Monocular R.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied navigation requires agents to achieve persistent spatial awareness and long-horizon execution stability in open-world environments. However, existing navigation architectures struggle to sustain both capabilities, remaining effective only over a handful of recent frames. We present Compass 1, the first embodied navigation foundation model to unify language understanding and video generation while enabling memory backtracking through nearly 2mins of visual history. Without altering the underlying architecture, we introduce History Representation, which integrates sparse visual keyframes with an explicit History Representation Map to preserve long-term spatiotemporal context. To effectively leverage this history, we further introduce History Utilization, a structured VQA supervision protocol comprising three categories: task-stage grounding, exploration consistency, and spatiotemporal target retrieval, enabling map-grounded reasoning and stable persistent long-horizon navigation. To fuel this system, we establish a complete annotation pipeline for monocular RGB videos and open-source a massive dataset featuring over 500 hours of high-quality real-world interactions and over 2,000 hours of annotated web videos. Trained mainly on the distribution of 1m height camera, Compass 1 generalizes seamlessly across diverse embodiments and scenarios, ranging from indoor environments to pedestrian-dense streets, spanning wheeled robot at 0.35m, quadruped dog at 0.5m, humanoid at 0.85m, and aerial drone at 1.5m. Compass 1achieves a dominant overall success rate of 79.4% across open-world evaluations, compared to 17.8% for the strongest baseline. It demonstrates exceptional zero-shot execution exceeding 90% on foundational tasks, a 250% boost in exploration, and an unparalleled leap from 0% to 58% in challenging persistent history backtracking.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.12087v1
- Authors: Hai Zhang, Siqi Liang, Yanjun Guo, Shoufeng Zhang, Yunhao Wang, Hangyu Du, Haoguang Mai, Hongchen Li, Jiazhi Yang, Jialong Zeng, Yu Hu, Chen Chen, Gangcheng Jiang, Zishun Zhuo, Lirui Zhao, Zhigang Li, Yu Qiao, Zhenjie Yang, Fu Zhang, Hongyang Li
- Published: 2026-11-09T09:04:48Z
- Age days: 1

</details>
