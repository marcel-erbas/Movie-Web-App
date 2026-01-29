import os
import requests

from dotenv import load_dotenv
from flask import Flask, render_template
from data_manager import DataManager
from models import db, Movie

omdb_api_key = os.getenv("OMDB_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Movie-Web-App!"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)