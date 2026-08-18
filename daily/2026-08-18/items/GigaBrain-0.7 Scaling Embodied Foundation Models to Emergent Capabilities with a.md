---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15875v1"
published: "2026-08-16T17:54:15Z"
age_days: 1
score: 43
created: 2026-08-18
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture

> [!summary] 一句话结论（基于摘要）
> Compared with the preceding GigaBrain-0 series and prior state-of-the-art models including $π_{0.5}$, GigaBrain-0.7 achieves substantial improvements in foundation zero-shot capabilities, language-conditioned instruction following, and post-training task succ…

## 关键点

- **问题**：Yet it remains an open question whether current VLA systems can benefit from more effective architectural design, scale to substantially larger and more heterogeneous data regimes, and achieve broader generalization across tasks and embodiments.
- **创新点 / 方法**：To this end, we present GigaBrain-0.7, an embodied foundation model with substantially improved generalization across diverse robot embodiments.
- **证据**：Compared with the preceding GigaBrain-0 series and prior state-of-the-art models including $π_{0.5}$, GigaBrain-0.7 achieves substantial improvements in foundation zero-shot capabilities, language-conditioned instruction following, and post-training task success rates.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/GigaBrain-0.7 Scaling Embodied Foundation Models to Emergent Capabilities with a.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have become a dominant paradigm for generalist embodied agents, demonstrating strong complex and long-horizon task completion in structured settings. Yet it remains an open question whether current VLA systems can benefit from more effective architectural design, scale to substantially larger and more heterogeneous data regimes, and achieve broader generalization across tasks and embodiments. To this end, we present GigaBrain-0.7, an embodied foundation model with substantially improved generalization across diverse robot embodiments. Specifically, GigaBrain-0.7 unifies understanding, prediction, and action through a three-system architecture, scales pretraining to over 37,000 hours of heterogeneous embodied data, and introduces one-stage alignment training that jointly optimizes vision-language understanding and multi-embodiment action generation. Compared with the preceding GigaBrain-0 series and prior state-of-the-art models including $π_{0.5}$, GigaBrain-0.7 achieves substantial improvements in foundation zero-shot capabilities, language-conditioned instruction following, and post-training task success rates. In particular, on our in-house Maker H01 platform and mainstream robot embodiments, GigaBrain-0.7 demonstrates strong task adaptability and completion ability across both home and industrial scenarios. All training code and pretrained model weights will be released.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15875v1
- Authors: GigaBrain Team, Angen Ye, Axiang Sun, Can Jin, Chenxi Cheng, Chong Shi, Dengke Shang, Dingqian Zhang, Guan Huang, Guangqiang Wang, Guangqing Ding, Guo Li, Hangcong Li, Hengyu Zhong, Hongtao Lu, Jianbo Qin, Jiming Mao, Jing Zhu, Jindi Lv, Jingzhi Cui, Junjie Xie, Junyi Bao, Kai Liu, Lei Yuan, Limin Long, Lv Feng, Mingming Yu, Peng Li, Pengfei Yi, Qi Li, Qianli Zhang, Qingfang Li, Qitang Hu, Rui Zhang, Shaoyan Sun, Shibo Sun, Shiying Duan, Tenghui Chen, Tianze Liu, Weijie Ke, Wenyao Xue, Xiaofeng Wang, Xiaoyu Tian, Xinyu Liu, Xinze Chen, Yang Wang, Yankai Wang, Yejun Zeng, Yifan Li, Yifei Nie, Yilong Li, Yilong Liu, Yongchao Feng, Yumeng Wang, Yun Ye, Zhichao Liu, Ziheng He, Zonghai Yang, Zheng Zhu
- Published: 2026-08-16T17:54:15Z
- Age days: 1

</details>
