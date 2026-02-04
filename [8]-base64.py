#!/usr/bin/env python3
"""
Base64 Decoder for CTF Challenges
Supports decoding Base64 encoded strings
"""

import base64
import sys
import re

def is_base64(s):
    """Check if a string looks like Base64"""
    # Base64 uses A-Z, a-z, 0-9, +, /, and = for padding
    base64_pattern = re.compile(r'^[A-Za-z0-9+/]*={0,2}$')
    
    # Must match pattern
    if not base64_pattern.match(s):
        return False
    
    # Length should be multiple of 4
    if len(s) % 4 != 0:
        return False
    
    return True

def decode_base64(encoded_string):
    """Decode Base64 string"""
    try:
        # Decode from Base64
        decoded_bytes = base64.b64decode(encoded_string)
        
        # Try to decode as UTF-8 text
        try:
            decoded_text = decoded_bytes.decode('utf-8')
            return decoded_text, decoded_bytes, True
        except UnicodeDecodeError:
            # If not valid UTF-8, return as bytes
            return None, decoded_bytes, False
            
    except Exception as e:
        return None, None, False

def display_bytes_hex(data, max_bytes=64):
    """Display bytes in hex format"""
    print("\nHex representation:")
    for i in range(0, min(len(data), max_bytes), 16):
        hex_part = ' '.join(f'{b:02x}' for b in data[i:i+16])
        ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in data[i:i+16])
        print(f'  {hex_part:<48}  |{ascii_part}|')
    if len(data) > max_bytes:
        print(f"  ... ({len(data) - max_bytes} more bytes)")

def main():
    print("=" * 60)
    print("Base64 Decoder - CTF Challenge Tool")
    print("=" * 60)
    
    # Challenge encoded string
    challenge_encoded = "ZmxhZ3tiYXNldnNiYXNzfQ=="
    
    if len(sys.argv) > 1:
        # User provided string
        encoded_string = sys.argv[1]
        print(f"\nDecoding user-provided string...")
    else:
        # Use challenge string
        encoded_string = challenge_encoded
        print(f"\nDecoding challenge string...")
    
    print(f"\nEncoded (Base64):")
    print(f"  {encoded_string}")
    
    # Validate
    if not is_base64(encoded_string):
        print("\n⚠️  Warning: This doesn't look like valid Base64!")
        print("   Base64 uses: A-Z, a-z, 0-9, +, /, and =")
        print("   Length should be a multiple of 4")
        response = input("\nTry to decode anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    # Decode
    decoded_text, decoded_bytes, is_text = decode_base64(encoded_string)
    
    if decoded_bytes is None:
        print("\n❌ Failed to decode! Invalid Base64 string.")
        return
    
    print(f"\n✅ Successfully decoded!")
    print(f"\nLength: {len(encoded_string)} characters → {len(decoded_bytes)} bytes")
    
    if is_text:
        print(f"\nDecoded (Text):")
        print(f"  {decoded_text}")
        
        # Check for flag
        if 'flag{' in decoded_text.lower():
            print("\n🚩 FLAG FOUND!")
            flags = re.findall(r'flag\{[^}]+\}', decoded_text, re.IGNORECASE)
            for flag in flags:
                print(f"   {flag}")
    else:
        print(f"\nDecoded data is binary (not readable text)")
        display_bytes_hex(decoded_bytes)
    
    # Show encoding breakdown
    print("\n" + "-" * 60)
    print("Encoding breakdown:")
    print(f"  Original bytes: {len(decoded_bytes)}")
    print(f"  Base64 length:  {len(encoded_string)}")
    print(f"  Padding chars:  {encoded_string.count('=')}")
    print(f"  Efficiency:     {len(decoded_bytes)/len(encoded_string)*100:.1f}%")
    
    print("\n" + "=" * 60)

def interactive_mode():
    """Interactive decoding mode"""
    print("\n" + "=" * 60)
    print("Interactive Base64 Decoder")
    print("=" * 60)
    print("\nEnter Base64 strings to decode (or 'quit' to exit)")
    
    while True:
        print("\n" + "-" * 60)
        encoded = input("Base64> ").strip()
        
        if encoded.lower() in ['quit', 'exit', 'q']:
            break
        
        if not encoded:
            continue
        
        decoded_text, decoded_bytes, is_text = decode_base64(encoded)
        
        if decoded_bytes is None:
            print("❌ Invalid Base64!")
            continue
        
        if is_text:
            print(f"Decoded: {decoded_text}")
        else:
            print(f"Decoded (binary): {len(decoded_bytes)} bytes")
            display_bytes_hex(decoded_bytes, 32)

if __name__ == "__main__":
    main()
    
    # Tips
    print("\n💡 Tips:")
    print("  - Base64 always uses: A-Z, a-z, 0-9, +, /")
    print("  - Padding (=) appears at the end if needed")
    print("  - Length is always a multiple of 4")
    print("  - Common in CTFs for data encoding and obfuscation")
    print("\n📚 Other bases you might see:")
    print("  - Base32: Uses A-Z and 2-7")
    print("  - Base58: Used in Bitcoin (no 0, O, I, l)")
    print("  - Base85: More efficient than Base64")
    print("\nRun with argument: python base64_decoder.py <base64_string>")
    print("Or try interactive mode by typing 'python -c \"from base64_decoder import interactive_mode; interactive_mode()\"'")