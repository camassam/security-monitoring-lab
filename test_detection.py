import unittest
from datetime import datetime, timezone

from detect_suspicious_logins import detect_alerts


def make_event(username, ip, minute, second, status):
    timestamp = datetime(2026, 10, 26, 10, minute, second, tzinfo=timezone.utc)
    return {
        "username": username,
        "source_ip": ip,
        "event_type": "login",
        "status": status,
        "timestamp": timestamp.isoformat().replace("+00:00", "Z"),
        "time": timestamp,
    }


class TestSuspiciousLoginDetection(unittest.TestCase):

    def test_repeated_failed_logins(self):
        logs = [
            make_event("alice", "203.0.113.10", 0, 0, "failure"),
            make_event("alice", "203.0.113.10", 0, 30, "failure"),
            make_event("alice", "203.0.113.10", 1, 0, "failure"),
            make_event("alice", "203.0.113.10", 1, 30, "failure"),
            make_event("alice", "203.0.113.10", 2, 0, "failure"),
        ]

        alerts = detect_alerts(logs)

        self.assertTrue(any(
            alert["rule"] == "Repeated failed logins"
            for alert in alerts
        ))

    def test_success_after_repeated_failures(self):
        logs = [
            make_event("bob", "198.51.100.10", 0, 0, "failure"),
            make_event("bob", "198.51.100.10", 0, 30, "failure"),
            make_event("bob", "198.51.100.10", 1, 0, "failure"),
            make_event("bob", "198.51.100.10", 1, 30, "success"),
        ]

        alerts = detect_alerts(logs)

        self.assertTrue(any(
            alert["rule"] == "Successful login after repeated failures"
            for alert in alerts
        ))

    def test_normal_login_does_not_trigger_alert(self):
        logs = [
            make_event("carol", "192.0.2.10", 0, 0, "failure"),
            make_event("carol", "192.0.2.10", 1, 0, "success"),
        ]

        alerts = detect_alerts(logs)

        self.assertEqual(alerts, [])


if __name__ == "__main__":
    unittest.main()
