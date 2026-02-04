# Extensions Lie

**Category:** Warmup  
**Points:** 10  
**Difficulty:** Easy

## Description

This is a picture. Honest. Would we lie? Maybe look at it with a text editor?

Download the file: [notapicture.jpg](notapicture.jpg)

## Learning Objectives

- Understand that file extensions don't determine file type
- Learn to inspect file contents manually
- Practice using text editors for forensics
- Recognize that file headers/magic bytes define true file types

## Hints

- Don't trust file extensions
- Try opening the file in a text editor (Notepad, vim, nano, VSCode, etc.)
- The actual content might be readable text, not binary image data
- Look for the flag format: `flag{}`

## Solution

### Method 1: Text Editor

1. Download the file `notapicture.jpg`
2. Open it with any text editor:
   - Windows: Notepad, Notepad++
   - Mac: TextEdit, Sublime Text
   - Linux: vim, nano, gedit
   - Cross-platform: VSCode

3. You'll see it's actually a text file containing:

```
This isn't really a JPEG image!

Images are binary files that would look like gibberish in a text editor.
If you can read this clearly, it's obviously a text file.

File extensions can lie. Always verify file types by their content.

Here's your flag: flag{ExtensionsDontMatter}

Fun fact: On Unix/Linux systems, file extensions are just conventions.
The 'file' command uses magic bytes to determine actual file types!
```

**Flag:** `flag{ExtensionsDontMatter}`

### Method 2: Command Line (Linux/Mac)

```bash
cat notapicture.jpg
# or
less notapicture.jpg
# or use the 'file' command to check file type
file notapicture.jpg
```

### Method 3: Python

```python
with open('notapicture.jpg', 'r') as f:
    content = f.read()
    print(content)
```

### Method 4: Use the Provided Script

```bash
python inspect_file.py notapicture.jpg
```

## Understanding File Types

### How File Types Really Work

**File extensions** (like .jpg, .txt, .pdf) are just naming conventions. The operating system and applications use them as hints, but they don't fundamentally change what a file is.

**True file type** is determined by:
1. **Magic bytes** (file signature) - First few bytes of the file
2. **File structure** - How data is organized inside

### Common File Signatures

- **JPEG:** Starts with `FF D8 FF`
- **PNG:** Starts with `89 50 4E 47`
- **GIF:** Starts with `47 49 46 38`
- **PDF:** Starts with `25 50 44 46` (`%PDF`)
- **ZIP:** Starts with `50 4B 03 04` or `50 4B 05 06`

### The 'file' Command

On Linux/Mac, the `file` command uses a database of magic bytes to identify file types:

```bash
$ file notapicture.jpg
notapicture.jpg: ASCII text
```

## Security Implications

This challenge demonstrates an important security concept:

1. **Malware** can disguise itself with fake extensions
2. **Upload filters** that only check extensions are insufficient
3. **Always validate** file contents, not just names
4. **Defense in depth** requires checking multiple attributes

## Tools

- Text editors (any)
- `cat`, `less`, `more` (Linux/Mac)
- `file` command (Linux/Mac)
- `type` command (Windows)
- Hex editors (for binary analysis)
- Python scripts

## References

- [List of File Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
- [Magic Bytes](https://en.wikipedia.org/wiki/Magic_number_(programming))
- [File Command](https://man7.org/linux/man-pages/man1/file.1.html)