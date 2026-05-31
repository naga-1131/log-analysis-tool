import json
from datetime import datetime

def parse_log_file(path):
    entries = []
    stats = {"malformed": 0}

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()

            if not line:
                stats["malformed"] += 1
                continue

            try:
                if line.startswith("{"):
                    data = json.loads(line)
                    entries.append(data)
                    continue

                parts = line.split()

                if len(parts) < 6:
                    stats["malformed"] += 1
                    continue

                entries.append({
                    "timestamp": " ".join(parts[:2]) if "/" in parts[0] else parts[0],
                    "ip": parts[-5],
                    "method": parts[-4],
                    "path": parts[-3],
                    "status": parts[-2],
                    "response_time": parts[-1]
                })
            except Exception:
                stats["malformed"] += 1

    return entries, stats
