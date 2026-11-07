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
url: "https://arxiv.org/abs/2611.07896v1"
published: "2026-11-05T12:17:27Z"
age_days: 1
score: 29
created: 2026-11-07
concepts: ["多模态基础模型"]
---

# AffordJEV: Affordance Grounding by Confirming Candidate Regions

> [!summary] 这篇论文到底做了什么（基于摘要）
> AffordJEV 找出物体上能完成指定操作的区域：先让分割器给出候选，再直接判断哪些候选可用。它不生成文字推理，而让物体、部件和子部件层面的判断互相纠正。

## 问题

任务不是识别“这是杯子”，而是定位“哪里可以握持”。摘要指出，常见方法先让多模态语言模型写推理，再输出框或点交给分割器：生成文字耗时，语义判断也难以直接控制最终区域的边界，选错后不易修正。

### 用一个例子理解

理解用例（非论文实验）：输入剪刀图片和“握持”，分割器给出整把剪刀、刀刃、手柄等候选；模型结合上下层证据确认手柄，输出对应区域，不输出操作说明文字。

## 创新点或方法

旧做法先形成语言结论，再转换成区域；本文把已有分割器冻结，让它提供可选区域，模型直接确认候选是否符合操作要求。这样，语义判断直接作用于区域选择。推理按物体、部件、子部件逐层进行，证据双向传递，避免某一层独自定案。训练时，用这套流程实际产生的问题训练判断模型，并让它一次判断同层所有候选；推理时不生成文本，每次判断请求只需一次前向计算。候选生成、证据传递和纠错的具体规则未说明。

### 方法如何工作

1. 把图像分成候选区域，使操作判断有明确的空间对象。
2. 对物体到子部件逐层提问，一次判断同层候选，减少逐个请求。
3. 让上下层传递证据以修正选择；摘要只说明到此，未解释修正规则。
4. 输出被确认的操作区域，省去文字结论到定位提示的转换。

### 必要术语

- 可供性定位：找出能执行某种操作的可见部位；这是本文的输出目标。
- System One：直接作判断、不生成文字推理；本文用它确认候选。
- 冻结分割器：保持参数不变的区域生成模型；它限定了可供选择的区域。

## 证据

摘要称，只用 InstructPart 训练，在域内及零样本迁移到 UMD、IIT-AFF 时超过文字推理方法；在同一推理流程下，整体优于已有 System One 模型，判断请求也更少。评测使用与定义对齐的操作词。摘要未给定位指标、分数、延迟或各基线名称，因此只能支持相对优势，不能量化提速，也不能推出机器人实际操作更成功。

## 局限

我最想核查的是：正确部位没被分割器提出来时，后续还能怎样补救，以及操作词换成更口语的表达后是否稳定。输入没有真机操作证据；区域定位表现与实际可抓、可操作仍有距离。

- **判断**：值得细读候选层级和双向纠错机制，因为它们决定这套方法能否超越简单的“分割后分类”。

## 研究关联

值得借鉴的是把“理解操作含义”和“确定区域边界”连接到同一个候选选择过程。当可靠候选容易获得时，可以尝试直接判断候选，而不必先生成一段文字再把它翻译回空间位置。

### 下一步读哪里

下一步检查候选覆盖率、层间证据如何改变判断、同层批量判断的训练标签，以及包含分割器开销的总延迟；还要看操作词对齐规则是否影响迁移难度。

- **概念**：多模态基础模型
- **筛选分数**：29
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-07/AffordJEV Affordance Grounding by Confirming Candidate Regions.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Affordance grounding asks which visible part of an object performs a requested operation, a basic capability for embodied manipulation and human--robot interaction. Most existing methods follow a System Two paradigm: a multimodal language model first writes a chain of thought and then turns its conclusion into a box or points for a segmenter. This incurs considerable inference cost, gives the semantic decision little direct control over the extent of the final region, and makes mistakes hard to correct. Yet locating an affordance is essentially a perceptual judgment that need not be argued out in words. We therefore propose, in which frozen segmenters propose candidate regions and a System One model decides directly which of them perform the operation, generating no text and reading each decision from a single forward pass. Our contributions are twofold. (1) An inference framework that confirms candidate regions level by level, from object to part to sub-part, with evidence passed between the levels in both directions so that the levels correct one another. (2) A System One model trained for this framework: existing System One models are built for general-purpose decisions, judge one candidate per request and are ill-suited to the framework's region questions, so ours learns directly from the requests the framework itself produces and judges all candidates of a level at once. Trained only on InstructPart and evaluated with definition-aligned operation words, outperforms chain-of-thought methods in domain and in zero-shot transfer to UMD and IIT-AFF, is better overall than existing System One models run in the same framework, and needs fewer judge requests. To our knowledge, is the first approach to bring System One models to affordance grounding.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.07896v1
- Authors: Jincheng Li, Yutian Zhang, Jianyu Zhang, Xinshun Wang, Mengyuan Liu
- Published: 2026-11-05T12:17:27Z
- Age days: 1

</details>
