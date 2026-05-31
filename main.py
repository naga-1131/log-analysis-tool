from parser import parse_log_file
from analyzer import generate_report
import sys

if len(sys.argv) != 2:
    print("Usage: python src/main.py <log_file>")
    sys.exit(1)

entries, stats = parse_log_file(sys.argv[1])
print(generate_report(entries, stats))
