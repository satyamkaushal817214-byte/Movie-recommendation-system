from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle

app = Flask(__name__)
CORS(app)

# Load data
movies = pd.read_csv("movies.csv")
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie_name):
    movie_name = movie_name.lower().strip()

    # Find closest match
    matches = movies[movies['title'].str.lower().str.contains(movie_name)]

    if matches.empty:
        print("No match found for:", movie_name)  # debug
        return []

    idx = matches.index[0]

    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]

@app.route("/recommend", methods=["POST"])
def recommend_api():
    data = request.get_json()
    movie = data.get("movie")

    results = recommend(movie)
    return jsonify({"recommendations": results})

if __name__ == "__main__":
    app.run(debug=True)