import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load dataset
movies = pd.read_csv("movies.csv")

# Combine features
movies["tags"] = movies["genre"] + " " + movies["overview"]

# Convert text to vectors
cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(movies["tags"]).toarray()

# Compute similarity
similarity = cosine_similarity(vectors)

# Save model
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("Model trained and saved!")