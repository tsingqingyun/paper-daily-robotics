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
url: "https://arxiv.org/abs/2610.36624"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 25
created: 2026-10-30
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction

> [!summary] 这篇论文到底做了什么（基于摘要）
> MoGAP 让用于机器人控制的视频模型在训练时多练习恢复运动区域，而不是平均关注整幅画面。它把动态区域加上更强噪声、静态区域保留得更清楚，让模型借背景理解并恢复与动作有关的变化。

## 问题

世界动作模型同时预测未来画面和机器人动作，视觉预测帮助预训练视频模型适应机器人场景。但标准目标对各区域一视同仁：背景和正在移动的手、物体都接受相同方式的监督，尽管它们对控制的重要程度不同。本文要改变这种监督分配。

### 用一个例子理解

理解用例（非论文实验）：机器人把杯子推到标记处。输入训练视频和动作时，桌面大多不动，机械臂和杯子发生移动；辅助路径重点恢复被重度加噪的移动区域，输出重建预测以训练共享骨干。部署时使用标准视频—动作预测路径产生动作。

## 创新点或方法

旧做法均匀处理视觉区域；MoGAP 增加运动引导的非对称预测，让动态区域受到更重破坏，再以较清楚的静态区域为上下文重建它们。这样有望把学习压力放到动作造成的变化上。该辅助路径与标准视频—动作预测共用视频扩散骨干，只在训练时使用；运动线索直接来自训练视频，无需外部教师或额外模态。推理时不使用这条辅助路径，但运动估计方式、损失权重和噪声比例，摘要没有交代。

### 方法如何工作

1. 从训练视频提取运动线索，确定哪些区域需要更集中的视觉学习。
2. 给动态区域加入更强噪声，同时让静态区域保留较清楚的上下文。
3. 通过共享骨干的辅助路径恢复画面，迫使模型练习解释运动区域。
4. 同时训练标准视频—动作预测；推理时仅使用标准路径，辅助路径到训练结束为止。

### 必要术语

- 世界动作模型（WAM）：同时预测未来视觉观察和动作的模型；本文调整它的视觉训练。
- 非对称加噪：不同区域接受不同强度的破坏；本文用它增加动态区域的恢复难度。
- 辅助预测路径：额外提供训练信号的预测过程；本文中只在训练时使用。

## 证据

摘要给出 GR-1 桌面基准结果：Fast-WAM（Wan2.2-5B）成功率由 38.8% 升至 47.5%，增加 8.7 个百分点；Cosmos3-Nano 由 52.3% 升至 62.3%，增加 10.0 个百分点。摘要还称多个操作基准和架构均有改善，但没有逐项结果、试验次数或误差范围，也未说明这些结果对应仿真还是真机。因此，数字支持这两个配置上的收益，不能直接外推到所有控制任务。

## 局限

运动并不天然等于控制相关性：移动阴影或旁观者也会动，关键目标也可能暂时静止。这是我会核查的适用边界；摘要没有说明这些情况是否已测试，也没有量化辅助训练的额外成本。

- **判断**：值得细读训练目标和消融实验：改动集中在训练阶段，且摘要给出了两个架构上的明确成功率收益。

## 研究关联

具体启示是：把视频生成模型用于控制时，预测画面的训练资源可以按任务相关性重新分配。若大量像素属于静态背景，可以先检查监督是否被背景占据，再尝试改变区域噪声与辅助目标，而不必立即更换整个骨干。

### 下一步读哪里

优先核查运动区域如何提取、是否处理相机运动，以及噪声强度和辅助损失怎样设置；消融应区分运动定位的贡献与单纯增加训练目标的贡献，并检查训练成本及各任务结果。

- **概念**：视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：25
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.36624v1 Announce Type: cross Abstract: World Action Models (WAMs) leverage pretrained video generative models for robotic control by jointly predicting future visual observations and actions. The visual prediction objective plays a key role in adapting pretrained video representations to the target robot domain. Yet standard visual prediction inherited from video pretraining treats all visual regions uniformly, despite their differing relevance to robotic control. We therefore investigate the spatial allocation of visual supervision in WAMs and show that focusing supervision on dynamic regions can substantially improve policy performance. Building on this finding, we introduce Motion-Guided Asymmetric Prediction (MoGAP), which augments WAM training with motion-focused visual prediction. MoGAP allocates noise asymmetrically across regions, training the model to reconstruct more heavily corrupted dynamic regions using less corrupted static regions as context. MoGAP is trained alongside standard video-action prediction through a training-only auxiliary prediction path within the shared video diffusion backbone. It uses motion cues derived directly from training videos, requiring neither an external teacher nor additional modalities. Across robot manipulation benchmarks and WAM architectures, MoGAP consistently improves policy performance, increasing success rates on the GR-1 tabletop benchmark from 38.8% to 47.5% for Fast-WAM (Wan2.2-5B) and from 52.3% to 62.3% for Cosmos3-Nano.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36624
- Authors: Taeyoung Kim, Junyoung Sung, Heeseung Kwon, Minseop Kim, Jinwoo Shin
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
