---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.18287v1"
published: "2026-05-18T12:15:16Z"
age_days: 1
score: 30
created: 2026-05-20
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# StableVLA: Towards Robust Vision-Language-Action Models without Extra Data

> [!summary] 一句话结论（基于摘要）
> Without requiring any extra data or augmentation strategies, IB- Adapter consistently improves over the baseline by an average of 30%, while adding fewer than 10M parameters, demonstrating notable efficiency and effectiveness.

## 关键点

- **问题**：It is infeasible to encompass all possible disturbances within the training dataset.
- **创新点 / 方法**：To mitigate this issue, we propose a lightweight adapter module grounded in information theory, termed the Information Bottleneck Adapter (IB-Adapter), which selectively filters potential noise from visual inputs.
- **证据**：Without requiring any extra data or augmentation strategies, IB- Adapter consistently improves over the baseline by an average of 30%, while adding fewer than 10M parameters, demonstrating notable efficiency and effectiveness.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-20/StableVLA Towards Robust Vision-Language-Action Models without Extra Data.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

It is infeasible to encompass all possible disturbances within the training dataset.
This raises a critical question regarding the robustness of Vision-Language-Action (VLA)
models when encountering unseen real-world visual disturbances, particularly under
imperfect visual conditions. In this work, we conduct a systematic study based on recent
state-of-the-art VLA models and reveal a significant performance drop when visual
disturbances absent from the training data are introduced. To mitigate this issue, we
propose a lightweight adapter module grounded in information theory, termed the
Information Bottleneck Adapter (IB-Adapter), which selectively filters potential noise
from visual inputs. Without requiring any extra data or augmentation strategies, IB-
Adapter consistently improves over the baseline by an average of 30%, while adding fewer
than 10M parameters, demonstrating notable efficiency and effectiveness. Furthermore,
even with a 14x smaller backbone (0.5B parameters) and no pre-training on the Open
X-Embodiment dataset, our model StableVLA achieves robustness competitive with 7B-scale
state-of-the-art VLAs. With negligible parameter overhead (<10M), our approach maintains
accuracy on long-horizon tasks and surpasses OpenPi under both synthetic and physical
visual corruptions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.18287v1
- Authors: Yiyang Fu, Chubin Zhang, Shukai Gong, Yufan Deng, Kaiwei Sun, Qiyang Min, Qibin Hou, Yansong Tang, Jianan Wang, Daquan Zhou
- Published: 2026-05-18T12:15:16Z
- Age days: 1

</details>
