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
url: "https://arxiv.org/abs/2611.09195v1"
published: "2026-11-06T09:17:27Z"
age_days: 3
score: 28
created: 2026-11-10
concepts: ["AI 核心知识地图"]
---

# InstantHMR : Real-Time Human Mesh Recovery on Your Phone

> [!summary] 这篇论文到底做了什么（基于摘要）
> InstantHMR 从单张图像直接预测三维人体网格，重点是让手机也能低延迟运行。摘要明确给出的路线是采用 MHR 参数人体模型、使用公开标注训练，并统一协议比较速度与精度；具体网络加速技巧未说明。

## 问题

任务是在移动设备上从单张图像恢复三维人体表面。瓶颈是精度与延迟：摘要称现有先进方法要么在手机上太慢，要么为速度牺牲精度。另一个问题是不同人体表示和评估流程会影响比较，因此需要统一协议重新评测。

### 用一个例子理解

理解用例（非论文实验）：输入手机拍到的一张人物图像；模型预测 MHR 人体参数并生成网格，输出可供界面显示的三维人体。连续使用时是否抖动，需要另行验证。

## 创新点或方法

旧方法的手机部署成本较高；InstantHMR 使用面向移动推理的单图回归模型系列，输出基于 MHR 的人体表示。训练仅使用 SAM 3D Body 数据集的公开标注；推理输入单图并恢复人体网格。摘要没有解释骨干、损失、量化或编译细节，因此目前只能确认设计路线，无法把速度优势归因于某项结构改动。

### 方法如何工作

1. 利用公开人体标注训练单图回归器，使图像能够映射到人体表示；损失和网络结构摘要未说明。
2. 推理时输入单张人物图像，预测基于 MHR 的表示，并恢复人体网格。
3. 在手机 NPU 等目标上测量耗时，判断模型是否满足移动推理需求。
4. 按统一协议转换并评估多个方法，减少人体表示差异对精度比较的干扰。

### 必要术语

- MHR：参数化人体模型；用一组参数表示人体形状与姿态，并生成网格。
- NPU：面向神经网络计算的处理器；本文手机延迟在该硬件上测量。
- PA-MPJPE：将预测与参考关节做对齐后计算的平均位置误差；衡量对齐后的姿态准确度，越低越好。

## 证据

以下均来自摘要：恢复每人 6,890 顶点网格，在 Galaxy S23 NPU 耗时 5.5 ms，在 RTX 4070 为 0.98 ms。相对唯一一个兼容手机且精度略优的对比方法，手机速度快 12 倍。PA-MPJPE 在 3DPW、EMDB、RICH 分别为 40.0、48.8、41.7 mm。作者统一复评 11 种方法，并测量 8 类运行目标。这支持所测条件下的速度与精度取舍，但摘要未给端到端应用延迟。

## 局限

单人模型推理耗时不能直接当作摄像头应用的完整延迟，还需核查人体检测、裁剪、转换和传输是否计入。PA-MPJPE 经过对齐，也不能单独说明绝对位置准确性或连续视频的稳定程度。

- **判断**：值得优先读部署设置和统一评测协议；若要复用方法，再深入看网络设计，摘要本身尚不足以解释为何这么快。

## 研究关联

可借鉴的是同时处理部署与比较协议：若目标是手机使用，桌面速度不足以代表可用性；若人体参数模型不同，也应先统一转换与评估，再判断谁更准确。

### 下一步读哪里

先核查延迟是否包含预处理与人体模型计算、手机运行精度及测量条件；再看官方 MHR 到 SMPL 转换如何用于评估，以及各方法的输入、训练数据和复现配置是否可比。

- **概念**：AI 核心知识地图
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-10/InstantHMR Real-Time Human Mesh Recovery on Your Phone.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Real-time 3D human mesh recovery from a single image on mobile devices is a challenging problem with many applications, including robotics, biomechanics, AR/VR, and exergames. Current state-of-the-art models are either too slow to run efficiently on mobile devices or sacrifice accuracy for speed. We present InstantHMR, a family of open-source single-image regressors suited for mobile inference, based on the Momentum Human Rig (MHR) parametric model and trained exclusively on publicly available annotations from the SAM 3D Body dataset. Our approach achieves remarkable performance on a Samsung Galaxy S23 NPU, recovering a 6,890-vertex body mesh in 5.5 ms per person, and 0.98 ms on an NVIDIA RTX 4070 GPU. This speed surpasses all existing methods we evaluated. On mobile, it is 12x faster than the single mobile-compatible method that slightly outperforms ours in accuracy, while achieving competitive accuracy with 40.0 mm PA-MPJPE on 3DPW, 48.8 mm on EMDB and 41.7 mm on RICH. To ensure fair comparisons, we re-evaluate 11 state-of-the-art methods under a unified protocol aligned with the closest MHR-based competitors, including Meta's official MHR-to-SMPL conversion, and report their reproduction results. Additionally, we measure latency across eight different targets, ranging from desktop TensorRT to two phone NPUs. Code and models are available at https://github.com/Naturalpad-studio/InstantHMR.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.09195v1
- Authors: Mohamed Adjel, Kahina Chalabi, Vincent Bonnet
- Published: 2026-11-06T09:17:27Z
- Age days: 3

</details>
