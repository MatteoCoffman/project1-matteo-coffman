import os
import random
import json
from flask import Flask, render_template
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

TMDB_API_KEY = os.environ["TMDB_API_KEY"]

def get_movie_data(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        movie_data = json.loads(response.text)
        return movie_data
    else:
        return None

def get_wikipedia_link(movie_title):
    search_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "utf8": 1,
        "formatversion": 2,
        "srsearch": f"{movie_title} film",
        "srlimit": 1
    }

    response = requests.get(search_url, params=params)
    data = response.json()

    if data["query"]["search"]:
        page_title = data["query"]["search"][0]["title"]
        wikipedia_link = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
        return wikipedia_link
    else:
        return None

@app.route("/")
def index():
    movie_ids = [496243, 530385, 12096, 1091, 348, 9806, 244786, 545611, 785084, 82507, 558, 374720, 4964, 11031, 137]

    movie_id = random.choice(movie_ids)

    movie_data = get_movie_data(movie_id)
    wikipedia_link = get_wikipedia_link(movie_data["title"])

    base_url = "https://image.tmdb.org/t/p/"
    poster_size = "w500"
    poster_url = f"{base_url}{poster_size}{movie_data['poster_path']}"
    
    genre_names_list = []
    for genre in movie_data["genres"]:
        genre_names_list.append(genre["name"])

    return render_template("index.html", movie_data=movie_data, wikipedia_link=wikipedia_link, poster_url=poster_url, genre_names_list=genre_names_list)

if __name__ == "__main__":
    app.run(debug=True)
