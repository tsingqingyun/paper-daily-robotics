---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.27284"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 47
created: 2026-09-04
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies

> [!summary] 先说人话（基于摘要）
> FineVLA要让VLA不仅理解“做什么”，还听懂“用哪只手、从哪边接近、接触哪里”。它通过FineVLA-Data、专用VLM标注器及细粒度/目标级指令混合训练，获得可控执行能力。

## 这篇到底在做什么

- **卡在哪里**：机器人轨迹通常只配目标级语言，缺少主动手臂、接近方向和接触区域等决定动作方式的信息，因此策略即使能完成任务，也难按人的具体要求执行；粗粒度标注还限制了机器人视频理解。
- **关键解法**：框架先统一10个开源数据集中的轨迹，再由机器人专用VLM扩展细粒度动作标注并进行人工核验；训练时以受控比例混合细粒度指令和原始目标指令，使策略同时学习任务目标与执行约束。关键差异是语言监督与动作细节对齐，而非只描述最终目标。
- **拿什么证明**：统一了972,247条轨迹、85K个任务，人工核验的FineVLA-Data含47,159条细粒度轨迹；留出基准含500个视频、11,631个原子事实和1,030道VQA题。FG-only较Raw-only提高1.4至8.1个成功率点；最佳混合比例位于1:2至1:1，RoboTwin达86.8%/82.5%，真实双臂任务为62.7/100，对照Raw-only为49.9；姿态、颜色和接近方向分别最高提升23、18、18点。

## 值不值得读

- **和你的研究有什么关系**：对VLA和具身智能研究者，这提供了可复用的数据构建工具、监督集与评测集，也给出直接的配比经验：细粒度语言应补充而非取代目标语言。它还可用于检查多模态模型是否真正编码了可执行的动作语义；与世界模型的联系则较间接。
- **先别急着信**：摘要中的“62.7/100”指标写法含义不够清楚，需要全文核查具体任务、分母和统计协议；不同设置下86.8%/82.5%的对应关系也需确认。
- **判断**：值得精读数据定义、混合训练和真实机器人评测；它不仅报出收益，还回答了细粒度监督是否损害目标完成率这个关键问题。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：47
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/FineVLA Fine-Grained Instruction Alignment for Steerable Vision-Language-Action.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2605.27284v3 Announce Type: replace Abstract: Vision-Language-Action (VLA) models are increasingly expected to not only complete robot tasks, but also follow human instructions about how those tasks should be executed. However, existing robot datasets usually pair trajectories with coarse goal-level language, leaving execution-critical details such as active arm, approach direction, and contact region unspecified. This limits steerable policy learning and robotic video understanding. We introduce FineVLA, an open framework for action-aligned fine-grained VLA supervision. The framework includes: (1) a data construction tool that unifies 972,247 trajectories across 85K tasks from 10 open-source robot datasets and builds FineVLA-Data, a human-verified dataset of 47,159 fine-grained trajectories; (2) a held-out benchmark with 500 videos, 11,631 atomic facts, and 1,030 VQA questions; (3) a robotics-specialized VLM annotator for scalable fine-grained annotation; and (4) a steerable VLA policy trained with controlled mixtures of fine-grained and raw goal-level instructions. Our experiments yield three findings. First, fine-grained supervision does not sacrifice goal-level success: FG-only improves over Raw-only by +1.4 to +8.1 success-rate points across settings. Second, fine-grained and raw instructions are complementary, following a consistent inverted-U trend peaking at FG:Raw = 1:2 to 1:1. The best mixed setting reaches 86.8%/82.5% in RoboTwin simulation and 62.7/100 in real-world dual-arm manipulation (vs. 49.9 Raw-only). Third, fine-grained supervision improves steerable control: the largest real-world gains appear on pose (+23), color (+18), and approach direction (+18)--factors where goal-level instructions provide no guidance. Overall, fine-grained language should augment goal-level instructions: specifying how to execute alongside what to achieve. Project page: https://finevla.xlang.ai/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.27284
- Authors: Xintong Hu, Xuhong Huang, Jinyu Zhang, Yutong Yao, Yuchong Sun, Qiuyue Wang, Mingsheng Li, Sicheng Xie, Yitao Liu, Junhao Chen, Yixuan Chen, Yingming Zheng, Shuai Bai, Tao Yu
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
