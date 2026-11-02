# Lab 6 SubAgent 5 Emerging Technology Adoption Agent

**Team repository setup:** This folder sits alongside Raphael's Diffusion and Promethean contributions. Read [TEAM_REPO_SETUP.md](TEAM_REPO_SETUP.md) before running local commands; the team's frozen scaffold lives elsewhere in this repository.

**Start here.** This specialist recommends whether a mid-sized 3PL should use agentic AI for freight-invoice reconciliation now. Primary conclusion: **BOUNDED EXPERIMENT**, restricted to offline evaluation with human review and no payment authority.

The scenario is illustrative. No actual freight operations or payments are performed by this package. This is the course's prompt-based specialist, not an invoice-processing application.

## Professor quick path

1. Open `TESTING.md`. From the scaffold root, run `python tools/check_frozen_core.py` and `python agents/adoption_agent/check_package.py`.
2. Read `responses/primary_response.json`, then compare the aggressive and conservative responses. General technology and application findings stay stable; exposure and timing change.
3. For a fresh model test, paste `prompts/primary_prompt.txt` into ChatGPT, save its JSON under this folder, and run the validator. Exact commands and acceptance criteria are in `TESTING.md`.

Python 3.10 or newer is recommended; no third-party packages or API key are required for these checks. If Windows uses the Python launcher, replace `python` with `py -3`.

## Where to look

- `specialist_instructions.md`: complete prompt-ready behavior and authority boundary.
- `decision_logic.md`: six categories, ordered gates, alternatives and reversal conditions.
- `cases/`, `prompts/`, `responses/`: four cases with reusable packets and representative outputs. `contrast_1` and `contrast_2` are compatibility aliases for aggressive and conservative inputs.
- `records/test_record.md`: scope of actual checks and reasoning review, plus remaining limits.
- `records/failures/`: preserved first candidate and its observed validation failure.
- `records/source_verification.md`: original sources and verification dates.
- `records/agent_record.md`: concise course record; formatted DOCX delivered in the package's `deliverables` folder.
- `TEAM_HANDOFF.md`: decision, decisive factor, reversal trigger and Organizational Adoption Agent question.

The frozen root README is unchanged. This agent README is the entry point for Lab 6. Read `SUBMISSION_CHECKLIST.md` before submitting: self-reflection, independent student endorsement and actual Brightspace rubric review remain outstanding.
