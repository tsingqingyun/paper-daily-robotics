---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.09612v2"
published: "2026-09-09T02:11:29Z"
age_days: 3
score: 25
created: 2026-09-12
concepts: ["世界模型", "Sim2Real", "具身智能评测与基准"]
---

# MuJoCable: Reduced-Order Surface-Routed Cable Transmission for Tendon-Driven Robots

> [!summary] 先说人话（基于摘要）
> MuJoCable让仿真中的肌腱传动考虑真实绕线、松弛和摩擦，改善仅靠简化肌腱模型难以表达的力传递行为。

## 这篇到底在做什么

- **卡在哪里**：肌腱机器人的运动取决于路径、单向受力和分段摩擦，而摘要指出主流刚体仿真器不能联合处理移动非圆接触、单向张力及分段摩擦。
- **关键解法**：插件随构型优化经过移动解析或网格表面的有序绳路，再用单向轴向定律、方向性Capstan传播和节点虚功计算分段张力与刚体受力，并在仿真中施加这些力。
- **拿什么证明**：滑轮基准的Capstan比值误差低于0.5%；在18关节欠驱动SpiRobs上呈现原生肌腱模型未表达的摩擦负载增长和近端转动重分配。SpiRobs及肌腱路径耦合手指的硬件测试复现了观测运动序列。

## 值不值得读

- **和你的研究有什么关系**：对Sim2Real和机器人学习，提供更贴近传动机制的仿真基础，也可在制造前研究绳路、线缆和执行器设计。
- **先别急着信**：这是降阶传动模型；需核查参数辨识和适用接触范围，滑轮解析精度不等于复杂硬件整体误差。
- **判断**：做肌腱驱动机器人值得精读模型与硬件验证，是明确针对仿真落差来源的工作。

## 研究关联

- **概念**：[[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/MuJoCable Reduced-Order Surface-Routed Cable Transmission for Tendon-Driven Robo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Tendon transmissions reduce distal inertia and add compliance, yet routing, slack, and friction govern motion and force transfer. Mainstream rigid-body robotics simulators such as MuJoCo do not jointly resolve moving noncircular contact, unilateral tension, and segment friction. We present MuJoCable, which adds a reduced-order, configuration-dependent cable transmission to MuJoCo. Its routing algorithm jointly optimizes an ordered path across moving analytic and mesh surfaces. A unilateral axial law, directional Capstan propagation, and nodal virtual work map this path to segment tensions and body forces. The warm-started engine plugin applies these forces during simulation and exposes route and load states for design. Pulley benchmarks recover analytical transmission relations with a Capstan-ratio error below 0.5%. On the underactuated 18-joint SpiRobs, MuJoCable reveals friction-driven load growth and proximal redistribution of joint rotation that the native tendon does not represent. Hardware tests on SpiRobs and a tendon-route-coupled finger reproduce observed motion sequences. By making physical threading executable, MuJoCable brings transmission sources of the simulation-to-reality gap into route, cable, and actuator design before fabrication.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.09612v2
- Authors: Yi Zhang, Qi Shao, Yicong Lin, Muyuan Ma, Tao Sun, Yue Xie
- Published: 2026-09-09T02:11:29Z
- Age days: 3

</details>
