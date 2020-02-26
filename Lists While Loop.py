movies = []

print("Enter your favourite movies from most favourite to least favourite, type 'stop' when you have finished the list")
keep_asking = True

while keep_asking == True:
    movie_name = input("Enter a favourite movie: ")
    if movie_name == "stop":
        keep_asking = False
    else:
        movies.append(movie_name)

for i in range(len(movies)):
    print("These are your favourite movies from most favourite to least favourite")
    print(i+1, movies[i])