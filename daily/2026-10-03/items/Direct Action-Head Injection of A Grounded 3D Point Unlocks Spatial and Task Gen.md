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
url: "https://arxiv.org/abs/2606.27663"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-10-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Direct Action-Head Injection of A Grounded 3D Point Unlocks Spatial and Task Generalization

> [!summary] 这篇论文到底做了什么（基于摘要）
> 3D Point Injection 把目标定位信息变成三维点，并通过两层 MLP 直接送进 VLA 的动作头。关键是让负责生成动作的模块直接收到空间目标，而不是仅把坐标写进提示。

## 问题

任务是在物体位置改变、或熟悉场景配上不同指令时完成操作。VLA 在这些条件下仍容易失效。已有方法提供二维像素定位或放置信号，但作者认为，仅有定位信号不够，它用什么表示、送到模型哪里，会显著影响动作是否利用它。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“拿起右边的杯子”；定位模块给出该杯子的二维位置，系统将其转换为三维点，MLP 编码后送入动作头，输出朝目标杯子运动的动作。例子不代表论文已验证这一任务。

## 创新点或方法

旧做法用语言或视觉提示表达定位信息；本文把合适的二维定位转换到三维，再用两层 MLP 生成嵌入，直接注入动作头。这样动作生成模块能直接读取空间信息。摘要称不改 VLA 主干或预训练流程，但未说明新增模块的训练数据、损失及哪些参数更新。推理时需要获得目标三维点并送入动作头；二维到三维转换所需的深度、标定或其他条件未说明。

### 方法如何工作

1. 根据观察和指令获得目标二维定位，为动作提供明确的目标位置。
2. 将定位转换为三维点，使目标以机器人操作所需的空间形式表达；摘要未说明转换细节。
3. 用两层 MLP 把三维点编码成嵌入，使动作头可以接收这项信息。
4. 把嵌入直接注入动作头，与已有条件共同生成动作，减少定位信息传递到动作决策的间接环节。

### 必要术语

- 定位信号（grounding）：指明指令对应哪个目标、位于哪里的信息；本文把它转换成三维点。
- 动作头：模型中负责输出动作的部分；本文将空间嵌入直接送到这里。
- MLP：多层全连接网络；本文用两层 MLP 将三维坐标编码为可注入的信息。

## 证据

摘要报告，LIBERO-PRO 上 GR00T-N1.6 的平均成功率在任务扰动下从 31.2 提高到 77.5，在位置扰动下从 28.1 提高到 60.2，分别增加 46.3 和 32.1 个百分点。摘要称 π₀.₅ 也有相近收益，并优于语言、视觉提示替代方案，但未给具体数值。另有真机实验，未给任务和结果。证据支持已测的扩散动作头 VLA，不能扩展到所有主干。

## 局限

摘要没有明确列出局限。我会核查三维点如何获取、定位误差多大时收益消失，以及实验是否使用理想定位。论文强调需要足够好的二维定位，因此上游定位质量是判断适用性的关键；目前不能把结果归因于三维表示或注入位置中的任一项单独作用。

- **判断**：值得细读定位来源与消融实验：方法简单、报告收益大，但复用前必须确认几何信息的获取成本和误差容忍度。

## 研究关联

这里值得借鉴的是，给策略补充外部信息时，要同时设计信息格式和入口。若瓶颈是目标空间位置，直接把几何信息送到动作生成处，可能比要求主干从提示中重新理解坐标更有效。

### 下一步读哪里

下一步检查二维转三维的条件、点代表抓取位置还是其他目标、嵌入怎样接入动作头，以及二维／三维和不同注入位置的消融；核查真机是否使用同一定位流程。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/Direct Action-Head Injection of A Grounded 3D Point Unlocks Spatial and Task Gen.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.27663v2 Announce Type: replace Abstract: Vision-Language-Action (VLA) models leverage large-scale vision-language pretraining for flexible robot manipulation, yet at test time they remain brittle to changed object positions and to familiar scenes paired with different instructions. A growing family of methods addresses this brittleness by supplying the policy with grounding signals, such as 2D pixel coordinates for object localization and placement. However, we find that how the grounding signal is represented and injected matters more than the signal itself. In this work, we propose a lightweight module that represents the grounding signal in 3D and injects the resulting embedding directly into the action head. The module is a two-layer MLP and requires no changes to the VLA backbone or pretraining pipeline, yet it yields substantially larger gains than language- or visual-prompting alternatives. On LIBERO-PRO, our method improves the average success rate of GR00T-N1.6 from $31.2$ to $77.5$ under task perturbation and from $28.1$ to $60.2$ under position perturbation. Comparable gains are also achieved for $\pi_{0.5}$, demonstrating that the mechanism is backbone-agnostic across VLAs with diffusion-based action heads. We further validate the practical applicability with real-world experiments. Together, these results support our central finding: lifting adequate 2D grounding into 3D and injecting it into the action head enables spatial and instance-level task generalization in VLAs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.27663
- Authors: Shiang-Feng Tsai, Jin-Cheng Jhang, Yen-Ling Tai, Jia-Hong Lai, Shih-Yun Wong, Kang-Tung Hsu, Yi-Ting Chen, Min Sun
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
