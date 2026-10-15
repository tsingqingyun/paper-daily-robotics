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
url: "https://arxiv.org/abs/2610.16313"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Listen Before Act: Audio-Conditioned Robot Manipulation with ListenVLA

> [!summary] 这篇论文到底做了什么（基于摘要）
> ListenVLA 让机器人结合声音生成动作，还用“其他条件相同、声音不同”的示范教它对应地改变动作。它要解决的不只是听见声音，而是让声音在决策中真正起作用。

## 问题

某些操作需要区分声音、响应声响，甚至先接触物体才能获得听觉证据，单靠图像无法可靠判断。传统视觉语言输入缺少这种信息；仅增加音频输入，也仍需解决声音差异如何对应动作差异的问题。

### 用一个例子理解

理解用例（非论文实验）：输入“挑出装有颗粒的盒子”和两个外观相似的盒子；机器人轻摇盒子，将声音历史与图像一起处理，再输出拿取目标盒子的动作。该例用于理解主动获取声音证据，不代表论文验证过此任务。

## 创新点或方法

ListenVLA 基于 GR00T N1.7，把音频语义表示与从波形提取的声学线索结合，只使用当前及过去的音频，通过音频 token 和特征调制影响连续动作生成。训练另加音频—动作绑定目标：在上下文匹配的示范中固定非音频观测、共享纯噪声动作输入，比较不同音频条件下的短时域流速度预测差异，并同时监督整段动作。这样限制其他变化，更直接地学习声音与动作变化的对应关系；推理时无需成对示范。

### 方法如何工作

1. 收集截至当前的音频，提取语义与声学线索，避免使用未来声音。
2. 用音频 token 和特征调制把声音接入动作生成，使动作能够随听觉条件变化。
3. 训练时固定其他观测和噪声输入，对齐音频差异与动作预测差异，减少模型忽略声音的机会。
4. 结合整段动作监督学习可执行动作；推理时根据当前多模态历史连续生成动作。

### 必要术语

- 因果音频历史：只包含当前和过去的声音；用于满足在线操作的信息条件。
- 特征调制：用声音调整内部特征；让音频影响动作计算。
- 流速度预测：动作生成过程中对更新方向的预测；本文在这一层监督不同声音导致的差异。

## 证据

摘要介绍 LIBERO-Audio 的八项任务，覆盖按声音选目标、响应听觉事件，以及主动交互获取声音证据；另有三项真机操作。摘要称表现优秀，并称消融支持绑定监督和音频调制，音频交换测试显示声音会影响动作预测。但没有成功率、基线名称或增幅，无法判断领先幅度；预测受声音影响也不等于影响方向总是正确。

## 局限

需要核查上下文匹配是否足够严格，以及模型是否依赖录音条件或背景噪声。真机任务说明方法不只在仿真中展示，但三项任务不能直接支持广泛的真实环境鲁棒性；噪声、音源位置变化和主动探测能力的覆盖范围仍待查看。

- **判断**：值得深入读绑定损失和配对数据构造，因为它们比单纯增加音频分支更能解释模型为何会用声音。

## 研究关联

具体启示是：新增一种传感器后，应设计让它必须影响动作的训练对照。若图像和指令已足以猜对大多数示范，模型可能忽略声音；固定其他条件、监督音频对应的动作差异，是值得尝试的办法。

### 下一步读哪里

先检查匹配示范如何获得、短时域流速度差异如何监督，再看音频交换是否改变了正确动作，以及真机测试的噪声和声音同步条件。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/Listen Before Act Audio-Conditioned Robot Manipulation with ListenVLA.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.16313v1 Announce Type: new Abstract: Vision-language-action (VLA) models have advanced robotic manipulation by connecting visual perception and language instructions to action generation. However, many manipulation tasks depend on auditory cues that cannot be reliably inferred from visual observations and may need to be elicited through physical interaction. To address this gap, we present ListenVLA, an audio-conditioned VLA policy built on GR00T N1.7 for sound-guided manipulation. ListenVLA combines semantic audio embeddings with waveform-derived acoustic cues over a causal audio history and conditions continuous action generation through audio tokens and feature modulation. Moreover, we introduce an audio-action binding objective that uses context-matched demonstrations to link auditory differences to demonstrated action differences. The objective supervises short-horizon differences between flow-velocity predictions under different audio conditions, with shared pure-noise action inputs and fixed non-audio observations, alongside full-chunk action supervision. Furthermore, we develop LIBERO-Audio, an eight-task benchmark covering sound-based target selection, responses to auditory events, and physical interactions that reveal acoustic evidence. Experiments on LIBERO-Audio and three real-world manipulation tasks show excellent performance. Ablation studies support the contributions of binding supervision and audio modulation, while audio swap tests show that sound influences action predictions. Our code and videos are available at https://anonymous.4open.science/r/listenvla-F18D

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.16313
- Authors: Jiaqi Fan, Rui Xu, Jiakun Xia, Xuyu Fan, Shuailei Ma, Yuefeng Wang, Qing Wang, Jiarui Zhang, Yili Fu, Xu Li
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
