---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02717"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 27
created: 2026-09-04
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# MV-dVRK: A Multi-Viewpoint Benchmark for Spatial Surgical Perception

> [!summary] 先说人话（基于摘要）
> MV-dVRK提供首个具有曝光同步多路立体内窥镜、准确表面几何和相机位姿的离体手术多视角基准，并比较单目、双目、多双目及多视图3D重建。结果显示增加视角有用，但优化式方法仍明显领先前馈基础模型。

## 这篇到底在做什么

- **卡在哪里**：临床遥操作通常只有一套体内立体相机，多视角手术数据极少，现有稀疏多视图重建方法因而从未在真实内窥镜图像上被严格比较。
- **关键解法**：静态子集用工业3D扫描仪验证稠密SfM参考几何，提供真值相机位姿和稀疏视角测试；控制视角数量，零样本比较多类重建方法。另含组织变形与运动复杂度递增的动态序列。
- **拿什么证明**：使用两套内窥镜时，多双目重建覆盖率最高；加入第三视角后，优化式多视图方法最佳，在1毫米误差内覆盖67%的真值表面点并恢复高精度相对位姿，前馈基础模型仅覆盖43%。数据还包含10条动态手术序列。

## 值不值得读

- **和你的研究有什么关系**：对手术机器人和具身空间感知研究者，它补上了真实内窥镜多视图评测空白，也直接揭示通用视觉基础模型在精密毫米级几何上的差距。
- **先别急着信**：数据为离体场景，且摘要中的最佳定量结果来自静态重建；动态组织变形条件下的方法表现尚未报告。
- **判断**：手术视觉和精细3D重建研究者应精读；基准的稀缺性和毫米级真值使它比单一方法排名更值得关注。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/MV-dVRK A Multi-Viewpoint Benchmark for Spatial Surgical Perception.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.02717v1 Announce Type: cross Abstract: Large-scale training and refined optimization techniques have greatly improved sparse multi-view 3D reconstruction. Despite their relevance to surgery, such methods have never before been rigorously evaluated on real endoscopic images. Current clinical telerobots deploy a single stereo camera inside the patient, making multi-viewpoint data extremely rare. This paper presents MV-dVRK, the first ex-vivo surgical dataset to combine multiple exposure-synchronized stereo viewpoints with accurate surface geometry and camera poses. The static subset of the benchmark provides dense SfM reference geometry, validated against an industrial 3D scanner, together with ground-truth camera poses and sparse-view test sets. We use MV-dVRK to systematically compare zero-shot monocular, stereo, multi-stereo, and multi-view 3D reconstruction methods as the number of viewpoints increases. With two endoscopes, multi-stereo reconstruction achieves the highest coverage. With a third viewpoint, optimization-based multi-view methods perform best, covering 67% of ground-truth surface points within a 1 mm tolerance and recovering highly accurate relative camera poses. By contrast, feed-forward foundation models cover only 43% of the ground-truth surface in the same setting. MV-dVRK also includes ten dynamic sequences spanning multiple surgical tasks, with increasing kinematic complexity and tissue deformation, providing a basis for future research in multi-viewpoint surgical perception. The project is available at: https://mv-dvrk.is.mpg.de.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02717
- Authors: Guido Caccianiga, Sergey Prokudin, Yutong Chen, Bernard Javot, Rachael L'Orsa, Omer Burak Alada\u{g}, Yarden Sharon, Jens Rolinger, Ivan Capobianco, Anton Deguet, Siyu Tang, Katherine J. Kuchenbecker
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
