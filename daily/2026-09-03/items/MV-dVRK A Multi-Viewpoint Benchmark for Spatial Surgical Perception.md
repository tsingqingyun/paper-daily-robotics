---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02717v1"
published: "2026-09-02T15:25:28Z"
age_days: 0
score: 27
created: 2026-09-03
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# MV-dVRK: A Multi-Viewpoint Benchmark for Spatial Surgical Perception

> [!summary] 先说人话（基于摘要）
> MV-dVRK 提供首个结合多台曝光同步立体内窥镜、精确表面几何和相机位姿的离体手术多视角基准。结果显示两台内窥镜时 multi-stereo 覆盖最好，加入第三视角后优化式多视图方法明显胜过前馈基础模型。

## 这篇到底在做什么

- **卡在哪里**：真实内窥镜多视角数据稀缺，现有稀疏3D重建方法虽进展迅速，却未在真实手术图像上严格验证；组织形变、复杂反光和视角约束使普通数据集难以代表临床感知。
- **关键解法**：静态子集以工业3D扫描仪验证的稠密 SfM 几何、真值位姿和稀疏视角测试组成，并随视角数系统比较单目、双目、多双目和多视图零样本方法；另含动态手术序列。
- **拿什么证明**：第三视角下，优化式多视图方法在1毫米阈值内覆盖67%的真值表面点，前馈基础模型为43%；数据还含10段动态序列，覆盖多种手术任务、运动复杂度和组织形变。

## 值不值得读

- **和你的研究有什么关系**：它为手术机器人和多模态基础模型提供了真实、毫米级的空间感知试金石，也证明通用前馈模型在临床几何精度上尚未取代优化方法。
- **先别急着信**：数据为离体环境，摘要也未说明样本规模、器械遮挡和动态序列是否具备稠密几何真值；临床外推有限。
- **判断**：值得精读数据采集、标定和评价协议；对手术三维感知而言，基准价值高于任何单一模型排名。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/MV-dVRK A Multi-Viewpoint Benchmark for Spatial Surgical Perception.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Large-scale training and refined optimization techniques have greatly improved sparse multi-view 3D reconstruction. Despite their relevance to surgery, such methods have never before been rigorously evaluated on real endoscopic images. Current clinical telerobots deploy a single stereo camera inside the patient, making multi-viewpoint data extremely rare. This paper presents MV-dVRK, the first ex-vivo surgical dataset to combine multiple exposure-synchronized stereo viewpoints with accurate surface geometry and camera poses. The static subset of the benchmark provides dense SfM reference geometry, validated against an industrial 3D scanner, together with ground-truth camera poses and sparse-view test sets. We use MV-dVRK to systematically compare zero-shot monocular, stereo, multi-stereo, and multi-view 3D reconstruction methods as the number of viewpoints increases. With two endoscopes, multi-stereo reconstruction achieves the highest coverage. With a third viewpoint, optimization-based multi-view methods perform best, covering 67% of ground-truth surface points within a 1 mm tolerance and recovering highly accurate relative camera poses. By contrast, feed-forward foundation models cover only 43% of the ground-truth surface in the same setting. MV-dVRK also includes ten dynamic sequences spanning multiple surgical tasks, with increasing kinematic complexity and tissue deformation, providing a basis for future research in multi-viewpoint surgical perception. The project is available at: https://mv-dvrk.is.mpg.de.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02717v1
- Authors: Guido Caccianiga, Sergey Prokudin, Yutong Chen, Bernard Javot, Rachael L'Orsa, Omer Burak Aladağ, Yarden Sharon, Jens Rolinger, Ivan Capobianco, Anton Deguet, Siyu Tang, Katherine J. Kuchenbecker
- Published: 2026-09-02T15:25:28Z
- Age days: 0

</details>
