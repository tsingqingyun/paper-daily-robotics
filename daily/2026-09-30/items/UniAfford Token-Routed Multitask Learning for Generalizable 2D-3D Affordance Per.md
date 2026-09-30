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
url: "https://arxiv.org/abs/2609.37264v1"
published: "2026-09-29T11:11:56Z"
age_days: 0
score: 33
created: 2026-09-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# UniAfford: Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Perception

> [!summary] 这篇论文到底做了什么（基于摘要）
> 同一个杯子，照片里要找“哪块能抓”，点云里也要找“哪些点能抓”，UniAfford 让这两种任务共用一套理解物体和操作的知识。它把大模型内部的理解直接交给像素、点云两个预测分支，并用两边的标注一起训练。

## 问题

任务是按语言要求定位可操作区域，输出图像像素或点云点的标签。瓶颈在于二维和三维研究的任务定义、标注及评测各自独立，同一种物体与操作的知识难以互通；简单汇集数据也无法消除监督格式的差异。

### 用一个例子理解

理解用例（非论文实验）：输入杯子的照片及“找到适合抓取的位置”→共享模型形成杯子与抓取的语义表示→路由器生成图像查询→像素解码器标出候选区域；若输入点云，则输出点级区域。这里还没有生成抓取轨迹。

## 创新点或方法

旧做法把二维、三维分开处理；UniAfford 用共享 MLLM 理解物体与操作，再由模态感知路由器生成各分支的查询。训练时，UniAfford-Data 用统一分类体系连接像素标注、点标注和指令，分支的密集预测损失直接影响共享表示，无需语言输出头先生成预设标记。推理时，图像查询调节 SAM 风格像素解码器，点云查询调节基于 SONATA 的点解码器，可接受单一模态或配对输入。语义配对不应自动理解为像素与点的精确对应。

### 方法如何工作

1. 用统一的物体—操作分类体系整理二维、三维标注，使不同格式的监督具有共同语义。
2. 共享 MLLM 处理输入，路由器从上下文隐状态产生对应模态的查询，为区域预测提供任务条件。
3. 查询分别驱动像素和点解码器，得到可操作区域；训练时用各分支目标更新共享表示。
4. 推理时按输入模态执行相应分支；联合输出怎样进一步协调，摘要只说明到解码器耦合。

### 必要术语

- Affordance：物体某个部位支持什么操作；本文要定位这些部位。
- Token 路由：把模型内部表示送往合适分支；本文用它连接共享语义与密集预测。
- 密集预测：为每个像素或点给出结果；本文据此提供区域级监督。

## 证据

摘要报告：在二维、三维 affordance 基准上，不做目标专用微调也有较强零样本泛化；在模态隔离协议下，各分支达到领先表现。消融涉及路由、联合监督和解码器耦合，语言头诊断支持隐状态包含物体—操作语义。但未提供基准名称、指标数值、基线名称及消融幅度，尚不能量化收益，也不能据此推断机器人执行成功率。

## 局限

摘要没有交代的关键问题是：语义配对怎样避免类别捷径，零样本划分是否隔离相近物体，以及解码器耦合在缺失模态时如何工作。输入未交代仿真或真机实验，感知泛化不能等同于物理交互泛化。

- **判断**：有二维、三维可操作区域数据，或需要给机器人先找准下手位置，值得读。它解决的是“哪里能操作”；仅凭摘要，还不能说机器人因此就抓得更稳。

## 研究关联

如果你手里有图像标注，也有点云标注，可以借鉴它把不同格式的数据用同一种“物体—操作”语义连起来。值得试的实验是：固定数据量，让两种任务一起学，看其中一种是否真能帮助另一种，尤其是在没见过的物体上。

### 下一步读哪里

下一步核查路由状态如何选取、分支损失怎样回传、语义配对是否需要同一实例，以及零样本和模态隔离协议允许使用哪些训练数据；再看消融能否分离数据与结构的收益。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


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
