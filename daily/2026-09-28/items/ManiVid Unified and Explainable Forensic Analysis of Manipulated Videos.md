---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30934v1"
published: "2026-09-25T07:51:50Z"
age_days: 3
score: 30
created: 2026-09-28
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# ManiVid: Unified and Explainable Forensic Analysis of Manipulated Videos

> [!summary] 先说人话（基于摘要）
> ManiVid 将局部视频篡改的检测、区域定位和异常解释放到同一任务里，ManiVidLens 则让多模态推理与分割共享底层取证证据。它直接服务于视频取证，机器人关联较弱。

## 问题

局部篡改保留大部分原视频，难以检测和精确定位；现有数据不足，多模态模型又难以利用低层取证线索并输出像素级区域。

## 创新点或方法

构建含真假标签、篡改掩码和异常解释的配对数据集。ManiVidLens 的证据路由器为推理与分割提供低层线索，Prompt Distill Module 将定位状态转成语义、几何提示，并蒸馏空间先验用于掩码解码与全视频传播。

## 证据

数据约含 19K 人工核验真假视频对，多数为 1080P，来自两种范式与 15 个生成模型；基准取 1K 对。相对最强对照，定位 mIoU、J&F 分别提升 21.1%、21.3%，解释 ROUGE-L、CSS 提升 131.3%、9.9%；检测 Acc 为 0.914，F1 为 0.913。

## 局限

上述增益是相对提升，不能读成百分点；解释指标提升是否对应更可信的取证解释，以及对未见篡改模型的泛化，需全文核查。

- **判断**：多模态定位与取证方向值得细读，纯机器人日报读者了解任务和机制即可。

## 研究关联

对多模态基础模型研究者，共享低层证据以协调解释和定位值得参考。但摘要没有机器人任务、VLA 或具身基准验证，不能直接作为具身能力提升证据。

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/ManiVid Unified and Explainable Forensic Analysis of Manipulated Videos.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Rapid advances in AI-generated video (AIGV) have increased the risks posed by deceptive video manipulation. Unlike fully synthetic videos, manipulated videos retain most source content and alter only localized regions, making forensic analysis particularly challenging. Existing video forgery research faces two limitations in both data and methodology: (1) High-quality datasets and benchmarks tailored for manipulated videos remain scarce. (2) Multimodal large language models (MLLMs) extend forgery analysis beyond binary classification but struggle to use low-level forensic cues and provide precise pixel-level grounding. Specifically, we introduce ManiVid, a unified forensic analysis task covering forgery detection, artifact grounding, and anomaly explanation for manipulated videos. We construct ManiVid-38K, the first dataset to combine paired, open-vocabulary localized manipulations of general videos with authenticity labels, forgery masks, and anomaly explanations. It comprises about 19K manually verified real-fake video pairs, mostly at 1080P resolution, generated under 2 paradigms with 15 powerful generation models. We sample 1K pairs for ManiVidBench, balanced across six manipulation types and generation models for fair evaluation. We further propose ManiVidLens, a unified framework for explainable video forgery analysis. Its Forensic Evidence Router supplies shared low-level forensic evidence for multimodal reasoning and video segmentation. Its Prompt Distill Module converts grounding states into semantic and geometric prompts and distills spatial priors for mask decoding and full-video propagation. ManiVidLens achieves relative gains over the strongest comparison methods in artifact grounding (+21.1% mIoU; +21.3% J&F) and anomaly explanation (+131.3% ROUGE-L; +9.9% CSS). Its forgery detection remains comparable to dedicated classifiers (0.914 Acc; 0.913 F1).

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30934v1
- Authors: Hengrui Kang, Zhonghao Yan, Yuxuan Yang, Ruoyan Jing, Yuncheng Guo, Hao Chen, Kongming Liang, Zhanyu Ma, Conghui He, Weijia Li
- Published: 2026-09-25T07:51:50Z
- Age days: 3

</details>
