
# FN—001 | Literature Review

## 1. Purpose

This review examines existing research on safety evaluation, robustness, and generalization in large language models.

Its purpose is to establish what is already known, identify methodological limitations, and determine whether FN—001 can contribute a meaningful empirical investigation.

## 2. Research Areas

The review focuses on:

- Safety evaluation benchmarks.
- Generalization of safety behavior.
- Robustness to prompt transformations.
- Evaluation reliability.
- Held-out scenario testing.
- Limitations of benchmark-based conclusions.

## 3. Initial Papers

### Paper 1 — SAGE-Eval

**Title:** SAGE-Eval: Evaluating LLMs for Systematic Generalizations of Safety Facts

**Venue:** NeurIPS 2025

**Link:** https://papers.neurips.cc/paper_files/paper/2025/hash/75a5df8d390c51d6aebfa2accb3f4911-Abstract-Datasets_and_Benchmarks_Track.html

**Research focus:**

Evaluates whether language models generalize established safety facts to novel situations.

**Relevance to FN—001:**

Provides a reference point for evaluating generalization of safety-relevant behavior beyond familiar formulations.

**Questions for review:**

- How are safety facts selected?
- How are novel scenarios constructed?
- What constitutes successful generalization?
- What limitations do the authors identify?

### Paper 2 — SG-Bench

**Title:** SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types

**Venue:** NeurIPS 2024

**Link:** https://proceedings.neurips.cc/paper_files/paper/2024/hash/de7b99107c53e60257c727dc73daf1d1-Abstract-Datasets_and_Benchmarks_Track.html

**Research focus:**

Evaluates safety generalization across tasks and prompt types.

**Relevance to FN—001:**

Provides existing methodologies for examining safety behavior under different evaluation conditions.

**Questions for review:**

- Which evaluation conditions are varied?
- How are safety outcomes measured?
- How does the benchmark distinguish different forms of generalization?
- What limitations remain?

### Paper 3 — Benchmark Robustness

**Title:** On Robustness and Reliability of Benchmark-Based Evaluation of LLMs

**Link:** https://arxiv.org/abs/2509.04013

**Research focus:**

Investigates changes in benchmark performance under paraphrased questions and implications for evaluation reliability.

**Relevance to FN—001:**

Provides a methodological reference for testing whether evaluation outcomes remain stable under linguistic variation.

**Questions for review:**

- How are paraphrases generated and validated?
- Which performance metrics are used?
- How are changes in absolute performance distinguished from changes in model rankings?
- What implications are drawn for benchmark reliability?

## 4. Preliminary Synthesis

The initial literature indicates that:

1. Safety generalization is already being studied directly.
2. Evaluation outcomes can be sensitive to changes in prompts and tasks.
3. Benchmark performance should not automatically be interpreted as evidence of universal behavioral reliability.
4. Existing benchmarks provide useful methodological foundations for further investigation.

These observations are preliminary and must be supported by a fuller review.

## 5. Research Gap Assessment

No novel contribution is claimed at this stage.

The next step is to compare existing evaluation approaches and identify a narrower question that can be investigated reproducibly.

Potential directions include:

- Comparing different scenario transformation methods.
- Examining how scenario difficulty affects measured generalization.
- Investigating evaluator agreement under transformed scenarios.
- Studying the reliability of specific safety evaluation metrics.

## 6. Review Status


## 7. Evidence Extracted from Initial Papers

### SAGE-Eval

**Source:** Chen, Davidson, and Lake — NeurIPS 2025.

**Method:**
- 104 safety facts sourced from reputable organizations.
- 10,428 systematically constructed scenarios.
- Seven common domains.
- Evaluation of models on applying safety facts to unfamiliar situations.

**Reported finding:**
The strongest evaluated model, Claude 3.7 Sonnet, passed 58% of the safety facts tested.

**Implication:**
Safety behavior may fail to generalize even when the relevant safety facts are established.

**Source:** https://arxiv.org/abs/2505.21828

### SG-Bench

**Source:** Mou, Zhang, and Ye — NeurIPS 2024.

**Method:**
- Combines generative and discriminative evaluation.
- Examines diverse tasks and prompt types.
- Evaluates proprietary and open-source models.

**Reported finding:**
The authors report differences across task types and susceptibility to prompting variations.

**Implication:**
Safety evaluation results depend partly on the evaluation task and prompting conditions.

**Source:** https://arxiv.org/abs/2410.21965

### Benchmark Robustness Study

**Source:** Lunardi et al. — ECAI 2025.

**Method:**
- Six common capability benchmarks.
- Thirty-four language models.
- Systematic paraphrasing of benchmark questions.

**Reported finding:**
Absolute performance scores declined under paraphrasing, while model rankings remained relatively stable.

**Important distinction:**
This study examines general capability benchmarks rather than directly measuring safety behavior.

**Implication:**
Linguistic robustness is a relevant evaluation concern, but its findings should not automatically be transferred to safety benchmarks.

**Source:** https://arxiv.org/abs/2509.04013

## 8. Preliminary Research Assessment

Existing research already addresses:
- Safety generalization across scenarios.
- Safety generalization across task types.
- Sensitivity to prompting conditions.
- Benchmark robustness under paraphrasing.

Therefore, FN—001 requires a more specific experimental contribution.

A potential direction is investigating how the method used to generate evaluation variants affects measured safety performance, while controlling semantic equivalence and scenario difficulty.

This direction remains provisional pending deeper review.


**Status:** Initial paper identification.

**Next:** Read the papers, extract their methodologies and limitations, and refine FN—001.

