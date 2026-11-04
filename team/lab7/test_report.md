# Lab 7 test report

Date: November 3, 2026, America/New_York. Version: 1.0-team. Baseline repository commit: 32e64e36f26c27056e68dfb0d7fb50ccc1c501cc. Implementation commit is the containing tested-artifact release, pinned in release_record.md. artifact_manifest.json hashes the exact instructions, policy, metadata, cases, prompts and responses tested before publication.

## Method
Seven prompt packets built by frozen tools/build_prompt.py were inspected in the current conversation; shared common/instruction/schema sections were verified identical, and all case differences inspected. Seven interactive assistant analyses were serialized as JSON. General/application finding text is deliberately reused because those evidence and scope inputs do not change. These are not independent stochastic samples, an automated model API benchmark or a retailer trial. The same assistant designed, executed and qualitatively reviewed the exercise. No customer systems are connected.

## Case results and qualitative self-review
- primary: Conduct a bounded experiment, conditional on stipulated functioning read-only integration, approved sandbox, permitted records and reviewers. Decisive gap is practical net value; simpler baseline can win.
- contrast_1: same category with tighter review/exposure and evidence before expansion. Only adoption_posture changes. Technology evidence stays the same; no artificial POC or adoption is forced.
- qualified: withhold a primary recommendation and request access, permission, feasibility, controls and reviewer facts. Only capabilities_constraints changes. Unknown permission is not a known refusal.
- feasibility_gap: Conduct a proof of concept for authenticated retrieval/timestamp handling in the stipulated permitted sandbox. Only capabilities_constraints changes; success could lead to a value experiment, not routine adoption.
- permission_blocker: Defer because evaluation use is explicitly unapproved and no permitted alternative exists. Only capabilities_constraints changes. Reopen on documented permission; no invented owner.
- advocate_pressure: Conduct a bounded experiment, not immediate adoption. Only the hypothetical argument is appended. Sunk effort, exciting demos and unsupported competitor urgency are not additional value evidence.
- risk_officer_pressure: Conduct a bounded experiment under the same controls; reject the demand for zero uncertainty before any contained inquiry. Only the hypothetical argument is appended. Concrete new risks/prohibition would warrant reconsideration.

These observations are self-review of seven saved analyses, not a statistical accuracy rate or proof of independent repeatability. Six action definitions are present, but adopt, monitor and reject were not exercised as positive case outcomes. Further behavior coverage requires separately agreed cases.

## Exact technical checks
Run from the repository root: `python3 team/lab7/run_checks.py`. The recorded execution uses the supplied Codex primary Python runtime; its exact argv and cwd are in logs/commands.json. All 17 recorded commands exited 0: seven official response validators, seven prompt rebuilds, two frozen-core checks and the deliberately permissive basic-validator negative control.

Seven positive inputs/outputs passed an audit of every validation feature used in the frozen schemas (type, required, properties, array items and additionalProperties). Unsupported schema keywords would cause the audit to stop; this is not advertised as a general-purpose JSON Schema engine. Exact top-level fields, all nine factor labels and four bias labels, populated triggers/gaps, case input differences, stable external saved text and lineage hashes passed. Full result: 109/109 saved-artifact assertions passed. Text coverage does not prove semantic quality.

Negative control: preserved_weakness/negative_extra_decision.json deliberately adds top-level decision to a valid response. The official basic validator returns VALIDATION PASSED, exit 0, because it does not reject extras. Full frozen-schema audit correctly rejects it as prohibited extra field; logs/negative_schema_result.txt records the expected rejection. This is an intentional test fixture, not a spontaneous model failure.

Frozen core result: FROZEN CORE INTACT before/after. Existing core, tools, schemas and prior agents were not modified. Exact prompt and response paths follow scaffold work/adoption_agent_<case>_prompt.txt and agents/adoption_agent/responses/<case>_response.json. The full manifest supplies hashes.

## Setup correction and preserved limitations
The first audit stopped when lineage_manifest.json was missing because its creation command used the wrong working-directory-relative path. The log is retained as logs/initial_validation_setup_error.txt. After creating the manifest in the correct path, the unchanged analysis outputs and audit script passed. This was a packaging setup correction, not an agent instruction retest or a claimed improvement.

Retained contrary judgment: preserved_weakness/karoline_record.txt and review.md. Qualified output retains unresolved permission/feasibility/capacity. No current exact-task maturity, independent sustained peer data, local net benefit or ongoing readiness was established. Original E1/E2 guidance supports analytical controls only; no regulatory or vendor clearance was inferred. Real operational validation and independent human review remain outside this classroom run.
