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
url: "https://arxiv.org/abs/2610.26174v1"
published: "2026-10-19T11:03:56Z"
age_days: 1
score: 31
created: 2026-10-21
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# PhantomTac: Hijacking Robotic Tactile Systems with Deploy-and-forget Tags

> [!summary] 这篇论文到底做了什么（基于摘要）
> PhantomTac 揭示了磁触觉传感器的一种物理漏洞：物体表面的无源磁标签会让机器人误读接触力。控制器随后根据错误读数调节抓握，可能把物体捏坏或放松到掉落。

## 问题

精细抓握需要持续判断按压力和切向力，再及时调整动作。磁触觉传感器能测三维力，也不怕视觉遮挡，但它通过磁场变化间接判断受力，因此外部磁场可能混入测量。摘要指出，现有抗干扰机制仍可能被绕过；攻击者也不必接触机器人本体，只需影响它将要抓的物体。

### 用一个例子理解

理解用例（非论文实验）：机器人抓一个薄壁杯，输入包括触觉读数和可用的其他感知信号；物体上的磁干扰让读数偏离真实受力，控制器据此调整夹持，输出可能成为过紧或过松的抓握。加入一致性检查后，系统可先识别信号冲突；这不代表论文已验证该杯子场景。

## 创新点或方法

正常情况下，接触引起的磁场变化被解释为力；PhantomTac 在物体表面加入磁标签，使传感器把外来磁场也算进受力。作者逆向分析商用传感器的感知机制，并设计可实际部署的标签。这里没有摘要明确描述的模型训练流程；运行时，干扰通过触觉读数进入闭环控制。作者还提出多模态一致性防御，但摘要未说明融合信号、判定规则或训练方式。

### 方法如何工作

1. 分析商用传感器怎样把磁信号转成力，确定外部干扰可能进入的位置。
2. 让物体表面的磁标签改变局部磁场，使测得的力偏离真实接触力。
3. 错误读数进入抓握反馈，控制器调整力度，由此产生损坏或掉落风险。
4. 用多模态一致性检查缓解风险；摘要只说明防御方向，没有交代具体实现和效果。

### 必要术语

- 磁触觉传感器：根据磁信号变化估计接触力的传感器；它是本文研究的受攻击环节。
- 法向力与剪切力：分别是垂直接触面和沿接触面的力；两者误读会影响不同抓握调整。
- 闭环控制：根据持续反馈反复调整动作；本文中错误反馈会推动错误调整。

## 证据

摘要报告标签厚约 0.5 毫米、无需电池，并在真实机器人和机械臂上完成端到端测试：抓取位置偏移限定在 8 毫米以内时，攻击成功率超过 95%。这些数字均来自摘要。它还报告能绕过现有抗干扰机制，但未列出机制名称、试验次数、物体种类及成功判据。因此可确认特定真机条件下的风险，不能扩展为所有磁触觉设备都同样易受攻击。

## 局限

摘要明确给出了位置偏移条件，也指出既有抗磁干扰机制存在局限。我的待核查问题是：换传感器、接触方向和物体材料后效果如何，以及所提防御能降低多少风险、会不会误拦正常抓握；摘要没有提供这些答案。

- **判断**：值得读到传感器测量原理、攻击成功定义和防御实验，因为真正需要理解的是错误读数怎样一路变成错误动作。

## 研究关联

具体启示是：反馈越及时，并不代表控制越可靠。如果多个决策都依赖同一项受污染的测量，闭环可能持续加重错误。值得尝试的是用独立感知证据检查触觉读数是否合理，前提是这些证据不会受到同一种干扰。

### 下一步读哪里

下一步核查真机型号、成功率分母、位置偏移的测量方式，以及防御前后的失败率和误报率；尤其要看防御是否经过独立端到端验证。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/PhantomTac Hijacking Robotic Tactile Systems with Deploy-and-forget Tags.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Tactile perception is crucial for precise robotic manipulation, providing an important foundation for dexterous, closed-loop force control. Among various tactile sensing techniques, magnetic tactile sensors stand out thanks to their fine-grained, three-dimensional force perception capability and strong robustness against visual occlusion. In this study, we discover a physical loophole called PhantomTac in magnetic tactile sensors. The attacker can alter the magnetic field, thus spoofing the force interpreted by magnetic tactile sensors. The attacker can stealthily deploy such an attack by simply attaching a thin (the thickness is around 0.5 mm), battery-free magnetic tag to the surface of an object. Hence, the attack tag can be easily concealed by a barcode sticker. Such an attack scheme is "deploy-and-forget" -- the attacker can deploy the tag and leave. When a robotic hand is picking up an object, it may severely damage the object. Specifically, spoofing the normal force can crush the object, whereas spoofing the shear force can lead to a loose grip, thus dropping the object. Compared with directly sabotaging the robotic hand, PhantomTac is much more concealed as the attacker does not need access to the device. We performed extensive reverse-engineering efforts to characterize the sensing mechanism of commercial-off-the-shelf tactile sensors and proposed a practical tag design. End-to-end evaluations conducted on real robots and robotic arms demonstrate that our attack can bypass existing anti-interference mechanisms and effectively hijack their closed-loop control processes, achieving an attack success rate exceeding 95% when the grasping-position offset is bounded within 8 mm. Finally, based on the limitations of existing anti-magnetic interference mechanisms, we propose a multimodal-consistency defense mechanism to mitigate such physical-layer security threats.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.26174v1
- Authors: Binbin Zhang, Yifeng Zhang, Xiaomeng Chen, Dongyao Chen
- Published: 2026-10-19T11:03:56Z
- Age days: 1

</details>
