# top_errors, a Journalctl Log Analyzer

This Python script parses system logs (`journalctl`) to identify repeated error, failure, or warning messages. It highlights the top 10 most frequent entries, making troubleshooting easier by focusing on recurring issues.

## Features

- Fetches logs from the current system boot.
- Identifies and counts occurrences of keywords (`error`, `fail`, `warning`).
- Outputs results color-coded for easier readability:
  - **Red** for `error` and `fail` messages.
  - **Yellow** for `warning` messages.

---

## Requirements

- **Python 3**
- A Linux distribution that uses **systemd** (and supports `journalctl`).
- Basic system permissions to access system logs.

---

## Tutorial

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/journalctl-log-analyzer.git
cd journalctl-log-analyzer
```

### 2. Make the Script Executable

```bash
chmod +x top_errors.py
```

### 3. Run the Script

#### Basic Usage:
```bash
./top_errors.py
```

#### Run with Python Directly:
```bash
python3 top_errors.py
```

#### To Access Restricted Logs:
Run with `sudo` if necessary:
```bash
sudo ./top_errors.py
```

---

## Example Output

If the system logs contain relevant messages, you will see something like this:

```
Top 10 most frequent error/warning messages:

(12x) [91mFailed to start NetworkManager.service.[0m
(8x) [91mError: Disk quota exceeded.[0m
(5x) [93mWarning: CPU temperature high.[0m
(3x) [91mUnable to fetch updates.[0m
```

If no errors or warnings are found:

```
No errors/warnings found in journalctl logs.
```

---

## How It Works

1. **Fetch Logs**: Uses the `journalctl` command to retrieve logs from the current system boot.
2. **Filter Relevant Messages**: Searches for lines containing the keywords `error`, `fail`, or `warning` (case-insensitive).
3. **Count Occurrences**: Counts the number of times each matching line appears.
4. **Sort and Display**: Displays the top 10 most frequent messages, highlighting severity using ANSI color codes.

---

## Customization

- **Change the Number of Messages Displayed**:  
  Modify the following line in the script to adjust the number of displayed results:
  ```python
  most_common_errors = counter.most_common(10)
  ```

- **Add More Keywords**:  
  Extend the search pattern in the script:
  ```python
  pattern = re.compile(r"(error|fail|warning|critical|alert)", re.IGNORECASE)
  ```

- **Customize Colors**:  
  Update the `colorize` function to use different ANSI color codes:
  ```python
  return f"\033[94m{line}\033[0m"  # Example: Blue for warnings
  ```

---

## Troubleshooting

- **`journalctl` Not Found**:
  Ensure your system uses `systemd`. Non-systemd distributions are not supported.

- **Permission Denied**:
  Use `sudo` to access restricted logs.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it.

---

Happy troubleshooting!

