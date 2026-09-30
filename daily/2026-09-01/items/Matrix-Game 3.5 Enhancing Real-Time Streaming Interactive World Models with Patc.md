---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29910v1"
published: "2026-08-30T17:11:00Z"
age_days: 1
score: 33
created: 2026-09-01
concepts: ["智能体 Agent", "世界模型"]
---

# Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory

> [!summary] 先说人话（基于摘要）
> Matrix-Game 3.5 用无新增可学习参数的 patch memory 与 tiled-PRoPE 保持几何记忆，再分离静态场景和动态主体，并通过两阶段蒸馏实现分钟级实时交互生成。

## 这篇到底在做什么

- **卡在哪里**：持续交互式世界生成必须同时维持场景几何、动态一致性和相机可控性，还要实时自回归运行；长时间生成容易遗忘场景、漂移主体或失去相机控制。
- **关键解法**：输入历史画面、相机控制和提示，输出可实时交互的连续世界视频。显式 3D patch 检索配合投影相机条件负责长时回忆，静态—动态表征分别维护几何与主体身份；Perceptual Flow Matching 和基于课程的 Self-Rollout DMD 把双向扩散模型蒸馏为少步因果生成器。
- **拿什么证明**：摘要称在 Unreal 仿真、开放世界游戏和互联网视频的统一语料上，于长时场景回忆、相机控制、主体一致性、提示驱动生成及实时交互方面表现强，并支持分钟级生成；未给帧率、分辨率或基准数字。

## 值不值得读

- **和你的研究有什么关系**：对世界模型和具身 Agent，它探索了长时空间记忆与实时因果生成的结合，可作为虚拟环境预测或交互数据生成底座；摘要未证明其可直接支持机器人控制。
- **先别急着信**：“实时”和“几何一致”均缺少量化定义，且显式检索可能只是复用外观而非学到可交互物理，需要全文核查。
- **判断**：世界模型研究者值得读方法，尤其是 patch memory 与蒸馏；机器人研究者可先看评测再判断其物理价值。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/Matrix-Game 3.5 Enhancing Real-Time Streaming Interactive World Models with Patc.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Interactive world models extend video generation from offline clip synthesis toward persistent simulation of interactive virtual worlds, enabling applications in games, robotics, embodied agents, and XR. Achieving stable long-horizon interactive generation, however, remains challenging, as the model must simultaneously preserve scene geometry, dynamic consistency, and camera control while supporting real-time autoregressive generation. Building upon Matrix-Game 3.0, we present Matrix-Game 3.5, as shown in Figure 1, which advances real-time interactive world generation toward geometry-aware and long-horizon consistent simulation through three key improvements. First, we propose a unified geometry-aware memory framework, whose patch-memory and tiled-PRoPE components introduce no additional learnable parameters, combining explicit 3D patch retrieval with projective camera conditioning to enable geometry-consistent camera control and faithful long-horizon scene recall. Second, we introduce a static-dynamic disentangled world representation that separately models static scene geometry and dynamic subjects, preserving both geometric consistency and subject identity throughout long-horizon generation. Third, we develop a two-stage progressive real-time distillation framework that converts a bidirectional diffusion model into a few-step causal generator through Perceptual Flow Matching and curriculum based Self-Rollout DMD, enabling minute-long real-time interactive generation. Extensive experiments demonstrate that, with a unified training corpus spanning Unreal simulation environments, open-world games, and internet videos, MatrixGame 3.5 achieves strong performance in long-horizon scene recall, precise camera control, subject consistency, prompt-driven world generation, and stable real-time open-world interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29910v1
- Authors: Runjia Qian, Zile Wang, Jihai Zhang, Kai Zou, Wei Yu, Jiaxing Li, Zexiang Liu, Yaokun Li, Fei Kang, Kaichen Huang, Mengyin An, Haobo Zhang, Biao Jiang, Jiahua Wang, Haofeng Sun, Yang Liu, Yangguang Li
- Published: 2026-08-30T17:11:00Z
- Age days: 1

</details>
