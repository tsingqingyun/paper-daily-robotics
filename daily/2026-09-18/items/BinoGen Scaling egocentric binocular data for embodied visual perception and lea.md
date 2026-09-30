---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19881v1"
published: "2026-09-17T08:29:52Z"
age_days: 0
score: 27
created: 2026-09-18
concepts: ["多模态基础模型"]
---

# BinoGen: Scaling egocentric binocular data for embodied visual perception and learning

> [!summary] 先说人话（基于摘要）
> BinoGen自动生成带密集标注的第一视角双目视频，并可改变观察者的高度、视野和双目配置，用可控数据研究具身视觉。

## 问题

连续双目观测与密集标注难以大规模采集；视觉经验还受观察者身体和运动方式影响，只改变场景不足以覆盖这种差异。

## 创新点或方法

联合生成场景、物体配置、外观和运动轨迹，并配置双目相机；输出同步视频、深度、光流、法线、语义、物体坐标和相机位姿，还可在同一环境生成类人和类鼠配对观测。

## 证据

构建超过2000万张标注图像的数据集。摘要称加入数据持续改善真实深度估计、目标检测和视频跟踪；本体特定适配提升表现，联合训练可兼顾两类本体，但未提供增益数字。

## 局限

摘要结尾截断，且未给出真实任务提升幅度；大规模图像数量本身不能说明时序多样性或向机器人控制的迁移。

- **判断**：视觉预训练与合成数据方向值得读生成配置和真实测试，动作学习方向暂作数据资源线索。

## 研究关联

对多模态基础模型，价值在于可控地扩充具身视觉训练数据，并把观察几何作为独立研究变量。

- **概念**：[[多模态基础模型]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/BinoGen Scaling egocentric binocular data for embodied visual perception and lea.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied visual perception relies on temporally coherent visual experience accumulated through continuous engagement with the environment. However, collecting large-scale egocentric binocular observations together with dense annotations remains costly and difficult. Moreover, visual experience is shaped not only by the environment but also by the embodiment of the observer, including viewing height, field of view, binocular geometry, and motion through the scene. To address these challenges, we present BinoGen, an automated framework for generating large-scale, embodiment-aware egocentric binocular visual experiences in indoor environments. BinoGen jointly models environmental and observer variation through generative scene synthesis, probabilistic object instantiation, appearance randomization, stochastic trajectory generation, and configurable binocular camera setups. The framework produces synchronized binocular videos together with dense multimodal supervision, including depth maps, optical flow, surface normals, semantic maps, object coordinates, and camera poses. Using BinoGen, we construct a dataset comprising more than 20 million annotated images for supervised learning. We demonstrate two complementary utilities of BinoGen. First, incorporating BinoGen data consistently improves real-world visual perception, including depth estimation, object detection, and video object tracking. Second, paired human-inspired and mouse-inspired observations from the same environments enable controlled investigation of how observer embodiment affects perceptual learning. Embodiment-specific adaptation substantially improves performance, while joint training enables a single model to perform competitively across both embodiments. Together, these results demonstrate that large-scale, controllable visual experience can improve embodied perception...

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19881v1
- Authors: Chunpeng Li, Ya-tang Li
- Published: 2026-09-17T08:29:52Z
- Age days: 0

</details>
