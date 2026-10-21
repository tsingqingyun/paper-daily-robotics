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
url: "https://arxiv.org/abs/2610.25534v1"
published: "2026-10-18T21:07:34Z"
age_days: 2
score: 40
created: 2026-10-21
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# AQUAACT: A Joystick-Level Underwater Teleoperation Dataset and Closed-Loop Benchmark

> [!summary] 这篇论文到底做了什么（基于摘要）
> AQUAACT 记录水下驾驶员“看到什么、怎样拨摇杆”，让策略学习接替驾驶员，并保留原有飞控负责把指令变成运动。它同时提供闭环测试：会预测驾驶动作，离真正完成水下任务仍有明显距离。

## 问题

水下机器人要执行检查设施、巡视珊瑚等任务，但多数仍由人看摄像头操纵。陆地 VLA 看似可以迁移，真正瓶颈却是缺少带任务语言和动作的水下数据，以及缺少持续执行后的任务检验；水下画面与控制条件是否适合陆地预训练，也不能靠模型规模推断。

### 用一个例子理解

理解用例（非论文实验）：输入前视画面和“沿管道向前巡视”；策略根据管道在画面中的位置输出前进及转向摇杆命令，飞控执行后返回新画面；策略持续修正方向，输出的是一串驾驶命令，而非一次性完整轨迹。

## 创新点或方法

本文沿用现有驾驶链路：人看图像、拨摇杆，飞控再把摇杆指令转成运动。采集时把图像与人类摇杆命令配对，加入语言标注和惯性测量；训练时让模仿学习或 VLA 策略学习这一驾驶接口，并考察仿真数据的作用。推理时由策略持续输出摇杆命令，环境响应后再观察、再行动。各策略具体使用哪些输入、时间窗口多长，摘要未说明。

### 方法如何工作

1. 记录人类驾驶过程，把图像与摇杆命令配对，获得可模仿的观察—操作样本。
2. 补充语言标注和惯性测量，让数据能描述任务并保留车辆运动信息；各模型如何使用它们摘要未说明。
3. 用真实及仿真演示训练策略，检验仿真经验能否降低真实数据需求。
4. 让策略在仿真中持续驾驶并统计任务完成情况，使自身动作造成的新状态也进入测试。

### 必要术语

- 摇杆级动作：驾驶员使用的操纵指令；本文把它作为策略输出接口。
- 闭环评测：每次动作后重新观察并继续行动；本文用它检验整段任务能否完成。
- 模仿学习：从人的观察与动作配对中学习行为；本文将其作为水下驾驶基线。

## 证据

摘要给出 1.9 小时真实演示和 17.9 小时仿真演示，均由人类驾驶。作者报告仿真演示能迁移到真实数据并减少真实演示需求，但没有给出节省比例或真实任务成功率。仿真闭环比较了七种策略，覆盖模仿学习基线与 VLA，按各自默认配方训练；没有策略完成超过五分之一的回合。摘要还指出，陆地预训练的大型 VLA 没有优于从零训练的小策略。具体任务、每种成功率及不确定性未提供。

## 局限

低成功率明确发生在仿真闭环基准，不能直接写成真机失败率；“迁移到真实数据”也不等于已完成真实自主部署。默认训练配方的比较反映直接使用时的表现，但尚不能证明充分调参后的能力上限。我会进一步核查任务难度、失败类型和真实数据评估方式。

- **判断**：值得细读数据接口与评测协议，因为它让“替代水下驾驶员”成为可以训练和检验的具体问题。

## 研究关联

一个实用启示是：自动化不一定要先重做底层控制，可以先学习人正在使用的操作接口。另一个启示是，迁移是否有效要看目标环境闭环结果，不能把陆地数据量直接当成水下能力的保证。

### 下一步读哪里

先核查摇杆各通道、相机与动作的时间对齐、语言标注粒度，以及惯性数据是否进入策略；再看七种策略的任务分项、仿真与真实数据混合方式，以及所谓迁移究竟用什么指标确认。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/AQUAACT A Joystick-Level Underwater Teleoperation Dataset and Closed-Loop Benchm.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Underwater robots support a growing range of work, from inspecting offshore structures and pipelines to surveying reefs and accompanying divers. Most of these tasks, however, are still flown by hand by a pilot, which raises the question of whether they can be carried out autonomously instead. On land, vision-language-action (VLA) models already let robots carry out tasks autonomously from language instructions, which makes them a natural candidate for taking the pilot's place. Underwater, however, there is little data to train such models. We take inspiration from how these tasks are flown today: the pilot watches the camera image and steers with a joystick, whose commands the flight controller turns into motion. We therefore record the pilots and introduce AQUAACT, to our knowledge the first publicly available language-annotated underwater dataset pairing camera images with human joystick commands. It comprises 1.9 hours of real-world and 17.9 hours of simulated demonstrations, both flown by human pilots, together with the vehicle's inertial measurements. Experiments with AQUAACT show that its simulated demonstrations transfer to real data and greatly reduce the real demonstrations a policy needs. A closed-loop benchmark of seven policies in simulation, from imitation-learning baselines to VLA models, each trained with its default recipe, shows that these tasks remain far from solved: no policy completes more than a fifth of the episodes. Pretraining on land data gives large VLA models no advantage over small policies trained from scratch, a gap that land-trained models have yet to close underwater.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.25534v1
- Authors: Zhenqi Wu, Trung Tien Dong, Aditya Penumarti, Mohamed A. Fouad, Menna A. Fouad, Mingyang Mao, Jane Jaejeong Shin, Xiaomin Lin
- Published: 2026-10-18T21:07:34Z
- Age days: 2

</details>
