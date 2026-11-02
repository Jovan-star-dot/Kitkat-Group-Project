# Professor Test Path

Run every command below from the extracted scaffold root, the directory containing `core`, `tools`, and `agents`. Python 3.10+ is recommended. No API key, network connection or package installation is needed for the saved-artifact checks.

## 1 Verify the frozen core and saved package

```text
python tools/check_frozen_core.py
python agents/adoption_agent/check_package.py
python tools/validate_response.py agents/adoption_agent/responses/primary_response.json
python tools/validate_response.py agents/adoption_agent/responses/contrast_aggressive_response.json
python tools/validate_response.py agents/adoption_agent/responses/contrast_conservative_response.json
python tools/validate_response.py agents/adoption_agent/responses/monitoring_response.json
```

Expected: `FROZEN CORE INTACT`, `PACKAGE CHECKS PASSED`, and four `VALIDATION PASSED` messages. The package checker prints `EXPECTED FAIL` for the deliberately preserved v0 candidate; this is a successful regression check, not a package failure. Its schema checker covers the types, required fields, properties, array items and closed-object rule used by the frozen schemas; it is not a general JSON Schema implementation.

## 2 Rebuild a primary packet and run a fresh model test

```text
python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json --out agents/adoption_agent/prompts/primary_prompt.txt
```

Open `agents/adoption_agent/prompts/primary_prompt.txt`, paste its entire contents into a new ChatGPT conversation, and request JSON only. Enable source verification if available; otherwise ask it to state that the embedded evidence was last verified November 2, 2026. Save the returned object without Markdown fences as `agents/adoption_agent/responses/primary_fresh_response.json`.

```text
python tools/validate_response.py agents/adoption_agent/responses/primary_fresh_response.json
python agents/adoption_agent/check_response.py agents/adoption_agent/responses/primary_fresh_response.json
```

Expected reasoning: bounded offline experiment; unknown local value; no payment authority; named evidence, owner, stop conditions and reversal conditions. Exact prose is not deterministic. This live step needs ChatGPT but no API key. The packaged responses were model-authored in the development Codex session; they are not claimed to be independent fresh-chat runs.

## 3 Test the posture contrast and missing evidence

Repeat step 2 with `contrast_aggressive`, `contrast_conservative`, then `monitoring` in the case and packet filenames. Save new responses with `_fresh_response.json` and run both validators on each.

| Case | Expected category | Contextual difference |
| --- | --- | --- |
| Primary | BOUNDED EXPERIMENT | Four-week offline comparison |
| Aggressive | BOUNDED EXPERIMENT | Earlier learning; conditional read-only shadow phase after offline gates |
| Conservative | PROOF OF CONCEPT | Isolated feasibility proof before any live shadow work |
| Monitoring | MONITOR | No lawful data/sandbox; monthly evidence review |

Technology and application findings should remain substantively stable for posture contrasts. Conservative proof requirements should change the management action. Aggressive appetite must not create unsupported maturity or payment authority. The monitoring response must explicitly ask for missing information. A different category can be defensible only with a documented case-grounded rationale and unchanged safeguards; review it rather than editing the input to force a pass.

## 4 Inspect the preserved failure and revision

```text
python tools/validate_response.py agents/adoption_agent/records/failures/v0_primary_response.json
python agents/adoption_agent/check_response.py agents/adoption_agent/records/failures/v0_primary_response.json
```

The first command passes because the frozen basic validator does not reject extra top-level properties. The second must exit with a failure for `decision`. Read `records/revision_log.md`: v1 moves the recommendation into the permitted string and adds traceable rationale, gates and monitoring. No frozen file was patched.

## What passing means

These checks establish contract compatibility, saved-case consistency and preservation of the core. They do not establish model reliability over repeated fresh runs, invoice accuracy, security, regulatory compliance, savings or organizational readiness. Use `records/test_record.md` for the distinction between model-authored examples, local checks and unperformed operational tests.
