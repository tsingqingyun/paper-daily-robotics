---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2603.14371"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 46
created: 2026-10-15
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA"]
---

# OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism

> [!summary] 这篇论文到底做了什么（基于摘要）
> OxyGen 让机器人做动作、说话等并发任务时，共用已经算过的观测缓存，并把尚未说完的语言请求接着往后排。这样既减少重复计算，又给每帧动作控制留出计算预算。

## 问题

机器人可能一边操作，一边回答问题和建立记忆：它们看的是同一批观测，却有不同时间要求。摘要指出，现有设备端推理把各任务的 KV 缓存分开管理，导致共享观测重复计算，也让语言生成与动作执行争抢资源。

### 用一个例子理解

理解用例（非论文实验）：机器人看到桌面后，一边抓杯子，一边回答“你拿的是什么”。系统先计算一次共享视觉输入；动作按当前周期执行，语言只生成预算允许的部分，未完成回答在后续周期继续推进，最终输出动作和完整回答。

## 创新点或方法

旧做法为任务各管一份缓存；OxyGen 把缓存作为跨任务、跨控制周期的共享资源。第一步共享观测对应的 KV，免去重复的输入预计算；第二步把不同帧尚未完成的语言请求持续组批，在每帧限定的解码预算内推进。本文改的是推理系统，摘要未描述重新训练模型；哪些缓存能够安全共享、预算如何设置，仍需看实现。

### 方法如何工作

1. 识别并发任务共同使用的观测，将其预计算结果保存下来，为复用建立基础。
2. 让兼容任务读取同一份观测 KV，减少重复 prefill，释放计算与存储资源。
3. 保留各帧未完成的语言请求并持续组批，让它们能够跨控制周期继续生成。
4. 在每帧解码预算内推进语言，同时运行动作输出，减少长回答对控制周期的占用。

### 必要术语

- KV 缓存：注意力计算保存的键和值；复用它可避免重复处理已有输入。
- Prefill：先把输入序列计算一遍并建立缓存；本文减少共享观测的重复 prefill。
- 连续组批：请求未结束就保留，新请求也可加入；本文将不同帧的语言请求一起推进。
- MoT：由不同 Transformer 部分承担不同输出的模型组织方式；本文面向这类多任务 VLA。

## 证据

摘要在 RTX 4090 和 Jetson AGX Thor 上评测 π₀.₅，报告相对独立执行最高 3.7 倍加速；在 RTX 4090 上同时实现超过 200 tokens/s 的语言吞吐和 70 Hz 动作频率。另在 Xiaomi-Robotics-0、StarVLA 上验证，并展示搭载 Thor 的人形机器人推理收益。摘要未给各硬件完整结果、延迟分布或任务成功率，不能把 4090 数字归给机器人板载实验。

## 局限

最高加速不能代表所有负载。语言吞吐高也不保证每次动作都准时；摘要中的动作频率还不足以说明最慢一帧的延迟。我会核查任务数量、语言长度变化时的控制抖动，以及跨帧请求怎样保持各自的观测语境。

- **判断**：如果关心多任务 VLA 上机部署，值得读到缓存兼容条件和调度实现；摘要已给明确系统收益，但还需用尾部延迟判断控制可靠性。

## 研究关联

可借鉴的思路是：多任务不一定要为每条输出重复处理同一幅图像。对共享输入、截止时间不同的请求，先复用计算，再按控制周期安排剩余生成工作，可能比单独加速每个任务更有效。

### 下一步读哪里

先查哪些 token、层和专家可以共享 KV，再查跨帧请求的缓存生命周期与解码预算。实验重点看相同并发负载下的显存、动作延迟分位数和语言响应时间，并核查 Thor 真机的具体数值。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA
- **筛选分数**：46
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/OxyGen Unified KV Cache Management for VLA Inference under Multi-Task Parallelis.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2603.14371v3 Announce Type: replace Abstract: Embodied AI agents increasingly require parallel execution of multiple tasks, such as manipulation, conversation, and memory construction, from shared observations under distinct time constraints. Recent Mixture-of-Transformers (MoT) Vision-Language-Action Models (VLAs) support such heterogeneous outputs, yet existing inference systems incur redundant computation and resource contention when serving concurrent tasks on-device. We identify isolated KV cache management as the root cause. To address this, we propose unified KV cache management, an inference design that treats the KV cache as a first-class shared resource across tasks and control cycles. This abstraction enables two key optimizations: cross-task KV sharing eliminates redundant prefill of shared observations, while cross-frame continuous batching batches unfinished language requests from different frames and advances them within a per-frame decoding budget. We implement this design in OxyGen and evaluate $\pi_{0.5}$ on NVIDIA GeForce RTX 4090 and Jetson AGX Thor. OxyGen achieves up to 3.7$\times$ speedup over isolated execution, delivering over 200 tokens/s language throughput and 70 Hz action frequency simultaneously on RTX 4090. We also validate the design on Xiaomi-Robotics-0 and StarVLA across different backbones and expert configurations. We further demonstrate the inference gains on a humanoid robot with on-board Jetson AGX Thor.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2603.14371
- Authors: Xiangyu Li, Huaizhi Tang, Xin Ding, Weijun Wang, Ting Cao, Yunxin Liu
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
