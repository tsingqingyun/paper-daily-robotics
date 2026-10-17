---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.22146v1"
published: "2026-10-15T16:17:18Z"
age_days: 1
score: 38
created: 2026-10-17
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> FastVLA 每次推理都先看任务主要依赖哪些图像区域，再决定保留多少视觉 token。注意力集中时多裁剪、分散时多保留，不用重新训练就能减少后续大模型计算。

## 问题

多视角图像转成大量视觉 token，拖慢闭环动作预测。固定裁剪比例忽视了不同步骤需要的信息量：有时要搜索全场景，有时只需局部区域。只按视觉显著性挑选，也可能保留醒目但与任务无关的内容。[S2](https://arxiv.org/html/2610.22146v1#S1.p1.1) [S3](https://arxiv.org/html/2610.22146v1#S1.p2.1) [S4](https://arxiv.org/html/2610.22146v1#S1.p3.1) [S5](https://arxiv.org/html/2610.22146v1#S1.p4.1)

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“把蓝杯放进托盘”→寻找目标时注意力较分散，保留更多 token→目标明确后注意力集中，减少送入后续层的 token→输出动作；每次新观察重新评分。

## 创新点或方法

旧做法固定预算；本文先用任务文本对视觉 token 的注意力评分，再看分数分布有多集中。逆 Simpson 指标估计有效 token 数，结合近期滑动窗口校准本步预算，最后硬选高分 token。[S5](https://arxiv.org/html/2610.22146v1#S1.p4.1) [S16](https://arxiv.org/html/2610.22146v1#S3.SS1.p1.1) 核心变化是动态决定保留数量，任务注意力本身并非作者声称的新贡献。[S17](https://arxiv.org/html/2610.22146v1#S3.SS2.p1.1) 推理中不训练、不复用历史 token；窗口只用于预算校准。真机基础策略仍预先做过 LoRA 微调。[S24](https://arxiv.org/html/2610.22146v1#S4.SS2.p2.1)

### 方法如何工作

1. 从当前图像与任务提取任务对视觉的注意力，为每个 token 给重要性分数。
2. 计算分数分布的有效 token 数，估计本步依赖的是少数区域还是较广信息。
3. 相对近期窗口校准预算，集中时更积极裁剪，分散时保留更多内容。
4. 按分数保留预算内的 token，让后续大模型处理更短序列并生成动作；下一步用新观察重新选择。

### 必要术语

- 视觉 token：图像区域的特征单元；数量影响后续 Transformer 计算。
- 逆 Simpson 指标：归一化权重平方和的倒数；越均匀，有效数量越大，本文用来估计预算需求。
- 硬裁剪：直接移除部分 token；本文不用合并或缓存来保留被移除的信息。

## 证据

RTX 4090 上，LIBERO/OpenVLA-OFT 的 FLOPs 3.98→1.65T、动作延迟118.52→81.17毫秒，成功率97.0%→96.5%；LightVLA 在相同成功率下更快，但需要训练。[S19](https://arxiv.org/html/2610.22146v1#S4.p1.1) [S30](https://arxiv.org/html/2610.22146v1#S4.SS3.p1.1) 真机两任务每条件50次：抓取延迟121.13→96.90毫秒、成功率84%→80%；抓放120.01→97.77毫秒、68%→66%。加速明确，成功率并非完全不变。[S24](https://arxiv.org/html/2610.22146v1#S4.SS2.p2.1) [S28](https://arxiv.org/html/2610.22146v1#S4.T3.5.1) 接近相同平均 token 预算时，动态方案在四套 LIBERO 任务均优于固定方案，较直接支持动态分配的作用。[S29](https://arxiv.org/html/2610.22146v1#S4.T4.5)

## 局限

节选未列专门的作者局限讨论，但作者明确承认效率存在权衡，训练方法可以更快。[S30](https://arxiv.org/html/2610.22146v1#S4.SS3.p1.1) 我的待核查问题是注意力错过小物体时会否同时低估预算，以及窗口突遇新场景如何响应。真机成功率下降是否处于随机波动范围，所给结果不足以确定。另外，H/延迟表示动作吞吐，不能等同新视觉反馈频率。[S21](https://arxiv.org/html/2610.22146v1#S4.SS1.p2.1)

- **判断**：值得读到动态预算公式和等预算消融；它是实用的免训练加速选择，但选型要同时接受实际成功率和硬件延迟检验。

## 研究关联

可以借鉴的是把预算分配和重要性排序分开：即便已知道哪些信息更重要，也还要判断本步需要多少信息。对于信息需求随阶段变化的闭环任务，平均预算相同也可能因分配方式不同而产生性能差异。

### 下一步读哪里

优先核查[S5](https://arxiv.org/html/2610.22146v1#S1.p4.1) [S16](https://arxiv.org/html/2610.22146v1#S3.SS1.p1.1)对应的窗口初始化、预算上下限、裁剪层和位置处理，再看[S29](https://arxiv.org/html/2610.22146v1#S4.T4.5)的等预算对照。SIMPLER 的基础压缩参数按任务设置不同，[S25](https://arxiv.org/html/2610.22146v1#S4.T2)因此还要问部署新任务需多少调参；比较表中哪些是统一复测、哪些仅引用也应区分。[S20](https://arxiv.org/html/2610.22146v1#S4.SS1.p1.1)

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.22146v1
- 获取时间：2026-10-17T00:17:20.639958+00:00
- [S1] [FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models · 正文段落 1](https://arxiv.org/html/2610.22146v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.22146v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.22146v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.22146v1#S1.p3.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.22146v1#S1.p4.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.22146v1#S1.p5.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.22146v1#S1.I1.i1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.22146v1#S1.I1.i2)
- [S9] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.22146v1#S1.I1.i3)
- [S10] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.22146v1#S1.F1)
- [S11] [2.1 Vision-Language-Action Models for Robot Manipulation · 正文段落 11](https://arxiv.org/html/2610.22146v1#S2.SS1.p1.1)
- [S12] [2.2 Visual Token Compression for Efficient VLA Inference · 正文段落 12](https://arxiv.org/html/2610.22146v1#S2.SS2.p1.1)
- [S13] [2.2 Visual Token Compression for Efficient VLA Inference · 正文段落 13](https://arxiv.org/html/2610.22146v1#S2.SS2.p2.1)
- [S14] [2.2 Visual Token Compression for Efficient VLA Inference · 正文段落 14](https://arxiv.org/html/2610.22146v1#S2.SS2.p3.1)
- [S15] [3 Method · 正文段落 15](https://arxiv.org/html/2610.22146v1#S3.p1.1)
- [S16] [3.1 Preliminary: Visual Token Compression in VLA Models · 正文段落 16](https://arxiv.org/html/2610.22146v1#S3.SS1.p1.1)
- [S17] [3.2 Task-conditioned visual token importance · 正文段落 17](https://arxiv.org/html/2610.22146v1#S3.SS2.p1.1)
- [S18] [3.2 Task-conditioned visual token importance · 正文段落 18](https://arxiv.org/html/2610.22146v1#S3.SS2.p2.1)
- [S19] [4 Experiments · 正文段落 38](https://arxiv.org/html/2610.22146v1#S4.p1.1)
- [S20] [4.1 Experiment Setup · 正文段落 39](https://arxiv.org/html/2610.22146v1#S4.SS1.p1.1)
- [S21] [4.1 Experiment Setup · 正文段落 40](https://arxiv.org/html/2610.22146v1#S4.SS1.p2.1)
- [S22] [4.2 Evaluation Environments · 正文段落 41](https://arxiv.org/html/2610.22146v1#S4.SS2.p1.1)
- [S23] [4.2 Evaluation Environments · 正文段落 42](https://arxiv.org/html/2610.22146v1#S4.F5)
- [S24] [4.2 Evaluation Environments · 正文段落 43](https://arxiv.org/html/2610.22146v1#S4.SS2.p2.1)
- [S25] [4.2 Evaluation Environments · 正文段落 44](https://arxiv.org/html/2610.22146v1#S4.T2)
- [S26] [4.2 Evaluation Environments · 正文段落 45](https://arxiv.org/html/2610.22146v1#S4.T2.5.1)
- [S27] [4.2 Evaluation Environments · 正文段落 46](https://arxiv.org/html/2610.22146v1#S4.T3)
- [S28] [4.2 Evaluation Environments · 正文段落 47](https://arxiv.org/html/2610.22146v1#S4.T3.5.1)
- [S29] [4.2 Evaluation Environments · 正文段落 49](https://arxiv.org/html/2610.22146v1#S4.T4.5)
- [S30] [4.3 Experiment Results · 正文段落 50](https://arxiv.org/html/2610.22146v1#S4.SS3.p1.1)
- [S31] [4.3 Experiment Results · 正文段落 52](https://arxiv.org/html/2610.22146v1#S4.SS3.p3.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/FastVLA Task-Conditioned and Temporally Adaptive Visual Token Compression for Ef.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often multi-view images are encoded into hundreds of visual tokens that dominate transformer computation and latency. Token compression via attention is a natural solution but is challenging for VLA control because (1) decision-critical tokens are determined by the task, not generic visual saliency, and (2) the token budget varies substantially across steps, so static metrics and budgets waste computation or discard control-critical tokens. We introduce FastVLA, a training-free, task-aware, and temporally adaptive visual token compression framework. At each step, FastVLA scores token importance via task-to-vision attention and adaptively sets the compression rate from the importance-distribution uniformity, measured by an inverse-Simpson metric with online sliding-window calibration. We evaluate FastVLA on OpenVLA, OpenVLA-OFT, and CogACT across LIBERO and SIMPLER, and on a physical Franka Research 3 robot. In simulation, it reduces LLM-backbone FLOPs by 35-59\% and action latency by 9-32\% (a 1.09$\times$-1.46$\times$ speedup) while maintaining task success, achieving a comparable or better efficiency-performance trade-off than existing plug-and-play token compression/pruning/reuse baselines. On the real robot, it cuts end-to-end latency by 20\% (1.25$\times$ speedup) at comparable success. Code is available at https://github.com/jiuyixu25/FastVLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22146v1
- Authors: Jiuyi Xu, Chengyuan Qian, Zhengzhong Tu, Yang Sui, Yangming Shi
- Published: 2026-10-15T16:17:18Z
- Age days: 1

</details>
