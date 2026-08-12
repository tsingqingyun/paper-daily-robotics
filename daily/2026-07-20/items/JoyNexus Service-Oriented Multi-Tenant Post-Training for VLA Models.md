---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.16074v1"
published: "2026-07-17T15:58:20Z"
age_days: 2
score: 34
created: 2026-07-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models

> [!summary] 一句话结论（基于摘要）
> Results show that, compared with isolated single-tenant execution, JoyNexus reduces aggregate GPU time and improves service utilization via cross-tenant scheduling on shared resources.

## 关键点

- **问题**：Multiple tenants submit workloads concurrently; their action modules, optimizers, rollout records, and policy versions remain isolated, and the service is scheduled by the global Training Queue and Inference Queue.
- **创新点 / 方法**：To address these challenges, we present JoyNexus, a unified service for multi-tenant VLA supervised fine- tuning, reinforcement learning, and evaluation.
- **证据**：Results show that, compared with isolated single-tenant execution, JoyNexus reduces aggregate GPU time and improves service utilization via cross-tenant scheduling on shared resources.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

The post-training of Vision-Language-Action (VLA) models is essential due to the
diversity of simulators, robot embodiments, and task objectives. Existing compute
services, whether offered as direct accelerator rental or batch-workload submission,
typically allocate an exclusive set of GPU and CPU resources to a single tenant. While
this paradigm maximizes client flexibility, it burdens users with infrastructure
adaptation, and the fixed card-hour accounting model renders short or bursty workloads
both expensive for tenants and inefficient for the service provider. To address these
challenges, we present JoyNexus, a unified service for multi-tenant VLA supervised fine-
tuning, reinforcement learning, and evaluation. JoyNexus decouples the Training Model
Service, Inference Model Service, and Environment Service, each accessed through APIs
and backed by resident shared base models with tenant-specific slots. Tenants can
directly invoke high-level semantic APIs for training, rollout, and evaluation, or
compose custom algorithms using lower-level APIs and their assigned endpoints. Multiple
tenants submit workloads concurrently; their action modules, optimizers, rollout
records, and policy versions remain isolated, and the service is scheduled by the global
Training Queue and Inference Queue. To further improve multi-tenant training efficiency,
JoyNexus introduces group batching for heterogeneous VLA data schemas that share a
compatible model-facing prefix, enabling a single shared backbone forward pass over
grouped samples. Finally, we evaluate JoyNexus through workload simulation and a group-
batching pipeline in a realistic embodied scenario. Results show that, compared with
isolated single-tenant execution, JoyNexus reduces aggregate GPU time and improves
service utilization via cross-tenant scheduling on shared resources.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.16074v1
- Authors: Haoran Sun, Wentao Zhang, Junyang Hua, Hedan Yang, Yongjian Guo, Yifei Zhang, Xiaolong Xiang, Mingxi Luo, Jing Long, Chen Zhao, Chen Zhou, Wanting Xu, Qiming Yang, Hui Zhang, Song Wang, Xiaodong Bai, Shuai Di, Xu Chu, Xiaotie Deng, Yicheng Gong, Junwu Xiong
- Published: 2026-07-17T15:58:20Z
- Age days: 2

</details>
