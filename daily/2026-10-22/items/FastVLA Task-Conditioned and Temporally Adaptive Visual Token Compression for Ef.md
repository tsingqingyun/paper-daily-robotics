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
url: "https://arxiv.org/abs/2610.22146"
published: "Wed, 21 Oct 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-10-22
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> FastVLA 根据当前任务挑选重要视觉 token，再随时间调整压缩力度，让 VLA 少处理一些图像信息。它无需训练，关键是同时回答“现在该看哪里”和“这一步需要保留多少”。

## 问题

闭环控制每一步都要处理高分辨率、常含多个视角的图像，数百个视觉 token 会占用大量 Transformer 计算。按通用视觉显著性压缩，可能漏掉任务关键区域；固定 token 预算又无法适应不同阶段的信息需求，容易浪费计算或损伤控制。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放进盒子”和多视角画面。FastVLA 根据任务注意力识别重要视觉信息，动态压缩 token，再交给 VLA 输出动作；下一帧重新评分，使计算分配能随接近、抓取和放置阶段变化。

## 创新点或方法

旧做法依赖静态重要性指标或固定预算；FastVLA 用任务到视觉的注意力给 token 评分，再根据分数分布有多均匀决定压缩率。直觉是：重要性集中时可以集中保留信息，重要性分散时要更谨慎。分布均匀度由逆 Simpson 指标衡量，并用在线滑动窗口校准。这些都在推理时发生，不训练新策略；具体压缩操作与校准映射摘要未展开。

### 方法如何工作

1. 读取当前图像与任务相关注意力，得到每个视觉 token 的重要性评分。
2. 衡量评分分布的均匀程度，估计当前信息需求是集中还是分散。
3. 结合滑动窗口校准压缩率，使预算随时间调整；具体规则摘要只说明到此。
4. 把压缩后的视觉信息交给原 VLA 预测动作，并在下一步重新计算，以适应场景变化。

### 必要术语

- 视觉 token：图像编码后的信息单元；数量影响后续 Transformer 计算。
- 任务到视觉注意力：任务信息对视觉位置的关注权重；本文用作重要性依据。
- 逆 Simpson 指标：衡量权重分布有多分散的量；本文据此调整压缩率。
- 滑动窗口校准：利用最近一段历史调整当前判断；用于在线设置压缩预算。

## 证据

摘要在 OpenVLA、OpenVLA-OFT、CogACT 上，使用 LIBERO、SIMPLER 测试：LLM 主干 FLOPs 减少 35–59%，动作延迟减少 9–32%，同时维持任务成功，效率与性能权衡可比或优于已有即插即用压缩、剪枝、复用基线。Franka Research 3 真机上，动作预测延迟减少 20%，成功表现相当。数字均来自摘要；缺少分模型结果、绝对延迟、成功率和误差范围。

## 局限

我会核查注意力分数是否漏掉细小但关键的对象，以及场景突变时滑动窗口能否及时调整。真机结果支持所测平台上的动作预测加速，不能直接推断整项任务耗时减少 20%，更不能推断控制频率必然同步提高。

- **判断**：值得读实现与逐任务结果；无需训练使它便于尝试，但应以实际延迟和关键任务成功率决定是否采用。

## 研究关联

可借鉴的是把计算预算当作随执行阶段变化的量，而不是整段任务固定配额。也要同时测计算量与实际延迟：这里 FLOPs 的降幅明显不等于延迟降幅，说明主干以外的耗时仍影响部署收益。

### 下一步读哪里

检查任务注意力取自哪里、token 怎样压缩、逆 Simpson 指标如何映射到预算，以及窗口长度和最低保留量；再看硬件、绝对延迟和真机失败案例。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-22/FastVLA Task-Conditioned and Temporally Adaptive Visual Token Compression for Ef.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.22146v2 Announce Type: replace Abstract: Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often multi-view images are encoded into hundreds of visual tokens that dominate transformer computation and latency. Token compression via attention is a natural solution but is challenging for VLA control because (1) decision-critical tokens are determined by the task, not generic visual saliency, and (2) the token budget varies substantially across steps, so static metrics and budgets waste computation or discard control-critical tokens. We introduce FastVLA, a training-free, task-aware, and temporally adaptive visual token compression framework. At each step, FastVLA scores token importance via task-to-vision attention and adaptively sets the compression rate from the importance-distribution uniformity, measured by an inverse-Simpson metric with online sliding-window calibration. We evaluate FastVLA on OpenVLA, OpenVLA-OFT, and CogACT across LIBERO and SIMPLER, and on a physical Franka Research 3 robot. In simulation, it reduces LLM-backbone FLOPs by 35-59\% and action latency by 9-32\% (a 1.09$\times$-1.46$\times$ speedup) while maintaining task success, achieving a comparable or better efficiency-performance trade-off than existing plug-and-play token compression/pruning/reuse baselines. On the real robot, it cuts action-prediction latency by 20\% (1.25$\times$ speedup) at comparable success. Code is available at https://github.com/jiuyixu25/FastVLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22146
- Authors: Jiuyi Xu, Chengyuan Qian, Zhengzhong Tu, Yang Sui, Yangming Shi
- Published: Wed, 21 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
