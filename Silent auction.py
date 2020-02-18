
highest_name = (" ")
highest_bid = 0
error_catch = True


Item_Name = input("What is the auction for?\n")
while error_catch == True:
    try:
        Reserve_Price = int(input("What is the reserve price?\n"))
        error_catch = False
    except:
        print("Please remove the dollar sign")

print("The auction for {} is underway.".format(Item_Name))
error_catch = True
while error_catch == True:
    try: 
        name = input("What is the bidders name?\n")
        try:
            bid = int(input("Enter your bid\n"))
        except:
            print("Please remove the dollar sign")
        if bid > highest_bid:
            print("The highest bidder is {} with a bid of {} dollars".format(name, bid))
            highest_bid = bid
        else:
            print("This bid does not exceed the highest bid, please enter a higher amount")
    except:
        print("This is not a valid entry, please try again")
        
        
        
        
    



