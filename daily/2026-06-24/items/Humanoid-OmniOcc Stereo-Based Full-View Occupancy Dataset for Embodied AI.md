---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22971v1"
published: "2026-06-22T07:52:25Z"
age_days: 1
score: 40
created: 2026-06-24
concepts: ["世界模型", "Sim2Real"]
---

# Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI

> [!summary] 一句话结论（基于摘要）
> Extensive experiments show that Humanoid-OmniOcc consistently outperforms monocular baselines and generalizes well to both unseen simulated test scenes and real-world environments, validating the effectiveness of the Real2Sim2Real design.

## 关键点

- **问题**：Existing occupancy datasets, however, are predominantly designed for autonomous driving with vehicle-centric biases -- forward- facing cameras, far-field geometry, and static road priors -- limiting their applicability to embodied humanoid perception.
- **创新点 / 方法**：We present Humanoid-OmniOcc, a large- scale panoramic stereo-based occupancy dataset tailored for humanoid robots.
- **证据**：Extensive experiments show that Humanoid-OmniOcc consistently outperforms monocular baselines and generalizes well to both unseen simulated test scenes and real-world environments, validating the effectiveness of the Real2Sim2Real design.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[Sim2Real]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-24/Humanoid-OmniOcc Stereo-Based Full-View Occupancy Dataset for Embodied AI.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Occupancy prediction at voxel-level granularity is essential for safe robotic navigation
and interaction in complex environments. Existing occupancy datasets, however, are
predominantly designed for autonomous driving with vehicle-centric biases -- forward-
facing cameras, far-field geometry, and static road priors -- limiting their
applicability to embodied humanoid perception. We present Humanoid-OmniOcc, a large-
scale panoramic stereo-based occupancy dataset tailored for humanoid robots. The dataset
encompasses 15 diverse simulated indoor scenes and 5 real-world environments, yielding
over 155K samples with broad scene and style diversity. Importantly, the dataset is
designed around a Real2Sim2Real closed-loop paradigm: real sensor specifications drive
physically accurate simulation, simulation produces large-scale annotated training data,
and models trained in simulation are directly evaluated on real-world captures --
enabling iterative refinement of the sim-to-real pipeline. We further propose
\textbf{H}umanoid \textbf{S}urround \textbf{S}tereo-guided \textbf{Occ}upancy model
(Humanoid-OmniOcc) that exploits robust depth priors for accurate 2D-to-3D lifting.
Extensive experiments show that Humanoid-OmniOcc consistently outperforms monocular
baselines and generalizes well to both unseen simulated test scenes and real-world
environments, validating the effectiveness of the Real2Sim2Real design. Code and data
will be available upon acceptance at https://d-robotics-ai-lab.github.io/humanoid-
omniocc.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22971v1
- Authors: Xianda Guo, Bohao Zhang, Chenwei Huang, Shiyuan Chen, Ruilin Wang, Yiqun Duan, Cong Yang, Qin Zou, Wei Sui
- Published: 2026-06-22T07:52:25Z
- Age days: 1

</details>
