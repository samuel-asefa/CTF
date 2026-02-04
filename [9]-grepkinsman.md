# grep is Your Kinsman

**Category:** Warmup  
**Points:** 10  
**Difficulty:** Easy

## Description

A flag... hidden in Shakespeare?!

If only you had access to a Global Regular Expression Processor like [this](shakespeare.txt)!

It is possible to do this problem with a simple text search, but expect more complicated grep in all CTF competitions and consider learning to do this one with grep. Here is a [nice tutorial](https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/).

## Learning Objectives

- Learn to use `grep` for text searching
- Understand regular expressions basics
- Practice command-line tools
- Search through large text files efficiently

## Hints

- grep stands for "Global Regular Expression Print"
- Use `grep` to search for patterns in files
- The flag format is `flag{something}`
- Try searching for "flag{" in the shakespeare.txt file
- On Windows without grep? Try `findstr` or install Git Bash

## Files

- [shakespeare.txt](shakespeare.txt) - Complete works of William Shakespeare

## Solution

### Method 1: Using grep (Linux/Mac)

The simplest approach:

```bash
grep "flag{" shakespeare.txt
```

Or case-insensitive search:

```bash
grep -i "flag{" shakespeare.txt
```

Or with line numbers:

```bash
grep -n "flag{" shakespeare.txt
```

### Method 2: Windows Command Prompt

```cmd
findstr "flag{" shakespeare.txt
```

### Method 3: Python Script

```bash
python grep_solver.py
```

Or search for any pattern:

```bash
python grep_solver.py shakespeare.txt "flag{"
```

### Method 4: Text Editor

Open `shakespeare.txt` in any text editor and use Find (Ctrl+F / Cmd+F) to search for "flag{"

### The Flag

After searching through the complete works of Shakespeare, you'll find:

**Flag:** `flag{ToGrepOrNotToGrep}`

## Understanding grep

### What is grep?

`grep` is a command-line utility for searching plain-text data for lines that match a regular expression. Its name comes from the ed command `g/re/p` (globally search for a regular expression and print matching lines).

### Basic Syntax

```bash
grep [options] pattern [file...]
```

### Common Options

- `-i` - Case-insensitive search
- `-n` - Show line numbers
- `-v` - Invert match (show non-matching lines)
- `-c` - Count matching lines
- `-r` or `-R` - Recursive search in directories
- `-l` - List only filenames with matches
- `-w` - Match whole words only
- `-A N` - Show N lines after match
- `-B N` - Show N lines before match
- `-C N` - Show N lines before and after match

### Examples

Search for a word:
```bash
grep "hello" file.txt
```

Case-insensitive search:
```bash
grep -i "HELLO" file.txt
```

Search recursively in directory:
```bash
grep -r "flag{" ./challenges/
```

Count occurrences:
```bash
grep -c "error" logfile.txt
```

Show line numbers:
```bash
grep -n "TODO" *.py
```

### Regular Expression Patterns

grep supports regex patterns:

- `.` - Any single character
- `*` - Zero or more of previous character
- `^` - Start of line
- `$` - End of line
- `[abc]` - Any character in brackets
- `[^abc]` - Any character NOT in brackets
- `\` - Escape special characters

Examples:
```bash
# Find lines starting with "flag"
grep "^flag" file.txt

# Find lines ending with "}"
grep "}$" file.txt

# Find email addresses
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" file.txt
```

## Why grep in CTF?

In CTF competitions, you'll often need to:

1. **Search log files** for specific events or errors
2. **Find flags** hidden in large datasets
3. **Extract patterns** like emails, IPs, or hashes
4. **Filter data** from command outputs
5. **Analyze memory dumps** or forensic artifacts

### CTF Examples

Search for flags in multiple files:
```bash
grep -r "flag{" .
```

Find IP addresses:
```bash
grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" access.log
```

Find base64 encoded strings:
```bash
grep -E "^[A-Za-z0-9+/]{20,}={0,2}$" data.txt
```

## Alternative Tools

- **ack** - Programmer's grep (respects .gitignore)
- **ag** (The Silver Searcher) - Very fast grep alternative
- **ripgrep (rg)** - Extremely fast, respects .gitignore
- **findstr** - Windows alternative
- **Select-String** - PowerShell's grep equivalent

### PowerShell Example

```powershell
Select-String -Pattern "flag{" -Path shakespeare.txt
```

## References

- [grep Manual](https://man7.org/linux/man-pages/man1/grep.1.html)
- [Regular Expressions Tutorial](https://regexone.com/)
- [grep Examples](https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/)
- [Regex Tester](https://regex101.com/)

## Fun Facts

- grep was created by Ken Thompson in 1973
- It's one of the most commonly used Unix commands
- The name comes from the ed editor command: `g/re/p`
- There's a whole family: grep, egrep, fgrep, zgrep, bzgrep