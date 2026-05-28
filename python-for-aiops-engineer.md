# Python for AIOps Engineers

This guide provides a quick AI-first start for AIOps engineers using Python to analyze logs, call APIs, process JSON, and build reliable automation.

## Session 0: Quick Start (AI First Approach)

This session starts with an AI-first example: calling an LLM from Python, handling the JSON response, and printing the result.

### Call an LLM API using Python

This example shows how to read the API key from an environment variable, send a prompt to an LLM endpoint, and parse the JSON response.

```python
import os
import requests

api_key = os.getenv("AIOPS_API_KEY")
endpoint = os.getenv("AIOPS_ENDPOINT", "https://api.example.com/v1")

payload = {
    "model": "gpt-4o-mini",
    "input": "Summarize the following log entry: Failed login for alice on auth service",
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

If the call succeeds, `result` will be a dictionary. A real response often includes fields like `id`, `status`, and the generated `output`.

### Understand the JSON response

This block shows how to inspect the response structure and verify the data before using it.

```python
# Example response structure
# {
#   "id": "abc123",
#   "output": "Summary text...",
#   "status": "success"
# }

ai_data = result
print(type(ai_data))           # <class 'dict'>
print("Response keys:", ai_data.keys())
print(ai_data.get("output"))  # The generated summary text
```

### Print AI output

```python
print("AI summary:", ai_data.get("output", "No output returned"))
```

---

## Section 1: Python Core (Minimal Required)

This section covers the minimal Python building blocks used in AIOps scripts: variables, strings, collections, and type checks.

### Variables

Variables store values in memory. In AIOps scripts, variables often represent counters, service names, or status flags.

```python
count = 12               # int
service = "auth"        # str
is_alerting = False       # bool
```

### Strings & basic operations

Strings are text values. You can combine them, change case, and measure their length.

```python
message = "error count"
status = service + ": " + message
print(status.upper())         # ERROR COUNT
print(len(message))           # 11
```

This shows string concatenation, converting text to uppercase, and counting characters.

### Lists `[ ]`

Lists hold ordered collections of items. In AIOps, a list often contains log lines, metric samples, or event records.

```python
logs = [
    "2026-05-22 12:00:01 auth ERROR Failed login",
    "2026-05-22 12:00:05 auth INFO User authenticated",
]
print(len(logs))              # 2
print(logs[0])                # First log line
```

### Dictionaries `{ }`

Dictionaries store key/value pairs, which is perfect for JSON-like records from logs or APIs.

```python
event = {
    "timestamp": "2026-05-22T12:00:01Z",
    "service": "auth",
    "level": "ERROR",
    "message": "Failed login",
}
print(event["service"])      # auth
print(event.get("level"))   # ERROR
```

### Type checking

Use `type()` to confirm the data type of a variable, especially when parsing logs or JSON.

```python
print(type(count))         # <class 'int'>
print(type(service))       # <class 'str'>
print(type(is_alerting))   # <class 'bool'>
print(type(logs))          # <class 'list'>
print(type(event))         # <class 'dict'>
```

---

## Section 2: Control Flow for System Thinking

Control flow lets you make decisions, iterate through data, and build monitoring loops for operational systems.

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
    print(f"Checking system status, attempt {retry + 1}")
    retry += 1
```

### break / continue

```python
for line in logs:
    if "INFO" in line:
        continue
    if "CRITICAL" in line:
        print("Critical event found")
        break
    print("Processing", line)
```

---

## Section 3: Functions for Reusability

Functions keep logic reusable and easier to maintain, which is critical when analyzing logs or calling APIs repeatedly.

### def functions

This function converts a text log line into a structured dictionary. It expects the log to use a fixed format such as:

```text
2026-05-22 12:00:01 auth ERROR Failed login for alice
```

The first tokens are date/time, service name, and log level, followed by the full message text.

```python
def parse_log_line(line):
    # Example supported log format:
    # 2026-05-22 12:00:01 auth ERROR Failed login for alice

    # Split the log line on spaces into separate words
    parts = line.split(" ")

    # Build a dictionary from the common log layout
    return {
        "timestamp": parts[0] + " " + parts[1],  # first two tokens are date and time
        "service": parts[2],                       # third token is service name
        "level": parts[3],                         # fourth token is log level
        "message": " ".join(parts[4:]),          # remaining tokens form the log message
    }
```

### Parameters & return values

This function checks whether a parsed log entry is an error or critical event. It takes one argument (`entry`), which should be the dictionary returned by `parse_log_line`, and returns `True` or `False`.

