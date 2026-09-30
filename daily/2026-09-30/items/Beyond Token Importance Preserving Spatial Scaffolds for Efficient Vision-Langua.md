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
url: "https://arxiv.org/abs/2609.36967v1"
published: "2026-09-29T08:03:21Z"
age_days: 0
score: 32
created: 2026-09-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference

> [!summary] 这篇论文到底做了什么（基于摘要）
> 让机器人少看一些图像信息能加速，但如果只留“看起来重要”的部分，可能把旁边关键位置整个漏掉。GeoScaffold 先给画面各区域分配保留名额，再把区域内的点选得分散一些，用更少的信息维持对空间的覆盖。

## 问题

任务是在压缩视觉输入后仍可靠地完成操作。已有剪枝主要按单个 token 的语义重要性保留信息，可能把名额集中在少数位置，留下控制需要却没有被观察到的区域。摘要中的 Stride 基线说明，简单均匀抽样有时有效，但预算稍变也可能突然失效。

### 用一个例子理解

理解用例（非论文实验）：输入“把积木放进右侧盒子”和相机图像→给积木与盒子区域更多名额，同时保留桌面其他区域的覆盖点→VLA 用剪枝后的输入输出动作，避免只看积木而丢失目标位置。

## 创新点或方法

旧做法逐个按语义挑 token；GeoScaffold 改成先划分空间区域，再按任务相关性分配区域预算，最后用最远点采样选择区域内的覆盖点。这样既让重要区域得到更多 token，又减少局部最大盲区。它无需训练，属于推理阶段的视觉剪枝；摘要未说明相关性权重的来源、区域粒度及在模型哪一层实施。

### 方法如何工作

1. 将图像划成空间区域，让 token 的选择受到位置结构约束，而不只依赖全局重要性排序。
2. 按任务相关性为区域分配预算，使有限名额更多流向任务需要的位置。
3. 区域内用最远点采样选择彼此分散的 token，降低保留集合留下的局部盲区。
4. 将保留 token 送入 VLA 后续推理，减少计算；是否保持控制质量仍需通过任务成功率验证。

### 必要术语

- 视觉 token：图像经编码后的信息单元；本文通过减少它们降低推理负担。
- 空间覆盖半径：保留点留下的最大空间盲区尺度；本文用它分析剪枝失效。
- 最远点采样：逐步选择离已选点较远的位置；本文用它分散区域内的保留点。
- Prefill：模型处理输入上下文的计算阶段；摘要的加速数字仅明确针对这一阶段。

## 证据

摘要在 pi 0.5 与 LIBERO 设置下报告：仅保留 20% 视觉 token，平均成功率为 93.2%，prefill 相对未剪枝基线加速 1.78 倍。93.2% 是成功率，不是原性能保留比例；未提供未剪枝成功率，无法计算性能损失。Stride 在部分比例下优于语义及随机剪枝，但对应数值未列出。空间结构与成功率的强相关支持覆盖诊断，尚不单独证明覆盖半径决定成败。

## 局限

作者明确说明：摘要没有专门列出；明确报告的预算敏感性属于 Stride，不能直接归为 GeoScaffold 的缺陷。我的待核查问题：小物体、遮挡和多相机输入下是否稳定。LIBERO 是仿真证据，摘要未提供真机结果；prefill 加速也不等于机器人整条控制链路同比加速。

- **判断**：想给 VLA 加速，这篇值得读，方法无需重训。摘要给出保留 20% 视觉 token 时 93.2% 的成功率，但没有未剪枝的成功率；1.78 倍加速也只针对输入处理阶段。

## 研究关联

做视觉输入压缩时，可以在重要性分数之外加一条约束：别让画面留下太大的空白区。一个直接可做的对照是，在相同保留数量下比较“只挑高分位置”和“兼顾位置覆盖”，再检查失败是否集中在被漏看的小物体或目标区域。

### 下一步读哪里

下一步核查覆盖半径的坐标定义、区域预算是否允许为零、最远点采样的开销，以及不同预算下的波动；速度实验还需查看硬件、计时边界和端到端延迟。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Beyond Token Importance Preserving Spatial Scaffolds for Efficient Vision-Langua.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Existing VLA pruning strategies primarily select individual visual tokens according to task-level semantic relevance, while overlooking the spatial information required for robotic manipulation. To examine this limitation, we construct a simple Stride baseline that uniformly samples tokens along the flattened one-dimensional visual sequence, representing a purely geometric pruning strategy. Surprisingly, Stride outperforms semantic pruning and random pruning at certain pruning ratios, but collapses when the token budget is only slightly reduced. We characterize this phenomenon through the spatial coverage radius, defined as the largest spatial blind spot induced by the retained token set after pruning. Our analysis reveals a strong correlation between the spatial structure of retained tokens and task success, suggesting that reliable VLA pruning requires preserving not only task-relevant tokens but also the spatial scaffold of the scene. Motivated by this diagnosis, we propose GeoScaffold, a training-free visual token pruning method that partitions each image into spatial regions, allocates inter-region token budgets using task-relevance weights, and selects intra-region scaffold tokens via farthest point sampling to reduce the local coverage radius. On pi 0.5 and LIBERO, GeoScaffold retains only 20% of visual tokens while preserving a 93.2% average success rate, and achieves a 1.78 times prefill speedup over the unpruned baseline.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.36967v1
- Authors: Jiayu Chen, Shuyong Gao, Jingkai Jia, Xiaosheng Bu, Jiyuan Fu, Lingyi Hong, Kaixun Jiang, Yipan Xu, Wenqiang Zhang
- Published: 2026-09-29T08:03:21Z
- Age days: 0

</details>
