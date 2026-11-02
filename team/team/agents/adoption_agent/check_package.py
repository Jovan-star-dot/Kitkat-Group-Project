"""Offline artifact checks; does not run an LLM or establish business validity."""
import json, sys, subprocess
from pathlib import Path
A=Path(__file__).resolve().parent
ROOT=A.parents[1]
def schema_errors(value,schema,path="$" ):
    errors=[]
    types={"object":dict,"array":list,"string":str}
    if schema.get("type") in types and not isinstance(value,types[schema["type"]]):
        return [f"{path}: expected {schema['type']}"]
    if isinstance(value,dict):
        for key in schema.get("required",[]):
            if key not in value: errors.append(f"{path}: missing {key}")
        props=schema.get("properties",{})
        if schema.get("additionalProperties") is False:
            for key in value.keys()-props.keys(): errors.append(f"{path}: unexpected property {key}")
        for key,item in value.items():
            if key in props: errors.extend(schema_errors(item,props[key],path+"."+key))
    elif isinstance(value,list):
        for i,item in enumerate(value): errors.extend(schema_errors(item,schema.get("items",{}),f"{path}[{i}]"))
    return errors

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def main():
    out=load(ROOT/"core/output_schema.json"); inp=load(ROOT/"core/input_schema.json")
    failures=[]
    for p in sorted((A/"cases").glob("*.json")):
        e=schema_errors(load(p),inp); failures.extend(e); print(p.name, "PASS" if not e else e)
    expected={"primary":"BOUNDED EXPERIMENT", "contrast_aggressive":"BOUNDED EXPERIMENT", "contrast_conservative":"PROOF OF CONCEPT", "monitoring":"MONITOR"}
    responses={}
    for case,category in expected.items():
        p=A/"responses"/(case+"_response.json"); d=load(p);responses[case]=d
        e=schema_errors(d,out)
        if not d.get("recommendation_management_implication","").startswith(category+":"): e.append(case+": wrong category")
        if not d.get("abstention_or_more_information_needed"): e.append(case+": missing information requests")
        failures.extend(e);print(p.name,"PASS" if not e else e)
    for case in ("contrast_aggressive","contrast_conservative"):
        b=load(A/"cases/primary.json");c=load(A/"cases"/(case+".json"))
        if [k for k in b if b[k]!=c[k]] != ["adoption_posture"]: failures.append("Posture contrast changes other fields")
        if responses[case]["general_et_finding"]!=responses["primary"]["general_et_finding"]: failures.append("General finding drift")
        if responses[case]["application_finding"]!=responses["primary"]["application_finding"]: failures.append("Application finding drift")
    weak=load(A/"records/failures/v0_primary_response.json")
    errors=schema_errors(weak,out)
    print("Preserved v0:", "EXPECTED FAIL" if errors else "UNEXPECTED PASS",errors)
    if not errors: failures.append("Failure fixture no longer fails")
    # Mutation controls prove that the checker rejects contract defects.
    for label,mutate in [("extra field",lambda d:d.update(extra=True)),("wrong type",lambda d:d.update(evidence="bad")),("missing field",lambda d:d.pop("agent"))]:
        d=load(A/"responses/primary_response.json");mutate(d)
        if not schema_errors(d,out): failures.append("Mutation not caught: "+label)
    result=subprocess.run([sys.executable,str(ROOT/"tools/check_frozen_core.py")],capture_output=True,text=True)
    print(result.stdout.strip())
    if result.returncode: failures.append(result.stderr+result.stdout)
    print("PACKAGE CHECKS PASSED" if not failures else "PACKAGE CHECKS FAILED\n"+"\n".join(failures))
    return bool(failures)
if __name__=="__main__":sys.exit(main())
