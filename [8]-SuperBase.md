# SuperBase

**Category:** Warmup  
**Points:** 10  
**Difficulty:** Easy

## Description

You may have heard of base 2 (binary), base 8 (octal), base 10 (decimal), base 16 (hexadecimal), and now you face something slightly different in base 64:

```
ZmxhZ3tiYXNldnNiYXNzfQ==
```

After some research, you learned that the `==` is padding. One or two equals signs at the end might mean it is a base 64 encoded string, and sometimes there is no padding at all.

Can you decode it for a flag?

## Learning Objectives

- Understand Base64 encoding
- Recognize Base64 encoded strings
- Learn when and why Base64 is used
- Practice using decoding tools

## Hints

- The `==` at the end is a strong indicator of Base64
- Base64 uses characters: A-Z, a-z, 0-9, +, /
- Many online tools can decode Base64
- Python has built-in Base64 support
- The word "bass" in the flag might be a pun on "base"

## Solution

### Method 1: Online Tool

1. Go to a Base64 decoder like:
   - https://www.base64decode.org/
   - https://gchq.github.io/CyberChef/ (use "From Base64" recipe)

2. Paste the encoded string: `ZmxhZ3tiYXNldnNiYXNzfQ==`

3. Decode to get: `flag{basevsbass}`

### Method 2: Command Line (Linux/Mac)

```bash
echo "ZmxhZ3tiYXNldnNiYXNzfQ==" | base64 -d
```

### Method 3: Python

```python
import base64

encoded = "ZmxhZ3tiYXNldnNiYXNzfQ=="
decoded = base64.b64decode(encoded).decode('utf-8')
print(decoded)
```

### Method 4: Use the Provided Script

```bash
python base64_decoder.py
```

Or decode any Base64 string:

```bash
python base64_decoder.py "ZmxhZ3tiYXNldnNiYXNzfQ=="
```

**Flag:** `flag{basevsbass}`

## What is Base64?

Base64 is an encoding scheme that converts binary data into ASCII text format using 64 different characters.

### Character Set

Base64 uses:
- Uppercase letters: A-Z (26 characters)
- Lowercase letters: a-z (26 characters)
- Numbers: 0-9 (10 characters)
- Special characters: + and / (2 characters)
- Padding: = (used at the end)

Total: 64 printable characters

### Why Base64?

Base64 is used to:
1. **Email attachments** - Encode binary files for MIME
2. **Data URLs** - Embed images in HTML/CSS
3. **API tokens** - Represent binary tokens as text
4. **Data storage** - Store binary data in text-only formats (JSON, XML)
5. **Obfuscation** - Hide strings from casual viewing (not encryption!)

### How Base64 Works

Base64 converts every 3 bytes (24 bits) of binary data into 4 Base64 characters:

```
Input:   3 bytes = 24 bits
Output:  4 characters (6 bits each)
```

Example:
```
Text:     "Man"
Binary:   01001101 01100001 01101110
Grouped:  010011 010110 000101 101110
Base64:   T      W      F      u
Result:   "TWFu"
```

### Padding

If the input length isn't a multiple of 3, padding (`=`) is added:
- 1 byte remaining → 2 characters + `==`
- 2 bytes remaining → 3 characters + `=`
- 3 bytes (no remainder) → 4 characters, no padding

### Recognizing Base64

Look for these signs:
- ✅ Only uses: A-Z, a-z, 0-9, +, /, =
- ✅ Often ends with `=` or `==`
- ✅ Length is usually a multiple of 4
- ✅ Looks like random alphanumeric text

### Base64 vs Binary vs Hex

```
Original:  "Hello"
Binary:    01001000 01100101 01101100 01101100 01101111
Hex:       48 65 6c 6c 6f
Base64:    SGVsbG8=
```

## Common CTF Uses

In CTFs, you'll often see:
1. Flags encoded in Base64
2. Multiple layers of encoding (Base64 → Hex → Base64)
3. Modified Base64 (different character sets)
4. Base64 in URLs, cookies, or headers
5. Base64-encoded executables or scripts

## Tools

- **Command line:** `base64` (Linux/Mac), `certutil` (Windows)
- **Python:** `base64` module
- **Online:** CyberChef, base64decode.org
- **Browser:** JavaScript `atob()` and `btoa()` functions

## References

- [Base64 - Wikipedia](https://en.wikipedia.org/wiki/Base64)
- [RFC 4648 - Base64 Specification](https://tools.ietf.org/html/rfc4648)
- [CyberChef](https://gchq.github.io/CyberChef/)

## Fun Fact

The flag `flag{basevsbass}` is a play on words:
- **base** - number systems (base 2, base 64, etc.)
- **bass** - the musical instrument or fish

It's highlighting that Base64 is about "base" (number encoding), not "bass" (fish/music)! 🐟🎸s