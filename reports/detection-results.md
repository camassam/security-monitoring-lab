# Authentication Log Analysis — Detection Results

## 1. Overview

This report documents the results of analysing simulated authentication logs using a custom Python detection script.

The objective was to identify potentially suspicious login activity, including repeated authentication failures and successful logins following multiple failures.

**Environment:** Local security monitoring lab  
**Dataset:** `data/authentication-logs.csv`  
**Analysis script:** `detect_suspicious_logins.py`  
**Events analysed:** 52  
**Alerts generated:** 6

All usernames, events, and IP addresses are simulated for educational purposes. The IP addresses belong to documentation-only address ranges and must not be treated as real attacker infrastructure.

## 2. Detection Rules

### Rule 1: Repeated Failed Logins

**Condition:** Five or more failed login attempts from the same username and source IP address within five minutes.

**Purpose:** Identify potential brute-force activity or repeated password-guessing attempts.

### Rule 2: Successful Login After Repeated Failures

**Condition:** A successful login following at least three failed attempts for the same username and source IP address within five minutes.

**Purpose:** Identify authentication sequences that may warrant investigation for possible account compromise.

## 3. Results

### 3.1 Repeated Failed Logins

Two alerts were generated.

| Username | Source IP | Failed Attempts | Time Window (UTC) |
|---|---|---:|---|
| `a.patel` | `203.0.113.77` | 5 | 10:24:39–10:26:12 |
| `admin` | `203.0.113.99` | 5 | 09:40:26–09:42:02 |

**Assessment:** Both events meet the configured detection threshold. Repeated authentication failures against an administrative account may warrant particular attention, but the available data does not establish malicious intent.

### 3.2 Successful Login After Repeated Failures

Four alerts were generated.

| Username | Source IP | Failed Attempts | Time Window (UTC) |
|---|---|---:|---|
| `j.smith` | `198.51.100.23` | 4 | 09:04:11–09:05:47 |
| `j.smith` | `198.51.100.23` | 3 | 09:52:43–09:54:02 |
| `m.chen` | `198.51.100.44` | 3 | 10:42:07–10:43:20 |
| `r.jones` | `198.51.100.88` | 4 | 10:07:31–10:09:10 |

**Assessment:** These sequences show multiple failed authentication attempts followed by successful authentication from the same source IP address. Possible explanations include repeated incorrect password entry, password guessing, or other authentication issues. Additional evidence would be required to determine the cause.

## 4. Key Findings

- The Python script successfully processed 52 simulated authentication events.
- The two detection rules generated six alerts in total.
- Two alerts met the repeated-failure threshold.
- Four alerts met the successful-login-after-failures condition.
- The results demonstrate how simple rule-based monitoring can identify patterns for further investigation.

The six alerts are not necessarily six separate security incidents, and none should be considered a confirmed compromise based on this dataset alone.

## 5. Recommended Investigation Steps

If these patterns appeared in a real environment, an analyst could:

1. Review authentication events immediately before and after each alert.
2. Check whether the affected users recognise the activity.
3. Review additional identity-provider or authentication logs for context.
4. Determine whether multifactor authentication was used and whether any additional security controls were triggered.
5. Correlate findings with other available telemetry before deciding whether to escalate.
6. Document the investigation, conclusions, and any actions taken.

These are recommended investigative steps, not actions performed during this lab.

## 6. Limitations

- The dataset is simulated and does not represent real user activity.
- The analysis is limited to the fields present in the CSV file.
- The rules use fixed thresholds that may not suit every environment.
- Legitimate users can generate repeated failures, resulting in false positives.
- The rules may miss suspicious activity that does not meet the configured thresholds.
- The script does not establish whether an account was compromised.
- The documentation-only IP addresses cannot be used to identify real attackers.

## 7. Conclusion

The lab demonstrates a basic authentication monitoring workflow using Python, CSV data, and rule-based detection.

The script identified repeated failed logins and successful logins following multiple failures. The results provide a foundation for further development, including improved alert deduplication, automated test cases, and structured output for security investigations.

All findings remain unconfirmed simulated alerts rather than evidence of real-world compromise.
