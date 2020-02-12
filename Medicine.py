AGE = 12
WEIGHT_MIN = 1
WEIGHT_MAX = 300
AGE_MIN = 0
keep_asking = True

while keep_asking == True:
    user_age = int(input("How old are you?\n"))
    
    if user_age >= AGE:
        print("Take 2 500mg Paracetamol tablets")
    elif user_age < AGE_MIN:
        print("That age is impossible")
        
    else:
        weight = int(input("How much do you weigh?\n"))
        
    if weight < WEIGHT_MIN or weight > WEIGHT_MAX:
        print("That weight is impossible")
    else:
        dose = (weight * 10)
        print("Your child is allowed {}mg of Paracetamol".format(dose))

