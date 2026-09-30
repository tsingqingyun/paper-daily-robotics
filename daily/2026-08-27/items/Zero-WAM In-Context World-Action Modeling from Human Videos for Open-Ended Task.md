---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26103v1"
published: "2026-08-26T17:59:34Z"
age_days: 0
score: 28
created: 2026-08-27
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization

> [!summary] 先说人话（基于摘要）
> Zero-WAM 把人类视频当作新任务的上下文规范，用因果视频—动作模型跟随演示执行未见任务；IFP目标迫使模型从视频提示读取任务，而非利用训练任务捷径。

## 问题

机器人零样本跨任务泛化仍困难，语言又无法完整表达操作的视觉演化；任务丰富且配对的人—机器人数据稀缺，模型还可能忽略上下文、记住已见任务。

## 创新点或方法

自动将按任务采样的机器人轨迹匹配为语义对应的人类视频，形成HumanGen；模型输入人类视频上下文和当前机器人状态，预测未来动作块。训练时用in-context future chunk prediction压制已见任务捷径。

## 证据

HumanGen含74.2K对人—机器人ICL样本、覆盖8.6K任务。在RoboTwin 2.0七个未见任务上平均成功率47.0%，比最强视频动作基线高29.5个百分点；真机可跟随视频处理多物体、长时程和精细插入的新配置，但未给数字。


## 局限

自动生成的“语义匹配”视频是否泄漏任务模板、与真实用户视频差距多大，是泛化结论的关键；真机证据也缺少定量结果。

- **判断**：值得精读数据生成和防捷径实验；仿真增益很强，但开放式人类视频泛化需由更自然的真机提示验证。

## 研究关联

它把人类视频从预训练素材提升为测试时任务接口，为开放词汇操作和无参数更新适配提供了更丰富的任务说明。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/Zero-WAM In-Context World-Action Modeling from Human Videos for Open-Ended Task.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Zero-shot cross-task generalization, where a policy must execute manipulation tasks never seen during training, remains a central challenge in robot learning. In large language models, a novel task can be performed simply by specifying it in the context, without any parameter update. This form of in-context learning (ICL) turns generalization into a problem of task specification. To achieve cross-task generalization, we bring this paradigm to robotic manipulation, and argue that the natural task specification for manipulation is a human video: unlike language, it provides rich visual cues about the intended task evolution. We present Zero-WAM, a causal video-action model that executes unseen tasks by following in-context human video guidance. To address the scarcity of task-rich paired human-robot data, we propose an automatic pipeline that converts task-sampled robot trajectories into semantically matched human videos, yielding HumanGen, a dataset of 74.2K human-robot ICL pairs across 8.6K tasks. For model training, we further introduce an in-context future chunk prediction (IFP) objective that suppresses shortcuts learned from seen tasks and forces the policy to draw task information from the video prompt. On seven unseen tasks in RoboTwin 2.0 simulation, Zero-WAM achieves a 47.0% average success rate, an absolute improvement of 29.5 percentage points over the strongest video-action baseline. In real-world evaluations, it follows human video guidance to generalize to unseen task configurations involving multi-object scenes, long-horizon manipulation, and fine-grained insertion.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26103v1
- Authors: Jiaming Zhou, Qihang Zhang, Gangwei Xu, Cunxin Fan, Yujie Zhao, Ruilin Wang, Yiming Luo, Shuai Yang, Xing Zhu, Yujun Shen, Junwei Liang, Yinghao Xu
- Published: 2026-08-26T17:59:34Z
- Age days: 0

</details>
