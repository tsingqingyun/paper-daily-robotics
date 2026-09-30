---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26103"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 28
created: 2026-08-29
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization

> [!summary] 先说人话（基于摘要）
> Zero-WAM把人类示范视频当作机器人新任务的上下文提示，无需更新参数就执行未见任务。其IFP训练目标迫使因果视频—动作模型从视频提示取任务信息，而非靠训练任务捷径。

## 这篇到底在做什么

- **卡在哪里**：机器人策略难以零样本泛化到训练外任务；语言往往缺少操作过程的视觉细节，而任务丰富、配对的人类—机器人数据又稀缺。模型还可能忽略提示，仅凭见过的任务模式预测动作。
- **关键解法**：输入当前机器人观测与人类任务视频，输出后续动作并建模未来。自动管线把按任务采样的机器人轨迹匹配为语义一致的人类视频，形成HumanGen；in-context future chunk prediction通过预测未来片段压制见过任务的捷径。
- **拿什么证明**：HumanGen含7.42万对人机ICL样本、覆盖8600个任务。在RoboTwin 2.0七个未见任务上平均成功率47.0%，比最强视频—动作基线绝对提高29.5个百分点；真实实验展示了多物体、长时程与精细插入泛化。

## 值不值得读

- **和你的研究有什么关系**：这是VLA与机器人学习中很实用的任务指定范式：视频提示比语言更能表达状态演化，并把跨任务泛化改写成上下文学习问题。对Agent和世界—动作联合建模也有直接参考。
- **先别急着信**：需核查自动匹配的人类视频与机器人轨迹是否泄露任务结构，以及七个仿真任务和真实演示能否代表开放式泛化。
- **判断**：今天最值得精读的机器人论文之一；数字明确、问题重要，优先看HumanGen生成、IFP消融和真实任务协议。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/Zero-WAM In-Context World-Action Modeling from Human Videos for Open-Ended Task.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.26103v2 Announce Type: replace-cross Abstract: Zero-shot cross-task generalization, where a policy must execute manipulation tasks never seen during training, remains a central challenge in robot learning. In large language models, a novel task can be performed simply by specifying it in the context, without any parameter update. This form of in-context learning (ICL) turns generalization into a problem of task specification. To achieve cross-task generalization, we bring this paradigm to robotic manipulation, and argue that the natural task specification for manipulation is a human video: unlike language, it provides rich visual cues about the intended task evolution. We present Zero-WAM, a causal video-action model that executes unseen tasks by following in-context human video guidance. To address the scarcity of task-rich paired human-robot data, we propose an automatic pipeline that converts task-sampled robot trajectories into semantically matched human videos, yielding HumanGen, a dataset of 74.2K human-robot ICL pairs across 8.6K tasks. For model training, we further introduce an in-context future chunk prediction (IFP) objective that suppresses shortcuts learned from seen tasks and forces the policy to draw task information from the video prompt. On seven unseen tasks in RoboTwin 2.0 simulation, Zero-WAM achieves a 47.0% average success rate, an absolute improvement of 29.5 percentage points over the strongest video-action baseline. In real-world evaluations, it follows human video guidance to generalize to unseen task configurations involving multi-object scenes, long-horizon manipulation, and fine-grained insertion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26103
- Authors: Jiaming Zhou, Qihang Zhang, Gangwei Xu, Cunxin Fan, Yujie Zhao, Ruilin Wang, Yiming Luo, Shuai Yang, Xing Zhu, Yujun Shen, Junwei Liang, Yinghao Xu
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
