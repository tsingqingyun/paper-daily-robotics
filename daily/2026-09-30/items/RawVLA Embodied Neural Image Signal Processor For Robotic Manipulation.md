---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37530v1"
published: "2026-09-29T13:16:37Z"
age_days: 0
score: 39
created: 2026-09-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> RawVLA 把相机 RAW 数据到 RGB 图像的处理变成可学习环节，让输入图像适配冻结的 VLA。它针对会影响动作的成像因素调整渲染，改善恶劣成像条件下的操作表现。

## 问题

VLA 通常直接使用固定 ISP 输出的 RGB，成像链路被排除在学习与评测之外。摘要指出增益、传感器噪声、色彩响应、色调响应和位深都会影响动作预测与操作成功，且影响程度不同。

## 创新点或方法

先系统分析五类 ISP 因素，再用流式神经 ISP 将 RAW 观察自适应转换为冻结 VLA 的视觉输入。RawVLA-Bench 在正常和退化采集条件下显式改变成像因素，将优化对象从策略扩展到相机前端。

## 证据

摘要报告 RawVLA 在 RawVLA-Bench 正常条件下保持性能，在退化成像下显著改善鲁棒性；摘要未给出可核查的结果数字。

## 局限

需核查神经 ISP 的训练目标、所需监督，以及它对不同相机和冻结策略的适用范围。

- **判断**：值得读方法和成像因素实验，选题直接触及部署接口，但收益幅度需看全文数字再判断。

## 研究关联

对 VLA 部署与评测研究者，它指出视觉鲁棒性的一部分可能来自成像接口，提供了无需改动策略权重的干预位置，也提示基准应明确相机处理条件。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/RawVLA Embodied Neural Image Signal Processor For Robotic Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models typically operate on RGB images produced by a fixed camera image signal processor (ISP), leaving the imaging pipeline outside the learning and evaluation loop. We systematically examine the consequences of this overlooked design choice across five fundamental ISP dimensions: gain, sensor noise, chromatic response, tonal response, and bit depth. Our analysis reveals that RAW-to-RGB processing materially shapes both action prediction and manipulation success, with different ISP dimensions exerting substantially different effects. Guided by these findings, we introduce RawVLA, a streaming neural ISP that adaptively renders RAW observations for frozen VLA policies while concentrating its capacity on the imaging factors relevant to embodied behavior. We further present RawVLA-Bench, a RAW-domain manipulation benchmark to expose image processing as an explicit evaluation variable across clean and adverse acquisition conditions. Experiments on RawVLA-Bench show that RawVLA preserves performance under standard conditions while substantially improving robustness under degraded imaging, establishing adaptive RAW processing as an effective interface between physical cameras and embodied policies.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37530v1
- Authors: Shuhong Liu, Heng Zhou, Lingfeng Qian, Yuhao Fang, Xianbao Hou, Qianyu Zhou, Lin Gu, Wei Sui, Jianfei Yang, Ziteng Cui
- Published: 2026-09-29T13:16:37Z
- Age days: 0

</details>
