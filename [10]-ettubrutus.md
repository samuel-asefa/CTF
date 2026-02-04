# Et Tu Brutus?

**Category:** Warmup  
**Points:** 10  
**Difficulty:** Easy

## Description

Cryptography is a key component to computer security and often separated into classical and modern. Examples of classical cryptography include Caesar, Vigenère, and substitution ciphers. Examples of modern ciphers include DES, 3DES, AES and Blowfish.

We are going to start with an easy classical Caesar cipher for you to decode where each letter is shifted by some consistent known value. While there are several web based decoders, it is an interesting project to write a solver in any number of programming languages (C or Python, for example) or you can manually decode the flag using good old fashioned paper and pencil.

Here is the flag:

```
mshn{ildhylaolpklzvmthyjo}
```

## Learning Objectives

- Understand the Caesar cipher (ROT cipher)
- Learn about classical cryptography
- Practice frequency analysis
- Implement or use cipher decoding tools

## Hints

- Julius Caesar used this cipher to protect military messages
- Each letter is shifted by the same amount
- The shift is consistent throughout the message
- Try all 26 possible shifts (brute force)
- The title references Shakespeare's "Julius Caesar" - "Et tu, Brute?"
- "Ides of March" might be relevant...
- Look for readable English text

## Solution

### Understanding Caesar Cipher

The Caesar cipher shifts each letter by a fixed number of positions in the alphabet:

```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C  (shift of 3)
```

### Method 1: Try All Shifts (Brute Force)

Since there are only 26 possible shifts, we can try them all:

```
Shift 0:  mshn{ildhylaolpklzvmthyjo}
Shift 1:  ntio{jmeizmabmqmaawnuizkp}
Shift 2:  oujp{knfjanabcnrnbbxovjalq}
Shift 3:  pvkq{logkbobcdsosccypwkbmr}
Shift 4:  qwlr{mphlcpcdletptddzqxlcns}
Shift 5:  rxms{nqimdqdemfuqueearxydot}
...
Shift 7:  flag{thefifteenthofmarch}  ✓ READABLE!
...
```

**The answer is shift 7!**

### Method 2: Use the Provided Script

```bash
python caesar_solver.py
```

This will try all 26 shifts and show you the readable results.

### Method 3: Online Tool

1. Go to a Caesar cipher decoder like:
   - https://www.dcode.fr/caesar-cipher
   - https://cryptii.com/pipes/caesar-cipher

2. Paste: `mshn{ildhylaolpklzvmthyjo}`

3. Try different shift values or use auto-solve

### Method 4: Manual Decoding

If you know the shift is 7:
- m → f (shift back 7)
- s → l (shift back 7)
- h → a (shift back 7)
- n → g (shift back 7)

Continue for all letters...

**Flag:** `flag{thefifteenthofmarch}`

## Explanation

"The fifteenth of March" refers to the **Ides of March** (March 15th), the date when Julius Caesar was assassinated in 44 BC. The phrase "Et tu, Brute?" ("And you, Brutus?") are supposedly Caesar's last words when he saw Brutus among his assassins.

The shift value of **7** is a nod to the fact that Caesar originally used a shift of 3, but this challenge uses 7 to make it slightly less obvious.

## How Caesar Cipher Works

### Encryption Formula

For each letter, shift forward by N positions:
```
E(x) = (x + n) mod 26
```

Where:
- x = position of letter (A=0, B=1, ..., Z=25)
- n = shift amount
- mod 26 = wrap around the alphabet

### Decryption Formula

Shift backward by N positions:
```
D(x) = (x - n) mod 26
```

### Example: Shift of 3

```
Plain:    THE QUICK BROWN FOX
Cipher:   WKH TXLFN EURZQ IRA
```

## Breaking Caesar Cipher

### Method 1: Brute Force
- Only 26 possible keys (shifts 0-25)
- Try all of them and look for readable text
- Very easy to break!

### Method 2: Frequency Analysis
- In English, 'E' is the most common letter
- Find the most frequent letter in ciphertext
- Calculate the shift needed to turn it into 'E'
- Test if result is readable

### Method 3: Known Plaintext
- If you know part of the message (like "flag{")
- Compare with ciphertext to determine shift
- Apply shift to entire message

## Historical Context

**Julius Caesar** (100-44 BC) used this cipher to protect military communications. According to Suetonius:

> "If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out."

Caesar used a shift of 3 (A→D, B→E, C→F, etc.), now known as **ROT3** or the "Caesar shift."

### ROT13

A special case is **ROT13** (shift of 13), which is its own inverse:
- Encrypt with ROT13: A→N, B→O, ...
- Decrypt with ROT13: Apply ROT13 again
- Commonly used in forums to hide spoilers

## Security Analysis

### Weaknesses:
1. **Tiny keyspace** - Only 25 meaningful keys
2. **No key distribution** - Shift is the key
3. **Pattern preservation** - Letter frequencies maintained
4. **Easily broken** - Seconds with any computer

### Why still studied:
- Foundation for understanding substitution ciphers
- Educational value for cryptography concepts
- Building block for more complex systems
- Historical significance

## Tools & Scripts

The repository includes:
- `caesar_solver.py` - Brute force solver
- `caesar_cipher.py` - Encoder/decoder with custom shifts

## Related Ciphers

- **ROT13** - Special case with shift of 13
- **Atbash** - Reverses the alphabet (A↔Z, B↔Y)
- **Substitution Cipher** - Random letter mapping
- **Vigenère Cipher** - Multiple Caesar shifts with a key

## References

- [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Frequency Analysis](https://en.wikipedia.org/wiki/Frequency_analysis)
- [Cryptography - Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography)
- [Julius Caesar Biography](https://en.wikipedia.org/wiki/Julius_Caesar)

## Practice More

Try creating your own Caesar cipher messages!

```python
python caesar_cipher.py --encode --shift 13 "Hello World"
```

Then decode it:
```python
python caesar_cipher.py --decode --shift 13 "Uryyb Jbeyq"
```