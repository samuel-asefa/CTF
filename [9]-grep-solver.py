#!/usr/bin/env python3
"""
grep Solver for CTF Challenges
Demonstrates text searching in Python as an alternative to grep
"""

import sys
import re

def search_file(filename, pattern, case_sensitive=True, show_line_numbers=True):
    """
    Search for a pattern in a file
    Similar to grep functionality
    """
    matches = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Determine if line matches
                if case_sensitive:
                    if pattern in line:
                        matches.append((line_num, line.rstrip('\n')))
                else:
                    if pattern.lower() in line.lower():
                        matches.append((line_num, line.rstrip('\n')))
        
        return matches
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def search_with_regex(filename, regex_pattern, show_line_numbers=True):
    """
    Search for a regex pattern in a file
    Similar to grep -E
    """
    matches = []
    
    try:
        pattern = re.compile(regex_pattern)
        
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if pattern.search(line):
                    matches.append((line_num, line.rstrip('\n')))
        
        return matches
    
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def highlight_match(text, pattern, case_sensitive=True):
    """Highlight the matched pattern in text"""
    if not case_sensitive:
        # For case-insensitive, we need to find actual match
        import re
        matches = list(re.finditer(re.escape(pattern), text, re.IGNORECASE))
        if matches:
            result = text
            for match in reversed(matches):
                start, end = match.span()
                result = result[:start] + '\033[91m' + result[start:end] + '\033[0m' + result[end:]
            return result
    else:
        return text.replace(pattern, f'\033[91m{pattern}\033[0m')
    
    return text

def main():
    print("=" * 70)
    print("grep Solver - CTF Challenge Tool")
    print("Python implementation of grep functionality")
    print("=" * 70)
    
    # Default challenge parameters
    default_file = "shakespeare.txt"
    default_pattern = "flag{"
    
    # Parse arguments
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        pattern = sys.argv[2]
    elif len(sys.argv) == 2:
        filename = default_file
        pattern = sys.argv[1]
    else:
        filename = default_file
        pattern = default_pattern
        print(f"\nUsing default challenge parameters:")
        print(f"  File: {filename}")
        print(f"  Pattern: '{pattern}'")
    
    print(f"\n🔍 Searching for: '{pattern}'")
    print(f"📄 In file: {filename}")
    print("-" * 70)
    
    # Search for pattern
    matches = search_file(filename, pattern, case_sensitive=True, show_line_numbers=True)
    
    if matches is None:
        return
    
    if not matches:
        print(f"\n❌ No matches found for '{pattern}'")
        print("\n💡 Tips:")
        print("  - Check if the pattern is correct")
        print("  - Try case-insensitive search")
        print("  - Try a simpler pattern")
        return
    
    # Display results
    print(f"\n✅ Found {len(matches)} match(es):\n")
    
    for line_num, line in matches:
        highlighted = highlight_match(line, pattern)
        print(f"  Line {line_num}: {highlighted}")
    
    # Check for flags
    flag_pattern = r'flag\{[^}]+\}'
    print("\n" + "-" * 70)
    print("🚩 Extracting flags...")
    
    flags_found = []
    for line_num, line in matches:
        flags_in_line = re.findall(flag_pattern, line, re.IGNORECASE)
        for flag in flags_in_line:
            flags_found.append((line_num, flag))
    
    if flags_found:
        print(f"\n🎉 Found {len(flags_found)} flag(s)!\n")
        for line_num, flag in flags_found:
            print(f"  Line {line_num}: {flag}")
    else:
        print("\n⚠️  No complete flags found in matches")
        print("   (Looking for pattern: flag{...})")
    
    print("\n" + "=" * 70)

def advanced_search():
    """Interactive search tool"""
    print("\n" + "=" * 70)
    print("Advanced Interactive Search")
    print("=" * 70)
    
    filename = input("\nEnter filename: ").strip() or "shakespeare.txt"
    
    print("\nSearch options:")
    print("  1. Simple text search")
    print("  2. Regular expression search")
    
    choice = input("Choose option (1 or 2): ").strip() or "1"
    
    pattern = input("Enter search pattern: ").strip()
    
    if not pattern:
        print("No pattern provided!")
        return
    
    if choice == "2":
        # Regex search
        print(f"\nSearching with regex: {pattern}")
        matches = search_with_regex(filename, pattern)
    else:
        # Simple search
        case = input("Case sensitive? (y/n): ").strip().lower()
        case_sensitive = case != 'n'
        matches = search_file(filename, pattern, case_sensitive)
    
    if matches is None:
        return
    
    if not matches:
        print(f"\nNo matches found!")
        return
    
    print(f"\nFound {len(matches)} matches:\n")
    for line_num, line in matches[:20]:  # Show first 20
        print(f"  {line_num}: {line}")
    
    if len(matches) > 20:
        print(f"\n  ... and {len(matches) - 20} more matches")

if __name__ == "__main__":
    main()
    
    # Usage tips
    print("\n💡 grep Command Equivalents:")
    print("  - This script:         python grep_solver.py shakespeare.txt 'flag{'")
    print("  - grep:                grep 'flag{' shakespeare.txt")
    print("  - grep (line nums):    grep -n 'flag{' shakespeare.txt")
    print("  - grep (case-insen.):  grep -i 'FLAG{' shakespeare.txt")
    print("\n📚 Learn more:")
    print("  - man grep (Linux/Mac)")
    print("  - https://www.gnu.org/software/grep/manual/")
    print("  - https://regexone.com/ (for regex)")
    print("\nFor interactive mode, run:")
    print("  python -c 'from grep_solver import advanced_search; advanced_search()'")