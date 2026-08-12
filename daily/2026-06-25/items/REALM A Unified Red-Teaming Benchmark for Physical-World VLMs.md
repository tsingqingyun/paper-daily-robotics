---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.23892v1"
published: "2026-06-22T19:41:57Z"
age_days: 2
score: 33
created: 2026-06-25
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.23892v1
- Authors: Yifei Zhao, Qian Lou, Mengxin Zheng
- Published: 2026-06-22T19:41:57Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
