import sys
import http.client
import os
import json

conn = http.client.HTTPSConnection("circleci.com")

headers = { 'Circle-Token': os.environ['CIRCLE_TOKEN'], 'Accept': "application/json" }

project_slug = f"{os.environ['VCS']}/{os.environ['ORG']}/{os.environ['REPO']}"

branch = sys.argv[1]

#commit-workflow made generic
conn.request("GET", f"/api/v2/insights/time-series/{project_slug}/workflows?branch={branch}&workflow-name={os.environ['WORKFLOW']}", headers=headers)

res = conn.getresponse()
data = res.read()

decoded = json.loads(data.decode("utf-8"))

total_runs = 0
success_runs = 0
total_credits = 0

for item in decoded['items']:
    base_metrics = item['metrics']
    total_runs += base_metrics['total_runs']
    success_runs += base_metrics['successful_runs']
    total_credits += base_metrics['total_credits_used']

if total_runs == 0:
    print("No runs found")
else:
    obj = {
        'total_runs': total_runs,
        'successful_runs': success_runs,
        'total_credits_used': total_credits,
        'average_credits_used': total_credits/total_runs
    }

    print(obj)