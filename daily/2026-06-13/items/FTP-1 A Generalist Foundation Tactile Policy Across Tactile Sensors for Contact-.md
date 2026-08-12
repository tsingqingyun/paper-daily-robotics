---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.13102v1"
published: "2026-06-11T09:30:09Z"
age_days: 1
score: 31
created: 2026-06-13
concepts: ["机器人学习", "具身智能评测与基准"]
---

# FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation

> [!summary] 一句话结论（基于摘要）
> Across downstream finetuning experiments spanning 5 hardware configurations, FTP-1 improves contact-rich manipulation on seen sensor setups by +17.2% and, surprisingly, transfers to two previously unseen tactile-sensor setups, achieving a +31% gain in success…

## 关键点

- **问题**：Despite the success of vision-based generalist robotic policies, existing tactile-based policies remain tied to fixed embodiments and sensor setups.
- **创新点 / 方法**：We present FTP-1,the first generalist foundation tactile policy pretrained to acquire transferable tactile manipulation abilities across diverse sensors and embodiments.
- **证据**：Across downstream finetuning experiments spanning 5 hardware configurations, FTP-1 improves contact-rich manipulation on seen sensor setups by +17.2% and, surprisingly, transfers to two previously unseen tactile-sensor setups, achieving a +31% gain in success rate.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-13/FTP-1 A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Despite the success of vision-based generalist robotic policies, existing tactile-based
policies remain tied to fixed embodiments and sensor setups. This is because tactile
signals are highly heterogeneous across hardware, making cross-sensor generalization
difficult. We present FTP-1,the first generalist foundation tactile policy pretrained to
acquire transferable tactile manipulation abilities across diverse sensors and
embodiments. FTP-1 supports varied tactile inputs, including image-, array-, and state-
based signals, by using heterogeneous encoders to project them into unified morphology-
aware latent tokens that are jointly modeled by a shared tactile Transformer expert.
Pretrained on around 3,000 hours of tactile manipulation data aggregated from 26 data
sources, spanning human and robot demonstrations across 21 sensors, FTP-1 learns tactile
skills that transfer beyond the sensors seen during pretraining. Across downstream
finetuning experiments spanning 5 hardware configurations, FTP-1 improves contact-rich
manipulation on seen sensor setups by +17.2% and, surprisingly, transfers to two
previously unseen tactile-sensor setups, achieving a +31% gain in success rate. FTP-1
establishes the first unified foundation baseline for tactile manipulation, providing
future tactile policies with a shared model-level starting point. Pretrained models,
datasets, training code and more visualization at https://ftp1-policy.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.13102v1
- Authors: Chengbo Yuan, Zicheng Zhang, Mingjie Zhou, Wendi Chen, Yi Wang, Zhuoyang Liu, Dantong Niu, Shuo Wang, Hui Zhang, Wenkang Zhang, Yingdong Hu, Yuanqing Gong, Wanli Xing, Chuan Wen, Cewu Lu, Kaifeng Zhang, Yang Gao
- Published: 2026-06-11T09:30:09Z
- Age days: 1

</details>
