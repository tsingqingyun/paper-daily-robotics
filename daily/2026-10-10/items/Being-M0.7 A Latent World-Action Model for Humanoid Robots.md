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
url: "https://arxiv.org/abs/2610.11283v1"
published: "2026-10-08T05:49:24Z"
age_days: 1
score: 32
created: 2026-10-10
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Being-M0.7: A Latent World-Action Model for Humanoid Robots

> [!summary] 这篇论文到底做了什么（基于摘要）
> Being-M0.7先从人类视频和运动数据学习“接下来场景和身体会怎样变化”，再把这份知识适配给人形机器人。最后由动作专家结合预测信息、当前图像和自身状态，输出机器人可执行的全身命令。

## 问题

人形机器人边移动边操作，需要同时考虑未来场景与全身运动，但机器人示范稀缺。人类数据虽然多，却常常只有视频或只有运动记录，而且人类运动本身不是机器人能直接执行的动作，不能简单拿来训练控制输出。

### 用一个例子理解

理解用例（非论文实验）：输入是机器人走近桌面的图像和关节状态；适配后的先验提供未来场景与身体运动相关表示，动作专家结合当前位置选择全身命令；输出让机器人继续靠近并准备伸手取物。

## 创新点或方法

与直接依赖机器人示范学习控制相比，本文先用混合模态人类数据学习视觉变化和身体运动结构，再经过机器人中期训练适配视角与身体动力学。联合预测未来视觉潜在状态和运动，目的是让视觉表示携带未来身体运动信息。动作后期训练时冻结适配后的先验，由动作专家通过门控交叉注意力融合预测表示、当前图像和本体感觉。推理时这套信息用于输出全身动作；摘要没有说明是否逐步生成显式未来序列，也未交代预测时域。

### 方法如何工作

1. 汇集视频、运动及配对数据，学习互补信息，以缓解机器人示范稀缺。
2. 联合预测未来视觉表示和运动，让场景表示包含后续身体变化；缺失模态处理方式摘要未说明。
3. 用机器人数据适配先验，使人类数据学来的信息对应机器人视角和身体。
4. 冻结该先验并训练动作专家，将预测信息与当前观测结合，得到可执行全身命令。

### 必要术语

- 潜在状态：压缩后的内部表示；本文在这种表示中预测未来视觉变化。
- 本体感觉：机器人自身关节等状态信息；帮助动作专家把视觉知识对应到当前身体。
- 门控交叉注意力：有选择地融合不同来源的信息；本文用于接入预测表示，具体门控方式未说明。

## 证据

摘要称数据语料来自超过10,000小时的原始人类中心数据，这是数据来源规模，不能等同于最终训练样本时长。SIMPLE上综合成功率在所比较基线中最高；真实Unitree G1移动操作任务上与最强基线持平。未提供成功率数值、任务清单、基线身份或波动范围，因此只能确认作者报告的相对排序，不能量化优势大小。

## 局限

摘要明确指出人类运动不能直接指定机器人动作，这正是动作训练必须解决的落差。我会核查只有视频或只有运动的样本如何参与联合学习，以及性能是否确实来自未来预测；目前的综合排名不能单独证明这条因果关系。真机结论也只覆盖所测G1任务。

- **判断**：值得读到混合模态训练目标和动作专家接口，因为它能否复用，取决于缺失模态怎样处理、预测信息怎样变成动作。

## 研究关联

值得借鉴的是把“学会理解未来运动”与“学会发出机器人命令”分开：前者可以吸收不完整的人类模态数据，后者负责落到具体身体上。若已有大量人类数据而机器人示范有限，这种训练分工值得检查，但仍需要机器人适配和动作监督。

### 下一步读哪里

核查三类人类数据各自的训练目标、机器人中期训练所需数据、冻结范围和门控机制；再看SIMPLE与G1的任务分项，以及去掉预测表示或各训练阶段后的对比。

- **概念**：世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/Being-M0.7 A Latent World-Action Model for Humanoid Robots.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid loco-manipulation requires coordinated locomotion and manipulation informed by future scene evolution and whole-body motion, yet learning these capabilities is constrained by scarce robot demonstrations. Human video and motion datasets offer scalable supervision, but many contain only video or motion rather than paired video-motion data. Moreover, human motion does not directly specify executable robot actions. We present Being-M0.7, a latent world-action model that transfers visual-motion priors learned from mixed-modality human data to humanoid control through pre-training, robot mid-training, and action post-training. We curate a corpus from more than 10,000 hours of raw human-centric data, integrating video-only, motion-only, and paired video-motion streams to learn complementary visual dynamics and whole-body kinematic structure. Joint prediction of future latent visual states and motion encourages visual representations to encode future kinematics. Robot mid-training adapts this coarse-grained prior to robot viewpoints and body dynamics. During action post-training, an action expert combines visual predictive representations from the frozen, adapted prior with current images and proprioception through gated cross-attention, grounding predictive context in executable whole-body commands. Being-M0.7 achieves the highest aggregate success rate among the compared baselines on SIMPLE and matches the strongest baseline on real-world Unitree G1 loco-manipulation tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.11283v1
- Authors: Junpeng Yue, Boyuan Li, Yuxuan Wang, Zepeng Wang, Yuhui Fu, Feiyang Xie, Yu Zhang, Jing Zhang, Xianqi Zhang, Weibo Li, Xiaofei Zheng, Yuming Fang, Jiangxing Wang, Zongqing Lu
- Published: 2026-10-08T05:49:24Z
- Age days: 1

</details>
