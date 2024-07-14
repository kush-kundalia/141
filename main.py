from flask import Flask, jsonify, request
import pandas as pd
movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies = movies_data[["original_title", "poster_link", "release_date", "runtime", "weighted_rating"]]
liked_movies = []
disliked_movies = []
not_watched_movies = []
# variables to store data
def extract_val():
  movie_data = {
    "original_title": all_movies.iloc[0,0], 
    "poster_link": all_movies.iloc[0,1],
    "release_date": all_movies.iloc[0,2],
    "duration": all_movies.iloc[0,3],
    "rating": all_movies[0,4]
  }

# method to fetch data from database
@app.route("/movies")
def get_movies():
  movie_data = extract_val()
  return jsonify ({
    "data": movie_data, 
    "status": "success"
  })

# /movies api

@app.route("/liked-movies")
def liked_movies():
  global all_movies 
  movie_data = extract_val()
  liked_movies.append(movie_data)
  all_movies.drop([0], inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify ({
    "status": "success"
  })


@app.route("/liked-list")
def like():
  global liked_movies
  return jsonify ({
    "data": liked_movies,
    "status": "success"
  })
# /like api

@app.route("/disliked-movies")
def disliked_movies():
  global all_movies 
  movie_data = extract_val()
  disliked_movies.append(movie_data)
  all_movies.drop([0], inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify ({
    "status": "success"
  })

@app.route("/did-not-watch")
def not_watched_movies():
  global all_movies 
  movie_data = extract_val()
  not_watched_movies.append(movie_data)
  all_movies.drop([0], inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify ({
    "status": "success"
  })

# /dislike api


# /did_not_watch api


if __name__ == "__main__":
  app.run()