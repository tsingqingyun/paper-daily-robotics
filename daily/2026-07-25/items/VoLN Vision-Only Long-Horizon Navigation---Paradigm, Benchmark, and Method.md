---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.21400v1"
published: "2026-07-23T15:02:01Z"
age_days: 1
score: 25
created: 2026-07-25
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# VoLN: Vision-Only Long-Horizon Navigation---Paradigm, Benchmark, and Method

> [!summary] 一句话结论（基于摘要）
> On the five-environment Test-Unseen split, it obtains success rates of 7.4%, 4.5%, and 1.8% on Easy, Normal, and Hard episodes, respectively.

## 关键点

- **问题**：However, route-level instructions commonly encode spatial priors, such as orientation, distance, and layout, that are not explicitly available from onboard sensing at deployment in open, GPS-denied environments.
- **创新点 / 方法**：As a complementary formulation, we propose Vision-Only Long-Horizon Navigation (VoLN), which shifts route-relevant information from externally supplied instructions and global guidance to locally observable in-scene cues.
- **证据**：On the five-environment Test-Unseen split, it obtains success rates of 7.4%, 4.5%, and 1.8% on Easy, Normal, and Hard episodes, respectively.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-25/VoLN Vision-Only Long-Horizon Navigation---Paradigm, Benchmark, and Method.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-and-Language Navigation (VLN) enables embodied agents to follow natural-language
instructions. However, route-level instructions commonly encode spatial priors, such as
orientation, distance, and layout, that are not explicitly available from onboard
sensing at deployment in open, GPS-denied environments. Benchmark performance under such
interfaces therefore jointly reflects visual navigation ability and the use of route
structure explicitly supplied by the task description. As a complementary formulation,
we propose Vision-Only Long-Horizon Navigation (VoLN), which shifts route-relevant
information from externally supplied instructions and global guidance to locally
observable in-scene cues. In VoLN, goal views specify the destination, while route-
relevant information is available only through locally observable in-scene cues that the
agent must detect, interpret, and select online. We instantiate VoLN for aerial
navigation through VoLN-UAV, a 7,210-episode benchmark that combines long-horizon goal-
directed flight, continuous 3D motion, large viewpoint changes, and context-dependent
beacon selection. We further provide VoLN-MLLM as an initial reference baseline. It
aligns self-supervised visual features with a structured semantic space and predicts
short-horizon waypoint segments from observation history, goal views, retrieved visual--
semantic tokens, and proprioception. On the five-environment Test-Unseen split, it
obtains success rates of 7.4%, 4.5%, and 1.8% on Easy, Normal, and Hard episodes,
respectively. These results provide an initial evaluation of VoLN and reveal substantial
remaining challenges in long-horizon evidence integration, cross-view goal matching, and
closed-loop stability. Project page: https://admire-ljb.github.io/VoLN-UAV/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.21400v1
- Authors: Jiabin Lou, Haopeng Wang, Yuanshuai Wang, Xinyu Liu, Xuxin Lv, Yuxin Guo, Lei Huang, Rongye Shi, Wenjun Wu
- Published: 2026-07-23T15:02:01Z
- Age days: 1

</details>
