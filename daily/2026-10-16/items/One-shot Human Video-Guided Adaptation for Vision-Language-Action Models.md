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
url: "https://arxiv.org/abs/2610.19746"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-10-16
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# One-shot Human Video-Guided Adaptation for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> CapPro 用一段人类示范视频告诉 VLA 陌生任务该怎样推进，无需为目标任务再收机器人示范或微调。关键是提取视频中的任务阶段信息并接入动作条件，让机器人获得执行线索，而不是逐帧照搬人的运动。

## 问题

预训练 VLA 面对训练分布之外的新操作任务，往往仍需任务专用机器人示范和额外训练，采集与计算成本都高。单个人类视频较容易获得，但人的身体与机器人不同，不能直接把人体运动当作机器人动作标签；还需要从长视频里找到与任务推进有关的信息。

### 用一个例子理解

理解用例（非论文实验）：输入一段人把抹布折好放进篮子的视频和当前机器人图像；CapPro 提取折叠、搬运等阶段线索并加入动作条件，VLA 输出机器人自己的操作动作，而非复制人的关节角。

## 创新点或方法

旧做法针对目标任务收机器人数据再训练；CapPro 预先学习怎样读人类视频和怎样把视频信息交给 VLA。第一部分通过可学习的视觉词元选择压缩视频，并利用阶段字幕监督学习任务相关的查询表示；第二部分把紧凑视频表示和查询导出的表示共同加入预训练策略的动作条件。部署到陌生目标任务时提供一段人类视频，不再做目标任务微调。摘要没有交代阶段字幕来源、训练数据规模或策略各部分是否冻结。

### 方法如何工作

1. 训练时通过视觉词元选择压缩人类视频，减少动作条件需要接收的冗余信息。
2. 利用阶段字幕监督学习任务相关查询表示，让视频信息与任务推进阶段建立联系。
3. 将紧凑视频和查询导出的表示接入 VLA 动作条件，学习怎样用示范线索指导机器人动作。
4. 面对未见目标任务时输入单段人类视频并生成动作，不收目标任务机器人示范，也不进行目标任务微调。

### 必要术语

- 视觉词元：视频画面经过编码后的信息单元；本文学习选择其中有用的部分。
- 阶段字幕监督：用描述任务阶段的文字提供学习信号；帮助表示关注任务推进。
- 动作条件：策略生成动作时可使用的输入信息；本文在其中加入人类视频提供的线索。

## 证据

摘要报告在来源任务与未见目标任务上评估，未见目标任务组的平均表现提高，来源任务表现保持相近。但没有给出具体任务、对比方法、成功率、改善幅度或仿真与真机划分。因此材料支持作者报告的跨任务适应方向，尚不足以判断收益大小、稳定性，以及距离较远的新任务是否同样有效。

## 局限

“一段视频”描述的是目标任务适应时的输入，不代表整套方法只用一段视频训练。仍需核查目标任务与来源任务的重合程度，以及换示范者、视角或阶段顺序后是否有效；摘要没有给出的实验不能据此认定全文未做。

- **判断**：值得读表示学习和任务划分，但在看到具体对比前，应把它视为利用人类视频引导已有能力的方案，暂不推断它能学会全新的控制技能。

## 研究关联

这里值得借鉴的是改变示范的用途：人类视频可以提供任务阶段与执行线索，不必先解决人体轨迹到机器人关节轨迹的完整映射。适合尝试的前提，是已有策略具备相关操作能力，主要缺的是如何组合、推进这些能力。

### 下一步读哪里

下一步核查阶段字幕怎样标注、查询表示怎样训练、词元选择保留了哪些信息，以及哪些参数参与训练；实验上重点看只用语言、只用视频和完整方法的对比，以及未见任务如何划分。输入没有正文节选。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/One-shot Human Video-Guided Adaptation for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.19746v1 Announce Type: new Abstract: Vision-language-action (VLA) models have recently achieved remarkable progress by leveraging large-scale robot datasets and foundation models for general-purpose robot manipulation. However, their ability to rapidly adapt to novel manipulation tasks beyond the training distribution remains limited. Existing approaches often require task-specific robot demonstrations and additional training, which are labor- and compute-intensive, limiting the scalability of VLA adaptation to open-world scenarios. To reduce this dependence on target-task robot data, we propose CapPro, a framework that enables a VLA policy to adapt to previously unseen manipulation tasks using only a single human demonstration video. CapPro consists of two components. First, a phase-aware human video representation module constructs a compact video representation through learned visual token selection and learns task-relevant query representations under phase-caption supervision. Second, a video-conditioned adaptation module jointly incorporates the compact video and query-derived representations into the action-conditioning context of the pretrained VLA policy. % This design introduces task-specific guidance while largely preserving the original VLA action-generation backbone. In this way, the human demonstration provides task-specific execution guidance rather than an embodiment-aligned trajectory to imitate, without requiring target-task robot demonstrations or target-task fine-tuning. Experiments across source and unseen target tasks show that CapPro improves average performance across unseen target groups while maintaining comparable performance on the source tasks. These results demonstrate the effectiveness of human-video guidance for cross-task VLA adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.19746
- Authors: Qi Chen, Yuwei Wu, Quan Chen, Kunpeng Gao, Jin Chen, Che Sun, Zhi Gao, Yunde Jia
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
