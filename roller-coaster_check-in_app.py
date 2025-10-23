# Roller Coaster Check-in

# screen the guests for the minimum height requirement
print("Welcome to Roller Coaster Check-in!")
height = int(input("What is your height in centimeters? "))
bill = 0

if height >= 120 :
  print("You can ride the roller coaster!")
  age = int(input("What is your age?"))
  if age <= 12 :
    bill = 7
    print("The price is $7.")
  elif age <= 18 :
    bill = 10
    print("The price is $10.")
  elif age >= 55 :
    bill = 7
    print("The price is $7.")
  else
    bill = 12
    print("The price is $12.")
else:
  print("Sorry, must be taller to ride the roller coaster!")
wants_photo = input()

