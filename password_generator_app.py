# Password Generator
import random

# Define character pools
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

# Combine all characters
all_chars = letters + numbers + symbols

# Desired password length
password_length = 10

# Empty password variable
password = ""

# Generate password using a for loop
for i in range(password_length):
    password += random.choice(all_chars)

# Check if password includes at least one number
has_number = False
for char in password:
    if char in numbers:
        has_number = True
        break

# Ensure at least one number is in the password
if not has_number:
    password = password[:-1] + random.choice(numbers)

print("Generated Password:", password)
