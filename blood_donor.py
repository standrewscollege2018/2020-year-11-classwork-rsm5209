AGE_MINIMUM = 16
AGE_MAXIMUM = 70
WEIGHT_MINIMUM = 50

age = int(input("How old are you?\n"))
weight = int(input("How much do you weigh?\n"))

if age >= AGE_MINIMUM and weight >= WEIGHT_MINIMUM and age <= AGE_MAXIMUM :
             print("You are eligible to donate blood")
else:
             print("You are not eligible to donate blood")
        
