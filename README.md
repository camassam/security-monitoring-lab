# Security Monitoring and Threat Detection Lab

## Overview

This project demonstrates a basic security monitoring workflow using Python to analyse simulated authentication logs and identify potentially suspicious login activity.

The lab focuses on rule-based detection, reviewing alerts, exporting results to CSV, documenting findings, and understanding the limitations of simple detection logic.

All data is fictional and intended for educational purposes.

## Objectives

- Analyse authentication events using Python.
- Identify repeated failed login attempts.
- Detect successful logins following multiple authentication failures.
- Export detection alerts to a structured CSV report.
- Test detection logic using automated unit tests.
- Review alert results and possible explanations.
- Document findings and recommend investigation steps.
- Consider false positives and detection limitations.

## Project Structure

```text
security-monitoring-lab/
├── data/
│   └── authentication-logs.csv
├── scope/
│   └── assessment-scope.md
├── reports/
│   ├── alerts.csv
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

The detection script was executed against the 52 simulated authentication events.

| Metric | Result |
|---|---:|
| Authentication events analysed | 52 |
| Total alerts generated | 6 |
| Repeated failed-login alerts | 2 |
| Successful login after repeated failures alerts | 4 |

### Alert Summary

| Detection rule | Username | Source IP | Failed attempts |
|---|---|---|---:|
| Successful login after repeated failures | `j.smith` | `198.51.100.23` | 4 |
| Successful login after repeated failures | `j.smith` | `198.51.100.23` | 3 |
| Repeated failed logins | `a.patel` | `203.0.113.77` | 5 |
| Successful login after repeated failures | `m.chen` | `198.51.100.44` | 3 |
| Repeated failed logins | `admin` | `203.0.113.99` | 5 |
| Successful login after repeated failures | `r.jones` | `198.51.100.88` | 4 |

These alerts identify activity that met the configured detection thresholds. They are investigation leads, not confirmed security incidents.

## CSV Alert Export

The detection script automatically exports its generated alerts to a CSV file:

**[View the generated alert report](reports/alerts.csv)**

The CSV report contains the following columns:

| Column | Description |
|---|---|
| `rule` | Detection rule that generated the alert. |
| `username` | Account associated with the alert. |
| `ip` | Source IP address associated with the alert. |
| `count` | Number of failed attempts counted by the detection rule. |
| `start` | Start of the relevant detection window, or the earliest counted failure. |
| `end` | End of the detection window, or the successful login timestamp. |

The script creates the `reports/` directory if it does not already exist and writes the alert records to `reports/alerts.csv`.

Running the script again overwrites the existing CSV report with the latest results.

## Automated Tests

The detection logic is tested using Python's built-in `unittest` framework. Three automated tests were executed successfully.

| Test | Purpose | Result |
|---|---|---|
| `test_repeated_failed_logins` | Verifies that five failed login attempts within the configured five-minute window trigger a repeated-failure alert. | PASS |
| `test_success_after_repeated_failures` | Verifies that a successful login following at least three failed attempts within five minutes triggers an alert. | PASS |
| `test_normal_login_does_not_trigger_alert` | Verifies that a single failed login followed by a successful login does not generate an alert. | PASS |

**Test summary: 3 passed, 0 failed.**

The tests use synthetic authentication events and documentation-only IP addresses. They verify the expected behaviour for these scenarios but do not establish complete detection coverage or prove that the system is free from false positives.

## How to Run

### Requirements

- Python 3
- No third-party Python packages required

Run the following commands from the project directory.

### 1. Run the Detection Script and Generate the CSV Report

```bash
python3 detect_suspicious_logins.py
```

The script:

1. Loads the authentication events from `authentication-logs.csv`.
2. Applies the configured detection rules.
3. Prints generated alerts in Terminal.
4. Exports the alerts to `reports/alerts.csv`.

The current dataset produces 52 analysed events and six alerts.

Expected final output:

```text
Exported 6 alerts to reports/alerts.csv
```

The script expects `authentication-logs.csv` to be in the project root. If your dataset is stored inside `data/`, update the `LOG_FILE` setting in the script to match its actual location.

### 2. View the Exported Report

```bash
cat reports/alerts.csv
```

This displays the generated CSV report in Terminal.

### 3. Run the Automated Tests

```bash
python3 -m unittest -v test_detection.py
```

Expected summary:

```text
Ran 3 tests in ...
OK
```

An `OK` result indicates that all three tests passed.

### 4. Check Python Syntax

```bash
python3 -m py_compile detect_suspicious_logins.py test_detection.py
```

No output indicates that both Python files compiled successfully.

## Tools and Technologies

- **Python 3** — log analysis and detection logic.
- **CSV** — structured authentication data and alert reporting.
- **`unittest`** — automated testing.
- **macOS Terminal** — script execution and validation.
- **GitHub** — source control and project documentation.

## Repository Contents

- [Assessment Scope](scope/assessment-scope.md)
- [Authentication Log Dataset](data/authentication-logs.csv)
- [Python Detection Script](detect_suspicious_logins.py)
- [Automated Tests](test_detection.py)
- [Detection Results Report](reports/detection-results.md)
- [Exported Alert Report](reports/alerts.csv)

## Limitations

- The dataset is simulated and does not represent real authentication activity.
- The detection rules use fixed thresholds.
- Legitimate users who mistype their passwords may generate false positives.
- The analysis is limited to the available log fields.
- The rules may miss suspicious activity that does not meet their thresholds.
- Alerts do not establish malicious intent or account compromise.
- The tests cover three specific scenarios and do not represent exhaustive testing.
- No production systems or real user credentials were involved.

## Future Improvements

- Expand automated tests to cover additional detection scenarios and edge cases.
- Improve alert deduplication.
- Evaluate false positives using additional simulated datasets.
- Add detection for other suspicious authentication patterns.
- Document detection coverage and known limitations.
- Explore how these detection rules could be implemented in a SIEM platform.

## Ethical Considerations

This project uses fictional data and is designed for defensive security education.

The IP addresses are reserved for documentation and examples and must not be treated as real malicious indicators.

No production systems, third-party systems, or real user credentials were targeted or used.
