# Team repository setup

This is Raphael's Lab 6 / SubAgent 5 contribution, alongside the earlier Diffusion and Promethean contributions on `raphael-synthesize-agent`.

Source: https://github.com/rap-hernando/MASY1800-Emerging-Technologies-Agents/commit/d3957f68767389ebffdf1b98ae99803a18c0837f

The original release record and Agent Record retain the personal source provenance. Only README and TEAM_HANDOFF were adapted for this team location; this setup guide was added. All analytical instructions, cases, responses, validators and the DOCX are unchanged.

## Run from a team checkout

The existing team scaffold is `MASY1800_ET_Agent_Scaffold_v1_0`. The contribution folder is outside it, so first copy this agent into a working copy of that scaffold. From the repository root, with Python installed:

```text
python -c "import shutil; shutil.copytree('team/team/agents/adoption_agent', 'MASY1800_ET_Agent_Scaffold_v1_0/agents/adoption_agent')"
cd MASY1800_ET_Agent_Scaffold_v1_0
python tools/check_frozen_core.py
python agents/adoption_agent/check_package.py
```

The copy intentionally refuses to overwrite an existing destination. If that agent folder already exists, use a clean checkout or compare it before proceeding. No core files need changing. Expected results: FROZEN CORE INTACT and PACKAGE CHECKS PASSED; the preserved v0 is an EXPECTED FAIL.

Continue with `agents/adoption_agent/TESTING.md` for the exact fresh ChatGPT test path. Alternatively, open the saved prompt packets and responses directly in this contribution folder for review.

## Decision for synthesis

BOUNDED EXPERIMENT for the illustrative mid-sized 3PL freight-invoice reconciliation case. Local comparative reliability and total-cost evidence are missing. No payment authority is granted. Organizational ownership, reviewer capacity and change readiness pass to the later Organizational Adoption Agent.

Self-reflection, student endorsement and the actual Brightspace rubric check remain before final submission. The push is a team handoff, not a claim that those steps are complete.
