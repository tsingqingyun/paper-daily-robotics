---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03680v1"
published: "2026-09-03T11:17:26Z"
age_days: 3
score: 25
created: 2026-09-07
concepts: ["AI 核心知识地图"]
---

# DropClick: Semi-Automated One-Click Segmentation for Agricultural Robotic Data

> [!summary] 先说人话（基于摘要）
> DropClick 用少量点击生成农业图像分割伪标签，而且允许大量目标不点击；只用5张图训练后，即使丢掉一半点击仍保持较高mIoU。

## 这篇到底在做什么

- **卡在哪里**：农业机器人分割标注耗时昂贵；普通一键分割通常仍要求场景中每个物体都点击，用户输入量随目标数量增长。
- **关键解法**：工具接收部分物体上的单击并输出植物或果实伪标签，无需每个实例都有点击；这些伪标签还能以半监督方式训练Mask2Former实例分割器。
- **拿什么证明**：仅用5张训练图初始化。在SB20/BUP20上，一键分割mIoU为70.0/72.6；缺失50%点击时仍为68.9/71.3。用其伪标签训练Mask2Former，SB20的AP50为70.1对全点击70.7，BUP20均为77.0，同时分别节省46.3%和31.9%输入。

## 值不值得读

- **和你的研究有什么关系**：它对农业机器人数据生产和低成本视觉标注有明确实用价值，但与VLA或世界模型的关联较弱。
- **先别急着信**：训练只用5张图虽醒目，但需核查图像选择方式、点击模拟或真人点击协议，以及跨农场和新物种的泛化。
- **判断**：农业视觉数据团队值得精读并考虑试用；其他具身研究者可把它当作高效伪标注案例浏览。

## 研究关联

- **概念**：[[AI 核心知识地图]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/DropClick Semi-Automated One-Click Segmentation for Agricultural Robotic Data.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Labelling vision datasets, especially for segmentation tasks, is a laborious and costly process that stymies novel developments in agricultural robotics. In this paper, we present DropClick, a click-guided segmentation tool that simplifies the annotation process. Our system utilises single-click inputs on objects to generate pseudo-labels, which can replace manual annotations. DropClick stands out as it is a semi-automated approach and does not require a click for every object in the scene. It can therefore further reduce the required amount of user input drastically. We evaluate our method on two challenging agricultural robotic datasets, SB20 and BUP20 for plant and fruit segmentation, respectively. DropClick is first trained on a small subset of just 5 images from the original training data. This DropClick model can then be deployed as a one-click segmentation system and achieves comparable or higher performance than other one-click methods achieving an mIoU of 70.0 and 72.6 points, for SB20 and BUP20 respectively. DropClick then excels at maintaining high performance when clicks are not given (e.g. dropped); when 50% of the clicks are missing it still maintains an mIoU of 68.9 and 71.3 points, for SB20 and BUP20 respectively. We validate DropClick as a pseudo-labelling approach by taking its outputs to train a Mask2Former instance-based segmentation model in a semi-supervised manner. In this process, partially removing user input from DropClick yields similar high performance when compared to providing all clicks, at 70.1 vs 70.7 points AP50 for SB20 and no difference for BUP20 at 77.0 for both models; at the same time saving 46.3% of total input for SB20 and 31.9% for BUP20.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03680v1
- Authors: Patrick Zimmer, Michael Halstead, Chris McCool
- Published: 2026-09-03T11:17:26Z
- Age days: 3

</details>
