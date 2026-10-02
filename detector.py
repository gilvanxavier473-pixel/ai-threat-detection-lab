import re

RULES = {
    "prompt_injection": [
        r"ignore\s+.*rules",
        r"ignore\s+.*instructions",
        r"bypass\s+.*security",
    ],
    "command_execution": [
        r"execute\s+.*command",
        r"run\s+.*command",
    ],
    "unauthorized_access": [
        r"access\s+.*server",
        r"access\s+.*system",
    ],
}

SEVERITY = {
    "prompt_injection": "MEDIUM",
    "command_execution": "HIGH",
    "unauthorized_access": "HIGH",
}

def detect_threat(user_input: str) -> dict:
    text = user_input.lower()

    for threat_type, patterns in RULES.items():
        for pattern in patterns:
            if re.search(pattern, text):
                return {
                    "detected": True,
                    "type": threat_type,
                    "severity": SEVERITY[threat_type],
                }

    return {"detected": False, "type": "none", "severity": "LOW"}
