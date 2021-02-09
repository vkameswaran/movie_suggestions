import pandas as pd
import json

data1 = pd.read_csv("datasets/tmdb_5000_credits.csv")

def analyse(m1):
    actors = []
    crew = []
    for p in json.loads(m1.cast):
        if p["order"] < 10:
            actors.append(p["name"])
    for p in json.loads(m1.crew):
        if p["job"] in ["Editor", "Director", "Writer", "Producer", "Screenplay", "Original Music Composer"]:
            crew.append(p["name"])
    return actors, crew

def compare(m2, actors, crew):
    score = 0
    for p in json.loads(m2.cast):
        if p["name"] in actors:
            score = score + 1
    for p in json.loads(m2.crew):
        if p["name"] in crew:
            score = score + 1
    return score

def find_movie_by_director(director):
    list_of_movies = []
    for idx, movie in data1.iterrows():
        credits = json.loads(movie.crew)
        credits = {c["job"]: c["name"] for c in credits}
        if "Director" in credits and credits["Director"] == "Steven Spielberg":
            list_of_movies.append(movie["title"])
    return list_of_movies

def search(title):
    # Try to find a perfect match
    for idx, movie in data1.iterrows():
        if movie.title.lower() == title.lower():
            return idx
    # Try to find a partial match
    for idx, movie in data1.iterrows():
        if title.lower() in movie.title.lower():
            return idx
    # Otherwise, we didn't find it
    raise LookupError("We couldn't find %s in our database." % title)

def find_similar_movies(movie, top_n=10):
    print("\nMovies similar to", movie.title, ":")
    actors, crew = analyse(movie)
    similar_movies = sorted(
        [(m[1].title, compare(m[1], actors, crew)) for m in data1.iterrows()],
        key=lambda m: m[1], reverse=True)[1:1+top_n]
    for i, m in enumerate(similar_movies):
        print("%d. %s" % (i + 1, m[0]))
    print()
