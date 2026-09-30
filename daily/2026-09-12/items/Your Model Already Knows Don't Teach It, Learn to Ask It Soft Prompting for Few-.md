---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11310v1"
published: "2026-09-10T09:38:11Z"
age_days: 1
score: 24
created: 2026-09-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models

> [!summary] 先说人话（基于摘要）
> 这篇工作通过学习极少量连续提示token，让冻结视觉语言模型适应新领域。关键是提示插入位置和初始化方式，并初步扩展到VLA操作。

## 这篇到底在做什么

- **卡在哪里**：域外少样本检测只有十张标注图像可用，需要在适配效果、训练参数量与保留原能力之间权衡；摘要比较了离散提示优化、LoRA和软提示。
- **关键解法**：冻结骨干，在视觉与文本token的跨模态边界学习1—3个软提示，以空格token初始化；VLA扩展则把提示放在梯度瓶颈位置。
- **拿什么证明**：Roboflow20-VL十样本设置达14.2 mAP，匹配最佳LoRA，平均训练7168参数、少逾2万倍；跨模态位置为10.0 mAP，其他位置8.4。匹配精度的LoRA使NaturalBench准确率相对降35%，软提示保持不变，但随机种子方差更高；RoboCasa三项任务中两项匹配LoRA。

## 值不值得读

- **和你的研究有什么关系**：对多模态模型和VLA研究者，提供极少可训练参数的适配路径，并把保留原能力作为评估维度。
- **先别急着信**：不遗忘结论应限于已报告评测；VLA仅三项任务，且软提示优化方差较高，不能据此认定普遍优于LoRA。
- **判断**：值得精读位置、初始化和方差实验，VLA结果适合作为进一步验证的起点。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/Your Model Already Knows Don't Teach It, Learn to Ask It Soft Prompting for Few-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision. Existing adaptation methods are discrete prompt optimization and LoRA fine-tuning. We revisit a third option: soft prompting, where a small number of continuous prompt tokens are optimized while the pretrained backbone remains frozen. We identify two key design choices. First, placing prompt tokens at the cross-modal boundary between visual and text tokens outperforms other placements (10.0 vs. 8.4 mAP). Second, initializing prompts from the empty space token outperforms semantic and random initialization. With these choices, one to three learned tokens (7,168 parameters on average) match the best LoRA configuration on Roboflow20-VL (14.2 mAP, 10-shot) while training over 20,000x fewer parameters. Soft prompting remains harder to optimize, exhibiting higher variance across random seeds. Unlike LoRA, however, it causes no forgetting: the LoRA rank matching our accuracy reduces NaturalBench VQA accuracy by 35% relative, rising to 56% at the largest rank, whereas soft prompting leaves pretrained performance unchanged. The learned tokens behave like prompts rather than weights. They transfer to a newer model without retraining (+0.8 mAP on Qwen3.5-9B) and can be verbalized into readable prompts competitive with prompt-search methods (matching DetPO and outperforming GEPA). The approach also extends beyond detection. On RoboCasa manipulation tasks, the frozen $π_{0.5}$ vision-language-action policy benefits from soft prompting, matching the LoRA baseline on two of three tasks when tokens are placed at the gradient bottleneck. These results suggest modern VLMs already encode much of what is needed for specialized domains; the challenge is learning how to ask.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11310v1
- Authors: Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang, Cesar Daniel Hernandez, Wei Zhao, Wolfgang M. Pauli, John Galeotti, Deva Ramanan
- Published: 2026-09-10T09:38:11Z
- Age days: 1

</details>
