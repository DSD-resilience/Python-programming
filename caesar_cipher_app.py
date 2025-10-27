# Caesar Cipher - Encrypt and Decrypt

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift  # reverse the shift for decryption

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # non-alphabetical characters stay the same

    return result

# User Input Section
text = input("Enter your message: ")
shift = int(input("Enter shift value (integer): "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

# Output the result
output = caesar_cipher(text, shift, mode)
print(f"Result: {output}")
