---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18410v1"
published: "2026-08-19T00:38:23Z"
age_days: 1
score: 27
created: 2026-08-21
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies

> [!summary] 一句话结论（基于摘要）
> At matched visual-KV budgets, RoleSub outperforms a trained token-only control in 33 of 36 settings, with the largest gains under aggressive compression.

## 关键点

- **问题**：However, directly applying sub-token compression to VLA policies is less effective because information important for perception, language understanding, and control is distributed differently across the multimodal representation.
- **创新点 / 方法**：We introduce Role-Conditioned Sub-Token Routing (RoleSub), which learns how to compress the value representations of retained tokens.
- **证据**：At matched visual-KV budgets, RoleSub outperforms a trained token-only control in 33 of 36 settings, with the largest gains under aggressive compression.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models process long multimodal token sequences, making inference expensive in both memory and computation. Existing efficiency methods mainly reduce visual tokens, but aggressive token pruning becomes fragile because removing a token discards its entire representation. Sub-token compression provides a complementary alternative by retaining more tokens while reducing their value width. However, directly applying sub-token compression to VLA policies is less effective because information important for perception, language understanding, and control is distributed differently across the multimodal representation. We introduce Role-Conditioned Sub-Token Routing (RoleSub), which learns how to compress the value representations of retained tokens. After visual token reduction, RoleSub partitions each retained value representation into groups in an orthogonal space and uses a lightweight router to determine which groups should be preserved. The routing decision is conditioned on the token representation, a learned latent role representation, and language context. The same mechanism can also be applied to language values, allowing visual and language representations to be compressed without removing additional tokens. We evaluate RoleSub on OpenVLA-OFT-7B across the four LIBERO suites. At matched visual-KV budgets, RoleSub outperforms a trained token-only control in 33 of 36 settings, with the largest gains under aggressive compression. Combining visual and language compression reduces total KV to 9.2--11.3% of the original while retaining strong control performance on most tasks. These results show that reducing the representation within retained tokens provides an effective complement to token pruning for aggressive VLA compression.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18410v1
- Authors: Wei Jiang, Wei Wang
- Published: 2026-08-19T00:38:23Z
- Age days: 1

</details>
