# BMI calculator
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight/(height)**2)

# now print your bmi
print(bmi)

if bmi >= 25 :
    print("overweight")
elif bmi >= 18.5 :
        print("normal weight")
else: 
        print("underweight")
