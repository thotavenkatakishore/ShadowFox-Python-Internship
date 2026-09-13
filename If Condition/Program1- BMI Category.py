# Get height and weight from the user
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")