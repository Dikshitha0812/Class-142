from flask import Flask,jsonify,request
from storage import all_movies, liked_movies, did_not_watch_movies, not_liked_movies
from demographic_filtering import output 
from contentFiltering import get_recommendation

app = Flask(__name__)

@app.route("/get-movies")
def get_movies():
    movie_data = {
        "title":all_movies[0][19],
        "poster_link":all_movies[0][27],
        "release_date":all_movies[0][13] or "N/A",
        "duration":all_movies[0][15],
        "rating":all_movies[0][20],
        "overview":all_movies[0][9]
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/liked-movies",methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    liked_movie.append(movie)
    all.movies.pop(0)
    return jsonify({
        "status": "success"
    })
    

@app.route("/unliked-movies",methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    not_liked_movie.append(movie)
    all.movies.pop(0)
    return jsonify({
        "status": "success"
    })
 
    

@app.route("/recommended-movies")
def recommended_movies():
    all_recommended = []
    for movie in liked_movie:
        output = get_recommendation(movie[19])
        for data in output:
            all_recommended.append(data)

    all_recommended.sort()
    import itertools
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))

    movie_data = []
    for movie in all_recommended:
        data = {
            "title":movie[19],
            "poster_link":movie[27],
            "release_date":movie[13] or "N/A",
            "duration":movie[15],
            "rating":movie[20],
            "overview":movie[9]
        }
        movie_data.append(data)

    return jsonify({
        "data": movie_data,
        "status": "successful"
    })

if __name__ == "__main__":
    app.run(debug = True)