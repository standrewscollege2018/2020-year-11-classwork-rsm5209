
# set up an empty list to store movies
movies = []

# greeting for user and instructions
print("Enter your 3 favourite movies of all time,\nin order from most favourite to least")

# start loop to ask for three movies
for counter in range (0,3):
    movie = input("Enter name of movie: ")
    movies.append(movie)
    
# telling user their favourite movies
print("Here are your favourite movies in order from most favourite to least favourite\n1. {} \n2. {} \n3. {}".format(movies[0], movies[1], movies[2]))