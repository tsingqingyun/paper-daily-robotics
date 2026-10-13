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
url: "https://arxiv.org/abs/2610.12832v1"
published: "2026-10-09T00:33:13Z"
age_days: 3
score: 32
created: 2026-10-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding

> [!summary] 这篇论文到底做了什么（基于摘要）
> EASG 把机器人动作的坐标参照直接画进腕部相机画面，再让 VLM 用原本的文本输出接口表达动作。关键是让模型看懂“往哪个方向动”对应什么，从而无需机器人动作预训练或额外动作模块，也能生成可执行动作。

## 问题

任务是把预训练 VLM 变成通用机械臂操作策略。瓶颈在于视觉空间理解与机器人动作之间缺少明确对应：传统 VLA 的动作 token、动作头或动作专家，需要通过机器人数据学会动作含义；模块化方法能利用 VLM 做零样本操作，却依赖外部规划和控制组件，难以作为统一连续动作策略直接训练。

### 用一个例子理解

理解用例（非论文实验）：输入是腕部相机看到的积木和投影坐标参照；模型判断夹爪相对积木应沿哪个方向移动，输出对应动作文本；执行端把文字表示转换成移动命令。具体单位、步长和夹爪控制方式仍需查正文。

## 创新点或方法

旧做法让模型学习一个新动作接口；EASG 则把动作接口变成模型能看到、能用文字表达的内容。它将以工具中心点为中心的动作坐标系投影到腕部图像，让输出方向具有可见参照。推理时，预训练 VLM 直接生成表示连续动作的文本；训练时，同一个接口也可用机器人轨迹微调。摘要未说明文本格式、动作范围，以及文本如何转换成底层控制命令。

### 方法如何工作

1. 获取腕部图像，并投影工具中心点附近的动作坐标系，使模型能看见动作方向的参照。
2. 让 VLM 根据目标与坐标参照判断移动方式，把视觉关系转换成有物理指向的动作描述。
3. 通过原生文本生成接口输出动作，再交给执行端；摘要只说明到此，没有给出转换和控制细节。
4. 需要改善能力时，用机器人轨迹微调同一动作接口，使零样本能力能够继续接受任务经验训练。

### 必要术语

- TCP：工具中心点，即机器人末端工具采用的参考位置；本文用它作为动作坐标系的中心。
- 动作空间落地：把动作数值或方向对应到可观察的物理参照；本文通过图像中的坐标投影完成。
- 零样本操作：不先用机器人动作数据训练就尝试操作；本文用于检验预训练 VLM 能否直接利用新接口。

## 证据

摘要报告了零样本操作，以及跨物体位置、类别和机器人本体的泛化，并称轨迹微调能继续改善表现。但没有提供任务清单、真机或仿真划分、对比模型、成功率和样本量。因此目前支持的是这种接口具有可行性，无法据此判断它在复杂操作中能替代多少专门训练的 VLA。

## 局限

我会核查坐标投影误差、工具遮挡和相机变化是否影响动作，以及接触操作需要的精度能否达到。摘要没有把这些作为作者明确局限，也没有提供足够实验来回答；跨本体泛化更不能直接理解为任意机器人无需适配。

- **判断**：值得读到动作编码和执行接口的细节，因为真正可复用的贡献是如何把连续动作变成 VLM 能直接理解的输入输出。

## 研究关联

值得借鉴的是：模型输出不可靠时，先检查它是否知道输出量的物理含义。若任务能通过局部坐标参照清楚描述，可以先尝试把动作语义放进观察，再判断是否需要新增动作网络。

### 下一步读哪里

先核查动作文本是否表达平移、旋转和夹爪状态，再看投影所需标定、控制频率，以及零样本与微调实验是否使用相同任务和动作接口。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-13/VLMs are Native Action Models Unleashing the Manipulation Capabilities of VLMs w.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Pretrained vision-language models (VLMs) already exhibit strong visual, spatial and reasoning capabilities relevant to robotic manipulation. The key challenge in turning pretrained VLMs into generalist manipulation policies is to expose these capabilities through an appropriate action interface. Vision-language-action (VLA) models provide a unified trainable policy, but typically introduce learned action tokens, action heads, or action experts whose semantics must be learned from robot data pretraining. In contrast, modular foundation-model-based manipulation methods can exploit pretrained VLM capabilities for zero-shot manipulation, but rely on external planning and control scaffolds that are not end-to-end trainable as a unified continuous-action policy. In this work, we introduce EASG, an Explicit Action-Space Grounding framework that bridges these two paradigms. By projecting a tool center point (TCP)-centered action frame into the wrist camera observation and expressing actions in the form of VLM's native textual generation interface, EASG makes the semantics of a continuous robot action space directly observable in the VLM's perceptual context. This allows pretrained VLMs to directly generate executable robot actions using their existing visual-spatial reasoning capabilities, without robot-action pretraining or additional action modules. Besides, the same action interface supports direct fine-tuning with robot trajectories, allowing the models to continuously improve beyond their manipulation capabilities unleashed by EASG. Overall, EASG enables zero-shot manipulation and generalization across object positions, categories, and robot embodiments, while supporting effective fine-tuning in the same continuous action space. These results demonstrate that, given an appropriate action interface, pretrained VLMs can themselves serve as native action models for robotic manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12832v1
- Authors: Jingkun Yi, Shujie Zhang, Zirui Zhou, Haoxiao Wang, Haiyang Sun, Yuhang Dong, Xudong Xu, Xing Shen, Tao Zhang, Yong Liu, Jiangning Zhang
- Published: 2026-10-09T00:33:13Z
- Age days: 3

</details>
