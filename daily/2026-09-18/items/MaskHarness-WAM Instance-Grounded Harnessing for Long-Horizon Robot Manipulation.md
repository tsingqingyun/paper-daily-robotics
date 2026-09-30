---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19974v1"
published: "2026-09-17T09:48:33Z"
age_days: 0
score: 27
created: 2026-09-18
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# MaskHarness-WAM: Instance-Grounded Harnessing for Long-Horizon Robot Manipulation

> [!summary] 先说人话（基于摘要）
> MaskHarness-WAM在局部操作策略外加一层实例跟踪与进度管理，用目标掩码告诉机器人“这次操作哪一个”，完成后再核实并切换目标。

## 问题

多个外观相同的物体要按指定顺序操作时，短程策略难以持续区分实例，也难以判断何时进入下一阶段。

## 创新点或方法

高层规划通过目标掩码连接低层策略；每个子任务边界重新观察场景、生成并验证初始目标掩码，根据经验证的完成状态切换实例，使空间条件随场景更新。

## 证据

摘要称实机顺序多物体操作中显著优于有限时域策略；摘要未给出可核查的结果数字。

## 局限

需核查掩码验证和完成判断如何实现，以及误判后能否恢复；摘要未交代任务长度和基线是否获得同等目标信息。

- **判断**：做长程系统集成值得读接口与失败处理，算法研究者可先确认收益是否超出额外实例信息本身。

## 研究关联

对具身Agent，提供通过执行管理层延长已有局部技能适用时域的方案；对评测，凸显同外观实例身份和阶段完成判断的重要性。

- **概念**：智能体 Agent 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/MaskHarness-WAM Instance-Grounded Harnessing for Long-Horizon Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon robot manipulation requires not only stable local visuomotor control, but also continuous target tracking and reliable task progress assessment throughout execution. This challenge becomes particularly critical when multiple objects share identical appearances and must be manipulated in a prescribed order. In such scenarios, relying solely on a limited-horizon manipulation policy is often insufficient to determine which instance should be operated on and when the task should transition to the next stage. To address this challenge, we propose MaskHarness-WAM, an instance-grounded harness for long-horizon manipulation. The proposed system connects high-level task planning with low-level manipulation policies through target masks, while leveraging visual feedback for subtask scheduling and continuous execution. Since each subtask corresponds to a different target instance, the low-level policy requires a newly established initial target mask under the updated scene at each subtask transition. The harness continuously re-observes the environment, generates, and verifies the target mask at subtask boundaries, thereby updating the instance-level spatial condition provided to the low-level policy. Furthermore, the system advances the manipulation process by switching target instances according to the verified completion status of each subtask. Experiments on a real robot platform demonstrate that MaskHarness-WAM substantially outperforms limited-horizon policies on sequential multi-object manipulation, showing its effectiveness in extending local manipulation skills to reliable long-horizon execution.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19974v1
- Authors: Zitai Huang, Taiyi Su, Jian Zhu, Jianjun Zhang, Chong Ma, Tianbin Liu, Weiyi Lu, Yi Xu, Hanli Wang
- Published: 2026-09-17T09:48:33Z
- Age days: 0

</details>
