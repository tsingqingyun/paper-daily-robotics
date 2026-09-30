---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29601v1"
published: "2026-08-30T06:46:18Z"
age_days: 2
score: 40
created: 2026-09-01
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# $\mathcal{N}_0$-Foundation: Towards the Age of Tactile Intelligence

> [!summary] 先说人话（基于摘要）
> N₀-Foundation 试图一次补齐触觉具身学习的硬件、数据、表征和评测基础设施：核心资产是 3 万小时 NeoData、跨传感器 NeoForce，以及 NeoReal/NeoSim 基准。

## 问题

现有操作语料缺少大规模、异构且同步的触觉信息，尤其限制柔性物体、精密装配、细致力控和持续表面接触任务；不同触觉设备的外观差异还妨碍表征迁移。

## 创新点或方法

系统以视觉触觉传感器、触觉 UMI 和同步视触采集系统收集机器人及 UMI 示范，产出配对 RGB—触觉数据；NeoForce 从异构测量中学习跨传感器表征，NeoReal 与 NeoSim 负责标准化评测。相较单一传感器或小规模数据工作，它覆盖六种 embodiment、数据采集到评测的完整链条。

## 证据

NeoData 超过 30,000 小时，覆盖六种 embodiment、450 个任务和数十亿配对帧，并开放其中 5,000 小时。摘要称 NeoReal 与 NeoSim 实验显示策略受益于物理接触状态而非设备特有的触觉外观，但未给出任务分数。


## 局限

宏大规模声明之外，摘要没有给出数据质量、任务分布、跨设备迁移幅度或策略收益数字，这些决定资源的实际含金量。

- **判断**：数据和基准研究者应精读，策略研究者至少应读数据组成与迁移实验；它的影响力更取决于资源可用性和质量，而不是新策略本身。

## 研究关联

对机器人学习和多模态基础模型研究者，其主要价值是把触觉从零散附加模态变成可规模化训练和比较的基础设施，可能直接推动接触丰富型操作。

- **概念**：多模态基础模型 机器人学习 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/$ mathcal{N}_0$-Foundation Towards the Age of Tactile Intelligence.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present $\mathcal{N}_0$-Foundation, a paradigm for tactile-enabled embodied manipulation, which integrates tactile sensing hardware, large-scale multimodal data, tactile representation learning, and standardized evaluation. First, we engineer the infrastructure for scalable data collection, including a vision-based tactile sensor, a tactile Universal Manipulation Interface (UMI), and a synchronized visuo-tactile data collection system supporting both robot embodiments and UMI-based demonstrations. Leveraging this infrastructure, we construct NeoData, which contains more than 30000 hours of synchronized visual and tactile demonstrations, spanning six embodiments, 450 tasks, and billions of paired RGB and tactile frames collected through a mixture of real-robot teleoperation and UMI-based demonstrations. To facilitate open research, we further release OpenNeoData, a 5000-hour open-source subset of NeoData. The dataset addresses a central limitation of existing manipulation corpora, critical for deformable-object manipulation, precise assembly, delicate force control, and sustained surface interaction. Capitalizing on the large-scale, heterogeneous tactile measurements, we propose NeoForce, a visuo-tactile representation model that learn transferable tactile representations across different sensor designs. To enable systematic evaluation of tactile embodied models built upon our infrastructure, datasets and tactile representations, we further propose a comprehensive benchmark, which combines the real-world NeoReal suite and the simulated NeoSim suite for standardized evaluation. Experiments across both suites show that policies benefit from the physical contact state rather than from the device-specific appearance of the tactile signal. We release the dataset, the representation, and the benchmark, aiming at supporting future work on tactile-enabled embodied manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29601v1
- Authors: NeoteAI Team, Fudan TEAI Team
- Published: 2026-08-30T06:46:18Z
- Age days: 2

</details>
