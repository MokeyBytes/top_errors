#!/usr/bin/env python3
"""
Simple script to parse systemd logs (journalctl) for repeated error/fail/warning messages.
Displays the top 10 repeated lines, color-coded for easy viewing.
"""

import subprocess
import re
import sys
from collections import Counter

def get_journal_lines():
    """
    Fetch logs from the current boot using journalctl. 
    If you want to limit logs further (e.g. only 'error' priority), 
    adjust the journalctl command accordingly.
    """
    # '-b' means logs from the current boot.
    # '--no-pager' ensures it doesn't prompt for pagination.
    cmd = ["journalctl", "-b", "--no-pager"]
    
    try:
        output = subprocess.check_output(cmd, universal_newlines=True)
        return output.splitlines()
    except FileNotFoundError:
        print("Error: journalctl not found on this system.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to run journalctl: {e}")
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
    lines = get_journal_lines()

    # Regex pattern to find lines containing 'error', 'fail', or 'warning' (case-insensitive)
    pattern = re.compile(r"(error|fail|warning)", re.IGNORECASE)

    # Filter lines
    relevant_lines = [line.strip() for line in lines if pattern.search(line)]

    # Count each repeated line
    counter = Counter(relevant_lines)
    most_common_errors = counter.most_common(10)

    if not most_common_errors:
        print("No errors/warnings found in journalctl logs.")
        return

    print("Top 10 most frequent error/warning messages:\n")
    for message, freq in most_common_errors:
        print(f"({freq}x) {colorize(message)}")

if __name__ == "__main__":
    main()
