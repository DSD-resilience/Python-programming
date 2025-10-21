# # first lets practice with strings and indexing 
# # remember that indexing starts at zero
# print("Hello"[4])
# print("Hello"[-3])
# print("Hello"[0:2])
# 
# # check your data types since certain functions require certain data types
# print(type("Hola"))
# print(type(2.24))
# print(type(False))
# 
# # change your data type
# print(bool(123))
# # use exponents
# print(2**3)

# now for the tip calculator
print("Welcome to the tip calculator!")
total = float(input("How much was your total bill? $"))
percent = int(input("How much do you want to tip? 10 15 or 20 percent? "))
party = int(input("How many people were in your party?"))
bill_with_tip = percent / 100 * total + total
bill_per_person = round(bill_with_tip/int(party), 2)
print(f"Each person should pay: ${bill_per_person}" )

