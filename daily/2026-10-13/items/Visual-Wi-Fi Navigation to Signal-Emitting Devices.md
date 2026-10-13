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
url: "https://arxiv.org/abs/2610.12733v1"
published: "2026-10-08T21:28:25Z"
age_days: 4
score: 31
created: 2026-10-13
concepts: ["具身智能评测与基准"]
---

# Visual-Wi-Fi Navigation to Signal-Emitting Devices

> [!summary] 这篇论文到底做了什么（基于摘要）
> ViFiNav 让机器人利用目标设备发出的 Wi-Fi 信号找路，即使设备很小或被遮住也能获得方向线索。它让机器人边走边汇集不同位置的信号测向结果，逐步估计目标位置，再结合深度观察导航。

## 问题

任务是在未知室内环境中找到发出 Wi-Fi 信号的设备，不连接设备，也不改造基础设施。视觉难以定位小目标、遮挡目标或外观不明显的设备；Wi-Fi 又会因室内多路径传播给出误导方向。训练还需要机器人每移动到一个位置，都能获得对应的无线观测。

### 用一个例子理解

理解用例（非论文实验）：机器人寻找被沙发遮挡的联网设备；输入是深度图和监听到的 Wi-Fi 数据包，系统从不同位置测向并更新目标位置与置信度，策略据此绕过障碍，逐步接近设备。终止距离和设备确认方式需查正文。

## 创新点或方法

本文先用 WiFiSpaces 扩展 Habitat，通过在线射线追踪生成连续位置上的天线阵列观测，供闭环策略训练使用。ViFiNav 的在线定位算法利用机器人运动，将多个视点的测向结果汇集成带置信信息的信号源估计；学习策略再融合估计与深度图行动。训练时可在射线追踪观测上微调；推理时继续移动、测量和更新位置估计。定位公式与策略结构未在摘要中说明。

### 方法如何工作

1. 在仿真中按机器人当前位姿生成无线观测，让训练获得随移动变化的信号反馈。
2. 机器人移动并采集多个位置的测向结果，为区分真实方向与反射方向提供更多证据。
3. 在线定位算法聚合观测，产生持续更新且带置信信息的目标位置估计。
4. 导航策略融合位置估计与深度观察输出动作，新的移动又带来观测，形成闭环。

### 必要术语

- 多路径传播：同一信号经墙面等反射沿多条路线到达；本文需要处理它造成的测向误差。
- 测向：估计信号从哪个方向到来；本文把多个位置的方向信息用于定位。
- 射线追踪：按传播路径模拟信号与环境的作用；WiFiSpaces 用它生成训练观测。
- 闭环导航：行动后重新观察并调整下一步；本文同时更新目标估计与移动决策。

## 证据

摘要报告，利用运动对准确定位很关键，在 WiFiSpaces 的无线观测上微调能提高成功率；策略还能零样本迁移到未见场景数据集，并部署到配有商用路由器改造传感器的真实机器人，无需真实世界训练。没有给出成功率、对比对象、场景数量和真机试验次数，因此可确认有仿真迁移与真机部署证据，无法量化可靠性。

## 局限

我会核查低发包率、移动目标和更复杂反射环境下的效果，以及仿真无线传播与真机之间的偏差。摘要没有说明这些是否已测试；无需真实世界训练不等于无需传感器设置，真机部署也不等于各种室内环境都已验证。

- **判断**：值得读定位算法及真机配置，因为能否复用主要取决于它如何处理多路径错误，以及实际需要什么无线观测。

## 研究关联

值得借鉴的是将运动当作获取信息的动作：换个位置后，新的观测可以帮助消除旧观测的歧义。对单次测量容易受干扰的传感器，保留跨位置估计及置信信息，比把每次测量直接交给策略更值得尝试。

### 下一步读哪里

先核查无线测向需要哪些包信息、天线和标定，再看运动消歧及置信估计方法；最后检查真机成功条件、失败案例和零样本迁移涉及的场景差异。

- **概念**：具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/Visual-Wi-Fi Navigation to Signal-Emitting Devices.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Indoor navigation to task-relevant targets remains difficult when the target is small, occluded, or visually indistinct. Meanwhile, smart appliances, mobile devices, and IoT tags emit Wi-Fi signals during everyday communication, providing a pervasive but underused spatial cue. We study visual-Wi-Fi navigation, where a robot reaches a signal-emitting device in an unmapped environment using onboard visual observations and Wi-Fi packets overheard from the device, without connecting to the device or modifying infrastructure. Realizing this requires pose-dependent Wi-Fi observations during closed-loop policy learning and reliable spatial cues from bearing measurements corrupted by indoor multipath propagation on a moving robot. We present WiFiSpaces, which extends the Habitat embodied simulator with online ray-traced Wi-Fi sensing, rendering Wi-Fi observations for a robot-mounted antenna array at continuous poses during policy rollouts. On top of it, we build ViFiNav, a localization-aware navigation framework: an online source-localization algorithm exploits robot motion to disambiguate and robustly aggregate bearings from multiple viewpoints into a confidence-aware source estimate, and a learned policy fuses this evolving estimate with depth observations and learns to act on it as it is refined. Experiments show that exploiting robot motion is key to accurate source estimates, and that fine-tuning on ray-traced Wi-Fi observations in WiFiSpaces improves the success rate of ViFiNav. The policy transfers zero-shot to unseen scene datasets, and we deploy it on a real robot with a Wi-Fi sensor built from a commodity router, without any real-world training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12733v1
- Authors: Lihao Wang, Tianjian Xu, Tianmin Shu, Renjie Zhao
- Published: 2026-10-08T21:28:25Z
- Age days: 4

</details>
