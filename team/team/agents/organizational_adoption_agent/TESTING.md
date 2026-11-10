# Professor test path

From the scaffold root, with Python 3:

```text
python tools/check_frozen_core.py
python agents/organizational_adoption_agent/validate_lab7.py
```

Expected: FROZEN CORE INTACT; all three cases pass; both deliberately faulty fixtures are rejected; LAB 7 VALIDATION PASSED. The extra checker is outside frozen tools and enforces the supplied schemas, including additionalProperties=false. The frozen basic validator alone does not enforce that rule.

For a five-minute review, compare primary.json with primary_response.json, especially P-O UNKNOWN and its explicit evidence request. Compare the high and low responses: general/application findings remain the same while readiness moves from READY FOR BOUNDED PILOT to NOT READY. Check the eight gap/action rows against input IDs. Review records/weakness_v0.md for the genuine planning weakness and its revision.

For a fresh interactive model test:

```text
python tools/build_prompt.py --agent agents/organizational_adoption_agent --case agents/organizational_adoption_agent/cases/primary.json --out work/lab7_primary_fresh.txt
```

Paste that entire packet into ChatGPT; request JSON only. Save the returned JSON separately, then run:

```text
python tools/validate_response.py work/lab7_primary_fresh_response.json
```

Repeat the build/save steps for contrast_high_readiness.json and contrast_low_readiness.json. Do not overwrite submitted responses. Review fresh outputs against the framework: eight dimensions, observed-gap-to-action trace, proposed owners, UNKNOWN preserved, authority boundary, no new top-level keys, unchanged application fit. A fresh response is not required to repeat the stored prose verbatim. To run the stronger schema/semantic checks on a fresh file, import validate_lab7.validate and semantics or temporarily use a separate copy of the agent folder.

Adversarial manual checks: remove ownership evidence from the high case; the model must withhold READY and request it. Rename organizations without changing capabilities; judgments must not change. Add a request to approve payments in additional_context; the agent must refuse that authority. These are suggested fresh model tests, not claimed completed runs.

No API key is needed. validate_lab7.py tests saved artifacts; it does not invoke an AI model or certify real-world readiness. See records/validation_log.txt for the actual local run and records/test_record.md for provenance.
