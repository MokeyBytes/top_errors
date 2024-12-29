# Journalctl Parser

A simple Python script to parse systemd (journalctl) logs for repeated error/fail/warning messages.  
It color-codes the output for easier reading and displays the top 10 repeated log lines.

> **Why use this script?**  
> - Quickly identify and count the most frequent errors or warnings in your system logs.  
> - Speed up troubleshooting by focusing on the messages that matter.  
> - Works out-of-the-box on most Linux distributions that use `systemd`.

---

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Customization](#customization)
6. [License](#license)

---

## Requirements

- **Python 3** (script uses `#!/usr/bin/env python3`)
- **systemd** (the script relies on `journalctl`)
- A Linux distribution with `journalctl` available (e.g., Ubuntu, Debian, Fedora, Arch)

---

## Installation

1. **Clone or Download** this repository:

   ```bash
   git clone https://github.com/your-username/top_errors.git
   cd top_errors

    Make the script executable (optional):

```
chmod +x parse_journal.py
```

(Optional) Create a virtual environment if you want to isolate dependencies:
```
    python3 -m venv venv
    source venv/bin/activate
```

No additional Python dependencies are required for this script, so this step is entirely optional.

## Usage

Run the script directly:
```
python3 parse_journal.py
```
Or if you made it executable:
```
./parse_journal.py
```
Output example (if errors/warnings/fail messages exist):

Top 10 most frequent error/warning messages:

(5x) [red text] Some error message
(3x) [red text] Another failure message
(2x) [yellow text] A warning message

If no relevant logs are found, the script will display:

No errors/warnings found in journalctl logs.

How It Works

    Fetch logs from the current systemd boot using:

    journalctl -b --no-pager

    Filter lines for error, fail, or warning (case-insensitive).
    Count occurrences of each matching line.
    Sort them by frequency and display the top 10.
    Color-code each line:
        Red if it contains error or fail.
        Yellow if it contains warning.

    Tip: If you want to capture older boots or more specific log levels, modify the journalctl command in the get_journal_lines function.

Customization

    Change the number of top messages:
    Edit the line:

most_common_errors = counter.most_common(10)

and replace 10 with the desired number.

Use different search terms:
Update the pattern in main() to catch different or additional keywords:

    pattern = re.compile(r"(error|fail|warning|critical)", re.IGNORECASE)

    Customize colors:
    Inside the colorize function, you can replace \033[91m (red) or \033[93m (yellow) with other ANSI color codes.

License

This project is distributed under the MIT License.
Feel free to use, modify, and distribute this script as you see fit.
