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

# # practice using range function
# for unit in range(1, 12) :
#   print(unit)
#   
# # or else the "Fizz Buzz Game," run through a range and test for conditions
# for number in range (1, 101) :
#   if number % 3 == 0 and number % 5 == 0 :
#     print("FizzBuzz")
#   elif number % 3 == 0  :
#     print("Fizz")
#   elif number % 5 == 0 :
#     print("Buzz")
#   else :
#     print(number)

# "Hard" Password
import random
import string

def generate_password():
    letters = random.choices(string.ascii_letters, k=2)
    digits = random.choices(string.digits, k=2)
    special_chars = random.choices('!@#$%^&*()-_=+[]{}|;:,.<>?', k=2)
    
    password_list = letters + digits + special_chars
    random.shuffle(password_list)
    
    password = ''.join(password_list)
    return password

# Generate and print the password
print("Generated Password:", generate_password())


  
