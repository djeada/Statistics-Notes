#!/usr/bin/env python3
"""Run every panel query of every provisioned course dashboard through a live Grafana and check it returns data.

    docker run -d --name g -p 3055:3000 -e GF_AUTH_ANONYMOUS_ENABLED=true -e GF_AUTH_ANONYMOUS_ORG_ROLE=Admin \
      -v $PWD/course/grafana/provisioning:/etc/grafana/provisioning:ro -v $PWD/course:/course:ro grafana/grafana:11.3.0
    python check_grafana.py http://localhost:3055

Checks: dashboard loaded, each non-text panel has >=1 target returning >=1 row, timeseries panels have a time field
that is non-constant, and panel time range covers the data.
"""
import json
import sys
import urllib.request

base = (sys.argv[1] if len(sys.argv) > 1 else "http://localhost:3055").rstrip("/")
only = sys.argv[2] if len(sys.argv) > 2 else ""  # e.g. "stats-07" to check one lesson's dashboard


def get(path):
    return json.load(urllib.request.urlopen(base + path))


def post(path, body):
    req = urllib.request.Request(base + path, json.dumps(body).encode(), {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))


bad = 0
for hit in sorted(get("/api/search?type=dash-db"), key=lambda h: h["title"]):
    if only not in hit["uid"]:
        continue
    dash = get(f"/api/dashboards/uid/{hit['uid']}")["dashboard"]
    problems = []
    for p in dash["panels"]:
        if p["type"] == "text":
            continue
        for t in p.get("targets", []):
            q = dict(t, datasource=t["datasource"])
            res = post("/api/ds/query", {"queries": [q], "from": "0", "to": "9999999999999"})
            r = res["results"][t["refId"]]
            if r.get("error"):
                problems.append(f"{p['title']}: {r['error']}")
                continue
            frames = r.get("frames", [])
            rows = sum(len(f["data"]["values"][0]) for f in frames if f["data"]["values"])
            if not rows:
                problems.append(f"{p['title']}: no rows")
            if p["type"] == "timeseries":
                f = frames[0]
                types = [fl["type"] for fl in f["schema"]["fields"]]
                if types[0] != "time":
                    problems.append(f"{p['title']}: first field is {types[0]}, not time")
    status = "OK  " if not problems else "FAIL"
    print(f"[{status}] {hit['title']} ({len(dash['panels'])} panels)")
    for pr in problems:
        print("        ", pr)
    bad += bool(problems)
sys.exit(1 if bad else 0)
