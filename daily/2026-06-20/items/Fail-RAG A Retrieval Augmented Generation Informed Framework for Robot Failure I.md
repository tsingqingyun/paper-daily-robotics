---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.19598v1"
published: "2026-06-17T21:02:47Z"
age_days: 2
score: 34
created: 2026-06-20
concepts: ["多模态基础模型", "世界模型"]
---

# Fail-RAG : A Retrieval Augmented Generation Informed Framework for Robot Failure Identification

> [!summary] 一句话结论（基于摘要）
> Fail-RAG achieved 25 percentage point higher failure detection accuracy on average across five types of robot operations compared to using off-the- shelf VLMs, indicating its effectiveness for real-world failure detection.

## 关键点

- **问题**：Specifically, we refer to any unexpected events as failures and develop methods to detect robot operations related failures.
- **创新点 / 方法**：We propose 'Fail-RAG', a Retrieval Augmented Generation (RAG)-based failure detection framework where failure images and context information are embedded and queried against a failure database by calculating their similarities.
- **证据**：Fail-RAG achieved 25 percentage point higher failure detection accuracy on average across five types of robot operations compared to using off-the- shelf VLMs, indicating its effectiveness for real-world failure detection.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Industry automation is witnessing an evolution in robotics driven by both technological
breakthroughs and societal changes: progress towards generalist robots, embodied and
physical artificial intelligence (AI), and increasing labor shortage in manufacturing.An
intelligent autonomous robot needs to not only act according to planned motions but also
react to any unexpected events. In this study, we focus on such unexpected events in
warehouses where robots are used for material handling. Specifically, we refer to any
unexpected events as failures and develop methods to detect robot operations related
failures. Rule-based detection methods may break since the form of failures could change
due to the dynamic nature of both environments and tasks. We propose 'Fail-RAG', a
Retrieval Augmented Generation (RAG)-based failure detection framework where failure
images and context information are embedded and queried against a failure database by
calculating their similarities. Vision-Language Models (VLMs) are further used to
analyze failures and provide details by following our instruction template. We evaluated
the performance of Fail-RAG by conducting both simulation and physical experiments using
fixed robot arms and a mobile manipulator for multiple tasks that are common in
warehouse automation. Fail-RAG achieved 25 percentage point higher failure detection
accuracy on average across five types of robot operations compared to using off-the-
shelf VLMs, indicating its effectiveness for real-world failure detection.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.19598v1
- Authors: Ameya Salvi, Jie Hu
- Published: 2026-06-17T21:02:47Z
- Age days: 2

</details>
