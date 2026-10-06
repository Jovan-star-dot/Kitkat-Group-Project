# KitKat Creation Agent
Version 0.2-team, Team Lab 3. Jovan-authorized integration; team human review unrecorded.
Run from MASY1800_ET_Agent_Scaffold_v1_0:
```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/creation_agent --case agents/creation_agent/cases/primary.json --out work/creation_agent_primary_prompt.txt
python3 tools/build_prompt.py --agent agents/creation_agent --case agents/creation_agent/cases/contrast_1.json --out work/creation_agent_contrast_1_prompt.txt
python3 tools/validate_response.py agents/creation_agent/responses/primary_response.json
python3 tools/validate_response.py agents/creation_agent/responses/contrast_1_response.json
```
Prompt building does not execute the model. Submit the packet in the course-approved
interactive model, save each new JSON response under a new versioned name, validate,
and review the reasoning. Saved test outputs are from the documented October 6 session.
The fields remain those of the frozen output contract. See records/agent_record.md
and ../../.. /team/lab3/ (repository-root team/lab3) for evidence and comparison.
