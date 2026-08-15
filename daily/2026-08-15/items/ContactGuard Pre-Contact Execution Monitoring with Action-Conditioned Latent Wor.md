---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.13438v1"
published: "2026-08-13T16:25:54Z"
age_days: 1
score: 29
created: 2026-08-15
concepts: ["世界模型"]
---

# ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models

> [!summary] 一句话结论（基于摘要）
> We introduce \emph{ContactGuard}, a pre-contact execution monitor for chunked visuomotor policies.

## 关键点

- **问题**：Contact-rich manipulation failures are often detected only after the robot has committed to contact.
- **创新点 / 方法**：We introduce \emph{ContactGuard}, a pre-contact execution monitor for chunked visuomotor policies.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-15/ContactGuard Pre-Contact Execution Monitoring with Action-Conditioned Latent Wor.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Contact-rich manipulation failures are often detected only after the robot has committed to contact. This is especially limiting in wrist-camera setups: close gripper--object views help observe contact, but a poor approach may already push, miss, slip, or disturb the object before conventional detectors react. We introduce \emph{ContactGuard}, a pre-contact execution monitor for chunked visuomotor policies. Given the policy's planned action chunk, ContactGuard predicts its short-horizon consequence in latent visual space and aborts if the predicted future latent indicates likely failure. Its latent world model is trained from unlabelled robot trajectories to predict compact multi-view visual embeddings under planned actions, avoiding pixel-level video prediction. A lightweight failure probe is then trained from a small labelled set of pre-contact clips. At deployment, ContactGuard anchors prediction before an imminent contact event, rolls the model forward under the policy's own actions, and verifies the predicted post-contact latent. Across real-world contact-rich manipulation tasks, ContactGuard predicts failure more accurately than direct and corrupted-action ablations, and transfers to live robot as a pre-contact abort signal without modifying the underlying policy.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.13438v1
- Authors: Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi
- Published: 2026-08-13T16:25:54Z
- Age days: 1

</details>
