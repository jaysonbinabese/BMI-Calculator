print("What is your name?\n")
name = input()
print("Hello! " + name + " \nWelcome to BMI Calculator")


height = input("Please enter your height in meters (e.g: 1.65):\n ")
weight = input("Please enter your weight in kilograms (e.g: 72):\n ")

Height = float(height)
Weight = int(weight)

bmi = Weight / (Height*Height)

if bmi < 18.5:
    print("Your BMI is " + str(bmi) + " and you are underweight.")
elif bmi < 25:
    print("Your BMI is " + str(bmi) + " and you are normal weight.")
elif bmi < 30:
        print("Your BMI is " + str(bmi) + " and you are overweight.")
else:
        print("Your BMI is " + str(bmi) + " and you are obese")
