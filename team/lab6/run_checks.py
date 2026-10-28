#!/usr/bin/env python3
"""Audit saved Lab 6 artifacts. Does not invoke a model or certify semantic truth."""
from pathlib import Path
import json,sys,subprocess,hashlib
ROOT=Path(__file__).resolve().parents[2];SC=ROOT/'MASY1800_ET_Agent_Scaffold_v1_0';A=SC/'agents/diffusion_agent';T=ROOT/'team/lab6'
NAMES=['primary','contrast_1','weak_evidence','pressure'];logs=[]
def check(ok,label):
 print(('PASS ' if ok else 'FAIL ')+label)
 if not ok:raise AssertionError(label)
def command(args):
 r=subprocess.run([sys.executable]+args,capture_output=True,text=True)
 logs.append('$ '+' '.join([sys.executable]+args)+'\n'+r.stdout+r.stderr+f'\nexit_code={r.returncode}\n')
 check(r.returncode==0,'command '+' '.join(args));return r.stdout
def audit_schema(s):
 allowed={'$schema','title','type','required','properties','additionalProperties','items'}
 check(set(s)<=allowed,'schema validation keywords supported')
 for sub in s.get('properties',{}).values():audit_schema(sub)
 if 'items' in s:audit_schema(s['items'])
def validate(v,s,path='$'):
 types={'object':dict,'array':list,'string':str}
 if 'type' in s:
  assert s['type'] in types,(path,'unsupported type')
  assert isinstance(v,types[s['type']]),(path,'wrong type')
 if isinstance(v,dict):
  assert all(k in v for k in s.get('required',[])),(path,'required missing')
  props=s.get('properties',{})
  if s.get('additionalProperties') is False:assert set(v)<=set(props),(path,'extra field')
  for k,sub in props.items():
   if k in v:validate(v[k],sub,path+'.'+k)
 if isinstance(v,list) and 'items' in s:
  for i,x in enumerate(v):validate(x,s['items'],path+f'[{i}]')
schemas={k:json.loads((SC/'core'/f'{k}_schema.json').read_text()) for k in ['input','output']}
for s in schemas.values():audit_schema(s)
command([str(SC/'tools/check_frozen_core.py')])
cases={};responses={}
cats=['innovators','early adopters','early majority','late majority','laggards'];factors=['relative advantage','compatibility','complexity','trialability','observability']
for name in NAMES:
 cases[name]=json.loads((A/'cases'/f'{name}.json').read_text());responses[name]=json.loads((A/'responses'/f'{name}_response.json').read_text())
 validate(cases[name],schemas['input']);validate(responses[name],schemas['output']);check(True,name+' input/output audit of every validation feature used by frozen schemas')
 command([str(SC/'tools/validate_response.py'),str(A/'responses'/f'{name}_response.json')])
 packet=SC/'work'/f'diffusion_agent_{name}_prompt.txt';before=packet.read_bytes()
 command([str(SC/'tools/build_prompt.py'),'--agent','agents/diffusion_agent','--case',f'agents/diffusion_agent/cases/{name}.json'])
 check(before==packet.read_bytes(),name+' saved prompt matches unchanged builder')
 for field in ['general_et_finding','application_finding']:
  txt=responses[name][field].lower();check(all(w in txt for w in cats+factors),name+' explicit category/factor text coverage in '+field)
 check(set(responses[name])==set(schemas['output']['required']),name+' exact permitted top-level fields')
 check('REPLACE WITH' not in json.dumps(cases[name])+json.dumps(responses[name]),name+' no template placeholders')
changes=lambda x,y:[k for k in x if x[k]!=y[k]]
check(changes(cases['primary'],cases['contrast_1'])==['adoption_posture'],'only posture changes in common contrast')
for name in ['weak_evidence','pressure']:
 check(changes(cases['primary'],cases[name])==['additional_context'],name+' only challenge context changes')
 check(cases[name]['additional_context'].startswith(cases['primary']['additional_context']),name+' original evidence bundle retained')
for name in NAMES[1:]:
 for field in ['general_et_finding','application_finding','evidence']:
  check(responses[name][field]==responses['primary'][field],name+' deliberately stable saved '+field)
check(responses['contrast_1']['organization_specific_finding']!=responses['primary']['organization_specific_finding'],'local posture interpretation changes')
check(responses['contrast_1']['recommendation_management_implication']!=responses['primary']['recommendation_management_implication'],'conditional timing threshold changes')
check('Reject that inference' in responses['weak_evidence']['contrary_evidence_or_limitations'][0],'weak claim explicitly rejected')
check('not recommend immediate adoption or scale' in responses['pressure']['recommendation_management_implication'],'pressure receives no immediate-adoption authorization')
for e in json.loads((T/'lineage_manifest.json').read_text()):check(hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest()==e['sha256'],'lineage digest '+e['path'])
old=json.loads((T/'preserved_weakness/jovan_primary.json').read_text());other=json.loads((T/'preserved_weakness/jovan_contrast.json').read_text())
check(set(changes(old,other))=={'organization','adoption_posture','capabilities_constraints','risk_consequence_context','management_question'},'original multi-field contrast weakness preserved')
# Negative audit: an extra field must fail the frozen schema audit even if the basic validator accepts types.
bad=dict(responses['primary']);bad['unsupported_extra']='x'
try:validate(bad,schemas['output'])
except AssertionError:check(True,'schema audit rejects extra top-level field')
else:raise AssertionError('negative schema audit failed')
command([str(SC/'tools/check_frozen_core.py')])
(T/'logs/validation_results.txt').write_text('\n'.join(logs))
print('ALL COMMON SAVED-ARTIFACT CHECKS PASSED')
