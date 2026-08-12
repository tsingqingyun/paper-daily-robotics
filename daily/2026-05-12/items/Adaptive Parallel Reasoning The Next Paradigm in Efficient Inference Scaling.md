---
type: update-item
tags: [update, ai, embodied-ai]
source: "Berkeley BAIR Blog"
url: "http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/"
published: "Fri, 08 May 2026 02:00:00 -0700"
score: 18
created: 2026-05-12
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling

## 为什么重要

自动筛选分数：18

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]], [[具身智能评测与基准]]

## 摘要

.apr-fig { text-align: center; margin: 1.35em 0; line-height: 1.4; } .apr-fig--wide img
{ display: inline-block; width: 100%; max-width: 100%; height: auto; vertical-align:
middle; } .apr-fig--wide-0-8 { max-width: 80%; margin-left: auto; margin-right: auto; }
.apr-fig--tall img { display: inline-block; max-height: 300px; width: auto; max-width:
100%; height: auto; object-fit: contain; vertical-align: middle; } .apr-fig--tall-1-2x
img { display: inline-block; max-height: 360px; width: auto; max-width: 100%; height:
auto; object-fit: contain; vertical-align: middle; } .apr-fig--tall-1-5x img { display:
inline-block; max-height: 450px; width: auto; max-width: 100%; height: auto; object-fit:
contain; vertical-align: middle; } .apr-fig--tall-2x img { display: inline-block; max-
height: 600px; width: auto; max-width: 100%; height: auto; object-fit: contain;
vertical-align: middle; } .apr-fig .apr-fig-cap { display: block; text-align: center;
font-size: 0.9em; font-style: italic; } .apr-ack a { color: #1565c0; font-weight: 500;
text-decoration: none; border-bottom: 1px solid #90caf9; padding-bottom: 0.06em; } .apr-
ack a:hover { color: #0d47a1; border-bottom-color: #1565c0; } Overview of adaptive
parallel reasoning. What if a reasoning model could decide for itself when to decompose
and parallelize independent subtasks, how many concurrent threads to spawn, and how to
coordinate them based on the problem at hand? We provide a detailed analysis of recent
progress in the field of parallel reasoning, especially Adaptive Parallel Reasoning.
Disclosure: this post is part landscape survey, part perspective on adaptive parallel
reasoning. One of the authors (Tony Lian) co-led ThreadWeaver ( Lian et al., 2025 ), one
of the methods discussed below. The authors aim to present each approach on its own
terms. Motivation Recent progress in LLM reasoning capabilities has been largely driven
by inference-time scaling, in addition to data and parameter scaling ( OpenAI et al.,
2024 ; DeepSeek-AI et al., 2025 ). Models that explicitly output reasoning tokens
(through intermediate steps, backtracking, and exploration) now dominate math, coding,
and agentic benchmarks. These behaviors allow models to explore alternative hypotheses,
correct earlier mistakes, and synthesize conclusions rather than committing to a single
solution ( Wen et al., 2025 ). The problem is that sequential reasoning scales linearly
with the amount of exploration. Scaling sequential reasoning tokens comes at a cost, as
models risk exceeding effective context limits ( Hsieh et al., 2024 ). The accumulation
of intermediate exploration paths makes it challenging for the model to disambiguate
amongst distractors when attending to information in its context, leading to a
degradation of model performance, also known as context-rot ( Hong, Troynikov and Huber,
2025 ). Latency also grows proportionally with reasoning length. For complex tasks
requiring millions of tokens for exploration and planning, it’s not uncommon to see
users wait tens of minutes or even hours for an answer ( Qu et al., 2025 ). As we
continue to scale along the output sequence length dimension, we also make inference
slower, less reliable, and more compute-intensive. Parallel reasoning has emerged as a
natural solution. Instead of exploring paths sequentially ( Gandhi et al., 2024 ) and
accumulating the context window at every step, we can allow models to explore multiple
threads independently (threads don’t rely on each other’s context) and concurrently
(threads can be executed at the same time). Figure 1: Sequential vs. Parallel Reasoning
Over recent years, a growing body of work has explored this idea across synthetic
settings (e.g., the Countdown game ( Katz, Kokel and Sreedharan, 2025 )), real-world
math problems, and general reasoning tasks. From Fixed Parallelism to Adaptive Control
Existing approaches show that parallel reasoning can help, but most of them still decide
the parallel structure outside the model rather than letting the model choose it. Simple
fork-and-join. Self-consistency/Majority Voting — independently sample multiple complete
reasoning traces, extract final answer from each, and return the most common one ( Wang
et al., 2023 ). Best-of-N (BoN) — similar to self-consistency, but uses a trained
verifier to select the best solution instead of using majority voting ( Stiennon et al.,
2022 ). Although simple to implement, these methods often incur redundant computation
across branches since trajectories are sampled independently. Heuristic-based structured
search. Tree / Graph / Skeleton of Thoughts — a family of structured decomposition
methods that explores multiple alternative “thoughts” using known search algorithms
(BFS/DFS) and prunes via LLM-based evaluation ( Yao et al., 2023 ; Besta et al., 2024 ;
Ning et al., 2024 ). Monte-Carlo Tree Search (MCTS) — estimates node values by sampling
random rollouts and expands the search tree with Upper Confidence Bound (UCB) style
exploration-exploitation ( Xie et al., 2024 ; Zhang et al., 2024 ). These methods
improve upon simple fork-and-join by decomposing tasks into non-overlapping subtasks;
however, they require prior knowledge about the decomposition strategy, which is not
always known. Recent variants. ParaThinker — trains a model to run in two fixed stages:
first generating multiple reasoning threads in parallel, then synthesizing them. They
introduce trainable control tokens ( <think_i> ) and thought-specific positional
embeddings to enforce independence during reasoning and controlled integration during
summarization via a two-phase attention mask ( Wen et al., 2025 ). GroupThink — multiple
parallel reasoning threads can see each other’s partial progress at token level and
adapt mid-generation. Unlike prior concurrent methods that operate on independent
requests, GroupThink runs a single LLM producing multiple interdependent reasoning
trajectories simultaneously ( Hsu et al., 2025 ). Hogwild! Inference — multiple parallel
reasoning threads share KV cache and decide how to decompose tasks without an explicit
coordination protocol. Workers generate concurrently into a shared attention cache using
RoPE to stitch together individual KV blocks in different orders without recomputation (
Rodionov et al., 2025 ). Figure 2: Various Strategies for Parallel Reasoning The methods
above share a common limitation: the decision to parallelize, the level of
parallelization, and the search strategy are imposed on the model, regardless of whether
the problem actually benefits from it. However, different problems need different levels
of parallelization, and that is something critical to the effectiveness of
parallelization. For example, a framework that applies the same parallel structure to
“What’s 25+42?” and “What’s the smallest planar region in which you can continuously
rotate a unit-length line segment by 180°?” is wasting compute on the former and
probably using the wrong decomposition strategy for the latter. In the approaches
described above, the model is not taught this adaptive behavior. A natural question
arises: What if the model could decide for itself when to parallelize, how many threads
to spawn, and how to coordinate them based on the problem at hand? Adaptive Parallel
Reasoning (APR) answers this question by making parallelization part of the model’s
generated control flow. Formally defined, adaptivity refers to the model’s ability to
dynamically allocate compute between parallel and serial operations at inference time .
In other words, a model with adaptive parallel reasoning (APR) capability is taught to
coordinate its control flow — when to generate sequences sequentially vs. in parallel.
It’s important to note that the concept of adaptive parallel reasoning was introduced by
the work Learning Adaptive Parallel Reasoning with Language Models ( Pan et al., 2025 ),
but is a paradigm rather than a specific method. Throughout this post, APR refers to the
paradigm, while “ the APR method ” denotes the specific instantiation from Pan et al.
(2025). This shift matters for three reasons. Compared to Tree-of-Thoughts, APR doesn’t
need domain-specific heuristics for decomposition. During RL, the model learns general
decomposition strategies from trial and error. In fact, models discover useful
parallelization patterns, such as running the next step along with the self-verification
of a previous step, or hedging a primary approach with a backup one, in an emergent
manner that would be difficult to hand-design ( Yao et al., 2023 ; Wu et al., 2025 ;
Zheng et al., 2025 ). Compared to BoN, APR avoids redundant computation. APR models have
control over what each parallel thread will do before branching out. Therefore, APR can
learn to produce a set of unique, non-overlapping subtasks before assigning them to
independent threads ( Wang et al., 2023 ; Stiennon et al., 2022 ; Pan et al., 2025 ;
Yang et al., 2025 ). Compared to non-adaptive approaches, APR can choose not to
parallelize. Adaptive models can adjust the level of parallelization to match the
complexity of the problem against the complexity and overhead of parallelization ( Lian
et al., 2025 ). In practice, this is implemented by having the model output special
tokens that control when to reason in parallel versus sequentially. Below is a condensed
ThreadWeaver-style trace: two outlines and two paths under a <Parallel> block, then the
threads agree on a single boxed answer. Figure 3: Example of an Adaptive Parallel
Reasoning Trajectory from ThreadWeaver, manually condensed for ease of illustration.
Figure 4: Special Tokens Variants across Adaptive Parallel Reasoning Papers Inference
Systems for Adaptive Parallelism How do we actually execute parallel branches? We take
inspiration from computer systems, and specifically, multithreading and multiprocessing.
Most of this work can be viewed as leveraging a fork-join design. At inference time, we
are effectively asking the model to perform a map-reduce operation: Fork the problem
into subtasks/threads, process them concurrently Join them into a final answer Figure 5:
Fork-join Inference Design Specifically, the model will encounter a list of subtasks. It
will then prefill each of the subtasks and send them off as independent requests for the
inference engine to process. These threads then decode concurrently until they hit an
end token or exceed max length. This process blocks until all threads finish decoding
and then aggregates the results. This is common across various adaptive parallel
reasoning approaches. However, one issue arises during aggregation: the content
generated in branches cannot be easily aggregated at the KV cache level. This is because
tokens in independent threads start at identical position IDs, resulting in encoding
overlap and non-standard behavior when merging KV cache back together. Similarly, since
independent threads do not attend to each other, their concatenated KV cache results in
a non-causal attention pattern, which the base model has not seen during training. To
address this issue, the field splits into two schools of thought on how to execute the
aggregation process, defined by whether they modify the inference engine or work around
it. Multiverse modifies the inference engine to reuse KV cache across the join. Before
taking a deeper look into Multiverse ( Yang et al., 2025 )’s memory management, let’s
first understand how KV cache is handled up until the “join” phase. Notice how each of
the independent threads share the prefix sequence, i.e., the list of subtasks. Without
optimization, each thread needs to prefill and recompute the KV cache for the prefix
sequence. However, this redundancy can be avoided with SGLang ’s RadixAttention ( Sheng
et al., 2023 ), which organizes multiple requests into a radix tree, a trie (prefix
tree) with sequences of elements of varying lengths instead of single elements. This
way, the only new KV cache entries are those from independent thread generation. Figure
6: RadixAttention’s KV Cache Management Strategy Now, if everything went well, all the
independent threads have come back from the inference engine. Our goal is now to figure
out how to synthesize them back into a single sequence to continue decoding for next
steps. It turns out, we can reuse the KV cache of these independent threads during the
synthesis stage. Specifically, Multiverse ( Yang et al., 2025 ), Parallel-R1 ( Zheng et
al., 2025 ), and NPR ( Wu et al., 2025 ) modify the inference engine to copy over the KV
cache generated by each thread and edits the page table so that it stitches together
non-contiguous memory blocks into a single KV cache sequence. This avoids the redundant
computation of a second prefill and reuses existing KV cache as much as possible.
However, this has several major limitations. First, this approach requires modifying the
inference engine to perform non-standard memory handling, which can result in unexpected
behaviors. Specifically, since the synthesis request references KV cache from previous
requests, it creates fragility in the system and the possibility of bad pointers.
Another request can come in and evict the referenced KV cache before the synthesis
request completes, requiring it to halt and trigger a re-prefilling of the previous
thread request. This problem has led the Multiverse researchers ( Yang et al., 2025 ) to
limit the batch size that the inference engine can handle, which restricts throughput.
Figure 7: KV Cache “Stitching” During Multiverse Inference Second, this approach
modifies how models see the sequence, which creates a distributional shift that models
are not pretrained on, therefore requiring more extensive training to align behavior.
Specifically, when we stitch together KV cache this way, we create a sequence with non-
standard position encoding. During independent-thread generation, all threads started at
the same position index and attended to the prior subtasks, NOT each other. So when the
threads merge back, the resulting KV cache has a non-standard positional encoding and
does not use causal attention. Therefore, this approach requires extensive training to
align the model to this new behavior. To address this, Multiverse ( Yang et al., 2025 )
and related works apply a modified attention mask during training to prevent independent
threads from attending to each other, aligning the training and inference behaviors.
Figure 8: Multiverse’s Attention Mask With these issues arising from non-standard KV
cache management, can we try an approach without engine modifications? ThreadWeaver
keeps the inference engine unchanged and moves orchestration to the client. ThreadWeaver
( Lian et al., 2025 ) treats parallel inference purely as a client-side problem. The
“Fork” process is nearly identical to Multiverse’s, but the join phase handles memory
very differently as it does NOT modify engine internals. Instead, the client
concatenates all text outputs from independent branches into one contiguous sequence.
Then, the engine performs a second prefill to generate the KV cache for the conclusion
generation step. While this introduces computational redundancy that Multiverse tries to
avoid, the cost of prefill is significantly lower than decoding. In addition, this does
not require special attention handling during inference, as the second prefill uses
causal attention (threads see each other), making it easier to adapt sequential
autoregressive models for this task. Figure 9: ThreadWeaver’s Prefill and Decode
Strategy How should we train a model to learn this behavior? Naively, for each parallel
trajectory, we can break it down into multiple sequential pieces following our inference
pattern. For instance, we would train the model to output the subtasks given prompt,
individual threads given prompt+subtask assignment, and conclusion given
prompt+subtasks+corresponding threads. However, this seems redundant and not compute
efficient. Can we do better? Turns out, yes. As in ThreadWeaver ( Lian et al., 2025 ),
we can organize a parallel trajectory into a prefix-tree (trie), flatten it into a
single sequence, and apply an ancestor-only attention mask during training (not
inference!). Figure 10: Building the Prefix-tree and Flattening into a single training
sequence Specifically, we apply masking and position IDs to mimic the inference
behavior, such that each thread is only conditioned on the prompt+subtasks, without ever
attending to sibling threads or the final conclusion. The engine-agnostic design makes
adoption easy since you don’t need to figure out a separate hosting method and can
leverage existing hardware infra. It also gets better as existing inference engines get
better. What’s more, with an engine-agnostic method, we can serve a hybrid model that
switches between sequential and parallel thinking modes easily. Training Models to Use
Parallelism Once the inference path exists, the next problem is teaching a model to use
it. Demonstrations are needed because the model must learn to output special tokens that
orchestrate control flow. We found the instruction-following capabilities of base models
insufficient for generating parallel threads. An interesting question here is: does SFT
training induce a fundamental reasoning capability for parallel execution that was
previously absent, or does it merely align the model’s existing pre-trained capabilities
to a specific control-flow token syntax. Typical wisdom is SFT teaches new knowledge;
but contrary to common belief, some papers—notably Parallel-R1 ( Zheng et al., 2025 )
and NPR ( Wu et al., 2025 )—argue that their SFT demonstrations simply induce format
following (i.e., how to structure parallel requests). We leave this as future work.
Figure 11: Sources of Parallelization Demonstration Data Demonstrations teach the syntax
of parallel control flow, but they do not fully solve the incentive problem. In an ideal
world, we only need to reward the outcome accuracy, and the parallelization pattern
emerges naturally given that it learns to output special tokens through SFT, similar to
the emergence of long CoT. However, researchers ( Zheng et al., 2025 ) observed that
this is not enough, and we do in fact need parallelization incentives. The question then
becomes, how do we tell when the model is parallelizing effectively? Structure-only
rewards are too easy to game. Naively, we can give a reward for the number of threads
spawned. But models can spawn many short, useless threads to hack the reward. Okay, that
doesn’t work. How about a binary reward for simply using parallel structure correctly?
This partially solves the issue of models spamming new threads, but models still learn
to spawn threads when they don’t need to. The authors of Parallel-R1 ( Zheng et al.,
2025 ) introduced an alternating-schedule, only rewarding parallel structure 20% of the
time, which successfully increased the use of parallel structure (13.6% → 63%), but had
little impact on overall accuracy. With this structure-only approach, we might be
drifting away from our original goal of increasing accuracy and reducing latency… How
can we optimize for the Pareto frontier directly? Accuracy is simple — we just look at
the outcome. How about latency? Efficiency rewards need to track the critical path. In
sequential-only trajectories, we can measure latency based on the total number of tokens
generated. To extend this to parallel trajectories, we can focus on the critical path,
or the longest sequence of tokens that are causally dependent, as this directly
determines our end-to-end generation time (i.e., wall-clock time). As an example, when
there are two <Parallel> sections with five threads each, the critical path will go
through the longest thread from the first parallel section, then any sequential tokens,
then the longest thread from the second parallel section, and so on until the end of
sequence. Figure 12: Critical Path Length Illustration The goal is to minimize the
length of the critical path. Simultaneously, we would still like the model to be
spending tokens exploring threads in parallel. To combine the two objectives, we can
focus on making the critical path a smaller fraction of the total tokens spent. Authors
of ThreadWeaver ( Lian et al., 2025 ) framed the parallelization reward as $1 -
L_{\mathrm{critical}} / L_{\mathrm{total}}$, which is 0 for a sequential trajectory, and
increases linearly as the critical path gets smaller compared to the total tokens
generated. Parallel efficiency should be gated by correctness. Intuitively, when
multiple trajectories are correct we should assign more reward to the trajectories that
are more efficient at parallelization. But how about when they are all incorrect? Should
we assign any reward at all? Probably not. To formalize this, $R =
R_{\mathrm{correctness}} + R_{\mathrm{parallel}}$. Assuming binary outcome correctness,
this can be written as $R = \mathbf{1}(\text{Correctness}) +
\mathbf{1}(\text{Correctness}) \times (\text{some parallelization metric})$. This way, a
model only gets a parallelization reward when it answers correctly, since we don’t want
to pose parallelization constraints on the model if it couldn’t answer the question
correctly. Figure 13: Differences in Reward Designs Across Adaptive Parallel Reasoning
Works Evaluation and Open Questions When all is said and done, how well do these
adaptive parallel methods actually perform? Well…this is a hard question, as they differ
in model choice and metrics. The model selection depends on the training method, SFT
problem difficulty, and sequence length. When running SFT on difficult datasets like
s1k, which contains graduate-level math and science problems, researchers chose a large
base model (Qwen2.5 32B for Multiverse ( Yang et al., 2025 )) to capture the complex
reasoning structure behind the solution trajectories. When running RL, researchers chose
a small, non-CoT, instruct model (4B, 8B) due to compute cost constraints. Figure 14:
Difference in Model Choice Across Adaptive Parallel Reasoning Papers Each paper also
offers a slightly different interpretation about how adaptive parallel reasoning
contributes to the research field. They optimize for different theoretical objectives,
so they use slightly different sets of metrics: Multiverse and ThreadWeaver ( Yang et
al., 2025 ; Lian et al., 2025 ) aim to deliver sequential-AR-model-level accuracy at
faster speeds. Multiverse shows that APR models can achieve higher accuracy under the
same fixed context window, while ThreadWeaver shows that the APR model achieves shorter
end-to-end token latency (critical path length) while getting comparable accuracy. NPR (
Wu et al., 2025 ) treats sequential fallback as a failure mode and optimizes for 100%
Genuine Parallelism Rate, measured as the ratio of parallel tokens to total tokens.
Parallel-R1 ( Zheng et al., 2025 ) does not focus on end-to-end latency and instead
optimizes for exploration diversity, presenting APR as a form of mid-training
exploration scaffold that provides a performance boost after RL. Open Questions While
Adaptive Parallel Reasoning represents a promising step toward more efficient inference-
time scaling, significant open questions remain. As noted above, Parallel-R1 ( Zheng et
al., 2025 ) presents APR as a form of mid-training exploration scaffold rather than a
primarily inference-time technique. This invites a more fundamental question: Does
parallelization at inference-time consistently improve accuracy, or is it primarily
valuable as a training-time exploration scaffold? Parallel-R1 suggests that the
diversity induced by parallel structure during RL may matter more than the
parallelization itself at test time. A related concern is stability. There’s also a
persistent tendency for models to collapse back to sequential reasoning when
parallelization rewards are relaxed. Parallel-R1 authors showed that removing
parallelization reward after 200 steps results in the model reverting to sequential
behavior. Is this a training stability issue, a reward signal design issue, or evidence
that parallel structure genuinely conflicts with how autoregressive pretraining shapes
the model’s prior? Beyond whether APR works, deployment introduces its own questions.
Can we design training methods that account for available compute budget at inference
time, so parallelization decisions are hardware-aware rather than purely problem-driven?
Finally, the parallel structures considered above are essentially flat. What if we allow
parallelization depth > 1? Recursive language models (RLMs; Zhang, Kraska and Khattab,
2026 ) effectively manage long context and show promising inference-time scaling
capabilities. How well do RLMs perform when trained with end-to-end RL that incentivizes
adaptive parallelization? Acknowledgements We thank Nicholas Tomlin and Alane Suhr for
providing us with helpful feedback. We thank Christopher Park, Karl Vilhelmsson, Nyx
Iskandar , Georgia Zhou, Kaival Shah , and Jyoti Rani for their insightful suggestions.
We thank Vijay Kethana , Jaewon Chang , Cameron Jordan , Syrielle Montariol , Erran Li,
and Anya Ji for their valuable discussions. We thank Jiayi Pan , Xiuyu Li , and Alex
Zhang for their constructive correspondences about Adaptive Parallel Reasoning and
Recursive Language Models.

## 来源

- Source: Berkeley BAIR Blog
- URL: http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/

- Published: Fri, 08 May 2026 02:00:00 -0700

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
