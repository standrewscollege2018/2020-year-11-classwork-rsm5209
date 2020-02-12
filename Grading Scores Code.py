""" This code gets the grade of your exam and tells you if you got excellence, merit or achieved or not achieved """

# get score of user
score = int(input("What is your score?\n "))

# grade score

if score >= 7:
    print("You got Excellence! Well done!")
elif score >= 5:
    print("You got merit! Well done!")
elif score >= 3:
    print("You got achieved! Well done!")
else:
    print("You got not achieved, better luck next time")
