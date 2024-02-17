# BMI Categories from wikipedia: https://en.wikipedia.org/wiki/Body_mass_index
print("BMI Categories: ")
print("Underweight (Severe thinness) < 16")
print("Underweight (Moderate thinness) = 16 - 16.9")
print("Underweight (Mild thinness) = 17 - 18.4")
print("Normal Weight = 18.5 - 24.9")
print("Overweight (Pre-obese) = 25 - 29.9")
print("Obese (Class I) = 30 - 34.9")
print("Obese (Class II) = 35 - 39.9")
print("Obese (Class III) = 40 or greater\n")


height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))


def bmi_calculator(h, w):
    """ Returns the calculated bmi, formula = weight(kg)/height(meters)**2 """
    return round(w / h ** 2, 2)


bmi = bmi_calculator(height, weight)
if bmi < 16:
    print(f"Your BMI is {bmi}, you are Underweight (Severe thinness).")
elif bmi < 17:
    print(f"Your BMI is {bmi}, you are Underweight (Moderate thinness).")
elif bmi < 18.5:
    print(f"Your BMI is {bmi}, you are Underweight (Mild thinness).")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are Obese Class I.")
elif bmi < 40:
    print(f"Your BMI is {bmi}, you are Obese Class II.")
else:
    print(f"Your BMI is {bmi}, you are Obese Class III.")
