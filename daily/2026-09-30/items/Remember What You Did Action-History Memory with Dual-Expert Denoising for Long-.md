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
url: "https://arxiv.org/abs/2609.37307v1"
published: "2026-09-29T11:43:19Z"
age_days: 0
score: 36
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> ActMem-VLA 给已有机器人模型加上动作记忆，解决“眼前画面差不多，但任务其实已经走到另一阶段”的混淆。记忆模块先决定下一步往哪个阶段推进，原模型再细化动作；LIBERO-Mem 的平均成功率从 65.2% 提到 80.8%，原模型无需重新训练。

## 问题

长任务中，相似画面和机器人状态可能对应不同进度，例如同样站在抽屉前，下一步可能是打开，也可能是关闭。缺少交互历史的 VLA 难以区分。已有方案可通过特征、动作先验或采样引导加入时间信息，但其中联合微调记忆与底座的方法增加策略训练成本。

### 用一个例子理解

理解用例（非论文实验）：输入“把物品放入抽屉后关好”和当前抽屉画面；记忆编码此前的打开与放置动作，PAE 据此生成关抽屉的动作方向，AE 细化手部运动；输出下一段控制动作。是否真的放置成功仍需当前观测判断。

## 创新点或方法

本文把历史引导与底座细化分开。Mamba 编码已执行动作历史，记忆与当前上下文一起输入轻量 PreAction Expert（PAE）；PAE 负责早期高噪声去噪，推动任务进度，再把半成品动作交给冻结的 Action Expert（AE）完成低噪声细化。训练时只联合优化 Mamba 和 PAE，已经微调好的底座始终冻结；推理时按上述顺序交接。直观上，先解决该往哪个阶段走，再处理动作细节；具体交接时刻与训练目标未说明。

### 方法如何工作

1. 把已执行动作序列编码成记忆，为当前画面补充任务进度线索。
2. 将记忆和当前上下文交给 PAE，在高噪声阶段形成符合进度的初步动作。
3. 把部分去噪动作交给冻结 AE，在低噪声阶段细化控制，复用底座能力。
4. 训练只更新记忆模块和 PAE，减少需要学习的参数；具体损失和计算节省摘要未说明。

### 必要术语

- 感知混淆：当前看起来相似，实际却处于不同任务阶段；本文要缓解的动作歧义。
- Mamba：一种适合处理序列的状态空间模型；本文用来编码已执行动作历史。
- 双专家交接：两个模块依次负责去噪的不同阶段；本文分别承担历史引导和动作细化。

## 证据

摘要报告 LIBERO-Mem 十项任务平均成功率为 80.8%，对照 π₀.₅ 为 65.2%、MemoryVLA 为 49.5%；新增参数为 3.45%。四项真机任务相对 π₀.₅ 的平均成功率提高 28.8%，但未说明该增幅是相对百分比还是百分点。未给方差、试验次数和训练耗时，因此参数少不能直接推出训练或推理开销同样小。

## 局限

作者未明确列出剩余局限。我会重点核查：动作历史能否识别抓取失败，当前视觉如何修正错误进度，以及交接设计是否优于其他同预算记忆方案。总体成功率提升不能单独证明双专家分工的因果作用；真机结果不能直接继承 LIBERO-Mem 的收益幅度。

- **判断**：已有策略能完成单步动作、却常在长任务中重复或跳步时，优先看这篇；重点查失败后怎样修正记忆。

## 研究关联

机器人长任务做错时，可以先查它是否忘了前面做过什么，再考虑扩大模型。这里还有一个关键检验：做过抓取动作不代表真的抓到了，记忆必须能被当前观测纠正，否则只是更坚定地沿着错误进度走。

### 下一步读哪里

下一步核查历史记录包含什么、Mamba 如何更新或重置、PAE 与 AE 在哪一步交接，以及去掉历史或改变交接位置后的结果；同时确认真机增幅定义和训练预算。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Remember What You Did Action-History Memory with Dual-Expert Denoising for Long-.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have driven rapid progress in robotic manipulation, demonstrating strong fine-grained control and promising performance on long-horizon tasks. However, many existing VLAs lack explicit access to interaction history, making them vulnerable to perceptual aliasing: similar current observations and robot states at different task stages may induce action ambiguity and lower success rate. Existing methods incorporate temporal or progress cues through feature conditioning, action-prior modification, or sampling guidance. However, methods that jointly fine-tune memory modules and the base VLA incur additional policy-training costs, motivating the separation of trainable history-conditioned steering from frozen base-policy refinement. We propose ActMem-VLA, a dual-expert handover architecture that augments a frozen, fine-tuned VLA with a memory plugin comprising a Mamba-based memory module and a lightweight PreAction Expert (PAE). Specifically, Mamba encodes executed-action history into memory that conditions PAE alongside current context. With these inputs, PAE steers task progression during early, high-noise denoising, then passes the partially denoised action to the frozen Action Expert (AE) to refine action details during the remaining low-noise steps. The fine-tuned base VLA remains frozen throughout training, while only the Mamba module and PAE are jointly optimized. On LIBERO-Mem, ActMem-VLA achieves 80.8\% average success across all ten tasks, compared with 65.2\% for $π_{0.5}$ and 49.5\% for MemoryVLA, while introducing only 3.45\% additional parameters. Across four real-world tasks, it improves the average success rate over $π_{0.5}$ by 28.8\%.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37307v1
- Authors: Yaxin Zhao, Dianye Huang, Chenwei Wang, Chenguang Yang, Zhongliang Jiang
- Published: 2026-09-29T11:43:19Z
- Age days: 0

</details>
