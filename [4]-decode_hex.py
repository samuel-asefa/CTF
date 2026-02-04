"""
Hex to ASCII Decoder
Challenge: Ask and Ye Shall Receive
"""

def hex_to_ascii(hex_string):
    """Convert hex string to ASCII"""
    # Remove spaces
    hex_string = hex_string.replace(" ", "")
    
    # Convert hex to bytes, then to string
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    
    return ascii_string

def main():
    # The encoded message from the challenge
    encoded = "66 6c 61 67 7b 49 6e 66 6f 72 6d 61 74 69 6f 6e 49 6e 74 65 72 63 68 61 6e 67 65 7d"
    
    print("Hex to ASCII Decoder")
    print("=" * 50)
    print(f"\nEncoded message:\n{encoded}\n")
    
    decoded = hex_to_ascii(encoded)
    print(f"Decoded message:\n{decoded}\n")
    
    # Show the breakdown
    print("Character breakdown:")
    hex_pairs = encoded.split()
    for hex_pair in hex_pairs:
        char = chr(int(hex_pair, 16))
        print(f"  {hex_pair} -> '{char}' (decimal: {int(hex_pair, 16)})")

if __name__ == "__main__":
    main()
