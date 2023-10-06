# JAMES MOSETI MOTURI
# SCT211-0095/2022

weight_in_kg = float(input("Enter your weight in kilograms: "))
height_in_metres = float(input("Enter your height in metres: "))

user_BMI = weight_in_kg / (height_in_metres*height_in_metres)

if user_BMI < 18.5:
    print(f"Your BMI is {round(user_BMI, 2)} and you are underweight! ")
elif (user_BMI >= 18.5) & (user_BMI <= 24.9):
    print(f"Your BMI is {round(user_BMI, 2)} and you are of normal weight. ")
else:
    print(f"Your BMI is {round(user_BMI, 2)} and you are overweight! ")
