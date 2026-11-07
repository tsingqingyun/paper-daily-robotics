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
url: "https://arxiv.org/abs/2611.08372v1"
published: "2026-11-05T17:50:35Z"
age_days: 1
score: 31
created: 2026-11-07
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> MOMASPLAT把已有操作示范重新制作成“机器人从其他底座位置观察并执行”的训练样本，连物体接触后的运动也一起重建。关键是既改画面，也按运动学变换动作，让新视角下看到的操作与要执行的动作对应。

## 问题

移动机械臂导航到目标附近后，底座通常与示范采集位置有偏差，模仿策略因此可能失效。已有新视角合成假定场景静止，无法正确重绘抓取、推动等接触后的物体变化，恰好漏掉最关键的操作阶段。

### 用一个例子理解

理解用例（非论文实验）：输入机器人正对抽屉拉开的示范，分别重建柜体和移动的抽屉，从偏左的底座位置重绘全过程，并变换拉动动作，输出一组画面与动作配对的新示范。

## 创新点或方法

旧做法重绘静态场景；本文分别重建背景和被操作物体，再合成完整动态示范。采集过程自然包含的多视角观察用于三维重建，方法结合3D Gaussian Splatting、前馈三维基础模型与运动学动作重定向。训练时用合成画面及变换后的动作做示范增强；执行时使用学到的视觉动作策略。动态物体如何逐帧定位、是否需要额外标注，摘要未说明。

### 方法如何工作

1. 从已有移动操作采集中取得多视角观察，为场景和目标物体提供三维信息。
2. 分开重建静态环境与被操作物体，使接触后物体运动也能进入新视角画面。
3. 从新的机器人底座位置渲染完整轨迹，并同步变换动作，得到几何一致的示范。
4. 用增强示范训练模仿策略，让它学习在底座位置变化时继续操作。

### 必要术语

- 新视角合成：根据已有观察生成另一个位置看到的画面；本文用来扩充示范。
- 3D Gaussian Splatting：用许多带颜色和形状的三维高斯单元表示场景；用于重建和渲染。
- 动作重定向：把原动作转换到新的机器人几何条件下；保证合成图像与动作配对。

## 证据

摘要报告三个场景中的五项真机移动操作任务，包含刚体和关节物体，另在仿真中对照真值检查合成质量。平均成功率超过最强基线的两倍；大底座位移下，基线均失败时仍有一定成功率。摘要未给绝对成功率、位移范围、基线名称与试验次数，因此可确认报告的相对优势，难以判断具体可用范围。

## 局限

我的待核查问题是：遮挡严重、物体反光或关节运动复杂时，重建误差会怎样传入策略。仿真合成保真度与真机任务成功是两类证据，前者不能替代后者；摘要没有给它们之间的定量联系。

- **判断**：值得读到数据生成与动作变换细节，因为它解决的是移动操作中明确存在、也容易被静态增强漏掉的偏差。

## 研究关联

这篇提醒我们，视角增强不能只把图像“换个角度”。机器人位置变了，动作表达也要随之调整；涉及接触时，还必须保留物体运动。已有多视角示范且能建立几何对应时，这种联合增强值得借鉴。

### 下一步读哪里

优先核查动态物体的分离、轨迹恢复和动作坐标变换，再看底座偏移的测试分布。还需检查真实采集量、合成数量，以及与增加真实示范的成本比较。

- **概念**：多模态基础模型 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/MOMASPLAT Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Visuomotor policies trained through imitation learning are highly sensitive to changes in camera viewpoint. This is particularly problematic for mobile manipulation (MoMa), where robots rarely execute manipulation from the exact same base pose used during demonstration collection due to navigation uncertainty, localization drift, and environmental constraints. Recent approaches use novel-view synthesis (NVS) to augment demonstrations with unseen viewpoints, but they assume static scenes and therefore fail to re-render the manipulated object during the post-contact interaction phase, leaving the most critical parts of the demonstration unaugmented. We present MOMASPLAT, a novel-view demonstration augmentation framework for mobile manipulation that synthesizes full manipulation trajectories from unseen robot base poses, including dynamic object interactions. Our key insight is that standard MoMa data collection naturally provides the multiview observations needed to reconstruct both the static scene and the manipulated object in 3D. MOMASPLAT combines 3D Gaussian Splatting, feed-forward 3D foundation models, and kinematics-based action retargeting to separately reconstruct the scene and manipulated object, render them from novel viewpoints, and generate geometrically consistent synthetic demonstrations paired with transformed actions. We evaluate MOMASPLAT on five real-world mobile manipulation tasks involving both rigid and articulated objects across three scenes, and validate the fidelity of its synthesized demonstrations against ground truth in simulation. MOMASPLAT substantially improves robustness to unseen base poses, more than doubling the average success rate of the strongest baseline and maintaining non-trivial success at large base displacements where all baselines fail, while reducing the need for largescale real-world data collection.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.08372v1
- Authors: Sateesh Kumar, Arnav Balaji, Arpit Bahety, Skand Peri, Georgios Pavlakos, Roberto Martín-Martín
- Published: 2026-11-05T17:50:35Z
- Age days: 1

</details>