```python
def is_error(entry):
    return entry.get("level") in {"ERROR", "CRITICAL"}

parsed = parse_log_line(logs[0])
print("Parsed entry:", parsed)
print("Is error event?", is_error(parsed))
```

### Reusable log analysis functions

This function processes a list of raw log lines, parses each line, and returns only the entries that are errors. It demonstrates how to combine smaller reusable functions into a simple log filter.

```python
def filter_errors(log_lines):
    parsed = [parse_log_line(line) for line in log_lines]
    return [entry for entry in parsed if is_error(entry)]

errors = filter_errors(logs)
print("Error entries:", errors)
```

---

## Section 4: Working with Real Data (AIOps Core)

This section shows how to handle real operational data sources like CSV, logs, and JSON payloads from APIs.

### Reading CSV files

This example loads a CSV file into a list of dictionaries, where each row becomes one record.

```python
import csv

with open("metrics.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    print("Loaded rows:", len(rows))
    print(rows[:3])
```

### Parsing logs (string-based)

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

### Working with JSON (API responses)

```python
import json

body = '{"service": "web", "status": "ok", "count": 125}'
obj = json.loads(body)
print(obj["service"])
obj["status"] = "degraded"
print(json.dumps(obj, indent=2))
```

---

## Section 5: API Interaction (Critical)

AIOps scripts must interact with external services. This section explains GET and POST requests, JSON parsing, and API error handling.

### Using requests library

```python
import requests

url = "https://api.example.com/health"
response = requests.get(url)
```

### GET request

This demonstrates a basic API health check. If the endpoint returns HTTP 200, the JSON body is parsed and printed.

```python
if response.status_code == 200:
    data = response.json()
    print("OK", data)
else:
    print("GET failed", response.status_code)
```

### POST request

A POST request is useful for sending alerts or event data to a service. Here the payload is sent as JSON.

```python
payload = {"service": "auth", "state": "warning"}
post_resp = requests.post(
    "https://api.example.com/alert",
    json=payload,
    headers={"Authorization": f"Bearer {api_key}"},
)
print("POST status:", post_resp.status_code)
print("Response body:", post_resp.text)
```

### Handling JSON responses

```python
try:
    result = response.json()
except ValueError:
    result = {}
print(result)
```

### Error handling for APIs

Always handle HTTP errors to avoid crashes and to log useful diagnostics.

```python
try:
    response.raise_for_status()
except requests.HTTPError as exc:
    print("API error:", exc)
    print("Response code:", response.status_code)
    print("Response body:", response.text)
```
```

---

## Section 6: Environment & Security

Environment variables and secure handling of API keys are essential for safe AIOps automation in production.

### Environment variables

```python
import os

api_key = os.getenv("AIOPS_API_KEY")
endpoint = os.getenv("AIOPS_ENDPOINT", "https://api.example.com/v1")
```

### API key management

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

### Secure coding practices

- never hardcode secrets
- validate all external input
- avoid printing raw API keys
- fail safely and log only non-sensitive details

---

## Section 7: Data Analysis Basics for AIOps

Pandas gives you a powerful way to explore log and metric data with tabular operations and aggregations.

### Introduction to Pandas

Pandas is a Python library used for data analysis and manipulation. Here, we build a DataFrame from a list of records to treat logs and metrics as structured data.

```python
import pandas as pd

df = pd.DataFrame([
    {"timestamp": "2026-05-22T12:00:01Z", "level": "ERROR", "service": "auth", "cpu": 70},
    {"timestamp": "2026-05-22T12:00:05Z", "level": "INFO", "service": "auth", "cpu": 55},
])
print(df.head())
```

This prints the table and shows how each log becomes a row with named columns.

### Load CSV → DataFrame

Use `pd.read_csv` to load a CSV file directly into a DataFrame.

```python
df = pd.read_csv("metrics.csv")
print("Columns:", df.columns.tolist())
print(df.head())
```

This lets you work with CSV data using the same row-and-column model as a spreadsheet.

### Filtering rows

Filtering keeps only the rows that match a condition, such as error-level logs.

```python
errors = df[df["level"] == "ERROR"]
print("Error rows:", len(errors))
print(errors)
```

### Basic aggregation

Aggregation summarizes columns across many rows, which is useful for monitoring average CPU and event counts.

```python
counts = df["level"].value_counts()
print("Log counts by level:\n", counts)

