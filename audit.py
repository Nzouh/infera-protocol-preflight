import argparse, json
from pathlib import Path

def audit(run):
    issues = []
    inventory = run["inventory"]
    for step in run["steps"]:
        if step["instrument"] not in run["available_instruments"]:
            issues.append({"step": step["id"], "code": "instrument_unavailable"})
        for reagent, amount in step.get("consumes", {}).items():
            inventory[reagent] = inventory.get(reagent, 0) - amount
            if inventory[reagent] < 0:
                issues.append({"step": step["id"], "code": "inventory_shortfall", "reagent": reagent})
        if step.get("temperature_c", 20) > step.get("instrument_max_c", 100):
            issues.append({"step": step["id"], "code": "temperature_limit"})
    return {"run_id": run["run_id"], "status": "review" if issues else "ready", "issues": issues}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("input"); p.add_argument("-o","--output",default="report.json")
    a=p.parse_args()
    result=audit(json.loads(Path(a.input).read_text()))
    Path(a.output).write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
    raise SystemExit(2 if result["issues"] else 0)
if __name__=="__main__": main()
