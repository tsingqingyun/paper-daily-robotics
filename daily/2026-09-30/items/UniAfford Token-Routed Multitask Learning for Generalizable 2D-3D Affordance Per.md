---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37264v1"
published: "2026-09-29T11:11:56Z"
age_days: 0
score: 33
created: 2026-09-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# UniAfford: Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Perception

> [!summary] 先说人话（基于摘要）
> UniAfford 让同一个多模态模型同时找出图像和点云中可用于交互的区域。它把共享语义状态直接路由给二维、三维预测分支，让密集预测任务共同塑造表示。

## 问题

二维与三维可供性定位的任务定义、标注和评测长期分离，限制了视觉与几何空间之间共享物体交互语义。仅靠分开训练难以利用互补监督。

## 创新点或方法

Token Router for Tasks 将上下文隐藏状态送到专属分支，无需语言头先生成预定义标记。统一数据集按物体—可供性语义配对二维像素与三维点标注，再用共享 MLLM 查询条件化 SAM 风格像素解码器和 SONATA 点解码器。

## 证据

摘要报告无需目标特定微调即可在二维和三维基准上零样本泛化，模态隔离协议下各分支达到最优水平；消融支持路由、联合监督和解码器耦合。摘要未给出可核查的结果数字。

## 局限

数据配对是语义层面的二维—三维配对，不能默认存在逐像素几何对应；需核查零样本划分和不同监督来源的可比性。

- **判断**：做可供性感知或多任务 MLLM 值得精读路由机制，纯控制研究者可先看其输出能否接入现有动作表示。

## 研究关联

对 VLA 感知前端，提供了把语言语义映射到可操作空间区域的统一接口，支持图像、点云或配对输入。实际是否改善动作策略仍需单独验证。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/UniAfford Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Per.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Affordance perception aims to localize actionable regions supporting embodied interaction, yet 2D and 3D affordance grounding have evolved as separate problems, with different task definitions, supervision formats, datasets, and evaluation protocols. This fragmentation limits the learning of transferable object-affordance semantics across visual and geometric spaces. We propose Token Router for Tasks, a multitask training paradigm for MLLM-based systems that routes contextual hidden states to task-specific branches without requiring the language head to generate predefined markers. Routed states are supervised directly by branch-specific objectives, enabling dense prediction losses to shape shared MLLM representations. We instantiate this paradigm as UniAfford, a unified framework for generalizable 2D-3D affordance perception, together with UniAfford-Data, a dataset integrating pixel-level 2D annotations, point-level 3D annotations, and language instructions under a shared object-affordance taxonomy, supporting heterogeneous supervision through semantic-level 2D-3D pairing. UniAfford adopts an MLLM as a shared semantic hub and a modality-aware token router to produce image- and point-cloud-affordance queries. These queries respectively condition a SAM-style pixel decoder and a SONATA-based point decoder, enabling flexible 2D, 3D, and joint affordance inference from image-only, point-cloud-only, or paired multimodal inputs. Experiments demonstrate strong zero-shot generalization across 2D and 3D affordance benchmarks without target-specific fine-tuning, alongside state-of-the-art branch-wise performance under modality-isolated protocols. Ablations validate token routing, joint 2D-3D supervision, and decoder coupling, while language-head diagnostics show that routed latent states carry meaningful object-affordance semantics. Project page: https://4dvlab.github.io/UniAfford

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37264v1
- Authors: Yuhao Liu, Yiming Zhong, Hanqing Wang, Shaocheng Yan, Yuhang Zhang, Wenzhou Lyu, Ziyang Ding, Wei Zhang, Xue Zhao, Jin Pan, Yuexin Ma, Xinge Zhu
- Published: 2026-09-29T11:11:56Z
- Age days: 0

</details>
