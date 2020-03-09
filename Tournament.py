""" This code creates a tournament that randomises games and tells you who won and how many points they ended up with """
# Creating a list so opponent team names can be stored
opponents = []
# So error catching and while loops can work properly
get_team = True
get_opponents = True
# Points tally so it can be recorded
points = 0
# So the opponent asking can be stopped
stop_options = ["end", "stop", "done"]
# Error catching for symbols
chars = set("$,`~!@#%^&*()':;./?><-_=+|{}[]")
# Getting own team name
while get_team == True:
    # Error Catching
    try:
        team_name = input("Enter the name of your team: ")
# Error catching for symbols
        if any((c in chars) for c in team_name) or team_name == "":
            print("Please enter a valid name")
        else:
# Exiting program after getting team name
            print("Great! {} is now entered in the tournament".format(team_name))
            get_team = False
    except:
# Error message if invalid input
        print("Please enter a valid name")
# Instructions to end asking for opponents 
print("Type 'end' when all the teams have been entered")
# Asking for opponent names
while get_opponents == True:
    try:
        opponent_team = input("Enter the name of an opponent: ")
        if opponent_team.lower() in stop_options:
            get_opponents = False
        elif any((c in chars) for c in opponent_team) or opponent_team == "":
            print("Please enter a valid name")
        else:
            print("Great! {} has been entered".format(opponent_team))
            opponents.append(opponent_team)
    except:
        print("Please enter a valid name")

for i in range(len(opponents)):
    get_result = True
    while get_result == True:
        try:
            print("Game versus {}:".format(opponents[i]))
            own_score = int(input("What did {} score?\n".format(team_name)))
            if own_score < 0:
                print("Please enter a valid score")
            else:
                other_score = int(input("What did {} score?\n".format(opponents[i])))
                if other_score < 0:
                    print("Please enter a valid score")            
            
                else:
                    if own_score > other_score:
                        print("{} score: {}".format(team_name, own_score))
                        print("{} score: {}".format(opponents[i], other_score))
                        print("You won!")
                        points +=3
                    elif own_score < other_score:
                        print("{} score: {}".format(team_name, own_score))
                        print("{} score: {}".format(opponents[i], other_score))
                        print("You lost")
                        points +=1
                    else:
                        print("{} score: {}".format(team_name, own_score))
                        print("{} score: {}".format(opponents[i], other_score))
                        print("You drew!")  
                        points +=2
                    get_result = False
        except:
            print("Please enter a valid score")
        
print("{} finished with a total of {} points".format(team_name, points))
        
    