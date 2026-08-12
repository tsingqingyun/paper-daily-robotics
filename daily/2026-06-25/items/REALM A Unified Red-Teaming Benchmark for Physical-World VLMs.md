---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23892v1"
published: "2026-06-22T19:41:57Z"
age_days: 2
score: 33
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs

> [!summary] 一句话结论（基于摘要）
> Our evaluation shows that text and typographic injection attacks induce the most failures, multimodal co-optimization yields the strongest visual-perturbation transfer, single- pass attacks approach iterative methods at much lower cost, and model scale alone…

## 关键点

- **问题**：Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluat…
- **创新点 / 方法**：We introduce REALM, to our knowledge the first unified red- teaming benchmark for physical-world VLMs.
- **证据**：Our evaluation shows that text and typographic injection attacks induce the most failures, multimodal co-optimization yields the strongest visual-perturbation transfer, single- pass attacks approach iterative methods at much lower cost, and model scale alone does not confer adversarial robustness.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-25/REALM A Unified Red-Teaming Benchmark for Physical-World VLMs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language models (VLMs) are increasingly used as perception-reasoning backbones
for embodied intelligence in safety-critical physical systems, where perception or
reasoning errors can lead to unsafe decisions or actions. Although many red-teaming
methods have been developed to probe VLM vulnerabilities, their evaluation remains
fragmented across datasets, metrics, and threat models, making direct comparison
difficult and obscuring whether observed differences arise from stronger attacks, more
vulnerable models, or incompatible evaluation settings. Existing chatbot-centric red-
teaming benchmarks mainly standardize jailbreak and content-safety evaluation, but they
do not systematically capture physically grounded functional failures or cover red-
teaming methods that target physical-world VLMs. This raises the key challenge of
comparing diverse attack methods under a unified protocol while targeting the same
scenario-specific failures. We introduce REALM, to our knowledge the first unified red-
teaming benchmark for physical-world VLMs. REALM integrates 12 red-teaming methods, 3
model-agnostic defenses, and 13 VLMs under a practical black-box threat model with
shared datasets and metrics. To align adversarial objectives across attack families,
REALM introduces an agentic target-generation pipeline that constructs shared, scenario-
specific, and physically grounded attack objectives for each scene, enabling fair
comparison of diverse red-teaming methods under aligned adversarial goals. Our
evaluation shows that text and typographic injection attacks induce the most failures,
multimodal co-optimization yields the strongest visual-perturbation transfer, single-
pass attacks approach iterative methods at much lower cost, and model scale alone does
not confer adversarial robustness. Code is available at https://github.com/UCF-ML-
Research/REALM.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23892v1
- Authors: Yifei Zhao, Qian Lou, Mengxin Zheng
- Published: 2026-06-22T19:41:57Z
- Age days: 2

</details>
