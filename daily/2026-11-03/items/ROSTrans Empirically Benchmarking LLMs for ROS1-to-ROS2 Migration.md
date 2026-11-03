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
url: "https://arxiv.org/abs/2610.41168v1"
published: "2026-10-30T02:44:28Z"
age_days: 3
score: 28
created: 2026-11-03
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# ROSTrans: Empirically Benchmarking LLMs for ROS1-to-ROS2 Migration

> [!summary] 这篇论文到底做了什么（基于摘要）
> ROSTrans 检查 LLM 把 ROS1 代码迁到 ROS2 后，节点能否真正启动并正确通信。它把候选代码放进固定测试环境中运行，揭示“编译成功”距离“迁移成功”还有很大差距。

## 问题

ROS 迁移涉及节点协作、中间件配置和生命周期语义，许多错误只有节点运行并交换消息后才暴露。只检查代码外观或编译，无法确认话题、服务、动作和参数行为仍然正确，因此通用代码评测不足以回答迁移是否可用。

### 用一个例子理解

理解用例（非论文实验）：输入一个 ROS1 服务节点的待迁移文件；模型生成 ROS2 实现；测试启动服务端并发送请求，输出编译结果和响应断言结果，从而识别“能启动但响应不对”。

## 创新点或方法

作者为每个补全任务建立可执行参考：已验证的 ROS2 实现、启动并测试节点的运行时测试，以及复现容器。评测只把模型生成的目标文件注入其余部分固定的参考包，候选无法替换测试。基础评测让模型生成迁移文件；执行引导修复则把运行反馈用于后续修改，最多三轮。摘要未说明模型训练过程，也未交代修复提示和反馈的具体内容。

### 方法如何工作

1. 从真实仓库构造带脚手架的迁移任务，使模型面对明确的目标文件和上下文。
2. 建立已验证参考实现与容器，为候选提供一致的运行环境。
3. 只替换候选目标文件并启动节点，实际触发通信与参数行为，得到超出编译结果的判断。
4. 把执行反馈用于后续修复，再次运行固定测试，衡量反馈能补救多少错误。

### 必要术语

- ROS1→ROS2 迁移：把机器人软件改为适配另一代 ROS；本文要求运行行为也正确。
- 运行时断言：程序启动后检查实际行为是否符合要求；用于发现编译器看不到的错误。
- pass@1：单次生成通过任务的比例指标；本文用它描述首次生成的可靠程度。

## 证据

摘要给出 108 个任务，来自 70 多个开源 ROS1 仓库；六个前沿 LLM 每题随机生成五次，pass@1 低于 10.9%。全部样本中，56.5% 编译成功后在运行时失败，32.0% 在迁移接口的运行断言上失败；这两项不能直接相加。三轮执行引导修复后，Claude Opus 4.6 和 GPT-5.5 的任务成功率分别为 49.1% 与 47.2%。结果支持运行测试能揭示编译检查遗漏的问题，不能当作任意完整仓库迁移的成功率。

## 局限

任务是有脚手架的目标文件补全，完整仓库迁移还可能涉及构建配置与跨文件改动，因此难度范围不同。参考包固定能保证公平，也限制了候选可修复的位置。还需核查测试对时序、并发和异常路径的覆盖；摘要未提供这些信息。

- **判断**：值得细读任务与运行测试设计，它比模型排名更能帮助判断迁移结果是否可信。

## 研究关联

可借鉴的是把验收条件写成节点之间真实发生的交互。对于依赖消息协议和运行状态的软件，评估模型生成代码时应实际触发这些行为；运行反馈也能成为修复依据。

### 下一步读哪里

检查接口、行为和系统三级正确性各自怎样测试，再看典型编译通过但运行失败的样例。修复实验应核查每轮反馈、总调用预算，以及最终成功率的统计口径。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/ROSTrans Empirically Benchmarking LLMs for ROS1-to-ROS2 Migration.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Although large language models have shown strong capabilities in domain-specific code generation, their performance in robotics software development, especially for the Robot Operating System (ROS), remains largely unexplored. ROS code generation presents distinctive challenges, including complex inter-node coordination, middleware configuration, and lifecycle semantics that go far beyond standard coding benchmarks, and many important correctness properties become observable only once migrated nodes are launched and communicate. We present ROSTrans, a benchmark for evaluating LLMs on ROS1-to-ROS2 code migration, a representative and practically important setting for ROS code generation. ROSTrans comprises 108 scaffolded completion tasks drawn from a diverse set of 70+ open-source ROS1 repositories and organized into a hierarchical taxonomy assessing interface-level, behavioral-level and system-level correctness. For every task we establish an executable reference: a verified ROS2 implementation, a runtime test suite that launches the nodes and exercises their topics, services, actions and parameters, and a container ensuring reproducibility. Candidates are scored by injecting only their target files into an otherwise fixed copy of the reference package, so a candidate can neither supply nor weaken the tests it is judged by. Evaluating six frontier LLMs over five stochastic generations per task, we find pass@1 below 10.9%, and that 56.5% of all samples build successfully and then fail at runtime,and 32.0% fail runtime assertions on the migrated interfaces, a class of error no compile-only oracle can detect. Execution-guided repair further improves task success, reaching 49.1% and 47.2% for Claude Opus 4.6 and GPT-5.5 after three rounds, respectively.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.41168v1
- Authors: Yichen Zhao, Minghao Shao, Zhuoyan Yu, Yijun Shen, Boyuan Chen, Yik-Cheung Tam, Muhammad Shafique
- Published: 2026-10-30T02:44:28Z
- Age days: 3

</details>
