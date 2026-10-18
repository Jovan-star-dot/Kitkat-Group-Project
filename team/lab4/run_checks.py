#!/usr/bin/env python3
"""Recheck saved Lab 4 artifacts, not model performance or semantic truth.
Run from any directory: python team/lab4/run_checks.py
"""
from pathlib import Path
import hashlib, json, subprocess, sys

repo=Path(__file__).resolve().parents[2]
scaffold=repo/'MASY1800_ET_Agent_Scaffold_v1_0'
agent=scaffold/'agents/innovation_classification_agent'
here=Path(__file__).resolve().parent
lines=[]
def note(s): print(s);lines.append(s)
def command(args):
    display=['python',*args]
    r=subprocess.run([sys.executable,*args],cwd=scaffold,text=True,capture_output=True)
    note('$ '+' '.join(display));note((r.stdout+r.stderr).strip());note('exit='+str(r.returncode))
    if r.returncode: raise RuntimeError('Command failed')

# Both frozen schemas use only these validation keywords. Reject unsupported
# validation keywords instead of silently purporting to implement full JSON Schema.
allowed={'$schema','title','type','required','properties','additionalProperties','items'}
types={'object':dict,'array':list,'string':str}
def audit_schema(schema):
    assert not set(schema)-allowed, 'Unsupported schema keyword'
    assert schema.get('type') in types, 'Unsupported schema type'
    for child in schema.get('properties',{}).values(): audit_schema(child)
    if 'items' in schema: audit_schema(schema['items'])
def validate(value,schema,path='$'):
    assert isinstance(value,types[schema['type']]), path+': wrong type'
    if isinstance(value,dict):
        assert not set(schema.get('required',[]))-set(value),path+': missing required field'
        if schema.get('additionalProperties') is False:
            assert not set(value)-set(schema.get('properties',{})),path+': additional field'
        for k,child in schema.get('properties',{}).items():
            if k in value: validate(value[k],child,path+'.'+k)
    if isinstance(value,list) and 'items' in schema:
        for i,item in enumerate(value): validate(item,schema['items'],path+f'[{i}]')

def main():
    command(['tools/check_frozen_core.py'])
    ins=json.loads((scaffold/'core/input_schema.json').read_text())
    outs=json.loads((scaffold/'core/output_schema.json').read_text())
    audit_schema(ins);audit_schema(outs)
    cases={};responses={}
    for name in ('primary','contrast_1','borderline'):
        case=json.loads((agent/f'cases/{name}.json').read_text())
        response=json.loads((agent/f'responses/{name}_response.json').read_text())
        validate(case,ins);note(f'INPUT SCHEMA AUDIT PASSED: {name}')
        command(['tools/validate_response.py',f'agents/innovation_classification_agent/responses/{name}_response.json'])
        validate(response,outs);note(f'OUTPUT SCHEMA AUDIT PASSED: {name}')
        cases[name]=case;responses[name]=response
    delta={k for k in cases['primary'] if cases['primary'][k]!=cases['contrast_1'][k]}
    assert delta=={'organization','capabilities_constraints'},delta
    note('CONTEXT CONTRAST PASSED: only organization and capabilities_constraints differ')
    assert responses['primary']['general_et_finding']==responses['contrast_1']['general_et_finding']
    note('SAVED GENERAL-FINDING INVARIANCE PASSED (interactive paired run; not blind robustness evidence)')
    assert responses['primary']['organization_specific_finding']!=responses['contrast_1']['organization_specific_finding']
    note('ORGANIZATION FINDING DIFFERS: semantic adequacy reviewed separately in test_report.md')
    for entry in json.loads((here/'lineage_manifest.json').read_text()):
        assert hashlib.sha256((here/entry['path']).read_bytes()).hexdigest()==entry['sha256'],entry['path']
    note('LINEAGE SNAPSHOT DIGESTS PASSED')
    command(['tools/check_frozen_core.py'])
    note('ALL SAVED-ARTIFACT CHECKS PASSED')

try:
    main()
except Exception as exc:
    note('FAILED: '+str(exc));(here/'logs/validation_results.txt').write_text('\n'.join(lines)+'\n');raise
(here/'logs/validation_results.txt').write_text('\n'.join(lines)+'\n')
