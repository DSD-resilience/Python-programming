print("Welcome to Python Pizza!")

# Step 1: Get pizza size
size = input("What size pizza do you want? (S/M/L): ").upper()

# Step 2: Ask about pepperoni
add_pepperoni = input("Do you want pepperoni? (Y/N): ").upper()

# Step 3: Ask about extra cheese
extra_cheese = input("Do you want extra cheese? (Y/N): ").upper()

# Step 4: Set base price
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
else:
    print("Invalid pizza size selected.")

# Step 5: Add extra cheese
if extra_cheese == "Y":
    bill += 2

# Step 6: Print the final bill
print(f"Your final bill is: ${bill}")

