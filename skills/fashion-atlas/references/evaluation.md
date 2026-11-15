# Evaluation before claiming improvement

Use a held-out set of owner-approved and owner-rejected references; preserve stated rejection reasons. Evaluate top-k precision for visual cues, duplicate-owned error rate, false-stock/false-price claims, complete-outfit coverage and unsupported generated-detail rate. Record sample size and source access limits. Synthetic tests are data invariants only, not a live fashion benchmark.

Required counterexamples:
1. Liked but already owned → do not lower taste rating.
2. Black baggy pants without distinctive construction → not a strong structural analogue.
3. Beautiful piece above all-in cap → no buy recommendation.
4. Online in-stock but branch unknown → no reserved/pickup claim.
5. Cropped reference photo → no measured full-body fit claim.
6. Sale garment cannot be exchanged → disclose before decision.
7. Two agents repeat one source → one evidence source, not two independent proofs.
8. Belt variant → same outfit/pose/shoes so comparison isolates belt effect.

Only assert a successful integration after actual execution with traces/outputs. This repository provides a workflow, not autonomous shopping infrastructure.
