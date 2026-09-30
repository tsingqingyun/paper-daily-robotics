---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.28108v1"
published: "2026-08-28T09:14:09Z"
age_days: 2
score: 31
created: 2026-08-31
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# DeicticVLA: Unifying Instruction Modes Based on Language and Deictic Gestures in a Single VLA

> [!summary] 先说人话（基于摘要）
> DeicticVLA 把纯语言、语言加指示手势和纯视觉指示统一成文本提示与指示掩码，让同一个预训练 VLA 接受三种交互方式。两阶段训练和第二阶段保留语言数据，是利用掩码又避免遗忘的关键。

## 问题

当多个物体同类或外观相似时，纯语言必须使用复杂描述，而 VLA 未必可靠理解；不同指令模态若各自训练策略，又难以共享骨干和示范数据。

## 创新点或方法

通过文本补全和指示手势定位，把 LI、VLI、VI 规范化为文本提示与 deictic mask，输入同一 VLA。作者比较 RGB 视觉提示、独立通道掩码提示及三种训练策略；两阶段训练先建立能力，再保留部分 LI 数据以抑制遗忘。

## 证据

仿真中四种提示方法在分布内均有高成功率，但未见布局下使用掩码的能力不同；消融显示两阶段训练更好，第二阶段保留 LI 数据能缓解遗忘且不降低 VLI/VI。三项真实任务中，一套策略支持全部模式；未见类别上 VLI、VI 均为 100%，联合训练 LI 为 16.7%。


## 局限

100% 对 16.7% 的比较来自未见类别这一特定设置，需核查试验次数、手势或掩码来源，以及真实部署是否依赖额外定位系统。

- **判断**：值得读到实验设计和失败案例层面；统一接口很实用，但泛化结论不能只靠单个百分比。

## 研究关联

对 VLA 和机器人学习者，它给出比自然语言更直接的目标消歧接口，并系统比较掩码注入和训练日程；适合人机协作中“指这个、放那里”的任务。与世界模型的联系不直接。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-31/DeicticVLA Unifying Instruction Modes Based on Language and Deictic Gestures in.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action models (VLAs) allow users to specify manipulation tasks in natural language, but distinguishing a target or placement goal among objects of the same category or similar appearance requires detailed expressions that VLAs may not use reliably. We propose DeicticVLA, which canonicalizes Language Instruction (LI), Vision-Language Instruction (VLI), and Visual Instruction (VI) into a text prompt and deictic masks through text-prompt completion and deictic gesture grounding, enabling a single pretrained VLA to handle all three instruction modes. With a shared backbone, demonstrations, and matched training steps, we compare two RGB visual prompting methods, two separate-channel mask prompting methods, and three training strategies in simulation. Under two-stage training, the four prompting methods achieve high in-distribution success but differ in their ability to use deictic masks in unseen layouts. Across methods, training-strategy ablations show that two-stage training improves such use, while retaining second-stage LI data mitigates forgetting without reducing VLI and VI performance. In three real-world tasks, one policy supports all modes. VLI and VI outperform LI under unseen expressions, appearance changes, and novel objects. For unseen categories, both achieve 100% success, compared with 16.7% for jointly trained LI. These results demonstrate the unified three-mode interface and guide DeicticVLA design.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.28108v1
- Authors: Kango Yanagida, Tatsuya Aoki, Yuichiro Yoshikawa, Takato Horii
- Published: 2026-08-28T09:14:09Z
- Age days: 2

</details>
