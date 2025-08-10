#!/usr/bin/env python3
"""
Simple script to parse systemd logs (journalctl) for repeated error/fail/warning messages.
Displays the top 10 repeated lines, color-coded for easy viewing.
"""

import subprocess
import sys
from collections import Counter

def get_journal_lines():
    """
    Fetch logs from the current boot using journalctl (streaming to reduce memory).
    """
    cmd = ["journalctl", "-b", "--no-pager"]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    except FileNotFoundError:
        print("Error: journalctl not found on this system.")
        sys.exit(1)

    try:
        for line in proc.stdout:
            yield line.rstrip("\n")
    finally:
        stderr = proc.stderr.read()
        retcode = proc.wait()
        if retcode != 0:
            msg = stderr.strip() or f"journalctl exited with code {retcode}"
            print(f"Error: Failed to run journalctl: {msg}")
            sys.exit(1)

def colorize(line):
    """
    Return the log line string with color codes based on severity keywords.
    """
    lowercase_line = line.lower()
    if "error" in lowercase_line or "fail" in lowercase_line:
        # Red
        return f"\033[91m{line}\033[0m"
    elif "warning" in lowercase_line:
        # Yellow
        return f"\033[93m{line}\033[0m"
    else:
        # No color
        return line

def main():
    counter = Counter()

    # Faster than regex: simple substring checks on lowercase
    for line in get_journal_lines():
        stripped = line.strip()
        lower = stripped.lower()
        if ("error" in lower) or ("fail" in lower) or ("warning" in lower):
            counter[stripped] += 1

    most_common_errors = counter.most_common(10)

    if not most_common_errors:
        print("No errors/warnings found in journalctl logs.")
        return

    print("Top 10 most frequent error/warning messages:\n")
    for message, freq in most_common_errors:
        print(f"({freq}x) {colorize(message)}")

if __name__ == "__main__":
    main()
