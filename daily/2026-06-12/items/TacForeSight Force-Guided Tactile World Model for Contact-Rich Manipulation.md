---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11184v1"
published: "2026-06-09T17:59:03Z"
age_days: 2
score: 32
created: 2026-06-12
concepts: ["世界模型", "机器人学习"]
---

# TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation

> [!summary] 一句话结论（基于摘要）
> Real- robot experiments on five representative tasks and three in-process perturbation settings show that TacForeSight consistently outperforms existing baselines, particularly under dynamic contact disturbances.

## 关键点

- **问题**：Contact-rich manipulation requires robots to continuously perceive and regulate evolving physical interactions under dynamic contact transitions or complex surface geometries.
- **创新点 / 方法**：To address this, we propose TacForeSight, a lightweight force-conditioned tactile foresight framework for real-time manipulation.
- **证据**：Real- robot experiments on five representative tasks and three in-process perturbation settings show that TacForeSight consistently outperforms existing baselines, particularly under dynamic contact disturbances.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-12/TacForeSight Force-Guided Tactile World Model for Contact-Rich Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Contact-rich manipulation requires robots to continuously perceive and regulate evolving
physical interactions under dynamic contact transitions or complex surface geometries.
Recent imitation learning methods improve contact-aware control by incorporating tactile
or force feedback, but they rarely model the asymmetric spatiotemporal roles of global
force and local tactile sensing. To address this, we propose TacForeSight, a lightweight
force-conditioned tactile foresight framework for real-time manipulation. The core
component is TacForceWM, a tactile world model that predicts short-horizon tactile
latent dynamics from dual-finger tactile observations conditioned on high-frequency
wrist force and torque signals. Another key component, the Predictive Tactile-
Conditioned Policy, leverages the predicted latents as anticipatory contact priors,
models the current-to-future tactile evolution via cross-attention, and adaptively fuses
visuo-tactile features through a tactile-guided gating module. By forecasting purely
within a compact latent space, TacForeSight enables proactive contact reasoning with
efficient real-time inference suitable for high-frequency manipulation control. Real-
robot experiments on five representative tasks and three in-process perturbation
settings show that TacForeSight consistently outperforms existing baselines,
particularly under dynamic contact disturbances. All models and datasets will be made
publicly available on the project website at https://tacforesight.github.io/ProjectPage.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11184v1
- Authors: Yujie Zang, Yuhang Zheng, Xian Nie, Yupeng Zheng, Shuai Tian, Songen Gu, Chen Gao, Zining Wang, Shuicheng Yan, Wenchao Ding
- Published: 2026-06-09T17:59:03Z
- Age days: 2

</details>
