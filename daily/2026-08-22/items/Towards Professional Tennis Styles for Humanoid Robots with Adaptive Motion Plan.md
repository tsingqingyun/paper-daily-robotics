---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20087v1"
published: "2026-08-20T14:19:36Z"
age_days: 1
score: 30
created: 2026-08-22
concepts: ["智能体 Agent", "世界模型", "Sim2Real", "具身智能评测与基准"]
---

# Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking

> [!summary] 一句话结论（基于摘要）
> To address these issues, our adaptation mechanism improves tracking robustness by learning to track randomized execution speeds, while conditioning the planner on a learned motion-speed adapter to mitigate compounding errors.

## 关键点

- **问题**：However, achieving professional motion styles while maintaining strong task performance remains challenging.
- **创新点 / 方法**：In this work, we propose AdaPT, an Adaptive Motion Planning and Tracking framework that learns professional tennis serving and rally styles directly from broadcast videos.
- **证据**：To address these issues, our adaptation mechanism improves tracking robustness by learning to track randomized execution speeds, while conditioning the planner on a learned motion-speed adapter to mitigate compounding errors.
- **局限**：However, achieving professional motion styles while maintaining strong task performance remains challenging.

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-22/Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Plan.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid robots have recently demonstrated promising capabilities in real-world ball sports. However, achieving professional motion styles while maintaining strong task performance remains challenging. In this work, we propose AdaPT, an Adaptive Motion Planning and Tracking framework that learns professional tennis serving and rally styles directly from broadcast videos. This hierarchical design is motivated by the key insight that the planner generates stylistic kinematic motions, while the tracker executes them with minimal interference with planning. Despite its effectiveness in simulation, a substantial sim-to-real gap emerges: tracking performance inevitably degrades on real robots, and this degradation is partially overlooked by autoregressive planning and further compounded by noisy perception. To address these issues, our adaptation mechanism improves tracking robustness by learning to track randomized execution speeds, while conditioning the planner on a learned motion-speed adapter to mitigate compounding errors. Real-world experiments on the Unitree G1 demonstrate the effectiveness of our adaptation mechanism in bridging the sim-to-real gap. We further deploy AdaPT policies on the full-size Dobot Atom humanoid robot (1.7m) and demonstrate in-the-wild serving without motion capture. Beyond these results, our real-world experiments reveal both algorithmic and engineering insights for future humanoid ball-sports systems. Videos and code are available on our \href{https://humanoidtennis.github.io/AdaPT/}{project website}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20087v1
- Authors: Tao Huang, Ruofei Liu, Xuchen Tang, Xinyin Zhang, Junli Ren, Huayi Wang, Feiyu Jia, Yukai Qi, Kangning Yin, Weishuai Zeng, Lipeng Chen, Xi Li, Ting Wu, Kailin Li, Ruoli Dai, Jingbo Wang, Lei Han, Jiangmiao Pang
- Published: 2026-08-20T14:19:36Z
- Age days: 1

</details>
