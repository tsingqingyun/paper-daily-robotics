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
url: "https://arxiv.org/abs/2607.18840"
published: "Wed, 21 Oct 2026 00:00:00 -0400"
age_days: 0
score: 40
created: 2026-10-22
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> WorldScape Policy 2.0 让同时预测画面变化和机器人动作的模型，既保留近期画面，也按事件查找过去发生过什么。检索出的历史帮助生成下一步计划，事件级数据则把具体指令、画面和动作联系起来。

## 问题

长任务要求机器人知道当前做到哪一步，也要接受细粒度指令、目标图像或视频示范。摘要指出，已有 WAM 的时间上下文短、语言监督多为整段任务描述，且主要依赖文字条件，因而难以跟踪进度、对应局部动作和利用视觉示范。

### 用一个例子理解

理解用例（非论文实验）：输入“收拾桌面”和当前画面，系统从历史查到盘子已经收好，用近期画面判断杯子位置，再生成收杯子的子目标与动作。输出包含后续画面变化预测和机器人动作。

## 创新点或方法

旧做法依靠有限上下文和粗粒度指令；本文加入两类记忆：近期观测作为 DiT 的预填充输入，保留局部交互；历史视觉语言模型输出按全局历史、当前局部事件及事件边界组织，供进度相关检索。检索结果参与感知和自回归规划标记生成，形成隐式子目标。训练还使用事件级数据和 semantic forcing，把局部指令语义传入规划路径；具体损失未说明。推理时可接高层指令或细粒度文字、图像、视频提示。

### 方法如何工作

1. 保存近期观测作为视觉上下文，让模型获得当前交互的连续信息。
2. 将较长历史组织成事件记录，再按当前进度检索，补回短上下文之外的信息。
3. 用检索历史辅助生成规划标记，为动作提供下一子目标条件。
4. 结合记忆和提示预测视觉变化与动作；事件监督如何具体进入训练，摘要只说明到此。

### 必要术语

- 世界动作模型（WAM）：联合建模视觉状态变化和动作；是本文的策略基础。
- 事件级监督：给一段局部活动配上描述及动作；用于细化语言与执行的对应。
- 规划标记：模型生成的内部计划序列；在本文中提供隐式子目标。
- DiT 预填充：把近期画面预先送入扩散 Transformer 作为上下文；具体实现需查方法。

## 证据

据摘要，ManipEvent-5M 含近 500 万个事件片段，对齐动作轨迹、整段指令、子任务描述、目标图像和视频示范。这说明监督粒度，但不是性能结果。摘要称仿真与真机实验在长任务规划、指令遵循和上下文适应上表现更好，却未给基准名、比较对象、指标或数值，无法量化收益。

## 局限

我的待核查问题是性能分别来自记忆、事件监督还是数据规模，以及历史描述出错后会不会影响后续规划。摘要提到跨形态迁移受到旧方法限制，但没有单独给出迁移结果，不能据此认定本文已验证这一能力。

- **判断**：值得读记忆更新与训练目标，但目前输入只能支持机制解释，性能判断需要具体对照和消融。

## 研究关联

可借鉴的是按时间尺度保存不同内容：近期画面保留动作细节，较久历史保存事件和进度。如果任务失败源于重复步骤或忘记已完成事项，这种组织方式值得尝试，前提是事件记录与检索足够准确。

### 下一步读哪里

核查事件何时切分、记忆怎样更新、检索如何识别任务进度，以及 semantic forcing 的实际目标；再查三类提示的独立测试、真机分项和各组件消融。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：40
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-22/WorldScape Policy 2.0 Empowering Steerable World Action Modeling with Reasoning-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2607.18840v3 Announce Type: replace Abstract: World Action Models (WAMs) offer a promising paradigm for robotic manipulation by jointly modeling visual state transitions and robot actions. However, existing WAMs are constrained by limited temporal context, coarse episode-level language supervision, and predominantly text-only conditioning, which hinder task-progress tracking and fine-grained language-video-action grounding while limiting visual-context reasoning and cross-embodiment transfer. In this paper, we introduce WorldScape Policy 2.0, a controllable WAM with reasoning-augmented long short-term memory. Its causal short-term visual memory supplies recent observations as DiT prefill to preserve local interaction dynamics, while its long short-term event memory organizes historical VLM outputs into global-history, local-active, and event-boundary representations for progress-aware retrieval. The retrieved history augments perception and autoregressively generated planning tokens, yielding an implicit subgoal condition for autonomous planning; semantic forcing further transfers event-level instruction semantics into this latent planning pathway. To establish fine-grained multimodal controllability, we construct ManipEvent-5M, an event-grounded embodied pretraining dataset containing nearly 5 million event segments with aligned action trajectories, episode-level task instructions, segment-level subtask captions, goal images, and video demonstrations. These designs provide a unified interface for autonomous planning from high-level instructions and controllable execution from fine-grained text, goal-image, or video-context prompts. Experiments in both simulation and real-world platforms demonstrate superior capabilities in long-horizon autonomous planning, fine-grained instruction following and in-context adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18840
- Authors: Haisheng Su, Zongdai Liu, Xin Jin, Haoxuan Dou, Chengming Hu, Baorun Li, Zhanwang Liu, Ruiyan Xu, Jianjie Fang, Xin Zhang, Zhenjie Yang, Xue Yang, Chen Gao, Junchi Yan, Yong Li, Wei Wu
- Published: Wed, 21 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
