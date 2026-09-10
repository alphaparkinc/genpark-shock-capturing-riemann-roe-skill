import sys
import json
from client import RoeRiemannSolver1D

roe = RoeRiemannSolver1D()

def handle_call(name, arguments):
    if name == "flux":
        rl = arguments["rho_L"]
        ul = arguments["u_L"]
        pl = arguments["p_L"]
        rr = arguments["rho_R"]
        ur = arguments["u_R"]
        pr = arguments["p_R"]
        return {"mass_flux": roe.compute_interface_flux(rl, ul, pl, rr, ur, pr)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
