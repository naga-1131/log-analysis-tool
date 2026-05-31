# Log Analyzer

## Requirements
- Python 3.10+

## Installation

```bash
pip install -r requirements.txt
```

## Run the analyzer

```bash
python src/main.py <log_file_path>
```

Example:

```bash
python src/main.py logs/server.log
```

## Generate test data

```bash
python scripts/generate_logs.py
```

This will create a sample log file containing:
- Standard log entries
- Different timestamp formats
- Different response-time formats
- Missing status codes
- JSON log entries
- Malformed lines
- Blank lines
