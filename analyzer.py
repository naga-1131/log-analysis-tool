from collections import Counter

def generate_report(entries, stats):
    status_counter = Counter()

    for e in entries:
        status = str(e.get("status", "-"))
        status_counter[status] += 1

    lines = []
    lines.append("LOG ANALYSIS REPORT")
    lines.append("=" * 20)
    lines.append(f"Valid Entries: {len(entries)}")
    lines.append(f"Malformed Entries: {stats['malformed']}")
    lines.append("")

    lines.append("Status Codes")
    for code, count in status_counter.items():
        lines.append(f"{code}: {count}")

    return "\n".join(lines)
