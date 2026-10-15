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
url: "https://arxiv.org/abs/2603.15046"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 42
created: 2026-10-15
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# AnolisVLA: Lightweight Vision-Language-Action Model with Deep State Space Models for Mobile Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> AnolisVLA 用深度状态空间模型处理视觉和语言序列，减少 VLA 生成动作轨迹的计算负担。摘要报告它在移动操作中同时取得更高成功率和更快推理。

## 问题

任务是根据画面和语言指令操作不同物体，并面向服务机器人部署。标准 Transformer 骨干计算成本高，限制资源较少的设备使用 VLA；这里要解决的是在有限计算条件下仍能及时生成有效动作。

### 用一个例子理解

理解用例（非论文实验）：输入机器人当前画面与“拿起桌上的杯子”，AnolisVLA 用状态空间模型处理视觉和语言，输出动作轨迹。机器人执行轨迹；是否逐轮更新内部状态、怎样接收新观察，摘要没有说明。

## 创新点或方法

旧做法用标准 Transformer 处理多模态序列，AnolisVLA 改用深度状态空间模型，以顺序状态建模处理视觉和文本，再生成轨迹。通俗地说，状态空间模型通过更新内部状态处理序列，但本文如何融合模态、构造状态和输出动作，摘要未说明。训练数据、损失及预训练流程也未交代；推理时使用该轻量骨干生成轨迹，速度优势由实验报告。

### 方法如何工作

1. 接收视觉观察与语言指令，为动作生成提供环境和目标信息。
2. 用深度状态空间模型处理多模态序列，得到供轨迹生成使用的表示；融合结构未说明。
3. 根据表示生成动作轨迹，形成机器人可执行的输出；动作空间和解码细节未说明。
4. 在仿真及两个真机平台测成功率和推理效率，检验计算节省是否伴随任务能力；训练流程摘要未说明。

### 必要术语

- 状态空间模型：通过更新内部状态处理序列的模型；本文用它承担多模态序列建模。
- 骨干：模型中主要负责处理输入的网络；本文替换它以降低计算负担。
- 移动操作：机器人移动与物体操作结合的任务；摘要在这类任务上给出量化比较。
- 百分点：两个百分比直接相减的单位；摘要的 21 个百分点不是相对提高 21%。

## 证据

摘要报告仿真和两个真机平台评估。与参数规模相近的 SmolVLA 相比，AnolisVLA 成功率更高、推理更快、GPU 显存相当，但未给具体数值。在移动操作中，相对 30 亿参数的 π₀.₅，成功率高 21 个百分点，推理约快三倍。这些数字来自摘要；任务组成、硬件、绝对延迟和训练条件未说明，所以不能直接推广到其他平台。

## 局限

我的待核查问题是，对比是否使用同等训练数据和相同推理硬件，以及加速来自骨干还是其他实现差异。更高成功率与更低延迟同时出现，不能据此断言前者由后者导致；两个真机平台也不能代表所有移动机器人。

- **判断**：值得读架构与效率评估，特别是硬件和训练条件；摘要给出实用的成功率与速度结果，但还不足以指导直接替换现有骨干。

## 研究关联

它提示我们把序列处理方式也当作机器人性能的变量。对于推理延迟占据明显执行时间的任务，状态空间骨干值得作为候选；但需要同时检查成功率、延迟和显存，摘要并未显示显存也显著降低。

### 下一步读哪里

我会检查视觉与语言如何进入状态空间模型、轨迹输出方式，以及延迟测量是否包含视觉编码和动作生成；再核查 SmolVLA、π₀.₅ 的训练条件与移动操作任务设置。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/AnolisVLA Lightweight Vision-Language-Action Model with Deep State Space Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2603.15046v2 Announce Type: replace Abstract: In this study, we address the problem of language-guided robotic manipulation, where a robot is required to manipulate a wide range of objects based on visual observations and natural language instructions. This task is essential for service robots that operate in human environments, and requires safety, efficiency, and task-level generality. Although Vision-Language-Action models (VLAs) have demonstrated strong performance for this task, their deployment in resource-constrained environments remains challenging because of the computational cost of standard transformer backbones. To overcome this limitation, we propose AnolisVLA, a lightweight VLA that uses a deep state space model to process multimodal sequences efficiently. The model uses lightweight, fast sequential state modeling to process visual and textual inputs. This design enables efficient trajectory generation. We evaluated the proposed method in simulation and on two real robot platforms. Compared with SmolVLA at a comparable parameter scale, AnolisVLA achieved higher task success rates, faster inference, and comparable GPU memory usage. In mobile manipulation, it outperformed the larger, 3-billion-parameter $\pi_{0.5}$ model by 21 percentage points in task success rate while achieving approximately three times faster inference.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2603.15046
- Authors: Yusuke Takagi, Motonari Kambara, Daichi Yashima, Koki Seno, Kento Tokura, Komei Sugiura
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
