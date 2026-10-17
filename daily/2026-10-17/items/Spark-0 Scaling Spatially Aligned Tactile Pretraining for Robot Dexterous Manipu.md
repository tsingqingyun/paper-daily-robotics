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
url: "https://arxiv.org/abs/2610.22342v1"
published: "2026-10-15T17:56:17Z"
age_days: 1
score: 37
created: 2026-10-17
concepts: ["世界模型", "具身智能评测与基准"]
---

# Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要）
> Spark-0 用触觉教视觉识别接触，也让动作模块直接读取触觉。这样训练出的同一模型，既能只靠摄像头执行，也能在有触觉传感器时利用实时接触信息。

## 问题

灵巧操作需要判断接触力、物体软硬和刚开始的滑动，这些信息往往难从图像看出。大规模视觉预训练虽能提供物体与场景知识，却不足以解决接触控制；这里要解决的是如何把大量人类触觉记录变成机器人可用的监督。

### 用一个例子理解

理解用例（非论文实验）：输入“拿起纸杯”和相机画面；视觉表示利用训练中学到的接触线索生成抓取动作；若另有触觉输入，动作模块还能读取力的变化，再输出后续动作。

## 创新点或方法

旧做法主要从图像学习，本文增加两条触觉用途。训练时，把手套测得的接触转换到图像位置，监督视觉 token，并用冻结的三维几何教师提供特征监督，让视觉表示学习接触位置和空间结构。这些监督目标推理时移除。另一条触觉通路把区域力的历史和三维触觉单元状态编码后交给动作专家，供有触觉的部署使用。两类监督的具体损失与混合方式，摘要未说明。

### 方法如何工作

1. 采集全手触觉与操作记录，把接触信息对应到图像位置，使视觉学习有空间明确的目标。
2. 结合接触图与冻结几何教师监督视觉 token，让图像表示吸收接触和结构线索。
3. 另行编码力历史和三维触觉状态，为动作专家提供实时接触条件。
4. 部署时移除训练监督目标，按传感器条件选择纯视觉或触觉条件输入，输出动作。

### 必要术语

- 接触图：标出图像中接触位置的监督信号；本文用它教视觉表示关注接触。
- Taxel：触觉传感器的感知单元；其三维状态进入触觉通路。
- 冻结教师：参数不更新的参考模型；本文用它提供三维几何特征监督。

## 证据

摘要报告：HumanTouch 含 1,000 小时全手触觉操作。相同数据、算力下，相比丢弃触觉的视觉预训练，保留触觉使 Ego Humanoid 的纯视觉成功率从 52.5% 到 71.7%；SparkArena-Real 在部署也使用触觉时，从 44.0% 到 52.0%。前者直接支持训练触觉能帮助视觉执行；后者同时涉及训练和部署触觉，不能单独归因于其中一项。摘要另报两个 SparkArena 赛道平均成功率最高、Ego Humanoid 八项汇总指标第一，但未给具体对手与误差。

## 局限

纯视觉结果不意味着图像能恢复所有瞬时接触力。我的待核查问题是：接触对齐误差有多大，几何监督与触觉监督各贡献多少，以及真机收益对物体和接触条件的覆盖范围。

- **判断**：值得细读监督构造与消融，因为它提供了触觉帮助纯视觉部署的直接对照证据。

## 研究关联

可借鉴之处是：某种传感器不必始终随机器人部署，也能作为训练教师。条件是能把它测到的信息准确对应到视觉位置；这种对应关系比简单把两种输入拼起来更值得检查。

### 下一步读哪里

下一步核查接触图如何投影到图像、三维教师监督什么，以及是否分别移除两类监督和部署触觉。尤其要看真机对照是否能分开训练收益与在线触觉收益。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/Spark-0 Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipu.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, image-space contact maps derived from tactile gloves, together with features from a frozen 3D geometry teacher, supervise the visual tokens; these objectives are removed at inference. In parallel, a tactile pathway encodes regional force histories and 3D taxel states to condition the action expert. A single checkpoint therefore supports both vision-only and tactile-conditioned deployment. To scale this supervision, we build HumanTouch, a 1,000-hour dataset of full-hand tactile human manipulation, and pretrain Spark-0 on it together with egocentric video, robot data, and simulation. We also release SparkArena, which pairs vision-only simulated tasks with tactile-conditioned real-robot tasks on one dexterous embodiment. Spark-0 achieves the highest mean success rate on both SparkArena tracks and ranks first on all eight aggregate metrics of the Ego Humanoid Manipulation Benchmark. Compared with vision-only pretraining on the same data and compute with touch discarded, retaining the touch of 1,000 hours of HumanTouch raises vision-only success on Ego Humanoid from 52.5% to 71.7%, and success on SparkArena-Real, where touch is also used at deployment, from 44.0% to 52.0%, indicating that touch serves not only as a policy input but also as scalable supervision for dexterous visuomotor pretraining. The Website is available at: https://xsparkai.com/Spark-0.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22342v1
- Authors: Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang, Tian Nian, Zijian Cai, Kehe Ye, Chenze Yu, Wenxuan Zhu, Eric J. Chen, Yan Qin, Yue Chen, Tongyu Wu, Junhao Gong, Kai-Chong Lei, Jiahao Zhang, Kailun Su, Qiwei Liang, Renjing Xu, Ping Luo, Wenbo Ding
- Published: 2026-10-15T17:56:17Z
- Age days: 1

</details>
