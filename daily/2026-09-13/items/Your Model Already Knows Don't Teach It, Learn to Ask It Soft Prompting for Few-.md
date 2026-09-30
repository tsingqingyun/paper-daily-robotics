---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11310"
published: "Sat, 12 Sep 2026 00:00:00 -0400"
age_days: 0
score: 24
created: 2026-09-13
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models

> [!summary] 先说人话（基于摘要）
> 这篇用少量可学习软提示适配冻结的视觉语言模型，把优化重点放在如何向模型传递任务上。关键是提示放置位置和初始化方式，机器人策略上也做了初步验证。

## 这篇到底在做什么

- **卡在哪里**：任务是在航拍、工业、医疗等域外图像中，仅凭十张标注图完成少样本检测适配。现有选择包括离散提示搜索和LoRA；论文检验能否用更少训练参数取得相近精度并保留原能力。
- **关键解法**：冻结骨干，只训练一至三个连续提示token；检测任务将其放在视觉与文本的跨模态边界，并以空格token初始化。VLA实验则在梯度瓶颈处放置提示，直接调节冻结策略的条件输入。
- **拿什么证明**：Roboflow20-VL十样本检测达到14.2 mAP，匹配最佳LoRA，平均训练7,168个参数，数量少逾20,000倍。跨模态边界放置为10.0 mAP，其他位置为8.4；软提示保持预训练表现，匹配精度的LoRA使NaturalBench准确率相对下降35%。RoboCasa三项任务中两项匹配LoRA。

## 值不值得读

- **和你的研究有什么关系**：对多模态基础模型和VLA研究者，它提供了冻结主干进行任务适配的具体设计，尤其适合研究接口位置与可操控性的关系。
- **先别急着信**：摘要明确指出软提示优化更难、随机种子方差更高；机器人证据仅涉及三项任务，不能将检测中的参数效率和能力保持结论直接推广到VLA。
- **判断**：值得精读提示位置、初始化和方差结果；VLA部分可作为低成本适配的试验起点。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-13/Your Model Already Knows Don't Teach It, Learn to Ask It Soft Prompting for Few-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.11310v1 Announce Type: cross Abstract: We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision. Existing adaptation methods are discrete prompt optimization and LoRA fine-tuning. We revisit a third option: soft prompting, where a small number of continuous prompt tokens are optimized while the pretrained backbone remains frozen. We identify two key design choices. First, placing prompt tokens at the cross-modal boundary between visual and text tokens outperforms other placements (10.0 vs. 8.4 mAP). Second, initializing prompts from the empty space token outperforms semantic and random initialization. With these choices, one to three learned tokens (7,168 parameters on average) match the best LoRA configuration on Roboflow20-VL (14.2 mAP, 10-shot) while training over 20,000x fewer parameters. Soft prompting remains harder to optimize, exhibiting higher variance across random seeds. Unlike LoRA, however, it causes no forgetting: the LoRA rank matching our accuracy reduces NaturalBench VQA accuracy by 35% relative, rising to 56% at the largest rank, whereas soft prompting leaves pretrained performance unchanged. The learned tokens behave like prompts rather than weights. They transfer to a newer model without retraining (+0.8 mAP on Qwen3.5-9B) and can be verbalized into readable prompts competitive with prompt-search methods (matching DetPO and outperforming GEPA). The approach also extends beyond detection. On RoboCasa manipulation tasks, the frozen $\pi_{0.5}$ vision-language-action policy benefits from soft prompting, matching the LoRA baseline on two of three tasks when tokens are placed at the gradient bottleneck. These results suggest modern VLMs already encode much of what is needed for specialized domains; the challenge is learning how to ask.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11310
- Authors: Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang, Cesar Daniel Hernandez, Wei Zhao, Wolfgang M. Pauli, John Galeotti, Deva Ramanan
- Published: Sat, 12 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
