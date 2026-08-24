---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.20791v1"
published: "2026-08-21T07:09:03Z"
age_days: 3
score: 24
created: 2026-08-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA"]
---

# CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> We introduce CertVLA, a certified defense for closed-loop VLA control under bounded patch and texture attacks.

## 关键点

- **问题**：Specifically, CertVLA normalizes action disagreement by the benign variation of each mask pair and accepts a single-mask anchor only when it remains consistent under every second mask.
- **创新点 / 方法**：We introduce CertVLA, a certified defense for closed-loop VLA control under bounded patch and texture attacks.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：Vision-Language-Action (VLA) policies are vulnerable to localized physical perturbations, yet existing certified patch defenses target discrete labels and cannot directly certify continuous, temporally correlated actions.

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-24/CertVLA Certified Defense against Physical Visual Attacks for Vision-Language-Ac.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) policies are vulnerable to localized physical perturbations, yet existing certified patch defenses target discrete labels and cannot directly certify continuous, temporally correlated actions. We introduce CertVLA, a certified defense for closed-loop VLA control under bounded patch and texture attacks. CertVLA proposes a calibrated region of behaviorally consistent actions, while deterministic covering masks ensure that at least one checked prediction is attack-free. Specifically, CertVLA normalizes action disagreement by the benign variation of each mask pair and accepts a single-mask anchor only when it remains consistent under every second mask. It then calibrates the resulting max-min-max episode score to provide finite-sample clean coverage. Conjoining query-level decisions extends the action certificate to the complete closed-loop rollout. Furthermore, we prove that against any adaptive attacker satisfying the bounded-support threat model, every rollout certified by CertVLA executes only action chunks consistent with attack-erased clean predictions. Under dual-mask rollout correctness, this consistency certificate further guarantees task success. The certificate is independent of patch content, generation method, and physical transformation. Experiments in simulation and the real world demonstrate the empirical and certified effectiveness of CertVLA against patch attacks, with additional simulation validation on texture attacks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.20791v1
- Authors: Hui Lu, Zhijie Peng, Yuqi Lin, Zaijia Yang, Jiaming He, Shuhan Ye, Yi Yu, Hanwei Zhu, Bingquan Shen, Alex Kot, Xudong Jiang
- Published: 2026-08-21T07:09:03Z
- Age days: 3

</details>
