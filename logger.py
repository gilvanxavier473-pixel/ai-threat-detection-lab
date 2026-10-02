import json
from datetime import datetime, timezone
from pathlib import Path

LOG_FILE = Path("logs/security_events.jsonl")

def log_event(user_input: str, result: dict) -> dict:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input": user_input,
        "detected": result["detected"],
        "threat_type": result["type"],
        "severity": result["severity"],
        "action": "BLOCKED" if result["detected"] else "ALLOWED",
    }

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event, ensure_ascii=False) + "\n")

    return event

def read_events() -> list[dict]:
    if not LOG_FILE.exists():
        return []

    events = []
    with LOG_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                events.append(json.loads(line))
    return events
