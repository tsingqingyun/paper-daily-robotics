---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18938v1"
published: "2026-08-19T14:06:31Z"
age_days: 1
score: 29
created: 2026-08-21
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# Breaking the weakest link to evade vision language models

> [!summary] 一句话结论（基于摘要）
> To efficiently generate adversarial examples, we propose a gradient-based attack method that performs optimization exclusively on the vision encoder of the VLM rather than on the entire multimodal architecture.

## 关键点

- **问题**：Despite their growing deployment, the robustness of VLMs against adversarial threats remains insufficiently explored, particularly in the context of evasion attacks targeting multimodal alignment.
- **创新点 / 方法**：To efficiently generate adversarial examples, we propose a gradient-based attack method that performs optimization exclusively on the vision encoder of the VLM rather than on the entire multimodal architecture.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Breaking the weakest link to evade vision language models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual inputs in real-world and safety-critical applications. Despite their growing deployment, the robustness of VLMs against adversarial threats remains insufficiently explored, particularly in the context of evasion attacks targeting multimodal alignment. In this work, we investigate the vulnerability of VLMs to adversarial perturbations applied to visual inputs and study two attack settings: untargeted attacks, where the goal is to disrupt the model's interpretation of the original image, and targeted attacks, where the adversary aims to force the model to generate a specific semantic description unrelated to the original image. To efficiently generate adversarial examples, we propose a gradient-based attack method that performs optimization exclusively on the vision encoder of the VLM rather than on the entire multimodal architecture. This design significantly reduces the computational cost and resource requirements of the attack while maintaining strong effectiveness. We evaluate our approach on several open-source VLMs, including Qwen2.5-VL, Granite-Vision, FastVLM, and Phi-3.5-Vision, and show that small, human-imperceptible perturbations can substantially alter the textual interpretation produced by the models. Our findings highlight the vulnerability of modern VLMs to adversarial manipulation and emphasize the need for improved robustness and security mechanisms in multimodal AI systems.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18938v1
- Authors: Ilan Zini, Boussad Addad, Katarzyna Kapusta
- Published: 2026-08-19T14:06:31Z
- Age days: 1

</details>
