import requests
import time
import datetime
from datetime import datetime
import json
import csv
import os


targets = ["https://google.com", "https://facebook.com", "https://github.com","https://noserver.com"]

def check(url):
    start = time.time()
    now = datetime.now().isoformat()
    try:
        r = requests.get(url, timeout=5)
        ms = round((time.time()-start)*1000)
        status = "UP" if r.status_code < 400 else "DOWN"
        return {"url": url, "status": status, "code": r.status_code, "ms": ms, "time": now}
    except requests.RequestException as e:
        return{"url": url, "status": "DOWN", "code": None, "ms": None, "time": now}

results = []
for url in targets:
    result =check(url)
    if result["status"] == "UP":
        print("🟢", f"url:{url}, status:{result["status"]}, code:{result["code"]} ms:{result["ms"]},Time:{result["time"]}")
    else:
        print ("🔴", f"url:{url}, status:{result["status"]}, status:{result["code"]}, ms:{result["ms"]}, Time:{result["time"]}") 
    results.append(result)

with open("status.json", "w") as f:
    json.dump(results, f, indent=2)
with open("history.csv", "a", newline="") as h:
    writer = csv.writer(h)
    for hist in results:
        writer.writerow([hist["url"], hist["status"], hist["code"], hist["ms"], hist["time"]])

        





















    
