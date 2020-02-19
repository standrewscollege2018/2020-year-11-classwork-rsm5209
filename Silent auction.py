
highest_name = (" ")
highest_bid = 0
error_catch = True


Item_Name = input("What is the auction for?\n")
while error_catch == True:
    try:
        reserve_price = int(input("What is the reserve price?\n"))
        if reserve_price < 0:
            print("Please enter a valid reserve price")
            error_catch = True
        else:
            error_catch = False
    except:
        print("Please remove the dollar sign or enter a vaild number")

print("The auction for {} is underway.".format(Item_Name))
error_catch = True
while error_catch == True:
    try: 
        name = input("What is the bidders name?\n")
        try:
            bid = int(input("Enter your bid\n"))
            if bid == -1:
                    print("The auction has ended. Well done {} on winning the {} with a bid of {}".format(highest_name, Item_Name, highest_bid))
                    error_catch = False
            elif bid > highest_bid:
                print("The highest bidder is {} with a bid of {} dollars".format(name, bid))
                highest_bid = bid
                highest_name = name  
            else:
                print("This bid does not exceed the highest bid, please enter a higher amount")
                
        except:
            print("Please remove the dollar sign or write a vaild number")
    except:
        print("This is not a valid entry, please try again")

if highest_bid < reserve_price:
    print("I'm sorry this item did not sell as the highest bid did not exceed the reserve price")


        
        
        
        
    



