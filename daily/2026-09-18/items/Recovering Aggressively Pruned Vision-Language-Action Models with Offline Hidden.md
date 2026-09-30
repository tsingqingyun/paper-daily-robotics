---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19579v1"
published: "2026-09-17T02:08:09Z"
age_days: 0
score: 30
created: 2026-09-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Recovering Aggressively Pruned Vision-Language-Action Models with Offline Hidden-State Distillation

> [!summary] 先说人话（基于摘要）
> 这项工作在大幅剪小VLA后，用离线缓存的教师隐藏状态恢复能力，避免依赖在线机器人探索。关键是缩窄网络块，同时保留残差流维度，使师生状态能直接对齐。

## 问题

VLA的大语言骨干难以部署到机器人硬件；OpenVLA-OFT剪去63%后，LIBERO-Long成功率从93.2%跌到0.8%。已有恢复方案需要监督微调加在线强化学习，耗费大量GPU时间。

## 创新点或方法

宽度剪枝保留隐藏状态形状，直接做无投影器的隐藏状态蒸馏；教师单次前向构建缓存，学生完全离线恢复。研究还比较不同剪枝比例、恢复预算及宽度与深度剪枝。

## 证据

63%缩减的学生约8 GPU小时恢复到距教师3.5个百分点以内。实机6自由度机械臂上，72%缩减的蒸馏学生成功率77.5%，监督恢复为59.5%；相对教师机载推理快2.23倍、内存少62%。9种比例扫描显示高压缩时蒸馏收益更明显。

## 局限

摘要同时指出同压缩率下宽度剪枝成功率较高、深度剪枝延迟较低；不能把参数缩减比例直接当作加速比例。

- **判断**：值得优先精读并关注复现条件，证据覆盖压缩强度、恢复目标、预算与实机收益，部署相关性很强。

## 研究关联

为VLA部署提供可离线执行的压缩恢复路线，并提示成功率、延迟和剪枝结构需要联合选择。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/Recovering Aggressively Pruned Vision-Language-Action Models with Offline Hidden.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models let robots follow language instructions, but their language backbones of several billion parameters are the main obstacle to running them on robot hardware. Structured pruning reduces that backbone, and removing 63% of it from OpenVLA-OFT drops LIBERO-Long success from 93.2% to 0.8%. A recent approach restores such a model with supervised fine-tuning followed by reinforcement learning, which needs online rollouts and hundreds of GPU-hours. We recover most of the lost success entirely offline. Width pruning narrows the blocks but keeps the residual stream at its original size, so teacher and student hidden states have the same shape and are matched directly, without a projector. Training against a cache built in one teacher pass lifts the 63%-reduced student to within 3.5 points of the teacher in about 8 GPU-hours. A sweep over nine ratios locates where the recovery objective starts to matter. Up to 45% reduction the two do not differ significantly on OpenVLA-OFT. Hidden-state distillation then adds +2.1 to +4.5 points there between 63% and 87%, and +9.4 to +22.1 points on CogACT from 63% onward. At 81% on CogACT, a tripled recovery budget narrows the distilled student's gap to the teacher to 3.9 points on average, while supervised recovery stays more than 20 points below. At matched compression, width pruning yields higher success and depth pruning lower latency. On a 6-DoF manipulator, the distilled student at 72% reduction reaches 77.5% success against 59.5% for supervised recovery, runs 2.23x faster on-board than the teacher, and uses 62% less memory.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19579v1
- Authors: Chiyoung Kim, Sanghyuk Roy Choi, Minhyeok Lee
- Published: 2026-09-17T02:08:09Z
- Age days: 0

</details>
