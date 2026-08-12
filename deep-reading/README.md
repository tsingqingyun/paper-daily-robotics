---
type: workflow
tags: [ai, robotics, paper, deep-read, research]
created: 2026-08-12
---

# AI 论文深读工作流

## 目标

日报负责低成本筛选，精读负责高精度核验。不要把每篇论文都精读；只把会改变研究路线、实验设计或技术判断的论文升级。

```text
L0 摘要快读（1–3 分钟）
  ↓ 值得核查
L1 定向精读（10–15 分钟）
  ↓ 仍会影响重要判断
L2 完整精读（45–90 分钟）
  ↓ 形成可复用知识
研究问题 / 实验计划 / 核心知识节点
```

## 何时升级

满足任意两项，就从 L0 升级到 L1：

- 直接命中当前研究问题或主线。
- 摘要中的关键证据、局限没有说明清楚。
- 结果明显优于强 baseline，或结论与既有认知冲突。
- 有真实机器人、跨任务、跨形态或安全相关证据。
- 方法、数据、评测协议或失败分析可以复用。
- 论文会影响选题、复现、采购、产品或投资判断。

满足任意一项，再从 L1 升级到 L2：

- 需要引用、复现或基于它设计实验。
- 关键结论依赖复杂实验设置，主表不足以判断。
- 需要确认比较是否公平、提升来自哪里、边界在哪里。
- 它可能成为知识地图中的长期核心节点。

否则停在 L0；“有趣”本身不足以触发精读。

## L1：定向精读

只核查四件事：

1. 作者最重要的主张是什么？
2. 哪张主表或关键图真正支持它？
3. 最强 baseline 是否公平，提升是否稳定？
4. 作者没有证明什么，真实外推边界在哪里？

完成标准：至少记录一个“主张 → 页码/表格/图 → 证据 → 可信度”链条，并写出一个限制。

## L2：完整精读

按 [[Paper Deep Read]] 完成以下板块：

- 问题与既有缺口：它替代了什么假设或方案？
- 方法机制：输入输出、关键模块、训练信号、推理流程。
- 主张—证据账本：每个关键主张必须绑定页码、表格或图。
- 实验可信度：数据、任务、baseline、公平性、消融、方差和失败案例。
- Physical AI 专项：仿真/真实、机器人硬件、任务数、成功定义、控制频率、延迟、安全和恢复。
- 边界与反证：什么条件下结论不成立？什么实验能推翻它？
- 研究落点：能复用的最小单元、影响的知识节点、下一步实验。

## 创建精读卡

在 vault 根目录运行：

```bash
# 10–15 分钟定向核查
python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/YYYY-MM-DD/论文笔记.md" --level focused

# 45–90 分钟完整精读
python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/YYYY-MM-DD/论文笔记.md" --level full
```

脚本会在 `50_Papers/Deep Reads/<论文标题 + arXiv ID>/` 下创建 `README.md` 精读卡和 `manifest.json` 状态清单，并登记到 [[精读论文索引]]；不会删除、移动或覆盖原论文快读卡。重复运行会返回已有精读卡路径。

完成全文核验后，把 `README.md` 的 `reading_status` 和 `manifest.json` 的同名字段都改为 `processed`。每日发布器只把已完成报告同步到 GitHub 的 `deep-reads/`；源 PDF 默认只在本地保存，公开目录保留校验值和 arXiv 原文链接。

## 证据纪律

- “作者声称”“论文证据”“我的推断”必须分开写。
- 数字、对比和因果结论必须标页码、表格或图。
- 找不到 PDF 或关键证据时停止下结论，保留“未核验”。
- Demo 不是泛化证据；仿真结果不是现实部署证据。
- 没有强 baseline、消融、方差或失败案例时，下调可信度。

## 完成后的去向

- 改变研究问题：创建 [[Research Question]]。
- 需要复现：创建 [[Experiment Log]]。
- 改变长期认知：回写相应核心知识节点。
- 没有改变任何判断：保留精读卡，但不升级为核心笔记。

## 设计参考

- DeepPaperNote：https://github.com/917Dhj/DeepPaperNote
- PaperQA2：https://github.com/Future-House/paper-qa
- Obsidian Research Vault Template：https://github.com/hoonsubin/obsidian-research-vault-template
