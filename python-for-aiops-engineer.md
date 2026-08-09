# Python for AIOps Engineers 🚀

Quick AI-first Python guide for AIOps engineers: analyze logs, call APIs, process JSON, and build reliable automation.

---

## 🎯 Why Python for AIOps?

- **Easy to learn** - Readable syntax, quick to write
- **Great for automation** - Perfect for scripts and tools
- **Rich ecosystem** - Libraries for APIs, data, monitoring
- **Cross-platform** - Runs on Linux, macOS, Windows

---

## 📚 Core Topics Covered

| Topic | Why It Matters for AIOps |
|-------|-------------------------|
| Variables & Data Types | Store counters, service names, status flags |
| Lists & Dictionaries | Handle log collections, JSON data |
| Control Flow | Make decisions, iterate through logs |
| Functions | Reusable log analysis code |
| API Interaction | Call monitoring services, send alerts |
| Environment Variables | Secure API key management |
| Pandas | Analyze metrics, filter logs |
| Time-Series | Monitor CPU/memory trends |
| Anomaly Detection | Flag unusual events |
| CLI Tools | Build flexible automation scripts |
| Error Handling | Make scripts reliable in production |
| AI Integration | Use LLMs for log analysis |

---

## 🚀 Session 0: Quick Start (AI First)

### 🟡 Call LLM API with Python

**Use Case:** Send a log to an AI model for analysis

```python
import os
import requests

api_key = os.getenv("AIOPS_API_KEY")
endpoint = os.getenv("AIOPS_ENDPOINT", "https://api.example.com/v1")

payload = {
    "model": "gpt-4o-mini",
    "input": "Summarize: Failed login for alice on auth service",
}

response = requests.post(
    f"{endpoint}/llm/generate",
    json=payload,
    headers={"Authorization": f"Bearer {api_key}"},
)
response.raise_for_status()

result = response.json()
print("AI output:", result)
```

**Output:**
```
AI output: {'id': 'abc123', 'output': 'Authentication failure detected', 'status': 'success'}
```

### 🔵 Understand JSON Response

```python
# Check response type and structure
print(type(result))           # <class 'dict'>
print("Keys:", result.keys())
print("Summary:", result.get("output", "No output"))
```

---

## 🔹 Section 1: Python Core

### Variables

```python
count = 12              # int
service = "auth"       # str
is_alerting = False     # bool
```

### Strings

```python
message = "error count"
status = service + ": " + message
print(status.upper())    # ERROR COUNT
print(len(message))      # 11
```

### Lists `[ ]` - For log collections

```python
logs = [
    "2026-05-22 12:00:01 auth ERROR Failed login",
    "2026-05-22 12:00:05 auth INFO User authenticated",
]
print(len(logs))         # 2
print(logs[0])           # First log line
```

### Dictionaries `{ }` - For JSON/API data

```python
event = {
    "timestamp": "2026-05-22T12:00:01Z",
    "service": "auth",
    "level": "ERROR",
    "message": "Failed login",
}
print(event["service"])    # auth
print(event.get("level")) # ERROR
```

### Type Checking

```python
print(type(count))    # <class 'int'>
print(type(service))  # <class 'str'>
print(type(logs))     # <class 'list'>
print(type(event))    # <class 'dict'>
```

---

## 🔹 Section 2: Control Flow

### if / else

```python
error_count = 7
if error_count > 5:
    print("High error rate")
else:
    print("Normal")
```

### for loops

```python
for line in logs:
    print(line)
```

### while loops

```python
retry = 0
while retry < 3:
    print(f"Checking, attempt {retry + 1}")
    retry += 1
```

### break / continue

```python
for line in logs:
    if "INFO" in line:
        continue
    if "CRITICAL" in line:
        print("Critical found!")
        break
    print("Processing", line)
```

---

## 🔹 Section 3: Functions

### def functions

```python
def parse_log_line(line):
    # Format: 2026-05-22 12:00:01 auth ERROR Failed login
    parts = line.split(" ")
    return {
        "timestamp": parts[0] + " " + parts[1],
        "service": parts[2],
        "level": parts[3],
        "message": " ".join(parts[4:]),
    }
```

### Parameters & return values

```python
def is_error(entry):
    return entry.get("level") in {"ERROR", "CRITICAL"}

parsed = parse_log_line(logs[0])
print("Is error?", is_error(parsed))
```

### Reusable functions

```python
def filter_errors(log_lines):
    parsed = [parse_log_line(line) for line in log_lines]
    return [entry for entry in parsed if is_error(entry)]

errors = filter_errors(logs)
print("Errors:", len(errors))
```

---

## 🔹 Section 4: Working with Real Data

### Reading CSV files

```python
import csv

with open("metrics.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    print("Loaded:", len(rows))
```

### Parsing logs

```python
raw = "2026-05-22 12:01:00 web INFO Request 200"
entry = parse_log_line(raw)
print(entry)
```

### Filtering data

```python
filtered = [entry for entry in rows if int(entry["status"]) >= 500]
print("Server errors:", len(filtered))
```

### Working with JSON

```python
import json

body = '{"service": "web", "status": "ok", "count": 125}'
obj = json.loads(body)
print(obj["service"])
obj["status"] = "degraded"
print(json.dumps(obj, indent=2))
```

---

## 🔹 Section 5: API Interaction

### GET request

```python
import requests

response = requests.get("https://api.example.com/health")
if response.status_code == 200:
    data = response.json()
    print("OK", data)
else:
    print("Failed:", response.status_code)
```

### POST request

