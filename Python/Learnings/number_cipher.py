def encrypt_a1z26(message):
    """Encrypts a message using the A1Z26 cipher."""
    encrypted_numbers = []
    for char in message.upper():  # Convert to uppercase for consistent mapping
        if 'A' <= char <= 'Z':
            number = ord(char) - ord('A') + 1
            encrypted_numbers.append(str(number))
        else:
            encrypted_numbers.append(char)  # Keep non-alphabetic characters as is
    return " ".join(encrypted_numbers)

def decrypt_a1z26(encrypted_message):
    """Decrypts an A1Z26 encrypted message."""
    decrypted_text = []
    numbers = encrypted_message.split()
    for num_str in numbers:
        if num_str.isdigit():
            number = int(num_str)
            if 1 <= number <= 26:
                char = chr(ord('A') + number - 1)
                decrypted_text.append(char)
            else:
                decrypted_text.append(num_str)  # Handle out-of-range numbers
        else:
            decrypted_text.append(num_str)  # Handle non-numeric parts (e.g., spaces)
    return "".join(decrypted_text)

# Example Usage:
plaintext = "HELLO WORLD"
encrypted = encrypt_a1z26(plaintext)
print(f"Encrypted: {encrypted}")


decrypted = decrypt_a1z26(encrypted)
print(f"Decrypted: {decrypted}")
