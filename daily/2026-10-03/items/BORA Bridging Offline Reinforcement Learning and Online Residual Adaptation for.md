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
url: "https://arxiv.org/abs/2605.30226"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 42
created: 2026-10-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> BORA 让灵巧手 VLA 用少量真机试错和人的纠正继续学习，同时冻结原有大模型，只训练一个小的动作修正器。它还用局部策略把人的粗略意图转成协调的手指动作，让纠正数据真正能执行。

## 问题

任务是涉及多关节、复杂接触的单臂和双臂灵巧操作。已有 VLA 能提供不错的初始行为，但接触失败后，人很难直接给出所有手指应如何调整的精细动作；真机交互又昂贵。瓶颈因此既在纠正数据的可执行性，也在如何用少量新数据有效改进策略。

### 用一个例子理解

理解用例（非论文实验）：机器人双手拧盖时打滑；人通过可穿戴设备示意重新抓紧并继续转动，局部策略将意图细化成手指动作；纠正轨迹进入训练，残差 actor 学会在类似状态下调整基础策略的输出。摘要未确认这一具体拧盖场景。

## 创新点或方法

BORA 把离线强化学习与在线修正连接起来：先在一致性策略 VLA 中加入根据动作评估结果的 critic，再把学到的 critic 用于冻结基础策略后的残差适应。人的纠正通过可穿戴臂—手遥操作输入，并由示范引导的局部策略细化成协调的手指运动。在线轨迹、人工纠正和离线数据混合训练，只更新轻量残差 actor。推理时由基础行为和学到的修正共同产生动作；两者怎样组合、critic 是否参与部署，摘要未说明。

### 方法如何工作

1. 利用离线数据训练带动作条件 critic 的策略，获得初始行为及评价动作的依据。
2. 把人的粗略纠正交给示范引导的局部策略，生成机器人能执行的精细接触动作。
3. 收集在线执行和纠正轨迹，与离线数据混合，给适应过程补充真实失败附近的信息。
4. 冻结基础模型，只更新轻量残差 actor，并复用 critic，让新经验转成动作修正。

### 必要术语

- Critic：评估某状态下某动作预期结果的模型；BORA 在离线学习后继续使用它辅助适应。
- 残差 actor：输出基础动作修正量的小策略；本文主要更新它。
- 一致性策略：一种生成动作的策略形式；本文以它作为基础 VLA，摘要未展开机制。
- 示范引导的局部策略：参考示范把粗略意图细化为动作的策略；本文用它提高纠正的可执行性。

## 证据

摘要报告六项真机任务，覆盖单臂、双臂平台及两种灵巧手。每项只使用 20 条在线轨迹，标准物体平均成功率从 60.8% 到 82.5%，留出物体从 52% 到 70%。这些数字支持该设置下的少量在线适应，但摘要未明确前后比较配置、测试次数和误差。双臂扭转中的策略辅助也提高了干预可靠性，未给具体数值；它不等同于最终任务成功率。

## 局限

20 条是在线轨迹数，不是全部训练数据量，也不能据此认定收集和人工介入成本都很低。我的待核查问题是离线数据规模、每条轨迹的纠正强度，以及成功率增益分别来自辅助纠正、critic 还是残差更新。真机结果有说服力，但范围仍是所测六项任务和硬件。

- **判断**：值得读到数据收集流程和组件消融，因为它的实用性取决于纠正是否容易获得，以及小修正器到底承担了多少改进。

## 研究关联

这里值得借鉴的是把“人知道该怎么纠正”与“人能直接控制每个关节”分开处理。当纠正意图明确但动作难以执行时，可以先用局部策略生成可用纠正，再用小模型学习修正已有技能。

### 下一步读哪里

核查 critic 的训练目标、残差动作的组合方式、混合数据比例和离线数据成本；再看有无分别移除局部辅助策略、critic 复用与残差学习的比较。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/BORA Bridging Offline Reinforcement Learning and Online Residual Adaptation for.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2605.30226v3 Announce Type: replace Abstract: Vision-Language-Action (VLA) policies provide strong behavioral priors for dexterous manipulation, yet adapting them on real robots remains challenging because high-DoF contact failures are difficult for humans to correct and online interaction is expensive. We present BORA, an offline-to-online reinforcement learning system that integrates an action-conditioned critic into a consistency-policy VLA and reuses the learned critic for frozen-base residual adaptation. To obtain executable corrective data, BORA combines wearable arm--hand teleoperation with a demonstration-guided local policy that translates coarse human intent into coordinated, embodiment-specific finger motions for contact-rich skills. Online robot rollouts and human corrections are mixed with offline data to update only a lightweight residual actor, avoiding full-model fine-tuning. We evaluate BORA on six real-world tasks using single-arm and bimanual platforms equipped with two dexterous-hand models. With only 20 online trajectories per task, BORA improves average success from 60.8% to 82.5% on standard objects and from 52% to 70% on held-out objects, while policy assistance substantially improves intervention reliability in bimanual twisting. These results demonstrate a practical route from executable human correction to efficient real-robot VLA adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.30226
- Authors: Zhongxi Chen, Yifan Han, Bin Qiu, Zhangliang Gao, Yanming Shao, Huanming Liu, Congsheng Xu, Xiaoyu Chen, Xingyu Ye, Yao Mu, Wenzhao Lian
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