```python
payload = {"service": "auth", "state": "warning"}
post_resp = requests.post(
    "https://api.example.com/alert",
    json=payload,
    headers={"Authorization": f"Bearer {api_key}"},
)
print("Status:", post_resp.status_code)
```

### Error handling

```python
try:
    response.raise_for_status()
except requests.HTTPError as exc:
    print("API error:", exc)
    print("Code:", response.status_code)
```

---

## 🔹 Section 6: Environment & Security

### Environment variables

```python
import os

api_key = os.getenv("AIOPS_API_KEY")
endpoint = os.getenv("AIOPS_ENDPOINT", "https://api.example.com/v1")
```

### API key validation

```python
if not api_key:
    raise RuntimeError("Missing AIOPS_API_KEY")
```

### .env usage

```python
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("AIOPS_API_KEY")
```

**Security Tips:**
- ✅ Never hardcode secrets
- ✅ Use .env files for development
- ✅ Don't commit .env to git
- ✅ Validate external input

---

## 🔹 Section 7: Pandas Basics

### Create DataFrame

```python
import pandas as pd

df = pd.DataFrame([
    {"timestamp": "2026-05-22T12:00:01Z", "level": "ERROR", "service": "auth", "cpu": 70},
    {"timestamp": "2026-05-22T12:00:05Z", "level": "INFO", "service": "auth", "cpu": 55},
])
print(df.head())
```

### Load CSV

```python
df = pd.read_csv("metrics.csv")
print("Columns:", df.columns.tolist())
```

### Filter rows

```python
errors = df[df["level"] == "ERROR"]
print("Error rows:", len(errors))
```

### Aggregation

```python
counts = df["level"].value_counts()
print("Counts:\n", counts, "\n")

mean_cpu = df["cpu"].mean()
print("Mean CPU:", mean_cpu)
```

---

## 🔹 Section 8: Time-Series

### Convert to datetime index

```python
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp").sort_index()
print(df["cpu"].resample("1T").mean())
```

### Detect spikes

```python
cpu_series = df["cpu"].resample("1T").mean().fillna(0)
print("Latest:\n", cpu_series.tail())
```

### Threshold alerts

```python
threshold = 80
spikes = cpu_series[cpu_series > threshold]
print("CPU spikes:", spikes)
```

---

## 🔹 Section 9: Anomaly Detection

### Average-based detection

```python
avg = cpu_series.mean()
std = cpu_series.std()
alert_threshold = avg + 2 * std
anomalies = cpu_series[cpu_series > alert_threshold]
print("Mean:", avg, "Std:", std)
print("Anomalies:\n", anomalies)
```

### Hard threshold

```python
hard_threshold = 90
alerts = cpu_series[cpu_series > hard_threshold]
print(alerts)
```

### Pattern detection

```python
if cpu_series.diff().abs().max() > 50:
    print("Sudden surge detected!")
```

---

## 🔹 Section 10: CLI Tools

### sys.argv

```python
import sys
print(sys.argv)  # ['script.py', '--source', 'logs.csv']
```

### argparse

```python
import argparse

parser = argparse.ArgumentParser(description="AIOps analyzer")
parser.add_argument("--log", default="/var/log/app.log")
parser.add_argument("--threshold", type=int, default=5)
args = parser.parse_args()
print("Log:", args.log, "Threshold:", args.threshold)
```

### CLI tool example

```python
def main():
    parser = argparse.ArgumentParser(description="Log analyzer")
    parser.add_argument("--source", default="logs.csv")
    parser.add_argument("--error-level", default="ERROR")
    args = parser.parse_args()

    with open(args.source) as f:
        lines = f.readlines()

    errors = [line for line in lines if args.error_level in line]
    print(f"Found {len(errors)} {args.error_level} lines")

if __name__ == "__main__":
    main()
```

**Run:** `python script.py --source logs.csv --error-level CRITICAL`

---

## 🔹 Section 11: Error Handling

### try / except

```python
try:
    value = int("not-a-number")
except ValueError as exc:
    print("Parse error:", exc)
```

### File not found

```python
try:
    with open("missing.log") as f:
        data = f.read()
except FileNotFoundError:
    print("Log file not found")
```

### Logging errors

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    response = requests.get(endpoint)
    response.raise_for_status()
except requests.RequestException as exc:
    logger.error("API failed: %s", exc)
```

---

## 🔹 Section 12: Package Management

### Install packages

```bash
pip install requests pandas python-dotenv
```

### requirements.txt

```
requests
pandas
python-dotenv
```

### Virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

**Best Practices:**
- ✅ Use virtual environments
- ✅ Keep requirements.txt in git
- ✅ Pin versions for production

---

## 🔹 Section 13: AI Integration

### Send prompt to LLM

```python
prompt = "Classify: Failed login for alice on auth service"
llm_payload = {
    "model": "gpt-4o-mini",
    "input": prompt,
}

resp = requests.post(
    f"{endpoint}/llm/generate",
    json=llm_payload,
    headers={"Authorization": f"Bearer {api_key}"},
)
```

### Structure prompts

```python
prompt = (
    "Analyze this log - is it a security alert or info?\n"
    "2026-05-22 12:00:01 auth ERROR Failed login for alice"
)
```

### Parse AI response

```python
result = resp.json()
print(result.get("output", "No AI response"))
```

---

## 💡 Quick Tips

- Start small, build up your workflow
- Treat logs as data, not just text
- Use `.env` for API keys (never hardcode)
- Use pandas for data analysis
- Wrap API calls in error handling
- Validate AI outputs before acting

---

## 📦 Install Required Packages

```bash
pip install requests pandas python-dotenv
```
