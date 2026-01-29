import os
import requests

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from data_manager import DataManager
from models import db, Movie

omdb_api_key = os.getenv("OMDB_API_KEY")

app = Flask(__name__)


@app.route('/')
def index():
    users = data_manager.get_users()
    return render_template('index.html', users=users)


@app.route('/users', methods=['POST'])
def add_user():
    name = request.form.get('name')
    data_manager.create_user(name)
    return redirect(url_for('index'))


@app.route('/users/<int:user_id>/movies', methods=['GET', 'POST'])
def user_movies(user_id):
    if request.method == 'POST':
        title = request.form.get('title')
        movie_data = get_omdb_data(title, user_id)
        if movie_data:
            data_manager.add_movie(movie_data)
        return redirect(url_for('user_movies', user_id=user_id))

    movies = data_manager.get_movies(user_id)
    return render_template('movies.html', user_id=user_id, movies=movies)


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    new_title = request.form.get('new_title')
    data_manager.update_movie(movie_id, new_title)
    return redirect(url_for('user_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(movie_id)
    return redirect(url_for('user_movies', user_id=user_id))


basedir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(basedir, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)


app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(data_dir, 'movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

load_dotenv()

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager() # Create an object of your DataManager class

def get_omdb_data(title, user_id):
    url = f"http://www.omdbapi.com/?t={title}&apikey={omdb_api_key}"
    response = requests.get(url)
    data = response.json()
    
    if data.get("Response") == "True":
        return Movie(
            title=data.get("Title"),
            director=data.get("Director"),
            year=int(data.get("Year")[:4]) if data.get("Year") else 0,
            poster_url=data.get("Poster"),
            user_id=user_id
        )
    return None


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)