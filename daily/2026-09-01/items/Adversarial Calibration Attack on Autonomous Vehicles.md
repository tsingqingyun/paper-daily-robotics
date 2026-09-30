---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.28778v1"
published: "2026-08-28T18:35:54Z"
age_days: 3
score: 29
created: 2026-09-01
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Adversarial Calibration Attack on Autonomous Vehicles

> [!summary] 先说人话（基于摘要）
> ACA 把自动驾驶在线相机—LiDAR 标定变成攻击面：一张同时优化几何与纹理的海报先诱发误标定检测，再把估计器引向错误外参，使错误持续污染后续感知与控制。

## 这篇到底在做什么

- **卡在哪里**：车辆会因振动、温度或轻微位移发生标定漂移，因此需要在线校正；现有攻击通常假定标定正确，却忽略一旦恶意标定更新被接受，其误差会跨多次融合持续传播。
- **关键解法**：输入是一张物理对抗海报，作用于误标定检测器和外参估计器；统一优化同时设计海报几何与纹理，完成“触发校准—操纵结果”两阶段目标。与一次性传感器欺骗不同，它攻击会被系统持久采用的校准状态。
- **拿什么证明**：在 KITTI、nuScenes、仿真和实体实验中评估；最高诱导 33.9°平均旋转标定误差并严重损害目标检测。CARLA 的攻击者构造脆弱场景中发生碰撞，真实 Husky 机器人上的打印海报复现了标定错误。

## 值不值得读

- **和你的研究有什么关系**：对多模态具身 Agent、自动驾驶和安全评测，它指出系统状态更新本身需要认证、置信度约束与回滚，而不能只防单帧感知攻击。
- **先别急着信**：摘要只说明在攻击者构造的脆弱场景中导致碰撞，需核查攻击距离、视角容差、系统先验知识和不同标定算法上的普适性。
- **判断**：安全与多传感融合研究者应精读；其“持久状态污染”威胁模型比单帧对抗样本更值得系统设计者警惕。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/Adversarial Calibration Attack on Autonomous Vehicles.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous vehicles (AVs) rely on accurate camera-LiDAR calibration for multimodal sensor fusion. In practice, calibration can drift due to vibration, temperature variation, or minor sensor displacement, motivating online calibration algorithms that detect and correct misalignment at runtime while allowing the vehicle to continue operating without a factory visit. Existing AV attacks largely assume correct calibration. We instead identify online sensor calibration as a new attack plane. A corrupted calibration update can persist across subsequent fusion operations, causing system-wide errors that propagate from perception to planning and control. We present Adversarial Calibration Attack (ACA), the first physical attack against camera-LiDAR online calibration. Using a single adversarial poster, ACA first spoofs the miscalibration detector to trigger the calibration process and then steers the calibration estimator toward an incorrect transformation. A unified optimization jointly designs the poster's geometry and texture for both objectives. We evaluate ACA across benchmark datasets, simulation, and physical experiments. On benchmark datasets such as KITTI and nuScenes, ACA induces up to 33.9 degrees mean rotational calibration error, thereby severely degrading object detection. In the CARLA simulator, the attack causes a collision when the corrupted calibration is accepted in vulnerable scenarios crafted by the attacker. On a real Husky robot, a printed adversarial poster successfully reproduces the calibration error. These results demonstrate that online calibration is a practical and safety-critical attack surface for AVs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.28778v1
- Authors: Liangkai Liu, Qingzhao Zhang, Kang G. Shin
- Published: 2026-08-28T18:35:54Z
- Age days: 3

</details>
