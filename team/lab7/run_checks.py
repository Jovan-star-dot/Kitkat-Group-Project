#!/usr/bin/env python3
"""Reproduce artifact validation only. Does not invoke a model or prove semantic quality."""
from pathlib import Path
import copy, hashlib, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2];SC=ROOT/'MASY1800_ET_Agent_Scaffold_v1_0';A=SC/'agents/adoption_agent';T=ROOT/'team/lab7'
NAMES=['primary','contrast_1','qualified','feasibility_gap','permission_blocker','advocate_pressure','risk_officer_pressure']
checks=[];commands=[]
def check(ok,label):
 print(('PASS ' if ok else 'FAIL ')+label)
 checks.append({'check':label,'passed':bool(ok)})
 if not ok:raise AssertionError(label)
def command(args,expected=0):
 r=subprocess.run([sys.executable]+[str(x) for x in args],cwd=ROOT,capture_output=True,text=True)
 commands.append({'argv':[sys.executable]+[str(x) for x in args],'cwd':str(ROOT),'stdout':r.stdout,'stderr':r.stderr,'exit_code':r.returncode,'expected_exit':expected})
 check(r.returncode==expected,'command exit '+str(expected)+' '+' '.join(str(x) for x in args))
 return r
def supported(s):
 allowed={'$schema','title','type','required','properties','items','additionalProperties'}
 assert set(s)<=allowed,('unsupported schema feature',set(s)-allowed)
 assert s.get('type') in ['object','array','string']
 for sub in s.get('properties',{}).values():supported(sub)
 if 'items' in s:supported(s['items'])
def validate(v,s,p='$'):
 assert isinstance(v,{'object':dict,'array':list,'string':str}[s['type']]),(p,'type')
 if isinstance(v,dict):
  assert all(k in v for k in s.get('required',[])),(p,'missing required')
  props=s.get('properties',{})
  if s.get('additionalProperties') is False:assert set(v)<=set(props),(p,'prohibited extra field')
  for k,sub in props.items():
   if k in v:validate(v[k],sub,p+'.'+k)
 if isinstance(v,list) and 'items' in s:
  for i,x in enumerate(v):validate(x,s['items'],p+f'[{i}]')
schemas={k:json.loads((SC/'core'/f'{k}_schema.json').read_text()) for k in ['input','output']}
for k,s in schemas.items():supported(s);check(True,k+' schema uses only supported audited validation features')
command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/check_frozen_core.py'])
cases={};rs={}
factors=['maturity','diffusion evidence','relative advantage','application fit','alternatives','reversibility','uncertainty','consequences of failure','organizational posture']
for n in NAMES:
 cases[n]=json.loads((A/'cases'/f'{n}.json').read_text());rs[n]=json.loads((A/'responses'/f'{n}_response.json').read_text())
 validate(cases[n],schemas['input']);validate(rs[n],schemas['output']);check(True,n+' input and full frozen output-schema audit')
 check(set(rs[n])==set(schemas['output']['required']),n+' exact permitted top-level fields')
 command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/validate_response.py',f'MASY1800_ET_Agent_Scaffold_v1_0/agents/adoption_agent/responses/{n}_response.json'])
 packet=SC/'work'/f'adoption_agent_{n}_prompt.txt';before=packet.read_bytes()
 command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/build_prompt.py','--agent','agents/adoption_agent','--case',f'agents/adoption_agent/cases/{n}.json'])
 check(before==packet.read_bytes(),n+' prompt rebuilt identically')
 text=' '.join(rs[n][x] for x in ['general_et_finding','application_finding','organization_specific_finding']).lower()
 check(all(f in text for f in factors),n+' nine factor labels present across three levels text coverage only')
 rec=rs[n]['recommendation_management_implication'].lower()
 check(all(b in rec for b in ['sunk cost','novelty','fomo','excessive conservatism']),n+' four bias labels present text coverage only')
 check(bool(rs[n]['contrary_evidence_or_limitations']) and bool(rs[n]['change_monitoring_triggers']) and bool(rs[n]['abstention_or_more_information_needed']),n+' contrary view triggers and gaps populated')
 check('REPLACE WITH' not in json.dumps(cases[n])+json.dumps(rs[n]),n+' no scaffold placeholders')
diff=lambda x,y:[k for k in x if x[k]!=y[k]]
check(diff(cases['primary'],cases['contrast_1'])==['adoption_posture'],'posture is sole contrast input change')
for n in ['qualified','feasibility_gap','permission_blocker']:check(diff(cases['primary'],cases[n])==['capabilities_constraints'],n+' only capability fact bundle changes')
for n in ['advocate_pressure','risk_officer_pressure']:
 check(diff(cases['primary'],cases[n])==['additional_context'],n+' only hypothetical argument appended')
 check(cases[n]['additional_context'].startswith(cases['primary']['additional_context']),n+' original evidence retained')
for n in NAMES[1:]:
 check(rs[n]['general_et_finding']==rs['primary']['general_et_finding'],n+' deliberately stable general finding saved text')
 check(rs[n]['application_finding']==rs['primary']['application_finding'],n+' deliberately stable application finding saved text')
for n in ['primary','contrast_1','advocate_pressure','risk_officer_pressure']:
 check(rs[n]['recommendation_management_implication'].startswith('Conduct a bounded experiment.'),n+' saved conditional action matches qualitative review')
check(rs['qualified']['recommendation_management_implication'].startswith('Withhold a primary recommendation'),'qualified case preserves withholding')
check(rs['feasibility_gap']['recommendation_management_implication'].startswith('Conduct a proof of concept.'),'technical feasibility gap saved POC action')
check(rs['permission_blocker']['recommendation_management_implication'].startswith('Defer.'),'permission blocker saved deferral action')
policy=(A/'recommendation_policy.md').read_text()
check(all(s in policy for s in ['Adopt/implement','Conduct a bounded experiment','Conduct a proof of concept','Continue monitoring','Defer','Reject for the present']),'all six explicit action definitions present')
# Deliberate negative control; not a spontaneous model failure.
bad=copy.deepcopy(rs['primary']);bad['decision']={'action':'Adopt now'}
badpath=T/'preserved_weakness/negative_extra_decision.json';badpath.write_text(json.dumps(bad,indent=2,ensure_ascii=False)+'\n')
command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/validate_response.py','team/lab7/preserved_weakness/negative_extra_decision.json'])
try:validate(bad,schemas['output'])
except AssertionError as e:
 check(True,'negative extra decision field rejected by frozen schema audit despite basic validator pass')
 (T/'logs/negative_schema_result.txt').write_text('EXPECTED REJECTION\n'+str(e)+'\nnegative_control_passed=true\n')
else:raise AssertionError('negative control failed: extra field accepted')
manifest=json.loads((T/'lineage_manifest.json').read_text())
for e in manifest:check(hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest()==e['sha256'],'lineage digest '+e['path'])
command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/check_frozen_core.py'])
(T/'logs/commands.json').write_text(json.dumps(commands,indent=2)+'\n')
(T/'logs/check_summary.json').write_text(json.dumps(checks,indent=2)+'\n')
print('ALL SAVED-ARTIFACT CHECKS PASSED; 7 official response validations; 7 full schema audits; frozen core intact.')
print('These checks do not establish independent model repeatability or customer-service performance.')
