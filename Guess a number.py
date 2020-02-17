import random 
num = random.randint(1,10)
keep_asking = True 

while keep_asking == True:
    guess = int(input("Guess a number between 1 and 10\n"))
    if guess == num:
        keep_asking = False
    elif guess > num:
        print("Your guess is too high, guess lower")
    else:
        print("Your guess is too low, guess higher")

print("You are correct, the number is {} :0".format(num))
            
