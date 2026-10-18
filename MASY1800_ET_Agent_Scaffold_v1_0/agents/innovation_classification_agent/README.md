# KitKat Innovation Classification Agent — Team Lab 4

Team-approved SubAgent 2, version **1.0-team**, approval reported by Jovan Diaz on behalf of KitKat on October 18, 2026. Five source designs contribute to the synthesis; Jie Zhu's revised design is the base.

Purpose: classify invention, innovation, entrepreneurship/commercialization and incremental/breakthrough change while separating technology evidence from organizational significance. It is not the adoption, Promethean or governance decision-maker.

Files: `specialist_instructions.md`, `classification_criteria.md`, `agent_metadata.json`, three common `cases/`, saved `responses/`, and `records/agent_record.md`. Complete lineage, evidence, preserved failure, acceptance and execution logs are in repository `team/lab4/`.

From the scaffold directory:

```sh
python tools/build_prompt.py --agent agents/innovation_classification_agent --case agents/innovation_classification_agent/cases/primary.json
python tools/validate_response.py agents/innovation_classification_agent/responses/primary_response.json
python tools/check_frozen_core.py
```

Build and review each of primary, contrast_1 and borderline. The builder creates a prompt packet, not a model call. The submitted responses were produced interactively by ChatGPT/Codex on October 18, 2026, with public source checks, then saved and validated. No separate inference endpoint, live company system or business experiment was run. See `team/lab4/run_checks.py` for reproducible saved-output checks and their limits.

Integration warning: do not convert local novelty, an autonomy label or a conditional high-impact scenario into a global invention claim, a breakthrough finding, an adoption recommendation or realized business value. These retail cases are illustrative, not the project's permanent sector.
