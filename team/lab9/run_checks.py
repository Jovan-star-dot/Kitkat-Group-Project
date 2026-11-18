#!/usr/bin/env python3
"""Verify recorded classroom outputs and frozen scaffold. Does not invoke a model."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[2]
TEAM=ROOT/'team/lab9'
SC=ROOT/'MASY1800_ET_Agent_Scaffold_v1_0'
AG=SC/'agents/landscape_agent'
CASES=('primary','contrast_1','weak_evidence')
SLOTS=('creation_agent','innovation_classification_agent','promethean_classification_agent','diffusion_agent','adoption_agent','organizational_adoption_agent','landscape_agent')
def read(path):
    return json.loads(path.read_text())
input_validator=Draft202012Validator(read(SC/'core/input_schema.json'))
output_validator=Draft202012Validator(read(SC/'core/output_schema.json'))
def command(*args):
    run=subprocess.run([sys.executable,*map(str,args)],cwd=SC,capture_output=True,text=True,check=True)
    return run.stdout.strip()
def check(ok, label):
    if not ok:
        raise AssertionError(label)
    print('PASS:',label)
def normalized(s):
    return s.lower()
def each_has(text,*tokens):
    return all(token in normalized(text) for token in tokens)
print(command('tools/check_frozen_core.py'))
responses={}
cases={}
source_ids=[s['id'] for s in read(TEAM/'source_register.json')]
assert len(set(source_ids))==len(source_ids)
with TemporaryDirectory() as temp:
    for name in CASES:
        c=AG/'cases'/f'{name}.json'
        p=AG/'responses'/f'{name}_response.json'
        cases[name]=read(c)
        responses[name]=read(p)
        input_validator.validate(cases[name])
        output_validator.validate(responses[name])
        check(command('tools/validate_response.py',p)=='VALIDATION PASSED',f'{name}: official validator plus full input/output schema')
        built=Path(temp)/f'{name}.txt'
        command('tools/build_prompt.py','--agent',AG,'--case',c,'--out',built)
        check(built.read_bytes()==(TEAM/'prompts'/f'{name}.txt').read_bytes(),f'{name}: exact composed prompt reproducible')
        check(responses[name]['agent']==read(AG/'agent_metadata.json'),f'{name}: canonical agent identity and version')
        evidence=responses[name]['evidence']
        ids=[e['claim'].split()[0] for e in evidence if e['claim'].split()[0] in source_ids]
        check(len(ids)==len(set(ids)) and {'S1','S2','S3'}<=set(ids),f'{name}: source origin retained without duplicates')
        check(len(responses[name]['change_monitoring_triggers'])>=3 and all('reopen' in v.lower() or 'pause' in v.lower() for v in responses[name]['change_monitoring_triggers']),f'{name}: explicit monitoring consequences')
p,c,w=(responses[k] for k in CASES)
check(all(cases['primary'][k]==cases['contrast_1'][k] for k in ('emerging_technology','organization','industry_sector','time_horizon','additional_context')), 'controlled contrast: identical technology, organization, horizon and evidence cut')
check(p['general_et_finding']==c['general_et_finding']==w['general_et_finding'],'general finding stays stable across both contrasts')
check(each_has(p['application_finding'],'fixed order','carrier','exception') and each_has(c['application_finding'],'keyword search','curated faq','provenance'),'strongest conventional comparator changes with application')
check(each_has(' '.join(p['change_monitoring_triggers']),'ticket','timestamp') and each_has(' '.join(c['change_monitoring_triggers']),'handbook','citation','permission'),'application monitoring shifts from delivery evidence to handbook controls')
check(p['application_finding']==w['application_finding'] and p['organization_specific_finding']==w['organization_specific_finding'] and 'keep p1 unchanged' in w['recommendation_management_implication'].lower(),'weak evidence does not upgrade position')
check(each_has(' '.join(w['contrary_evidence_or_limitations']),'25% time reduction is an unsupported gate','s1 reports expectation','not corroboration'),'constructed false adoption claim and invented numerical gate explicitly rejected')
bad=dict(p,landscape_score=100)
check(not output_validator.is_valid(bad),'negative schema control: extra landscape_score rejected')
for slot in SLOTS:
    ag=SC/'agents'/slot
    m=read(ag/'agent_metadata.json')
    out=read(ag/'responses/primary_response.json')
    output_validator.validate(out)
    check(out['agent']==m,f'interface smoke audit: {slot} ({m["version"]})')
print('SUMMARY: 3 Landscape cases and 7 representative specialist contracts passed; frozen core intact. No orchestrator execution.')
