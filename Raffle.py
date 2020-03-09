""" This code creates a raffle and randomizes all the names and picks a winner """
# These imports allow this raffle to randomise names and make it work as intended 
import random
import time
# Creating a list so names can be stored
names = []
#Allowing error catching
get_prize = True
keep_asking = True
#Catches symbols and numbers in certain inputs
chars = set("0123456789$, `~!@#%^&*()-_=+|")

while get_prize == True:
        try:
                prize_name = input("What is the prize for the raffle?\n")
                if any((c in chars) for c in prize_name) or prize_name == "":           
                        print("Please enter a valid name")        
                else:
                        prize_price = int(input("What is the prize's monetary value?\n"))
                        if prize_price == "":  
                                print("Please enter a valid price")
                        else:
                                get_prize = False
        except:               
                                print("Please enter a valid price")
            
print("type 'end' when you want the raffle to be drawn")
while keep_asking == True:
        try:
                name_input = input("Please enter your name: ")
                if name_input == "end":
                        keep_asking = False
                elif any((c in chars) for c in name_input) or name_input == "":            
                        print("Please enter a valid name")
                else:
                        names.append(name_input)
        except:
                print("Please enter a valid name")
print("These are the people that have entered the raffle")
for i in range(len(names)):
        print(names[i])
print("The winner will now be drawn")
time.sleep(1)
print("Drawing...")
time.sleep(2)
print("The winner is: {}, well done on winning the {} which is worth ${}".format(random.choice(names), prize_name, prize_price))




        
