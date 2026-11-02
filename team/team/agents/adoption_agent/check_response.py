"""Check one response against every keyword used by the frozen output schema."""
import json,sys
from pathlib import Path
from check_package import schema_errors, ROOT
if len(sys.argv)!=2: raise SystemExit("Usage: python check_response.py RESPONSE.json")
try:
    data=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
except Exception as e: raise SystemExit("INVALID JSON: "+str(e))
errors=schema_errors(data,json.loads((ROOT/"core/output_schema.json").read_text()))
print("SCHEMA CHECK FAILED\n"+"\n".join(errors) if errors else "SCHEMA CHECK PASSED")
sys.exit(bool(errors))
