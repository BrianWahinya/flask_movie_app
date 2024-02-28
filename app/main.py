from flask import Flask, request, render_template
from trending_movies import get_trending_movies_data
from latest_movies import get_latest_movies_data


app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
def index():
    data = get_trending_movies_data()

    pages=data["total_pages"]
    results=data["total_results"]
    trending_list = []

    for movie in data["results"]:
        if "original_title" in movie:
            trending_list.append(movie['original_title'])

    return render_template("index.html", 
        message=f"Trending: {pages} pages, {results} movies", 
        trending_list=trending_list
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)