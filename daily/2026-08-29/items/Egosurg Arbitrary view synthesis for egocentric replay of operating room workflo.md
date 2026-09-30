---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2510.04802"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 25
created: 2026-08-29
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# Egosurg: Arbitrary view synthesis for egocentric replay of operating room workflows from ambient cameras

> [!summary] 先说人话（基于摘要）
> EgoSurg用稀疏墙面双目相机重建动态手术室，再合成不同角色的第一视角回放，无需给医护人员佩戴设备。核心是尺度感知深度初始化3D Gaussian Splatting，并用条件扩散修正遮挡导致的渲染伪影。

## 这篇到底在做什么

- **卡在哪里**：固定环境相机只能记录房间视角，无法还原某位团队成员实际看到的内容；稀疏覆盖、人员拥挤和遮挡又使动态三维重建及任意视角渲染产生明显伪影。
- **关键解法**：输入墙面双目视频，逐时间点由尺度感知立体深度初始化3DGS；图像条件扩散模型修正辅助视角渲染，再输出角色特定的任意第一视角。它避免给人员加装设备，并把环境记录变成可导航三维回放。
- **拿什么证明**：评测包括两个医院的4次真实机器人肺科手术和2次模拟全流程。近场重建PSNR为26.8 dB、SSIM为0.895；对配对手持第一视角的合成结果为17.8 dB和0.766，并展示三类用途案例。

## 值不值得读

- **和你的研究有什么关系**：对具身评测与机器人手术Agent，它可生成多角色视角的流程记录，用于安全事件复盘、训练和反事实位置分析；但不是决策策略评测本身。
- **先别急着信**：合成第一视角明显低于近场重建指标，且扩散修正可能生成未被相机观测的细节；临床证据用途尤其需要全文核查真实性边界。
- **判断**：应用证据具体，做手术工作流重建或具身数据采集值得精读；用于安全裁决前必须重点审查生成内容的可验证性。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/Egosurg Arbitrary view synthesis for egocentric replay of operating room workflo.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2510.04802v2 Announce Type: replace Abstract: Observing surgical practice has historically relied on fixed vantage points or recollections, leaving the egocentric perspectives that shape clinical decisions undocumented. Ambient fixed cameras capture the operating room (OR) at room scale but cannot recover what any individual team member actually saw. We present EgoSurg, a framework that reconstructs dynamic OR scenes from sparse wall-mounted stereo video and renders arbitrary, role-specific egocentric views without instrumenting personnel or interfering with clinical workflow. EgoSurg initializes a per-timestamp 3D Gaussian Splatting representation from scale-aware stereo depth and refines it with an image-conditioned diffusion model that corrects auxiliary rendered views, mitigating artifacts caused by limited camera coverage, crowding, and occlusion. We evaluated the framework on four real robotic pulmonology procedures and two simulated full-workflow sessions across two hospital sites. Near-field reconstruction fidelity was consistent (PSNR 26.8~dB, SSIM .895) across five workflow phases and both sites, and synthesized egocentric views reached a PSNR of 17.8~dB and an SSIM of .766 against paired hand-held point-of-view recordings. We further demonstrate three case studies for intended use: adjudicating a simulated sterile field violation, replaying a procedure from role-specific viewpoints, and testing a counterfactual change in personnel position. These results indicate that existing ambient camera infrastructure can be turned into a navigable 3D record of surgical work, supporting retrospective review of safety events, training, and workflow analysis from every angle.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2510.04802
- Authors: Han Zhang, Lalithkumar Seenivasan, Jose L. Porras, Roger D. Soberanis-Mukul, Hao Ding, Hongchao Shu, Benjamin D. Killeen, Ankita Ghosh, Lonny Yarmus, Jeffrey K. Jopling, Masaru Ishii, Angela C. Argento, Mathias Unberath
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
