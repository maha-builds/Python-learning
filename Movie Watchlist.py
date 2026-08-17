watchlist = []

for i in range(3):
    movie_name = input("Enter movie name: ")
    watchlist.append(movie_name)

print(watchlist)

count = len(watchlist)
print("Length of watchlist is", count)

remove_name = input("Enter remove movie name: ")
watchlist.remove(remove_name)
print("Remove movie name is", watchlist)

search_name = input("Enter search movie name: ")

if search_name in watchlist:
    print("movie found")
else:
    print("movie not found")
