---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.18847v1"
published: "2026-07-21T08:35:22Z"
age_days: 0
score: 28
created: 2026-07-22
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Data Leakage Prevention in Agentic Applications via Preemptive Hardening

## 为什么重要

自动筛选分数：28

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Agentic systems integrate LLM driven planning with interfaces to external tools, making
data leakage and tool misuse feasible via instruction/data boundary failures and prompt
injection attacks. Enforcing required controls consistently is particularly challenging
in workflows spanning many codebases and heterogeneous agents. To address this challenge
in multi agentic systems, we present a pre-deployment pipeline for scanning, hardening,
and validation of agentic applications. The pipeline analyzes prompt templates, tool
interfaces, and tool-invocation code to identify leakage-enabling patterns and generate
actionable patches. The hardened application is then validated through adversarial
prompt injection attacks and benign input variations ensuring that mitigations do not
disrupt intended behavior. In the hardening stage, high-risk tools are prioritized, and
minimally invasive mitigations are applied, including schema tightening, boundary
sanitization, allowlist-based tool gating, and least-privilege checks. In the validation
stage, the pipeline automatically generates attack inputs that mimic jailbreaks,
instruction overrides, and tool-targeted manipulation, along with benign task variants,
to confirm that the functionality of the hardened application is preserved after
remediation. We evaluated the pipeline on five real-world agentic applications, as well
as on the AgentDojo benchmark. Across all applications, the proposed pipeline identified
recurring leakage-enabling patterns and generated patches that can be integrated without
disrupting the intended application behavior. The resulting modifications of application
code were shown to eliminate leaks when targeted by basic jailbreak and instruction-
override attacks, achieving a 100% reduction in leakage, and reduce leaks by 91% under
conditions of stress-induced manipulation, without the need of continuous runtime policy
enforcement.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.18847v1
- Authors: Akansha Shukla, Emily Bellov, Parth Atulbhai Gandhi, Yuval Elovici, Asaf Shabtai
- Published: 2026-07-21T08:35:22Z
- Age days: 0

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
