# ANSWERS.md

## 1. How to run

Requirements:
- Python 3.10+

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/main.py <log_file_path>
```

Generate sample logs:

```bash
python scripts/generate_logs.py
```

---

## 2. Stack choice

I chose Python because it provides excellent support for text processing, file handling, regular expressions, JSON parsing, and rapid development.

A worse choice would have been a frontend-only framework such as React because the primary challenge is backend log processing rather than UI rendering.

---

## 3. One real edge case

Edge Case:
Malformed log lines and partial stack-trace entries.

File:
src/parser.py

Line:
(Replace with actual line number after implementation.)

Handling:
The parser catches parsing failures, increments a malformed-line counter, logs the issue, and continues processing.

Without this handling:
The application could terminate early and fail to analyze the remainder of the log file.

---

## 4. AI usage

Tool:
ChatGPT

Usage:
- Generated initial project structure ideas.
- Suggested parsing strategies for mixed log formats.
- Suggested README and ANSWERS.md templates.

Modification:
The generated parser logic was reviewed and modified to improve error handling and support additional timestamp formats.

Reason:
The original suggestion did not fully address malformed entries and mixed-format logs.

---

## 5. Honest gap

Current limitation:
The tool performs analysis on a single machine and keeps statistics in memory.

Improvement with another day:
- Add streaming analytics for very large files.
- Add export formats (JSON/CSV).
- Add a web dashboard with charts and filtering.
