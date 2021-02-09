import pandas as pd
import json
from utils import analyse, compare, search, find_similar_movies, data1

# my_movie = data1.iloc[3]
# topN = 10
# find_similar_movies(my_movie, 5)

searchIndex = search(input("Enter a movie name: "))
new_movie = data1.iloc[searchIndex]

find_similar_movies(new_movie, 5)
