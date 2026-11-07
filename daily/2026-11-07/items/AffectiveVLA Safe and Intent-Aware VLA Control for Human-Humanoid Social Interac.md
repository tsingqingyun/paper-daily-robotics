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
url: "https://arxiv.org/abs/2611.07712v1"
published: "2026-11-05T09:29:21Z"
age_days: 1
score: 34
created: 2026-11-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction

> [!summary] 这篇论文到底做了什么（基于摘要）
> AffectiveVLA 让人形机器人先判断人是否想握手、碰拳或拥抱，再决定是否启动 VLA 动作。它同时用接触顺应控制和独立语音停止机制，分别处理误启动与接触中的控制问题。

## 问题

社交接触需要同时解决三个问题：识别人想做什么、生成合适动作、接触时控制身体响应。仅有能执行动作的 VLA，并不能保证它在正确时机启动；误判意图可能直接触发不合适的身体接触。

### 用一个例子理解

理解用例（非论文实验）：人向机器人伸出拳头，两路画面进入意图模型；识别为碰拳且置信度达标后，语言提示启动相应动作，接触阶段调整手臂响应；若判断不确定，则不启动。

## 创新点或方法

从让动作策略直接承担交互判断，改为在前面加一个轻量 RGB 意图模型：读取两路机载相机，把识别结果转成语言提示，低置信度则阻止执行。训练时通过 VR 遥操作收集交互数据，微调四种 VLA；部署时再按交互类型调整手臂阻抗，并由独立语音机制触发锁定式安全停止。各层分别处理意图、动作和停止，减少单个模型承担的判断；意图模型训练细节未说明。

### 方法如何工作

1. 用 VR 遥操作收集交互过程，得到用于微调 VLA 的多模态示范。
2. 部署时从两路 RGB 画面识别人类意图，得到候选交互及置信度，为动作启动提供依据。
3. 把可信意图转成语言提示交给 VLA；不可信预测抑制执行，避免判断直接变成误动作。
4. 接触时切换相应顺应设置，并保留独立语音停止通道，分别处理接触响应和紧急终止。

### 必要术语

- 意图门控：先判断是否允许动作执行；本文用低置信度抑制误启动。
- 阻抗控制：调节机械臂受力时的响应方式；本文按交互类型设置接触顺应性。
- macro-F1：各类别 F1 的等权平均；用于概括分类表现，但不直接衡量接触风险。

## 证据

摘要给出约 1,300 段多模态交互，微调 GR00T、RLDX-1、Being-H0.5 和 UnifoLM-VLA-0，并在带灵巧手的 Unitree G1 真机上评估。GR00T 是最佳独立模型，加入意图识别后 macro-F1 从 0.75 升至 0.90；意图模型 p95 推理延迟为 6.27 毫秒。摘要未定义 F1 对应的事件类别，也未给接触力、伤害风险或整条控制链延迟，因此不能把该提升直接等同于安全性提升。

## 局限

摘要提供了真实机器人证据，但没有量化顺应控制和语音停止各自的贡献。还需核查误启动减少是否伴随漏响应增加，以及遮挡、多人和语音识别失败时的表现；这些是待查问题，不能据此断言全文未测试。

- **判断**：值得读系统接口和消融实验，尤其是置信度如何转成动作许可；目前证据更直接支持交互识别可靠性，而非完整的接触安全保证。

## 研究关联

当动作本身可执行、但启动时机难判断时，可以把“是否执行”显式拆出来，并允许系统拒绝低把握输入。这里的启示是让识别不确定性真正影响动作许可，而不是只输出一个标签。

### 下一步读哪里

优先核查 macro-F1 的标签定义、测试人数与数据划分、门控阈值，以及停止锁定后的恢复条件。再看是否有接触力测量和各安全部件的独立实验；本次只有摘要。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/AffectiveVLA Safe and Intent-Aware VLA Control for Human-Humanoid Social Interac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent, generate contact-rich motions, and maintain safe physical contact. We present AffectiveVLA, an intent-gated Vision-Language-Action (VLA) pipeline deployed on a Unitree G1 humanoid with dexterous hands. A lightweight RGB-based model recognizes interaction intent from two onboard cameras and converts it into a language prompt for the VLA policy. Low-confidence predictions suppress motion execution, reducing unintended activations. During physical contact, interaction-specific compliance profiles adjust arm impedance, while an independent voice-triggered mechanism initiates a latched safe-stop procedure. Using VR teleoperation, we collected approximately 1,300 multimodal interaction episodes and fine-tuned four VLA models: GR00T, RLDX-1, Being-H0.5, and UnifoLM-VLA-0. On-robot evaluation identifies GR00T as the best-performing standalone model. Integrating intent recognition increases its macro-F1 score from 0.75 to 0.90, while the intent model achieves a p95 inference latency of 6.27 ms. These results demonstrate that explicit intent gating improves the reliability of VLA-based social interaction without compromising real-time operation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.07712v1
- Authors: Nikita Kuzmin, Georgii Demianchuk, Mariya Lezina, Yara Mahmoud, Iana Zhura, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- Published: 2026-11-05T09:29:21Z
- Age days: 1

</details>
