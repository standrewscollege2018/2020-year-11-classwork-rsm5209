import random 
num = random.randint(1,10)
error_catching = True 

while error_catching == True:
    try:
        guess = int(input("Guess a number between 1 and 10\n"))
        if guess in range (1,10):
            if guess == num:
                error_catching = False
            elif guess == num:
                error_catching = False
        
            elif guess > num:
                print("Your guess is too high, guess lower")
            else:
                print("Your guess is too low, guess higher")
        else:
            print("Out of range")
    except:
        print("Error, invalid number")

print("You are correct, the number is {} :0".format(num))
            
