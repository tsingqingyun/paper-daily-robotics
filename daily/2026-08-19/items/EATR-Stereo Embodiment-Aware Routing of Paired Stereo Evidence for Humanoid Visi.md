---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17453v1"
published: "2026-08-18T07:32:50Z"
age_days: 0
score: 32
created: 2026-08-19
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control

> [!summary] 一句话结论（基于摘要）
> EATR-Stereo achieves 60.0% full-task success, 100.0% grasp success, and 80.0% stage success.

## 关键点

- **问题**：Long-horizon humanoid vision--language--action (VLA) control with head-mounted stereo cameras requires visual interfaces that can exploit complementary views while maintaining compatibility with pretrained representations.
- **创新点 / 方法**：We present EATR-Stereo, an embodiment-aware token-routing framework that retains primary-view tokens and constructs primary-aligned Cross-View Auxiliary Tokens (CVATs) by querying the synchronized auxiliary-view token sequence.
- **证据**：EATR-Stereo achieves 60.0% full-task success, 100.0% grasp success, and 80.0% stage success.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/EATR-Stereo Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Visi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon humanoid vision--language--action (VLA) control with head-mounted stereo cameras requires visual interfaces that can exploit complementary views while maintaining compatibility with pretrained representations. Existing interfaces often discard complementary stereo evidence or fuse additional observations without preserving the native primary-view pathway and adapting auxiliary information to robot embodiment. We present EATR-Stereo, an embodiment-aware token-routing framework that retains primary-view tokens and constructs primary-aligned Cross-View Auxiliary Tokens (CVATs) by querying the synchronized auxiliary-view token sequence. A body-segmented proprioceptive encoder further conditions token-wise auxiliary usage on robot configuration history, enabling selective incorporation of stereo evidence during action generation. The routed auxiliary stream augments the language and primary-visual context of a pretrained VLA while keeping its vision--language model frozen. On a 33-DoF physical humanoid with a 37-D proprioceptive state, we evaluate nine configurations in over-100-s search--approach--grasp--place--return tasks. EATR-Stereo achieves 60.0% full-task success, 100.0% grasp success, and 80.0% stage success. Under severe asymmetric occlusion, it improves recovery to 80% compared with 30% for CVAT alone. Ablation studies further show the importance of preserving primary tokens and combining cross-view auxiliary features with structured proprioceptive routing. These results demonstrate that selectively routed paired stereo evidence improves spatial grounding for reliable long-horizon humanoid VLA control.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17453v1
- Authors: Songwei Wu, Rui Zhao, Fan Yang, Zhongqiang Nie, Zhiduo Jiang, Wandong Sun, Yuwei Li, Yang Liu, Hong Liu
- Published: 2026-08-18T07:32:50Z
- Age days: 0

</details>
