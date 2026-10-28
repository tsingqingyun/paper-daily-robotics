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
url: "https://arxiv.org/abs/2610.36598v1"
published: "2026-10-27T03:58:54Z"
age_days: 0
score: 34
created: 2026-10-28
concepts: ["机器人学习", "具身智能评测与基准"]
---

# OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> OpenJaws 用双目相机配合手持夹爪采集示范，让人的操作轨迹成为机器人更可靠的动作标签。关键是更准确地恢复带真实尺度的轨迹，同时开放硬件、软件和定位评测。

## 问题

手持 UMI 能在没有机器人参与时采集操作示范，但训练需要知道夹爪实际移动了多少、到了哪里。单目视觉惯性定位受尺度不确定性和漂移影响；封闭跟踪模块或外部设施又增加成本与部署负担。标签不准会把采集误差带进策略训练。

### 用一个例子理解

理解用例（非论文实验）：人手持夹爪把积木放入盒子，双目图像用于恢复相机的空间运动，再经标定形成夹爪动作标签；这些示范用于训练，输出是在机器人上执行放置动作的策略。

## 创新点或方法

本文把常见的单目定位方案换成低成本双目相机，并配上模块化 3D 打印夹爪和标准 ISO 适配接口。双目定位恢复具有物理尺度的相机轨迹，为动作标注提供依据；相机轨迹怎样转换成末端动作仍需看标定细节。训练阶段使用 OpenJaws 采集的数据学习策略，推理阶段把策略部署到机器人；摘要未说明策略结构，也未说明部署时是否继续使用同一相机。

### 方法如何工作

1. 人用带双目相机的夹爪演示任务，采集视觉与操作信息，减少对机器人现场参与的依赖。
2. 从双目观测恢复带真实尺度的相机轨迹，为动作标签提供位置依据。
3. 通过设备标定关联相机运动与夹爪运动；摘要未说明具体转换流程。
4. 用采集数据训练并部署策略，同时用独立定位基准检查数据采集质量。

### 必要术语

- UMI：用手持设备记录可供机器人学习的操作示范；本文改进其采集硬件与定位。
- 双目定位：利用两路相机观测估计空间运动；本文用它恢复带物理尺度的轨迹。
- 漂移：运动估计误差随过程累积；本文将其视为动作标签质量的威胁。

## 证据

摘要介绍真机定位基准 UMI-Loc-Bench-v1，报告双目定位明显优于单目替代方案，并称所采数据训练的策略已在真实机器人多个任务上部署。没有定位误差数值、指标定义、任务名称或成功率。因此支持双目方案的方向性优势与端到端可用性，尚不能量化定位改进给策略带来的收益。软硬件和数据以允许商业使用的许可证发布，具体条款仍需查验。

## 局限

更准的定位与更好的策略表现是两层证据，摘要没有给出严格连接两者的受控实验。双目在遮挡、弱纹理或快速运动下的表现，以及跨机器人所需标定工作，都是待核查问题。

- **判断**：值得读硬件清单、标定流程和定位基准；是否适合复现，主要取决于实际误差、采集条件和部署成本。

## 研究关联

这里值得借鉴的是先检查示范标签，而非把训练失败全部归给策略。若示范来自便携设备，定位误差就是训练数据的一部分；建立独立定位基准能帮助区分采集问题和学习问题。

### 下一步读哪里

优先核查定位真值如何获得、单目基线如何调参、相机与夹爪如何标定，以及轨迹漂移是否随采集时长累积。随后看真机策略实验是否控制数据量与训练设置，以隔离标签质量的作用。

- **概念**：机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/OpenJaws An Open Hardware UMI Framework with Stereo Localization for Generalist.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Handheld data-collection interfaces such as the Universal Manipulation Interface (UMI) allow manipulation demonstrations to be gathered in the wild without a robot in the loop, but the quality of the resulting action labels is bounded by the accuracy of vision-based localization. Existing systems recover end-effector pose from monocular visual-inertial odometry, which is subject to scale ambiguity and drift, or delegate tracking to closed-source modules and external infrastructure that reintroduce cost and setup burden. We present OpenJaws, a fully open hardware and software framework for sensorized UMI that improves localization and simplifies deployment across robot platforms. OpenJaws pairs a modular, 3D-printed gripper exposing a standardized ISO adapter with a low-cost stereo camera to recover metric camera trajectories. We further introduce UMI-Loc-Bench-v1, a benchmark quantifying real-world localization accuracy for handheld data-collection devices, and show that stereo localization substantially outperforms monocular alternatives. Finally, we demonstrate that policies trained on data collected with OpenJaws can be deployed on a real robot across multiple tasks. Hardware, software, and data are released under a commercially permissive license. Code, data, and videos are available at https://open-jaws.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36598v1
- Authors: Adithyavairavan Murali, Yash Oza, Karanbir Chahal, Neel Jawale, Silas De Vries, Hesam Rabeti, Erwin Coumans, Balakumar Sundaralingam, Stan Birchfield
- Published: 2026-10-27T03:58:54Z
- Age days: 0

</details>
