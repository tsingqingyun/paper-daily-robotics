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
url: "https://arxiv.org/abs/2611.33635v1"
published: "2026-11-25T02:03:41Z"
age_days: 1
score: 32
created: 2026-11-26
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> FreshVLA 从没有动作标签的视频里学两种线索：任务大体进行到哪，以及局部动作怎么动。它让编码器多关注画面变化，再把这两种线索和真实机器人动作一起交给策略学习。

## 问题

无动作标签视频能看到物体和手的变化，却没有可直接监督机器人的控制指令。若只要求从潜在动作重建画面，编码可能用掉容量去记背景和场景身份。摘要还指出，同一组有限的离散代码容易混杂不同速度的变化，例如手已经移到杯口附近，与夹爪此刻应该怎样微调。

### 用一个例子理解

理解用例（非论文实验）：输入是一段无动作标签的插销视频。较长时间窗可提供从靠近到对准再到插入的进度线索，较短窗口可提供接触前的微小横向修正。训练时把这两类表示与机器人控制数据联合学习，最终得到能输出自身控制动作的策略。

## 创新点或方法

先用高通先验引导视频编码器关注发生变化的区域，再通过跨时间尺度采样和频域约束，把连续潜在动作组织成粗粒度进度和细粒度执行动态。训练控制策略时冻结预训练的编码器，用流匹配联合学习潜在动作与机器人动作。摘要未说明推理时两个分支如何参与生成、编码器是否在线调用，以及具体的采样间隔和频域约束形式。

### 方法如何工作

1. 从无标签视频取视觉变化，用高通先验增加动态区域在编码中的作用。
2. 用不同时间跨度取样并施加频域约束，让连续表示分别捕捉任务进度和局部执行动态。
3. 冻结视频编码器，把学到的表示与机器人动作一起用于流匹配训练，建立到控制的联系。
4. 部署训练后的策略输出机器人动作。编码器是否在线参与，摘要只说明到此。

### 必要术语

- 潜在动作：从画面变化中学出的向量，在本文中用来把视频里的运动线索带入控制策略。
- 高通先验：让较快变化更有影响的设计，在本文中用来减少编码器依赖静态外观。
- 流匹配：学习样本如何从简单分布逐步变化到目标分布的生成训练方法，在本文中用于联合建模潜在动作和机器人动作。

## 证据

摘要报告，LIBERO 和 LIBERO-Long 平均成功率分别为 98.2% 和 98.0%，后者较 GR00T-N1.6 高 3.6%。CALVIN 平均序列长度为 4.52，零样本 LIBERO-PLUS 总体成功率为 80.4%。在 35 步动作回归中，相对误差降幅比层级离散版本高 51.3 个百分点。真机平均成功率较 π₀.₅ 高 7.5%。摘要把两项基线差值记作百分比，未解释计算口径，也未列真机任务、试验次数或波动范围。

## 局限

摘要报告了视觉扰动下的稳健性和两个分支更清晰的频率分工。我会核查高通先验在相机移动或背景持续变化时是否仍能抓住操作区域，以及高通、时间分层和连续表示各自贡献多少。动作回归的对照与真机成功率回答的是不同问题。

- **判断**：值得读到预训练目标、推理流程和消融，尤其要确认两个时间尺度各保存了哪些线索，以及这些线索怎样进入实际动作。

## 研究关联

从视频学控制线索时，可以按时间尺度设计训练目标。任务进度需要跨一段时间辨认，接触附近的微调则要尽量保留短时变化。对于同时包含长流程和精细操作的任务，这是一种可以直接做对照实验的设计选择。

### 下一步读哪里

先看高通先验作用在哪类视觉输入、两个时间尺度如何采样，再查推理需要哪些分支。核对 35 步回归的误差分母、离散版本是否有可比容量，以及真机比较的任务与重复次数。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/FreshVLA Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning reusable latent actions from action-free videos offers an effective route to improving Vision-Language-Action (VLA) policies. However, reconstruction-oriented latent actions do not necessarily benefit policy learning: as they may encode task-irrelevant static appearance with scene identity, or entangle slowly varying task progress with fine-grained execution dynamics in limited discrete code. We propose FreshVLA, a VLA framework built on a frequency-guided, dynamics-sensitive learning paradigm for acquiring temporally hierarchical continuous latent actions. FreshVLA uses a high-pass prior to guide visual transition encoding toward dynamical regions, thereby reducing reliance on static appearance cues. It further organizes latent actions into coarse-grained task progress and fine-grained execution dynamics through cross-timescale sampling and frequency-domain regularization, enhancing their capacity to represent long-horizon behaviors. During policy training, we freeze the pretrained latent action encoder and transfer its representations to robot control through joint flow-matching of latent and robot actions. FreshVLA achieves 98.2% average success on LIBERO and 98.0% on LIBERO-Long, exceeding GR00T-N1.6 on the latter by 3.6%. It also reaches an average sequence length of 4.52 on CALVIN and strong overall success rate of 80.4% in the zero-shot LIBERO-PLUS evaluation. Furthermore, FreshVLA exhibits greater robustness to visual perturbations and a more distinct division of roles between two branches in modeling low- and high-frequency motion, respectively. In 35-step action regression, it achieves a 51.3-percentage-point higher relative error reduction than its hierarchical discrete counterpart. Real-world experiments demonstrate that FreshVLA improves the average success rate over $π_{0.5}$ by 7.5%. The FreshVLA project page is available at https://freshvla.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33635v1
- Authors: Jiaming Liang, Yifeng Zhan, Rongyi He, Mu Li, Jiaqi Fan, Zhiyuan Zhang, Qiwei Liang, Zhengjie Zhang, Boyang Cai, Ningyuan Zhang, Xingjian Jing, Qiang Nie
- Published: 2026-11-25T02:03:41Z
- Age days: 1

</details>
