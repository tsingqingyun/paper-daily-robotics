---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02046"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 26
created: 2026-09-04
concepts: ["世界模型", "具身智能评测与基准"]
---

# Modeling What Changes: Sparse, Residual World Models for Object-Centric Manipulation

> [!summary] 先说人话（基于摘要）
> 论文主张世界模型只预测真正变化的对象：先用逐对象门控判断谁会变，再由残差头只更新这些对象。相比整体重预测，它更小、更准、更省数据，也更不容易在长滚动中让静态物体漂移。

## 问题

单体世界模型每步重建整个下一状态，把容量浪费在静态场景上，还会给本来不动的对象注入误差；即使单步预测不错，规划器访问到的分布也可能使模型控制失败。

## 创新点或方法

输入对象中心状态和动作，变化门控为每个对象判断是否更新，残差头只预测被标记对象的状态增量，输出组合后的下一状态。模型还针对规划器实际访问的状态进行特征化与训练，区别于密集MLP全量预测和只做离线预测训练。

## 证据

在3至8物体MuJoCo推物基准上，8物体时姿态预测准确度提高2.5至4.6倍，参数少8.6至11.1倍；变化检测F1为0.80至0.87，跨物体数零训练迁移保留99.4%的F1，用四分之一数据达到约90%完整数据精度。规划中稀疏模型成功率为0.23±0.06（三个随机种子），密集模型各种子均为0；真实模拟器oracle使用同一规划器可解任务。


## 局限

目前证据来自MuJoCo桌面推物，且最佳规划成功率仍只有0.23±0.06；方法在视觉输入、复杂接触和真实机器人上的有效性尚无摘要证据。

- **判断**：值得精读，尤其是滚动误差和规划分布实验；它的负结果与低绝对成功率同样重要，说明结构偏置有效但远未解决模型规划。

## 研究关联

对对象中心世界模型和机器人规划研究者，它给出强而可解释的归纳偏置，也明确揭示离线预测准确并不足以保证规划成功，训练分布必须覆盖规划器访问状态。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：26
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/Modeling What Changes Sparse, Residual World Models for Object-Centric Manipulat.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.02046v1 Announce Type: new Abstract: Monolithic world models predict the entire next state at every step, spending capacity re-predicting the static majority of a scene and injecting error into it. We ask whether explicitly modeling change (a per-object change gate plus a residual delta head that perturbs only the objects the gate flags) is a more effective and interpretable bias for physical prediction and control. On a MuJoCo tabletop pushing benchmark scaling from 3 to 8 objects, the sparse/residual model predicts next-state poses 2.5 to 4.6 times more accurately than a dense multilayer perceptron at 8.6 to 11.1 times fewer parameters, sustains change-detection F1 of 0.80 to 0.87 where the dense baseline is degenerate, transfers across object counts with zero retraining (99.4 percent F1 retention), and reaches about 90 percent of its full-data accuracy with a quarter of the data. In autoregressive rollout it compounds far less error, hugging the no-motion floor while the dense model drifts. Finally, inside a sampling-based planner, prediction-only models fail (though a true-simulator oracle solves the task with the identical planner, confirming the planner is sound), but once featurized and trained for the states a planner visits, the sparse model begins to plan (0.23 plus or minus 0.06 success over three seeds) while the dense monolith stays at zero at every seed. Modeling what changes, rather than re-predicting the whole world, is a simple, effective bias for object-centric physical AI; code, data generators, and all checkpoints will be released upon publication.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02046
- Authors: Param Thakkar, Parsika Paresh Shah, Manisha Sushant Gote
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