mean_cpu = df["cpu"].mean()
print("Mean CPU", mean_cpu)
```

---

## Section 8: Time-Series & Metrics Thinking

AIOps works with metric streams and log timestamps. This section introduces time-series analysis and trend detection.

### CPU / Memory / Logs as time-series

Convert timestamp text into a datetime index so you can analyze metrics by time windows.

```python
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.set_index("timestamp").sort_index()
print(df["cpu"].resample("1T").mean())
```

This resamples the CPU values into one-minute buckets and computes the average for each minute.

### Detect spikes and trends

A series of values can reveal spikes, drops, and trends when viewed across time.

```python
cpu_series = df["cpu"].resample("1T").mean().fillna(0)
print("Latest CPU values:\n", cpu_series.tail())
```

### Simple threshold-based alerts

```python
threshold = 80
spikes = cpu_series[cpu_series > threshold]
print("CPU spikes:", spikes)
```

---

## Section 9: Basic Anomaly Detection Logic

Anomaly detection helps you flag unusual events in logs and metrics using simple statistical rules.

### Average-based anomaly detection

This simple rule flags values that are far above the recent average, which often indicates a spike.

```python
avg = cpu_series.mean()
std = cpu_series.std()
alert_threshold = avg + 2 * std
anomalies = cpu_series[cpu_series > alert_threshold]
print("Mean:", avg)
print("Std Dev:", std)
print("Anomaly points:\n", anomalies)
```

### Threshold detection

```python
hard_threshold = 90
threshold_alerts = cpu_series[cpu_series > hard_threshold]
print(threshold_alerts)
```

### Pattern-based detection

```python
if cpu_series.diff().abs().max() > 50:
    print("Sudden surge detected")
```

---

## Section 10: CLI Tools for AIOps Engineers

CLI tools make your AIOps scripts flexible and reusable by allowing configuration without changing source code.

### sys.argv

`sys.argv` contains the list of command-line arguments passed to the script. The first element is the script name.

```python
import sys

print(sys.argv)
```

If you run `python script.py --source logs.csv`, `sys.argv` will contain `['script.py', '--source', 'logs.csv']`.

### argparse

`argparse` parses arguments and provides helpful usage messages.

```python
import argparse

parser = argparse.ArgumentParser(description="AIOps CLI analyzer")
parser.add_argument("--log", default="/var/log/app.log")
parser.add_argument("--threshold", type=int, default=5)
args = parser.parse_args()
print("Log file:", args.log)
print("Threshold:", args.threshold)
```

Use `python script.py --log my.log --threshold 10` to pass values without changing code.

### Build CLI log analyzer tool

```python
def main():
    parser = argparse.ArgumentParser(description="Analyze logs and alert on anomalies")
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

---

## Section 11: Error Handling & Reliability

Robust scripts handle runtime failures cleanly and provide useful feedback when something goes wrong.

### try / except

```python
try:
    value = int("not-a-number")
except ValueError as exc:
    print("Parse error:", exc)
```

### Handling runtime failures

```python
try:
    with open("missing.log") as f:
        data = f.read()
except FileNotFoundError:
    print("Log file not found")
```

### Logging errors in scripts

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    response = requests.get(endpoint)
    response.raise_for_status()
except requests.RequestException as exc:
    logger.error("API request failed: %s", exc)
```

---

## Section 12: External Packages & Ecosystem

External packages extend Python with requests, pandas, and dotenv support; use package management to keep deployments stable.

### pip install

```bash
pip install requests pandas python-dotenv
```

### requirements.txt

```
requests
pandas
python-dotenv
```

### Package management basics

- use virtual environments with `python -m venv venv`
- keep `requirements.txt` in source control
- pin versions when needed for production

---

## Section 13: Introduction to AI Integration

This section shows how to send structured prompts to LLM APIs and parse the model response safely.

### Sending prompts to LLM APIs

```python
prompt = "Classify this log entry: Failed login for alice on auth service"
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

### Structuring prompts

```python
prompt = (
    "Analyze the following log and suggest whether it is a security alert or informational event:\n"
    "2026-05-22 12:00:01 auth ERROR Failed login for alice"
)
```

### Parsing AI responses

```python
result = resp.json()
print(result.get("output", "No AI response"))
```

---

## Practical Notes

- Start with small scripts and build up your AIOps workflow.
- Treat logs as data, not just text.
- Keep API keys out of code by using environment variables and `.env` files.
- Use pandas for data exploration and simple anomaly detection.
- Wrap API calls and file I/O in error handling.
- Use AI to accelerate incident understanding, but validate outputs before acting.
