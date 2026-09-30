---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26103v2"
published: "2026-08-26T17:59:34Z"
age_days: 3
score: 28
created: 2026-08-30
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization

> [!summary] 先说人话（基于摘要）
> Zero-WAM把人类示范视频当作机器人任务的上下文提示，让因果视频—动作模型无需更新参数就执行未见任务；IFP 训练目标迫使策略真正从视频提示读取任务。

## 问题

零样本跨任务操控难点是如何明确指定未见任务；语言缺少完整视觉演化，而真实配对的人类—机器人任务视频稀缺，模型还可能靠训练任务捷径忽略上下文。

## 创新点或方法

输入人类视频提示和当前机器人观测，输出未来动作块。自动流水线把按任务采样的机器人轨迹匹配为语义对应的人类视频，构成 HumanGen；in-context future chunk prediction 抑制已见任务捷径，训练因果 World-Action Model 跟随视频意图。

## 证据

HumanGen含 7.42 万个人机 ICL 对、覆盖 8600 个任务。RoboTwin 2.0 七个未见任务平均成功率 47.0%，比最强视频—动作基线绝对提升 29.5 点；真机定性覆盖多物体、长时程和精细插入的新配置。


## 局限

需核查自动匹配视频与机器人任务的语义泄漏，以及仅七个未见仿真任务能否支撑“开放式”泛化；真机结果没有数字。

- **判断**：值得精读数据生成和 IFP 目标；这是很有潜力的任务规范方式，但开放性主张仍需更广评测。

## 研究关联

对 VLA、世界模型和机器人学习者，它把上下文学习从语言扩展到更具过程信息的人类视频，为开放任务规范和跨任务泛化提供了可检验路线。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/Zero-WAM In-Context World-Action Modeling from Human Videos for Open-Ended Task.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Zero-shot cross-task generalization, where a policy must execute manipulation tasks never seen during training, remains a central challenge in robot learning. In large language models, a novel task can be performed simply by specifying it in the context, without any parameter update. This form of in-context learning (ICL) turns generalization into a problem of task specification. To achieve cross-task generalization, we bring this paradigm to robotic manipulation, and argue that the natural task specification for manipulation is a human video: unlike language, it provides rich visual cues about the intended task evolution. We present Zero-WAM, a causal video-action model that executes unseen tasks by following in-context human video guidance. To address the scarcity of task-rich paired human-robot data, we propose an automatic pipeline that converts task-sampled robot trajectories into semantically matched human videos, yielding HumanGen, a dataset of 74.2K human-robot ICL pairs across 8.6K tasks. For model training, we further introduce an in-context future chunk prediction (IFP) objective that suppresses shortcuts learned from seen tasks and forces the policy to draw task information from the video prompt. On seven unseen tasks in RoboTwin 2.0 simulation, Zero-WAM achieves a 47.0% average success rate, an absolute improvement of 29.5 percentage points over the strongest video-action baseline. In real-world evaluations, it follows human video guidance to generalize to unseen task configurations involving multi-object scenes, long-horizon manipulation, and fine-grained insertion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26103v2
- Authors: Jiaming Zhou, Qihang Zhang, Gangwei Xu, Cunxin Fan, Yujie Zhao, Ruilin Wang, Yiming Luo, Shuai Yang, Xing Zhu, Yujun Shen, Junwei Liang, Yinghao Xu
- Published: 2026-08-26T17:59:34Z
- Age days: 3

</details>
