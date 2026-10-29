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
url: "https://arxiv.org/abs/2610.37350v1"
published: "2026-10-27T14:51:03Z"
age_days: 1
score: 30
created: 2026-10-29
concepts: ["具身智能评测与基准"]
---

# Generalizable Target-Less Joint Intrinsic-Extrinsic Camera-LiDAR Calibration using Deep Pixel-Point Correspondences

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇从原始相机图像和激光雷达扫描出发，同时估计相机内部参数、镜头畸变以及两传感器的相对位置和朝向。关键是让像素与点云的匹配网络适应不同内参和畸变，再交替做匹配与几何优化。

## 问题

任务是无需专用标定目标地完成相机与激光雷达联合标定。摘要指出，已有学习像素—点对应的方法虽能准确估计外参、跨环境使用，却依赖已经校正且内参已知的图像。于是相机必须先单独标定，限制了整套流程的自动化。

### 用一个例子理解

理解用例（非论文实验）：输入一台新装相机的原始街景图像和同步雷达扫描；网络匹配图像位置与三维点，优化器调整相机模型和传感器变换，输出可用于点云投影的标定参数。

## 创新点或方法

旧流程先校准相机，再求相机与雷达的关系；本文直接处理原始图像。训练时通过合成增强，让对应关系网络接触内参和畸变变化，学习在这些变化下寻找像素与三维点的匹配。标定时反复预测对应关系并做非线性优化，联合更新内参、径向与切向畸变、外参。更准确的参数有望改善后续匹配，再支撑下一轮优化；增强分布、初始化和目标函数未说明。

### 方法如何工作

1. 训练时合成内参与畸变变化，让匹配网络适应未经校正的图像。
2. 输入原始图像与雷达点云，预测像素和三维点的对应关系，提供几何约束。
3. 通过非线性优化联合调整相机参数与传感器变换，使对应关系更一致。
4. 用更新后的参数继续匹配与优化，逐步细化标定；摘要未说明收敛保证和停止规则。

### 必要术语

- 内参：焦距、主点等相机成像参数；决定三维点如何映到图像。
- 外参：相机与雷达之间的旋转和平移；用于转换两者的坐标。
- 径向与切向畸变：镜头造成的两类图像位置偏移；本文与内外参一起估计。
- 像素—点对应：图像位置与雷达三维点的匹配；是优化标定参数的约束来源。

## 证据

摘要报告，在 KITTI 的未见相机—雷达配置及三个真实机器人平台上零样本评估。作者称，其外参精度优于使用预标定相机的对应关系方法，同时恢复准确内参。但未给旋转、平移或内参误差数值，也未列基线名称。因此证据支持所测配置下的联合标定可行性，尚不能判断误差大小及相对工程标定的水平。

## 局限

无标定目标不代表任意场景都能解出唯一参数。我的待核查问题是：图像与点云重叠不足、结构单一或初值偏差较大时是否会失败，以及哪些参数容易互相补偿。这些是可辨识性问题，摘要未给边界。

- **判断**：值得细读对应关系增强和联合优化，采用前必须检查收敛范围及各参数的绝对误差。

## 研究关联

可借鉴的思路是把过去视为固定前提的相机参数纳入求解：通过训练覆盖参数变化，使匹配器能够配合几何优化工作。对于相机参数未知或可能变化的系统，这比必须先拿到可靠内参更灵活。

### 下一步读哪里

我会先查增强是否覆盖实际镜头参数，再看初始化需求、迭代停止条件、内外参分别的误差，以及三个真机平台与训练配置差异有多大。

- **概念**：具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/Generalizable Target-Less Joint Intrinsic-Extrinsic Camera-LiDAR Calibration usi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Accurate camera-LiDAR calibration is an essential prerequisite for robust multi-modal perception in robotics. Recent target-less methods based on learned pixel-point correspondences achieve high extrinsic calibration accuracy and generalize across environments. However, they operate on rectified images with known camera intrinsics, restricting their applicability to systems whose cameras have already been individually calibrated. We present a fully automatic, target-less framework that jointly estimates camera intrinsics, radial-tangential distortion, and camera-LiDAR extrinsics from raw images and LiDAR scans. Our method generalizes deep correspondence-based calibration from rectified images to raw cameras through intrinsic- and distortion-aware correspondence learning via synthetic augmentations. During calibration, we iteratively couple correspondence prediction and nonlinear optimization to jointly refine the camera parameters and relative sensor transformation. We evaluate our approach on an unseen camera-LiDAR configuration from the KITTI dataset and on three real robotic platforms in a zero-shot manner. The results demonstrate that joint calibration with our generalized pixel-point correspondence network improves extrinsic accuracy over correspondence-based methods using pre-calibrated cameras, while additionally recovering accurate intrinsics.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37350v1
- Authors: Simon Bultmann, Daniele Cattaneo, Abhinav Valada
- Published: 2026-10-27T14:51:03Z
- Age days: 1

</details>
