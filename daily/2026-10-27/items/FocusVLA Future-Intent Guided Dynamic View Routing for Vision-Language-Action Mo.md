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
url: "https://arxiv.org/abs/2610.31423v1"
published: "2026-10-22T15:25:02Z"
age_days: 4
score: 33
created: 2026-10-27
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> FocusVLA 让机器人根据接下来可能发生的交互，动态决定更依赖全局相机还是腕部相机。关键是从历史动作预测未来交互意图，再用这个预测引导视角路由。

## 问题

多视角操作需要同时掌握物体、末端执行器及其空间关系，但多放几个相机不保证策略会用。作者观察到现有 VLA 持续偏向腕部视角，难以随着操作阶段调整全局与局部观察的依赖，因此不同阶段的适应性和鲁棒性受限。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放到托盘上”、两路图像和近期动作；系统预测即将接近杯子时利用全局位置，进入抓取阶段后增加局部观察的作用，最后输出机械臂动作。这是机制示意，具体路由形式待核查。

## 创新点或方法

旧做法输入多视角，却可能一直依赖同一视角；FocusVLA 增加未来意图预测和动态路由，让动作生成时的观察选择跟随交互阶段变化。历史动作提供“接下来要干什么”的线索，帮助选择当前更有用的空间信息。推理时这两个模块参与动作生成；它们如何训练、意图用什么标签表示、路由是加权还是选择，摘要未说明。

### 方法如何工作

1. 读取历史动作，获得当前操作进程的线索，避免只凭单帧猜阶段。
2. 预测未来交互意图，为接下来需要什么观察提供条件。
3. 根据意图动态路由全局和局部视角，让动作生成使用阶段相关的信息。
4. 生成并执行动作；模块如何训练、路由如何计算，摘要只说明到此。

### 必要术语

- VLA：把视觉、语言指令转成动作的模型；本文在其动作生成过程中加入观察调节。
- 未来交互意图：对接下来交互的预测；本文用它指导视角路由，具体表示未说明。
- 视角路由：调节不同相机信息如何被使用；本文用它改变全局与局部观察的依赖。

## 证据

摘要报告：在 RoboTwin 2.0 上，平均成功率比最强基线 π0.5 高 10.10 个百分点；真机成功率从 71.7% 升至 85.0%，相差 13.3 个百分点，摘要将其称为 13.3% 增益。未给任务数、试验次数、方差和分任务成绩。结果支持所测仿真与真机任务上的整体收益，但不能单凭总成功率确定收益全部来自更合理的视角选择。

## 局限

摘要称模块可接入现有 VLA 而不修改核心架构，但这不等于无需训练或没有延迟。还需核查意图预测错误时是否会选错视角，以及遮挡、相机变化下的表现；真机结果的适用范围取决于未提供的任务设置。

- **判断**：值得细读意图定义和路由消融，因为真正可借鉴的是“预判下一步交互如何改变当前观察”，而不只是成功率数字。

## 研究关联

具体启示是：传感器信息是否充分，与策略是否在合适时刻使用它，是两个问题。当任务在定位目标和局部接触之间切换时，可以尝试用动作历史指导观察分配，而不是只增加图像输入。

### 下一步读哪里

先核查未来意图的预测目标、训练监督和路由公式，再看去掉历史动作、意图预测或动态路由各有什么变化；同时检查真机任务、重复次数和推理开销。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-27/FocusVLA Future-Intent Guided Dynamic View Routing for Vision-Language-Action Mo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have become an important paradigm for robotic manipulation by unifying visual perception, language understanding, and action generation. Since reliable manipulation requires sufficient observation of objects, end-effectors, and their spatial relationships, multi-view inputs are widely used to provide complementary spatial information. However, our experiments show that existing VLA models do not fully exploit such multi-view complementarity. The policy tends to persistently rely on the wrist view, lacking the ability to dynamically adjust global-local view dependency across manipulation stages, which limits stage adaptability and robustness. To address this issue, we propose FocusVLA, a stage-aware multi-view routing framework. FocusVLA predicts future interaction intent from historical actions and uses it to guide dynamic view routing during action generation. By adaptively coordinating global and local observations across different task stages, FocusVLA improves multi-view utilization. On RoboTwin 2.0, FocusVLA improves the average success rate over the strongest baseline $π_{0.5}$ by 10.10 pp. In real-world evaluation, FocusVLA improves the success rate from 71.7\% to 85.0\%, achieving a 13.3\% gain over $π_{0.5}$. Moreover, the intent prediction and dynamic routing modules of FocusVLA can be integrated into existing VLA frameworks without modifying their core architectures.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.31423v1
- Authors: Huixin Xu, Ziya Yu, Peng Li
- Published: 2026-10-22T15:25:02Z
- Age days: 4

</details>
