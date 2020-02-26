import random
import time
number_of_people = []
get_prize = True
keep_asking = True


while get_prize == True:
    try:
        prize_name = input("What is the prize for the raffle?\n")
        try:
            prize_price = int(input("What is the prizes monetary value?\n"))
            get_prize = False
        except:
            print("Please enter a valid price")
            
    except:
        print("Please enter a valid prize name")

while keep_asking == True:
    try:
        name_input = input("Please enter your name: ")
        if name_input == "end":
            keep_asking = False
        else:
            number_of_people.append(name_input)
    except:
        print("Please enter a valid name")
print("These are the people that have entered the raffle")
for i in range(len(number_of_people)):
    print(number_of_people[i])
print("The winner will now be drawn")
time.sleep(1)
print("Drawing...")
time.sleep(2)
print("The winner is: {}, well done on winning the {} which is worth ${}".format(random.choice(number_of_people), prize_name, prize_price))




        
