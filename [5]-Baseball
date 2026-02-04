# BaseBall

**Category:** Warmup  
**Points:** 10  
**Difficulty:** Easy

## Description

Everyone knows decimal aka base 10. Computer Scientists like to use other bases including base 2 (binary), base 8 (octal), and base 16 (hexadecimal) and our competition will use all these bases - maybe even more. Base 16 is particularly interesting for computers and is notable for using the symbols A, B, C, D, E and F in addition to 0-9.

To help you on your journey, please calculate:

**1011 (binary) + 1011 (octal) + 1011 (decimal) + FFFF (hexadecimal)**

Please express your answer in decimal and remember that your answer should be surrounded by `flag{}`

## Learning Objectives

- Understand different number base systems
- Practice converting between bases
- Learn binary, octal, and hexadecimal representations

## Solution

### Step 1: Convert Each Number to Decimal

**1011 (binary) to decimal:**
- 1×2³ + 0×2² + 1×2¹ + 1×2⁰
- 1×8 + 0×4 + 1×2 + 1×1
- 8 + 0 + 2 + 1 = **11**

**1011 (octal) to decimal:**
- 1×8³ + 0×8² + 1×8¹ + 1×8⁰
- 1×512 + 0×64 + 1×8 + 1×1
- 512 + 0 + 8 + 1 = **521**

**1011 (decimal):**
- Already in decimal = **1011**

**FFFF (hexadecimal) to decimal:**
- F×16³ + F×16² + F×16¹ + F×16⁰
- 15×4096 + 15×256 + 15×16 + 15×1
- 61440 + 3840 + 240 + 15 = **65535**

### Step 2: Add Them Together

11 + 521 + 1011 + 65535 = **67078**

**Flag:** `flag{67078}`

## Using the Provided Calculator

Run the Python script:

```bash
python base_calculator.py
```

## Quick Reference

### Binary (Base 2)
- Uses digits: 0, 1
- Example: 1011₂ = 11₁₀

### Octal (Base 8)
- Uses digits: 0-7
- Example: 1011₈ = 521₁₀

### Decimal (Base 10)
- Uses digits: 0-9
- Example: 1011₁₀ = 1011₁₀

### Hexadecimal (Base 16)
- Uses digits: 0-9, A-F (where A=10, B=11, C=12, D=13, E=14, F=15)
- Example: FFFF₁₆ = 65535₁₀

## Tools

- Python (built-in `int()` function)
- Calculator with base conversion
- Online converters
- The provided `base_calculator.py` script

## References

- [Number Base Systems](https://en.wikipedia.org/wiki/Radix)
- [Binary Number System](https://en.wikipedia.org/wiki/Binary_number)
- [Hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal)
