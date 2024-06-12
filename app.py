from flask import Flask, render_template, request
import csv
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_id = request.form['user_id']

    sorted_movies = read_csv('sorted_movies_by_rating.csv')
    average_movies = read_csv('average_merged_movies.csv')
    user_favorites = read_csv('user_favorite_genres_and_movies.csv')

    user_sorted_movies = get_user_sorted_movies(sorted_movies, user_id)
    user_average_movies = get_user_average_movies(average_movies)
    user_favorite_movies = get_user_favorite_movies(user_favorites, user_id)

    return render_template('results.html', user_sorted_movies=user_sorted_movies, user_average_movies=user_average_movies, user_favorite_movies=user_favorite_movies)

import sys

def read_csv(filename):
    data = []
    max_int = sys.maxsize
    while True:
        try:
            csv.field_size_limit(max_int)
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)
                return data
        except OverflowError:
            max_int = int(max_int / 10)

def get_user_sorted_movies(sorted_movies, user_id):
    user_movies = []
    for row in sorted_movies:
        if int(row['userId']) == int(user_id):
            movies = eval(row['movies'])  # Using eval to convert string representation to list of dictionaries
            user_movies = [{'title': movie['title'], 'genre': movie['genre'], 'imdbId': movie['imdbId']} for movie in movies[:20]]
            break
    return user_movies

def get_user_average_movies(average_movies):
    user_movies = [{'title': row['title'], 'genre': row['genre'], 'imdbId': row['imdbId']} for row in average_movies[:20]]
    return user_movies

def get_user_favorite_movies(user_favorites, user_id):
    user_favorite_movies = []
    for row in user_favorites:
        if int(row['userId']) == int(user_id):
            favorite_movies = eval(row['Movies'])  
            for movie in favorite_movies[0]:
                user_favorite_movies.append({'title': movie['title'], 'imdbId': movie['imdbId']})
            break
    return user_favorite_movies

if __name__ == '__main__':
    app.run(debug=True)
