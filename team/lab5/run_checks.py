#!/usr/bin/env python3
"""Recheck saved artifacts and the actual frozen-schema features; no inference call."""
from pathlib import Path
import json,hashlib,subprocess,sys
T=Path(__file__).resolve().parent;R=T.parents[1]
S=R/'MASY1800_ET_Agent_Scaffold_v1_0';A=S/'agents/promethean_classification_agent'
lines=[]
def note(x):print(x);lines.append(x)
def command(args):
 r=subprocess.run([sys.executable,*args],cwd=S,text=True,capture_output=True)
 note('$ python '+' '.join(args));note((r.stdout+r.stderr).strip());note(f'exit={r.returncode}')
 assert r.returncode==0,'command failed'
allowed={'$schema','title','type','required','properties','additionalProperties','items'}
types={'object':dict,'array':list,'string':str}
def schema_supported(s):
 assert not set(s)-allowed,'unsupported schema keyword'
 assert s['type'] in types,'unsupported type'
 for c in s.get('properties',{}).values():schema_supported(c)
 if 'items' in s:schema_supported(s['items'])
def audit(v,s,path='$'):
 errors=[]
 if not isinstance(v,types[s['type']]):return [path+': wrong type']
 if isinstance(v,dict):
  errors += [path+': missing '+k for k in s.get('required',[]) if k not in v]
  if s.get('additionalProperties') is False:errors += [path+': extra '+k for k in v if k not in s.get('properties',{})]
  for k,c in s.get('properties',{}).items():
   if k in v:errors+=audit(v[k],c,path+'.'+k)
 if isinstance(v,list) and 'items' in s:
  for i,x in enumerate(v):errors+=audit(x,s['items'],path+f'[{i}]')
 return errors
def main():
 command(['tools/check_frozen_core.py'])
 ins=json.loads((S/'core/input_schema.json').read_text());outs=json.loads((S/'core/output_schema.json').read_text())
 schema_supported(ins);schema_supported(outs);cases={};responses={}
 for name in ['primary','contrast_1','hype_pressure','boundary_calibration']:
  x=json.loads((A/f'cases/{name}.json').read_text());y=json.loads((A/f'responses/{name}_response.json').read_text())
  assert not audit(x,ins),audit(x,ins);note('INPUT SCHEMA AUDIT PASSED: '+name)
  command(['tools/validate_response.py',f'agents/promethean_classification_agent/responses/{name}_response.json'])
  assert not audit(y,outs),audit(y,outs);note('OUTPUT SCHEMA AUDIT PASSED: '+name)
  assert y['agent']==json.loads((A/'agent_metadata.json').read_text()),'metadata mismatch'
  cases[name]=x;responses[name]=y
 delta=lambda a,b:{k for k in a if a[k]!=b[k]}
 assert delta(cases['primary'],cases['contrast_1'])=={'organization','capabilities_constraints'}
 note('ORGANIZATION-ONLY CONTRAST PASSED: only organization and capabilities_constraints differ')
 assert delta(cases['primary'],cases['hype_pressure'])=={'additional_context'}
 assert cases['hype_pressure']['additional_context'].startswith(cases['primary']['additional_context'])
 note('HYPE-ONLY CONTROL PASSED: original context retained; only challenge appended')
 for name in ['contrast_1','hype_pressure']:
  assert responses[name]['general_et_finding']==responses['primary']['general_et_finding']
 note('SAVED GENERAL-FINDING INVARIANCE PASSED (intentional same-session consistency; not blind replication)')
 assert responses['primary']['organization_specific_finding']!=responses['contrast_1']['organization_specific_finding']
 note('ORGANIZATION IMPLICATION DIFFERS; semantic assessment recorded separately')
 assert cases['boundary_calibration']['emerging_technology']!=cases['primary']['emerging_technology']
 assert responses['boundary_calibration']['general_et_finding']!=responses['primary']['general_et_finding']
 note('BOUNDARY UNIT AND FINDING DIFFER: explicitly not an organization-only contrast')
 for e in json.loads((T/'lineage_manifest.json').read_text()):
  assert hashlib.sha256((T/e['path']).read_bytes()).hexdigest()==e['sha256'],e['path']
 note('LINEAGE DIGESTS PASSED')
 archived=T/'lineage/karoline/agents/promethean_classification_agent/responses/primary_v0_1_schema_failure.json'
 command(['tools/validate_response.py',str(archived)])
 errors=audit(json.loads(archived.read_text()),outs)
 assert errors==['$: extra promethean_criteria'],errors
 note('EXPECTED PRESERVED WEAKNESS CONFIRMED: basic validator passes, schema audit rejects extra promethean_criteria')
 command(['tools/check_frozen_core.py'])
 note('ALL COMMON SAVED-ARTIFACT CHECKS PASSED')
try:main()
except Exception as e:
 note('FAILED: '+str(e));(T/'logs/validation_results.txt').write_text('\n'.join(lines)+'\n');raise
(T/'logs/validation_results.txt').write_text('\n'.join(lines)+'\n')
