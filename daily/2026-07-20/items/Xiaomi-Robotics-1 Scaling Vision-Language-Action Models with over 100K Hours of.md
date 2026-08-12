---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.15330v1"
published: "2026-07-16T16:02:25Z"
age_days: 3
score: 43
created: 2026-07-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories

> [!summary] 一句话结论（基于摘要）
> Xiaomi- Robotics-1 consistently improves with increased data scales and model sizes during pre- training.

## 关键点

- **问题**：We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data.
- **创新点 / 方法**：We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data.
- **证据**：Xiaomi- Robotics-1 consistently improves with increased data scales and model sizes during pre- training.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-20/Xiaomi-Robotics-1 Scaling Vision-Language-Action Models with over 100K Hours of.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable
of (1) following diverse language instructions to perform a wide range of mobile
manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting
to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training
recipe consisting of pre-training and post-training. During pre-training, we imbue the
model with broad and generalizable action-generation capabilities by training on over
100k hours of real-world manipulation trajectories collected via UMI devices. Crucially,
we develop a scalable auto-labeling pipeline that annotates trajectory clips with
natural languages describing scene state transitions, providing rich and precise
conditioning for action learning. During post-training, we aim to align these
capabilities with robot embodiments and imperative instructions that humans naturally
use to prompt robots. Extensive experiments demonstrate strong scaling behavior. Xiaomi-
Robotics-1 consistently improves with increased data scales and model sizes during pre-
training. This scaling behavior directly transfers to post-training, where a stronger
pre-training model yields better out-of-the-box real-robot performance in unseen
environments. Furthermore, Xiaomi-Robotics-1 serves as a strong robot foundation policy
that can be efficiently fine-tuned on complex, dexterous tasks with high data
efficiency. Across multiple simulation benchmarks, Xiaomi-Robotics-1 outperforms state-
of-the-art methods. Notably, it establishes a new state-of-the-art with a 57.6% success
rate on RoboCasa365, surpassing the previous best of 46.6%. Furthermore, it achieves an
average score of 20.07 on RoboDojo, significantly outperforming the prior state-of-the-
art (13.07). Code and model checkpoints will be released. Project page:
https://robotics.xiaomi.com/xiaomi-robotics-1.html

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.15330v1
- Authors: Xiaomi Robotics Team, Jun Guo, Piaopiao Jin, Jason Li, Peiyan Li, Yingyan Li, Futeng Liu, Wanli Peng, Optimus Qin, Yifei Su, Nan Sun, Qiao Sun, Runze Suo, Heyun Wang, Yunhong Wang, Rujie Wu, Caoyu Xia, Lina Zhang, Jack Zhao, Guoliang Chen, Wenlong Chen, Xinze He, Bin Li, Qing Li, Zhuorong Li, Heng Qu, Wenxuan Song, Diyun Xiang, Yifan Xie, Peiran Xu, Hangjun Ye, Wen Ye, Han Zhao, Quanyun Zhou
- Published: 2026-07-16T16:02:25Z
- Age days: 3

</details>
