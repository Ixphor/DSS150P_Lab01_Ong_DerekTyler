import json
from datetime import datetime, timezone
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(API_URL, timeout=20)
    
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Hi :( Request failed: {e}")
    exit(1)

print("status:", response.status_code)
print("content-type:", response.headers.get("Content-Type"))

payload = response.json()

top_level_type = type(payload).__name__
print("top-level type:", top_level_type)

if top_level_type == "list":
    print("number of records:", len(payload))
    if len(payload) > 0:
        print("\nSample Record")
        print(json.dumps(payload[0], indent=2))
elif top_level_type == "dict":
    print("number of records: 1")
    print("\nSample Record")
    print(json.dumps(payload, indent=2))

snapshot_path = "data/raw/api_snapshot.json"
with open(snapshot_path, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)
print(f"\nSaved response to {snapshot_path}")

utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
print(f"Retrieval timestamp (UTC): {utc_now}")