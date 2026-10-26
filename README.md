# Security Monitoring and Threat Detection Lab

## Overview

This project demonstrates a basic security monitoring workflow using Python to analyse simulated authentication logs and identify potentially suspicious login activity.

The lab focuses on rule-based detection, reviewing alerts, documenting findings, and understanding the limitations of simple detection logic.

All data is fictional and intended for educational purposes.

## Objectives

- Analyse authentication events using Python.
- Identify repeated failed login attempts.
- Detect successful logins following multiple authentication failures.
- Review alert results and possible explanations.
- Document findings and recommend investigation steps.
- Test detection logic using automated unit tests.
- Consider false positives and detection limitations.

## Project Structure

```text
security-monitoring-lab/
├── data/
│   └── authentication-logs.csv
├── scope/
│   └── assessment-scope.md
├── reports/
│   └── detection-results.md
├── detect_suspicious_logins.py
├── test_detection.py
└── README.md
```

## Dataset

The dataset contains 52 simulated authentication events with the following fields:

| Field | Description |
|---|---|
| `timestamp` | Time of the authentication event in UTC. |
| `username` | Fictional account name associated with the event. |
| `source_ip` | Documentation-only source IP address. |
| `event_type` | Type of event recorded. |
| `status` | Authentication outcome, such as success or failure. |

The dataset is designed to demonstrate detection logic and does not represent real user activity or real attacker infrastructure.

## Detection Rules

### Rule 1: Repeated Failed Logins

Detects five or more failed login attempts from the same username and source IP address within a five-minute window.

**Purpose:** Identify potential password-guessing or brute-force activity that may require further investigation.

### Rule 2: Successful Login After Repeated Failures

Detects a successful login following at least three failed attempts for the same username and source IP address within five minutes.

**Purpose:** Identify authentication sequences that may warrant investigation for possible account compromise.

These rules identify potentially suspicious patterns. They do not independently prove malicious activity or account compromise.

## Detection Results

The detection script was run against the 52 simulated authentication events.

| Metric | Result |
|---|---:|
| Authentication events analysed | 52 |
| Total alerts generated | 6 |
| Repeated failed-login alerts | 2 |
| Successful login after repeated failures alerts | 4 |

The alerts identified authentication patterns that met the configured thresholds.

These results are based on synthetic data. Each alert would require further investigation in a real security monitoring environment before drawing conclusions about malicious activity.

See the [Detection Results Report](reports/detection-results.md) for additional findings and recommendations.

## Automated Tests

The detection logic is tested using Python's built-in `unittest` framework. Three automated tests were executed successfully.

| Test | Purpose | Result |
|---|---|---|
| `test_repeated_failed_logins` | Verifies that five failed login attempts within the configured five-minute window trigger a repeated-failure alert. | PASS |
| `test_success_after_repeated_failures` | Verifies that a successful login following at least three failed attempts within five minutes triggers an alert. | PASS |
| `test_normal_login_does_not_trigger_alert` | Verifies that a single failed login followed by a successful login does not generate an alert. | PASS |

**Test summary: 3 passed, 0 failed.**

The tests use synthetic authentication events and documentation-only IP addresses. They verify the expected behaviour for these specific scenarios, but do not establish complete detection coverage or prove that the system is free from false positives.

## How to Run

### Requirements

- Python 3
- No third-party Python packages required

Run the following commands from the project directory.

### 1. Run the Detection Script

```bash
python3 detect_suspicious_logins.py
```

The script reads the authentication log CSV, analyses the events using the configured detection rules, and prints any generated alerts.

The script expects the CSV file to be named `authentication-logs.csv` in the project directory. If the dataset is stored in the `data/` folder, update the `LOG_FILE` setting in the script accordingly.

### 2. Run the Automated Tests

```bash
python3 -m unittest -v test_detection.py
```

The test runner displays the result of each test individually.

Expected summary:

```text
Ran 3 tests in ...
OK
```

The exact execution time may vary. An `OK` result indicates that all three tests passed.

### 3. Check Python Syntax

```bash
python3 -m py_compile detect_suspicious_logins.py test_detection.py
```

No output indicates that both
