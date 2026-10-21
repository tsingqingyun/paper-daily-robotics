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
url: "https://arxiv.org/abs/2610.26545v1"
published: "2026-10-19T15:08:06Z"
age_days: 1
score: 32
created: 2026-10-21
concepts: ["视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ReInsVLN: Revisiting Historical Evidence for Training-Free Vision-and-Language Navigation

> [!summary] 这篇论文到底做了什么（基于摘要）
> ReInsVLN 让不再训练的导航模型既压缩历史画面，也按预定时机回看保留下来的观察。它针对两个不同问题：历史越积越冗余，以及模型明明保留了线索却没有用好。

## 问题

视觉语言导航要求机器人按指令行走，并利用过去看见的地标判断接下来怎么走。历史增长会带来重复信息、推理开销和记忆占用，但删减历史也可能丢掉关键线索；另一方面，线索留在上下文里并不保证模型会使用。本文因此同时处理历史如何保留、如何重新被利用。

### 用一个例子理解

理解用例（非论文实验）：输入“经过第二扇门后右转”和连续走廊画面；系统压掉重复视图、保留与门有关的线索，并在预定时机提醒回看历史；导航模型据此输出继续前进或转向的动作。该例没有声称论文验证过这条指令。

## 创新点或方法

ReInsVLN 面向冻结的导航模型，不更新权重。压缩部分先减少时间上的重复，再保护覆盖范围，并按指令选择视觉 token，构造紧凑历史；利用部分按预定计划加入历史回看提醒，促使模型重访已有观察，且不增加模型调用次数。这里的改变发生在推理输入和提醒安排上，训练与部署之间没有新增参数学习阶段。摘要未说明覆盖保护的计算方式、token 评分规则以及具体提醒日程。

### 方法如何工作

1. 用受控续跑诊断历史利用，检查已有上下文能否通过回看帮助失败任务，定位干预依据。
2. 削减重复历史并保护覆盖范围，再按指令选择 token，得到较紧凑且与任务相关的视觉上下文。
3. 按预定日程提醒冻结模型重访保留的观察，使已经保存的线索有机会进入当前决策。
4. 模型结合当前观察、压缩历史和指令输出导航动作；具体提醒文本和调度参数，摘要只说明到此。

### 必要术语

- 冻结模型：使用时不更新权重的模型；本文通过管理上下文改善其行为。
- 视觉 token：图像转成模型可处理的信息单元；本文选择和删减它们来压缩历史。
- Prefill：模型首次处理输入上下文的计算阶段；历史压缩可减少这部分开销。
- KV 缓存：保存注意力计算中间信息的内存；本文用其占用衡量压缩收益之一。

## 证据

诊断基准 ReInsBench 通过受控续跑测试发现，提醒重看历史能利用既有上下文挽回部分导航失败。在 R2R Val-Unseen 上，ReInsVLN 相对原生 StreamVLN 和 InternVLA-N1 的成功率分别提高 8.48、3.37 个百分点，达到 64.27%、64.44%。匹配观察工作量时，视觉压缩基本保留导航表现，prefill 延迟和 KV 缓存占用最多分别减少 21.77%、32.25%，均来自摘要；两个最大值不应假定同时出现。另有人形及四足机器人真机试验，但没有给出数量或成功率。

## 局限

诊断结果支持部分失败可以靠重看历史挽回，并不说明所有失败都源于遗忘。“不增加模型调用”也不等于提醒完全没有 token 或时间成本。我会核查受控续跑如何保证可比性、提醒频率的敏感性，以及压缩是否更容易漏掉稀有但关键的地标。

- **判断**：值得先读 ReInsBench 的诊断设计，再读压缩与提醒的独立消融；它既提供可用改法，也帮助判断导航失败究竟卡在记忆的哪一环。

## 研究关联

最可借鉴的诊断思路是：遇到长程任务失败，先检查已有线索是否被使用，再决定是否增加记忆。保留历史和引导回看是两种干预；这篇把它们分开处理，适合用于分析冻结模型的历史利用问题。

### 下一步读哪里

优先检查 ReInsBench 的续跑控制条件，以及压缩、提醒各自带来多少收益。再核查覆盖保护和指令选 token 的规则、完整端到端延迟，以及真机顺序指令与序数导航的试验规模。

- **概念**：视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-21/ReInsVLN Revisiting Historical Evidence for Training-Free Vision-and-Language Na.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-and-language navigation (VLN) relies on retaining and using relevant observations. Yet growing histories introduce redundancy, and retained information may remain underused. We introduce ReInsBench, a diagnostic benchmark that examines history utilization through controlled continuation trials. Its results show that history-review reinstruction can recover navigation failures using the existing task context. Motivated by this finding, we propose ReInsVLN, a training-free framework supporting memory construction and utilization in frozen navigators. Coverage- and Instruction-Aware Compression constructs compact visual context through temporal redundancy reduction, coverage-aware protection, and instruction-guided token selection. Forgetting-Inspired History Reminders guide navigators to revisit retained observations according to a predefined schedule, without additional model calls. On R2R Val-Unseen, ReInsVLN improves success rates by 8.48 and 3.37 percentage points over the native StreamVLN and InternVLA-N1, reaching 64.27% and 64.44%, respectively. Visual compression largely preserves navigation performance while reducing prefill latency and KV cache memory by up to 21.77% and 32.25%, respectively, on matched observation workloads. Real-world trials on humanoid and quadruped robots further support the applicability of ReInsVLN to sequential instruction following and ordinal navigation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.26545v1
- Authors: Siwei Cheng, Hao Wu, Zitong Qi, Xinming Zhang, Haoyu Xi, Peiran Yin, Haozhe Hu, Xudong Wang, Xiaoyu Shen, Wei Zhang
- Published: 2026-10-19T15:08:06Z
- Age days: 1

</details>
