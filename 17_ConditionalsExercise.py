#This program calculates the body mass of a person.
#It asks for height in meters and provides weight in kg

print("This program calculates your Body Mass Index (BMI) and its classification")

weight = float ( input("Type your Weight in Kg (example 80): ") )
height = float ( input("Type your Height in Meters (example 1.80): ") )

bmi = weight / (height ** 2)
print("Your BMI is: ", round(bmi, 2))

if (bmi <= 18.5):
    classification = "Underweight"
elif (bmi > 18.5 and bmi <= 24.9):
    classification = "Normal Weight"
elif (bmi > 24.9 and bmi <= 29.9):
    classification = "Overweight"
else:
    classification = "Obese"
print("The classification of your BMI is: ", classification)