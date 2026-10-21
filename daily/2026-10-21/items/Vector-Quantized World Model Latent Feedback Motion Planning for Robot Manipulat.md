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
url: "https://arxiv.org/abs/2610.25600v1"
published: "2026-10-19T00:06:44Z"
age_days: 2
score: 40
created: 2026-10-21
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Vector-Quantized World Model: Latent Feedback Motion Planning for Robot Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> VQ-WM 把长任务拆成一串视觉状态：先在离散状态之间找路线，再让连续控制器看着实际画面逐段走到。巧处是按“控制器需要多久才能到达”划分状态，让规划地图更贴近机器人真正能走的路。

## 问题

任务是从视觉观测规划并执行长程操作，例如完成汉诺塔。困难有三层：预测越远，误差越容易累积；连续空间里的路线太多，搜索昂贵；预测出的中间状态还可能是控制器到不了的。摘要指出，已有视觉世界模型会遇到这些问题，而所比较的基础模型在汉诺塔上依赖训练集中出现完整解题轨迹。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“把积木移到盒内”的目标；系统把当前与目标映射为离散状态，搜索经过可抓取、已抬起、位于盒上方等状态的路线；控制器根据实时图像逐段输出动作，最终完成放置。这些具体中间状态仅用于解释。

## 创新点或方法

旧做法在连续潜空间中预测未来，或按欧氏距离把状态归类；但视觉表示接近，不代表动作上容易互达。VQ-WM 改用首次到达时间的估计来组织量化状态，再学习离散状态之间的转移。训练得到状态表示、转移预测器和连续控制器；具体损失及训练顺序未说明。推理时先搜索通往目标的最短离散路径，再用视觉反馈逐段执行，实际偏离时由控制器纠正。

### 方法如何工作

1. 把视觉状态量化为有限节点，并让划分考虑到达时间，以便压缩空间时保留执行难度。
2. 学习节点之间的转移，得到能搜索的状态连接关系，避免直接穷举连续未来。
3. 从当前节点搜索到目标的最短路径，产生连续控制器要依次达到的中间目标。
4. 控制器读取实时视觉并逐段行动，用反馈修正偏差，减少长程误差积累；具体重规划机制摘要未说明。

### 必要术语

- 向量量化：把连续表示归入有限个代表状态；本文用它建立离散搜索空间。
- 首次到达时间：从一个状态第一次到达另一个状态所需的时间；本文用其估计反映控制难度。
- 准度量：允许两个方向距离不同的距离规则；本文借此表达去程与回程可能难度不同。

## 证据

摘要报告：真实机器人汉诺塔任务中，仅用短时自由操作数据训练，VQ-WM 达到 100% 成功率；所比较的 VLA、WAM 基础模型仅在训练数据包含解题轨迹时成功。摘要还报告，在覆盖操作与运动控制的仿真基准中，相对最强世界模型提高 13.3—85.3 个百分点。未给出试验次数、汉诺塔规模、具体基线及各任务结果，因此支持这些设置下的长程组合能力，尚不能据此判断任意长任务的可靠性。

## 局限

提供的摘要没有展开适用条件。我会核查到达时间估计面对未见状态是否可靠，以及视觉闭环能纠正多大偏差。真实汉诺塔证据与仿真跨任务证据应分别看；整体成功也不能单独证明收益主要来自新距离，而不是搜索或反馈控制。

- **判断**：值得深入读方法与消融，因为它直接处理了长程规划中“路线合理但执行不到”的断点。

## 研究关联

值得借鉴的是按执行难度压缩状态，而非只按视觉相似度压缩。当规划器总选出低层控制器无法完成的中间目标时，可以先检查：规划使用的距离，是否真的反映控制器的可达能力。

### 下一步读哪里

先核查首次到达时间怎样估计、为何允许方向不对称，以及它如何参与量化；再检查离散转移是否对应可执行动作、偏离后的处理方式，以及去掉新距离和视觉反馈各自损失多少。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/Vector-Quantized World Model Latent Feedback Motion Planning for Robot Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visual world models have shown strong potential for robot planning, yet long-horizon manipulation remains challenging due to compounding prediction errors, large search complexity, and latent plans that the low-level controller cannot reliably reach. In this work, we introduce Vector-Quantized World Model (VQ-WM), a latent feedback motion planning framework that integrates discrete long-horizon search with continuous visual feedback control: a discrete latent predictor models transitions between vector-quantized latent states, allowing the planner to look far ahead and find a shortest path to the goal through discrete search and a continuous learned controller sequentially reaches the planned states through visual feedback, correcting deviations to mitigate compounding errors. Whereas most vector quantization uses Euclidean distance, we use a novel estimator of the first-passage-time as a quasi-metric, which aligns the planning abstraction with the controller's capabilities. We evaluate on the physical robot manipulation of the Tower of Hanoi puzzle: whereas existing state-of-the-art foundation models (VLAs, WAMs) only succeed when the solution trace in their training dataset, our method achieves 100\% success rate with only short-play data, demonstrate its ability to compose long-horizon solutions beyond the short demonstrated trajectories and execute them reliably. Our solution also outperforms strongest world-models by 13.3--85.3 percentage points on simulation benchmarks spanning manipulation and locomotion, demonstrating consistent progress and new capabilities.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.25600v1
- Authors: Xuezhou Xu, Chung-Pang Wang, Zhenzhen Li, Benjamin Riviere
- Published: 2026-10-19T00:06:44Z
- Age days: 2

</details>
