#!/usr/bin/env python3
"""Audit saved Lab 8 artifacts; not an inference runner or independent reasoning evaluation."""
from pathlib import Path
import json,hashlib,subprocess,sys,copy
ROOT=Path(__file__).resolve().parents[2];SC=ROOT/'MASY1800_ET_Agent_Scaffold_v1_0';A=SC/'agents/organizational_adoption_agent';T=ROOT/'team/lab8'
NAMES=['primary','contrast_1','missing_information','production_stage','funding_authority'];checks=[];commands=[]
def check(ok,label):
 print(('PASS ' if ok else 'FAIL ')+label);checks.append({'check':label,'passed':bool(ok)})
 if not ok:raise AssertionError(label)
def command(args,expected=0):
 r=subprocess.run([sys.executable]+args,cwd=ROOT,capture_output=True,text=True)
 commands.append({'argv':[sys.executable]+args,'cwd':str(ROOT),'stdout':r.stdout,'stderr':r.stderr,'exit_code':r.returncode,'expected_exit':expected})
 check(r.returncode==expected,'command expected exit '+str(expected)+' '+' '.join(args));return r
def supported(s):
 assert set(s)<={'$schema','title','type','required','properties','items','additionalProperties'},'unsupported schema keyword'
 assert s.get('type') in ['object','array','string'],'unsupported schema type'
 for sub in s.get('properties',{}).values():supported(sub)
 if 'items' in s:supported(s['items'])
def validate(v,s,p='$'):
 assert isinstance(v,{'object':dict,'array':list,'string':str}[s['type']]),(p,'wrong type')
 if isinstance(v,dict):
  assert all(k in v for k in s.get('required',[])),(p,'required missing')
  props=s.get('properties',{})
  if s.get('additionalProperties') is False:assert set(v)<=set(props),(p,'prohibited extra field')
  for k,sub in props.items():
   if k in v:validate(v[k],sub,p+'.'+k)
 if isinstance(v,list) and 'items' in s:
  for i,x in enumerate(v):validate(x,s['items'],p+f'[{i}]')
ss={k:json.loads((SC/'core'/f'{k}_schema.json').read_text()) for k in ['input','output']}
for k,s in ss.items():supported(s);check(True,k+' schema validation features fully supported by audit')
command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/check_frozen_core.py'])
framework=json.loads((A/'readiness_framework.json').read_text());fields=framework['dimension_fields'];dims=framework['dimensions'];cases={};packets={};responses={}
check(len(dims)==8 and len({x['id'] for x in dims})==8,'framework has eight distinct dimensions including operating ownership')
for n in NAMES:
 cases[n]=json.loads((A/'cases'/f'{n}.json').read_text());packets[n]=json.loads(cases[n]['additional_context']);responses[n]=json.loads((A/'responses'/f'{n}_response.json').read_text())
 validate(cases[n],ss['input']);validate(responses[n],ss['output']);check(True,n+' input and full frozen-schema output audit')
 check(set(responses[n])==set(ss['output']['required']),n+' exact permitted top-level fields')
 command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/validate_response.py',f'MASY1800_ET_Agent_Scaffold_v1_0/agents/organizational_adoption_agent/responses/{n}_response.json'])
 p=SC/'work'/f'organizational_adoption_agent_{n}_prompt.txt';before=p.read_bytes()
 command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/build_prompt.py','--agent','agents/organizational_adoption_agent','--case',f'agents/organizational_adoption_agent/cases/{n}.json'])
 check(before==p.read_bytes(),n+' full saved prompt rebuilds identically')
 text=responses[n]['organization_specific_finding']
 for d in dims:check('\n'+d['name']+'\n' in text,n+' dimension label '+d['name'])
 for f in fields:check(text.count('\n'+f+': ')==8,n+' field label in each dimension '+f+' text coverage only')
 ids={x['evidence_id'] for x in packets[n]['readiness_evidence'].values()}
 check(all(x in text for x in ids),n+' all supplied dimension evidence IDs traced')
 check(len(responses[n]['evidence'])==9,n+' shared technical assumption plus eight dimension references')
 check(bool(responses[n]['change_monitoring_triggers']) and bool(responses[n]['abstention_or_more_information_needed']) and bool(responses[n]['contrary_evidence_or_limitations']),n+' triggers questions and contrary interpretation populated')
 check('REPLACE WITH' not in json.dumps(cases[n])+json.dumps(responses[n]),n+' no template placeholders')
