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
url: "https://arxiv.org/abs/2601.22153"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 47
created: 2026-10-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> 机器人算完动作时，移动物体可能已经不在刚才的位置。DynamicVLA 一边执行一边继续推理，并丢掉动作序列中已经过期的前半段，让实际执行尽量跟上物体运动。

## 问题

任务是抓取、操作运动中的物体。真正瓶颈是感知与执行之间的时间差：静态场景里，旧画面往往仍然有用；动态场景里，依据旧位置生成的动作到执行时已经失效。摘要认为，已有 VLA 在静态操作上的表现不能直接解决这种延迟造成的错位。

### 用一个例子理解

理解用例（非论文实验）：输入是“拿起传送带上的红色杯子”和当前画面；模型预测一段接近杯子的动作，同时机器人继续运动；新预测返回后，系统去掉已经错过执行时刻的前段，输出可继续执行的后段。这个例子解释时间对齐，不代表论文验证过传送带任务。

## 创新点或方法

原来的问题链条是“看一帧、等待模型算完、执行基于旧状态的动作”。本文同时改三处：用紧凑的 0.4B 模型和卷积视觉编码器缩短计算；让推理与执行重叠，避免控制被推理阻塞；用 Latent-aware Action Streaming 丢弃因延迟而失效的动作前缀，只执行仍与当前时间对应的后缀。巧处是把动作当成有有效时刻的序列，而非算出来就全执行。训练方面，作者建设 DOM 数据基础，但摘要未说明损失、具体训练流程或时间信息如何编码；推理方面，重叠调度与前缀裁剪则是明确改动。

### 方法如何工作

1. 图像和指令进入紧凑模型，得到一段候选动作；缩短计算时间是为了少落后于物体状态。
2. 机器人执行期间继续进行下一轮推理，产生更新的动作；这样控制不必每轮都停下来等待。
3. 检查返回序列中因延迟而失效的前缀并丢弃，留下时间仍有效的后缀；具体判定规则摘要未说明。
4. 执行保留下来的动作并持续更新，让后续控制不断获得较新的预测。

### 必要术语

- 感知—执行错位：看到的状态与动手时的状态不同；本文要处理由推理延迟造成的错位。
- 动作块：一次预测的一串动作；本文需要判断其中哪些部分仍能执行。
- 连续推理调度：执行动作时仍继续计算下一轮动作；本文用它减少等待。
- 动作前缀：预测序列最前面的一段；本文丢弃其中已经失效的动作。

## 证据

摘要给出 DOM 的规模：200K 合成回合，覆盖 2.8K 场景和 206 个物体，并能无需遥操作地快速收集 2K 真机回合。评估覆盖仿真和真实机器人，报告在变化的物体运动、需要较多视觉判断的指令和未见运动模式下提高成功率。摘要没有列出基线名称、成功率数值、测试次数或分项消融，因此可以确认评估范围，尚不能比较增益大小，也不能判断三个机制各贡献多少。

## 局限

摘要没有解释裁剪后怎样接续动作，也没有给出可承受的运动速度与延迟范围，这些是我的待核查问题。仿真与真机都做了评估，但两者的结果没有分别给出；不能据此认定任意快速运动都能处理。

- **判断**：值得读到控制调度和动作裁剪的实现细节，因为这两处决定它是否真正解决执行时的时间错位。

## 研究关联

当环境变化速度接近模型推理速度时，减少延迟和处理延迟都值得考虑。这里可借鉴的是：除了加速模型，还检查预测序列中哪些动作在执行时仍有效；这种思路尤其适合连续输出多个动作的控制方式。

### 下一步读哪里

先核查动作的有效时刻如何确定、裁剪是否需要时间戳，以及新旧动作如何衔接；再找分别关闭模型加速、重叠推理、动作裁剪的实验，并查看真机速度和端到端延迟。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：47
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/DynamicVLA A Vision-Language-Action Model for Dynamic Object Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2601.22153v2 Announce Type: replace Abstract: Manipulating dynamic objects remains an open challenge for Vision-Language-Action (VLA) models. Although recent VLAs generalize well in static manipulation, dynamic scenes introduce a latency-induced perception-execution mismatch: object states continue to evolve during inference, making actions predicted from past observations stale at execution time. We present DynamicVLA, a latency-aware VLA model for dynamic object manipulation. It combines a compact 0.4B architecture and convolutional vision encoder for efficient multimodal inference with a continuous inference schedule that overlaps reasoning and execution for non-blocking control. Latent-aware Action Streaming then discards latency-invalid action prefixes and executes only the temporally valid suffix of each predicted chunk, preserving action-time alignment under dynamic object motion. To fill the missing foundation of dynamic manipulation data, we introduce the Dynamic Object Manipulation (DOM) benchmark, built with an automated collection pipeline that gathers 200K synthetic episodes across 2.8K scenes and 206 objects, and enables fast collection of 2K real-world episodes without teleoperation. Extensive evaluations in simulation and on real robots show that DynamicVLA improves dynamic manipulation success under changing object motion, perception-heavy instructions, and unseen motion patterns.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2601.22153
- Authors: Haozhe Xie, Beichen Wen, Jiarui Zheng, Zhaoxi Chen, Fangzhou Hong, Haiwen Diao, Ziwei Liu
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
