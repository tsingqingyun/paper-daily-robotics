---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19463v1"
published: "2026-09-16T22:05:05Z"
age_days: 1
score: 29
created: 2026-09-18
concepts: ["AI 核心知识地图"]
---

# ParticleSplat: Self-supervised Object-centric Latent Particle Splatting

> [!summary] 先说人话（基于摘要）
> ParticleSplat把多视角场景压缩成可移动、可编辑的三维潜粒子，并用这些粒子生成三维高斯来重建画面，使对象表示具备明确空间结构。

## 问题

已有Deep Latent Particles主要是二维表示，难以显式表达机器人操作需要的三维位置与几何关系。

## 创新点或方法

输入多视角图像及相机位姿，联合编码成共享的三维对象中心潜空间，再转成与粒子对齐的三维高斯重建场景，以新视角合成目标自监督训练。

## 证据

摘要称在仿真和真实数据中无需掩码监督即可学出对象掩码，支持通过修改潜粒子移动物体，并改善下游机器人操作表现；摘要未给出可核查的结果数字。

## 局限

需核查粒子与语义对象的对应质量，以及操作任务收益；静态场景表示和编辑能力不能直接说明学到了交互动力学。

- **判断**：做三维对象表示值得读方法与下游验证，世界模型研究者应先确认其是否覆盖自己需要的动态建模能力。

## 研究关联

在AI核心知识地图中，可将其放在对象中心表示、自监督学习与三维场景重建的交叉处；对机器人学习的价值是提供结构化空间输入。

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/ParticleSplat Self-supervised Object-centric Latent Particle Splatting.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present ParticleSplat, a self-supervised object-centric learning method that decomposes scenes into a set of latent ''particles'' representing semantic entities through feedforward 3D Gaussian Splatting. Building on the Deep Latent Particles (DLP) framework, which represents images as a set of particles with attributes such as position, scale, and visual appearance, we address a key limitation of DLP: its inherently 2D nature, which prevents explicit 3D spatial and geometric reasoning that are critical for downstream tasks such as robotic manipulation. Leveraging the structural similarity between latent particles and 3D Gaussian primitives, we introduce a 3D latent particle space trained with a novel view synthesis objective. Our model jointly encodes multiple views with camera poses into a shared 3D object-centric latent space, then transforms particles into particle-aligned 3D Gaussians whose composition reconstructs the full scene. On simulated and real-world datasets, we show that this formulation inherently learns object masks without supervision and supports controllable 3D scene editing, such as moving objects by modifying particles in the latent space. We further establish that the learned 3D representation improves downstream performance on robotic manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19463v1
- Authors: Lyuxing He, Daniel Guo, Elizabeth Terveen, Deepak Pathak, David Held, Tal Daniel
- Published: 2026-09-16T22:05:05Z
- Age days: 1

</details>