diff=lambda x,y:[k for k in x if x[k]!=y[k]]
check(set(diff(cases['primary'],cases['contrast_1']))=={'organization','additional_context'},'main contrast changes organization and organizational evidence only')
for n in NAMES[1:]:
 for k in ['technical_assumption','application_authority','evidence_basis']:check(packets[n][k]==packets['primary'][k],n+' unchanged '+k)
 for k in ['general_et_finding','application_finding']:check(responses[n][k]==responses['primary'][k],n+' deliberately stable saved '+k)
for n in ['missing_information','production_stage','funding_authority']:check(diff(cases['primary'],cases[n])==['additional_context'],n+' only evidence/stage packet changes')
check(diff(packets['primary']['readiness_evidence'],packets['missing_information']['readiness_evidence'])==['operating_ownership'],'qualified case isolates missing owner evidence')
check(diff(packets['primary'],packets['production_stage'])==['requested_stage'],'stage case changes requested stage only')
check(diff(packets['primary']['readiness_evidence'],packets['funding_authority']['readiness_evidence'])==['resources_budget'],'funding case changes resources evidence only')
review=json.loads((T/'qualitative_review.json').read_text());expected={'primary':'Ready to proceed to the next management gate','contrast_1':'Not ready to proceed yet','missing_information':'Insufficient evidence to conclude','production_stage':'Insufficient evidence to conclude','funding_authority':'Ready to proceed to the next management gate'}
for v in review:check(v['readiness']==expected[v['case']] and responses[v['case']]['organization_specific_finding'].startswith('Overall readiness: '+v['readiness']),v['case']+' saved finding matches recorded qualitative self-review')
check('not proof that ownership is absent' in responses['missing_information']['recommendation_management_implication'],'missing owner evidence not recorded as confirmed absence')
check('budget and reviewer/support allocation remain explicitly approved' in responses['funding_authority']['recommendation_management_implication'],'approved-budget fact preserved in funding analysis')
check('does not establish business value' in (A/'specialist_instructions.md').read_text() or 'business value' in responses['primary']['application_finding'],'readiness not equated with value')
# Constructed negative controls: expected rejection, not observed spontaneous agent failures.
bad=copy.deepcopy(responses['primary']);bad['readiness']={'overall':'ready'}
badpath=T/'preserved_weakness/negative_extra_readiness.json';badpath.write_text(json.dumps(bad,indent=2,ensure_ascii=False)+'\n')
command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/validate_response.py','team/lab8/preserved_weakness/negative_extra_readiness.json'])
try:validate(bad,ss['output'])
except AssertionError as e:check(True,'extra readiness field rejected by full schema despite basic validator acceptance');extra=str(e)
else:raise AssertionError('extra field accepted')
bad=copy.deepcopy(responses['primary']);bad['organization_specific_finding']={'overall':'ready'}
(T/'preserved_weakness/negative_wrong_type.json').write_text(json.dumps(bad,indent=2,ensure_ascii=False)+'\n')
command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/validate_response.py','team/lab8/preserved_weakness/negative_wrong_type.json'],expected=1)
try:validate(bad,ss['output'])
except AssertionError as e:check(True,'object substituted for required readiness string rejected by full schema');wrong=str(e)
else:raise AssertionError('wrong type accepted')
(T/'logs/negative_controls.txt').write_text('EXTRA FIELD EXPECTED REJECTION: '+extra+'\nWRONG TYPE EXPECTED REJECTION: '+wrong+'\nBoth negative controls passed. These are deliberately constructed fixtures.\n')
for e in json.loads((T/'lineage_manifest.json').read_text()):check(hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest()==e['sha256'],'source snapshot digest '+e['path'])
command(['MASY1800_ET_Agent_Scaffold_v1_0/tools/check_frozen_core.py'])
(T/'logs/commands.json').write_text(json.dumps(commands,indent=2)+'\n');(T/'logs/check_summary.json').write_text(json.dumps(checks,indent=2)+'\n')
print(f'ALL SAVED-ARTIFACT CHECKS PASSED: {len(checks)} assertions; 5 official positive validators; 5 full input/output audits; frozen core intact.')
print('Two constructed negative controls correctly rejected by full schema. No independent inference or operating-readiness certification.')
