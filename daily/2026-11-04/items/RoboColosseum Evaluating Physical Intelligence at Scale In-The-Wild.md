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
url: "https://arxiv.org/abs/2611.02497"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 34
created: 2026-11-04
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild

> [!summary] 这篇论文到底做了什么（基于摘要）
> RoboColosseum 把各地真实机器人接入统一评测流程，在当地相同条件下成对比较策略。它同时测直接使用和等量示范微调，发现一个榜单上的领先者未必换台机器人或微调后仍领先。

## 问题

任务是评估通用机器人策略跨机器人、任务和环境的表现。真实场景越多样，测试越接近实际使用，却越难复现和公平比较；只看任务成功还会把“差一点完成”和“几乎没动”混为一谈。

### 用一个例子理解

理解用例（非论文实验）：同一站点用同一机械臂分别运行两个策略完成收纳任务，按协议匹配当地条件并记录成功和进度；多站点结果汇总后比较策略，再另测两者接受等量示范后的表现。

## 创新点或方法

相较在单一场地测一个成功率，本文统一策略服务与操作协议，由各地人员运行机器人。开放赛道在匹配的当地条件下做盲测成对比较，不做任务专门适配；微调赛道则给每种 VLA 每任务相同的 100 条示范，测适配效果。推理评测记录完成情况和部分进度，再积累比较结果形成排名；主动匹配用于减少获得稳定排名所需的物理试验。

### 方法如何工作

1. 通过统一服务接口运行不同策略，减少接入方式对比较的影响。
2. 在当地匹配条件下做盲测成对试验，得到更可比的策略表现。
3. 另给 VLA 等量示范进行微调，区分直接使用能力和适配能力。
4. 同时记录成功与部分进度，再用累计比较和主动匹配估计排名，减少只看二元结果的信息损失。

### 必要术语

- 具身形态：机器人的身体与执行机构配置；本文比较四类机器人。
- 成对比较：在匹配条件下比较两个策略；用于组织开放赛道试验。
- Kendall W：衡量多组排名一致程度的统计量；本文的 0.24 表示跨任务集排名一致性较弱。
- 主动匹配：有选择地安排下一轮比较对象；本文用它节省排名所需试验。

## 证据

摘要给出初始研究覆盖五种 VLA、三种前沿智能体和四类机器人。开放赛道在 124 个站点进行了 5,699 次成对比较，智能体可与专门 VLA 抗衡，但整体可靠完成仍困难。微调后 GR00T N1.7 在 SO-101 领先，π0.5 在 Franka 和 Bimanual-YAM 领先；跨机器人任务集排名一致性弱，Kendall W 为 0.24。两个赛道共有的三类机器人都出现明显排名反转。G1 五项任务无策略成功，但平均进度为 13.3%—23.2%。这些是真实分布式试验证据，未给全部置信区间和逐项结果。

## 局限

跨机器人排名变化同时伴随任务集变化，不能单独归因于机器人形态。我的待核查问题是各站点执行一致性、盲测具体方式、进度评分定义，以及主动匹配是否让少数策略获得不足的比较机会。

- **判断**：值得深入读评测协议和分组结果，因为它能帮助判断榜单结论适用到哪里，而不是只提供另一个总排名。

## 研究关联

选择策略时，应先明确要直接部署还是允许示范适配，再看对应机器人和任务的结果。本文尤其提醒：零样本排名不能替代微调能力评估，而失败任务中的进度也能暴露成功率掩盖的差异。

### 下一步读哪里

优先核查当地条件如何匹配、任务如何分配、进度如何打分，以及排名的不确定性；再看微调训练预算是否除示范数量外也可比。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/RoboColosseum Evaluating Physical Intelligence at Scale In-The-Wild.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2611.02497v1 Announce Type: new Abstract: General-purpose robot policies must work across robots, tasks, and environments, yet the variation that makes physical trials informative also makes them difficult to reproduce. We introduce RoboColosseum, a distributed evaluation framework that combines unified policy serving and standardized protocols across a network of locally operated robots in diverse environments. Our initial study evaluates five vision-language-action (VLA) policies and three frontier AI agents across four embodiments (SO-101, Franka, Bimanual-YAM, and G1 Humanoid). The Open Track compares models without task-specific adaptation in blinded, pairwise trials under matched local conditions. The Fine-tune Track measures how well VLA policies adapt to 20 tasks across all four embodiments when each policy receives the same 100 demonstrations per task. Across 5,699 pairwise Open Track comparisons at 124 sites, frontier agents rival specialized VLA policies, while all systems struggle to complete open-world tasks reliably. After fine-tuning, GR00T N1.7 leads on SO-101 and pi0.5 leads on Franka and Bimanual-YAM. Policy rankings show weak agreement across embodiment-specific task suites (Kendall W = 0.24). Open Track rankings poorly predict relative performance after fine-tuning, with substantial rank reversals on all three embodiments shared between tracks. Measuring partial progress reveals differences that task success alone misses. On the G1 Humanoid, no policy completes any of the five tasks, yet average progress ranges from 13.3% to 23.2% across policies. Open Track rankings stabilize as trials accumulate, and active matchmaking achieves comparable ranking agreement with substantially fewer physical trials than uniform sampling. These results show how distributed physical evaluation can reveal where robot policies generalize, how well they adapt to new tasks, and how far they progress on tasks they fail to complete.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.02497
- Authors: Tan Sang Nguyen, Yi Ru Wang, Shailesh Shailesh, Gang Yang, Jiamo Hu, Jianuo Jiang, Haoquan Fang, Zhongzheng Ren, Zhongyi Luo, Ian Chong, Aaron Tung, Santiago Pravisani, Minghui Lin, Yao Mo, Ishneet Singh, Benjamin Tee, Harold Soh, Siddhartha Srinivasa, Dieter Fox, David Hsu, Haoming Song, Maxime Ellerbach, Thomas Wolf, Pepijn Kooijmans, Ruijie He, Michael Cho, Jiafei Duan
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
