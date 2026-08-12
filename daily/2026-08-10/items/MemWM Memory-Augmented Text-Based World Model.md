---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.07107v1"
published: "2026-08-07T11:03:32Z"
age_days: 3
score: 24
created: 2026-08-10
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# MemWM: Memory-Augmented Text-Based World Model

> [!summary] 一句话结论（基于摘要）
> Compared with SFT, memory-augmented training improves SSF by up to 206.3%.

## 关键点

- **问题**：World models are increasingly used to support planning in agents by predicting how environment states evolve in response to agent actions.
- **创新点 / 方法**：To address such systematic prediction errors, we introduce MemWM, a memory-augmented text-based world model.
- **证据**：Compared with SFT, memory-augmented training improves SSF by up to 206.3%.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-10/MemWM Memory-Augmented Text-Based World Model.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World models are increasingly used to support planning in agents by predicting how
environment states evolve in response to agent actions. Yet fluent next-state
predictions can still omit task-critical facts, corrupt product attributes, or apply
incorrect transition rules. To address such systematic prediction errors, we introduce
MemWM, a memory-augmented text-based world model. MemWM uses world memory, a curated
memory bank of transition rules, state caches, and hard-to-predict facts, to condition
next-state imagination. We evaluate factual state preservation with Structured State
Fidelity (SSF), which scores predicted states through benchmark-specific facts and
fields. Compared with SFT, memory-augmented training improves SSF by up to 206.3%. In
the full planning setting, we keep the policy model frozen and provide policy-side world
skill: retrieved task-level skills and step-wise corrective guidance for action
selection. Across ALFWorld, WebShop, and ScienceWorld, memory-augmented agents improve
downstream success over an SFT-trained world-model agent, with up to a 65.4% relative
gain. Sensitivity analyses further show that retrieved memory improves task success and
efficiency under different memory and action-budget settings.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.07107v1
- Authors: Yujun Wang, Tao Zhang, Jinhe Bi, Aniri, Wenxuan Ye, Boliang Liu, Sikuan Yan, Shuning Wang, Xuebing Zhou, Sören Pirk, Hinrich Schütze, Yunpu Ma
- Published: 2026-08-07T11:03:32Z
- Age days: 3

</details>
