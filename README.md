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
└── README.md
```

## Dataset

The dataset contains 52 simulated authentication events with the following fields:

- `timestamp` — time of the authentication event.
- `username` — fictional account name.
- `source_ip` — documentation-only source IP address.
- `event_type` — type of event.
- `status` — authentication outcome.

The dataset is designed to demonstrate detection logic and does not represent real user activity or real attacker infrastructure.

## Detection Rules

### Rule 1: Repeated Failed Logins

Detects five or more failed login attempts from the same username and source IP address within five minutes.

**Purpose:** Identify potential password-guessing or brute-force activity.

### Rule 2: Successful Login After Repeated Failures

Detects a successful login following at least three failed attempts for the same username and source IP address within five minutes.

**Purpose:** Identify authentication sequences that may warrant investigation for possible account compromise.

## Results

The Python script processed 52 authentication events and generated six alerts:

| Detection rule | Alerts |
|---|---:|
| Repeated failed logins | 2 |
| Successful login after repeated failures | 4 |
| **Total** | **6** |

These are simulated alerts, not confirmed security incidents. Legitimate user behaviour can also trigger detection rules.

## Tools and Technologies

- Python 3
- CSV log analysis
- Rule-based threat detection
- macOS Terminal
- GitHub for version control and documentation

## Repository Contents

- [Assessment scope](scope/assessment-scope.md)
- [Authentication log dataset](data/authentication-logs.csv)
- [Python detection script](detect_suspicious_logins.py)
- [Detection results report](reports/detection-results.md)

## Limitations

- The dataset is simulated.
- The rules use fixed thresholds.
- False positives are possible.
- The analysis is limited to the available log fields.
- Alerts do not establish malicious intent or account compromise.
- No production systems or real user credentials were involved.

## Future Improvements

- Add automated test cases for detection rules.
- Improve alert deduplication.
- Export alerts to a structured CSV report.
- Add detection for other suspicious authentication patterns.
- Document false-positive testing and detection coverage.

## Ethical Considerations

This project uses fictional data and is designed for defensive security education. The IP addresses are reserved for documentation and examples and must not be treated as real malicious indicators.
