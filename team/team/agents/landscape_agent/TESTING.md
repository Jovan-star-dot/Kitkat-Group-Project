# TESTING — Professor Test Path

## Goal
Confirm that the specialist keeps the general Agentic AI landscape stable while changing application-relevant alternatives, risks, dependencies and monitoring signals when context changes.

## 1. Integrity
From the scaffold root:

`python tools/check_frozen_core.py`

Expected: `FROZEN CORE INTACT`.

## 2. Build prompt packets
- Primary: `python tools/build_prompt.py --agent agents/landscape_agent --case agents/landscape_agent/cases/primary.json`
- Marketing contrast: same command with `contrast_1.json`
- Bank contrast: same command with `contrast_2.json`

## 3. Validate saved representative outputs
- `python tools/validate_response.py agents/landscape_agent/responses/primary_response.json`
- `python tools/validate_response.py agents/landscape_agent/responses/contrast_1_response.json`
- `python tools/validate_response.py agents/landscape_agent/responses/contrast_2_response.json`

Expected: all three pass.

## 4. Context-sensitivity check
### Should stay stable
- Agentic AI capability/ecosystem is accelerating but uneven.
- Broad AI adoption must not be treated as agentic/application maturity.
- Interoperability standards are strengthening but do not prove workflow reliability.

### Should change
- **3PL:** strongest alternative = deterministic AP/document/rules workflow; monitor logistics peer deployments, ERP/TMS interoperability, economics, financial-control evidence.
- **Marketing:** strongest alternatives = standard LLM assistants and marketing automation; monitor workflow quality, cost, usability and vendor feature shifts.
- **Bank:** strongest alternatives = deterministic regulated workflows/RPA/supervised assistants; monitor identity/authorization, auditability, comparable regulated deployments and regulatory guidance.

## 5. Preserved failure
Read `records/weakness_v0.md`. The failed reasoning incorrectly used 88% overall AI adoption as proof that agentic freight-invoice autonomy is mainstream. The revision adds scope/source labels and incumbent-alternative comparison.

## 6. Freshness check
Before reuse after the submission date, recheck fast-moving adoption, standards, vendor/ecosystem and regulatory claims. The source ledger is dated 2026-11-16.
