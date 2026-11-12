# FN—001 | Research Note

## The Safety Evaluation Gap

**Series:** The Frontier Notes  
**Investigation:** FN—001  
**Status:** Research design and methodology development  
**Research type:** Independent investigation  
**Version:** 0.1

---

## 1. Abstract

Safety evaluations provide evidence about how AI systems behave under particular testing conditions. However, evaluation performance may not fully represent behavior across scenarios that differ from those used during testing.

FN—001 investigates how reliably safety evaluation performance generalizes to held-out scenarios that differ from original evaluation conditions.

The investigation examines scenario selection, prompt variation, and evaluation reliability. It builds on existing research on safety generalization and benchmark robustness.

This note documents the research question, proposed methodology, evaluation framework, and limitations. No experimental findings are presented at this stage.

---

## 2. Research Question

**How reliably does safety evaluation performance generalize to held-out scenarios that differ from original evaluation conditions?**

### Supporting Questions

- How sensitive are measured safety outcomes to changes in prompt wording?
- How does performance on original scenarios compare with performance on held-out scenarios?
- What limitations arise when safety conclusions rely on a fixed set of evaluation scenarios?
- How should evaluation results communicate uncertainty and generalization limitations?

---

## 3. Motivation

Safety evaluation results are often interpreted as evidence about an AI system's behavior.

However, an evaluation measures behavior under defined conditions. Scenario selection, wording, task structure, and evaluation methodology may influence the resulting measurements.

This creates an important distinction:

**Performance on an evaluation set is not necessarily equivalent to performance across unfamiliar scenarios.**

Existing research has examined safety generalization, prompt sensitivity, and benchmark reliability. FN—001 builds on this literature to investigate the relationship between evaluation conditions and measured safety performance.

---

## 4. Investigation Framework

The proposed investigation considers three evaluation conditions.

### 4.1 Baseline

Original evaluation scenarios provide the reference condition.

Purpose:
- Establish baseline measured performance.
- Document scenario characteristics.
- Record evaluation assumptions.

### 4.2 Paraphrase

Semantically similar scenarios are expressed using alternative wording while preserving the intended underlying task.

Purpose:
- Examine sensitivity to wording.
- Identify inconsistencies across equivalent scenario formulations.
- Distinguish linguistic variation from changes in task meaning.

### 4.3 Held-Out Scenarios

Scenarios excluded from the original evaluation set are used to examine behavior beyond the baseline examples.

Purpose:
- Examine generalization beyond original scenarios.
- Identify differences between original and held-out evaluation performance.
- Assess the limitations of conclusions drawn from a fixed evaluation set.

Held-out scenarios must be defined carefully to avoid accidental overlap with baseline examples.

---

## 5. Proposed Methodology

The methodology remains under development.

The proposed workflow is:

1. Review relevant safety evaluation and generalization literature.
2. Define the evaluation scope and scenario inclusion criteria.
3. Develop a documented scenario-generation and selection process.
4. Establish baseline, paraphrase, and held-out conditions.
5. Define safety outcome categories and scoring criteria.
6. Select an appropriate model and evaluation configuration.
7. Conduct controlled evaluation runs.
8. Analyze differences across evaluation conditions.
9. Document uncertainty, limitations, and reproducibility requirements.

The final methodology will specify the model configuration, data sources, scenario construction, evaluation procedures, and scoring rules before experiments begin.

---

## 6. Proposed Measurements

Potential measurements include:

| Measurement | Purpose |
|---|---|
| Safety outcome rate | Estimate observed safety behavior under each condition |
| Condition-level differences | Compare baseline, paraphrase, and held-out outcomes |
| Scenario consistency | Examine variation across equivalent scenario formulations |
| Evaluator agreement | Assess consistency in outcome classification |
| Uncertainty | Communicate limitations of observed measurements |

These measurements are provisional. Final metrics and scoring criteria will be established during methodology development.

---

## 7. Threats to Validity

The investigation must account for:

- **Scenario selection bias:** Selected scenarios may not represent the broader space of relevant behavior.
- **Semantic inconsistency:** Paraphrases may unintentionally change the underlying task.
- **Contamination:** Held-out scenarios may overlap with original examples or model training data.
- **Evaluator reliability:** Outcome classification may introduce measurement error.
- **Model configuration:** Changes in system instructions, model versions, or settings may affect comparability.
- **Limited scope:** Results from a particular model or scenario set may not generalize universally.

These limitations will inform interpretation of any experimental findings.

---

## 8. Research Integrity

The following distinctions are maintained throughout FN—001:

- Literature findings are attributed to their original sources.
- Proposed methodology is distinguished from completed methodology.
- Synthetic examples are not presented as empirical evaluation data.
- Code scaffolds are not described as validated safety evaluators.
- Experimental findings are reported only after evaluation has been conducted.
- Novelty claims are withheld until supported by systematic literature review.

---

## 9. Current Status

| Component | Status |
|---|---|
| Research question | Defined |
| Initial literature review | Completed |
| Investigation framing | Documented |
| Methodology | In development |
| Evaluation implementation | Initial scaffold |
| Experimental evaluation | Not started |
| Findings | Not available |

---

## 10. Next Steps

1. Refine the evaluation methodology.
2. Define scenario construction and validation criteria.
3. Establish the evaluation configuration.
4. Implement the evaluation pipeline.
5. Conduct initial controlled experiments.
6. Analyze results and document limitations.

---

## 11. References

See [Literature Review](literature_review.md) for the reviewed literature, supporting evidence, and research positioning.

---

*The Frontier Notes — Building a deeper understanding of AI systems through research.*
