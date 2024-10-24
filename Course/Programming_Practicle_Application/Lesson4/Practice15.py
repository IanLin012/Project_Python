movies = {'Inception': 8.8, 'The Shawshank Redemption': 9.3, 'The Godfather': 9.2}
total = 0
for score in movies.values():
    total+=score
print("The average score is " + str(total/3))