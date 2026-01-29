from flask_sqlalchemy import SQLAlchemy


# -------------------------------------------------------------------
# Database Setup
# -------------------------------------------------------------------

db = SQLAlchemy()


# -------------------------------------------------------------------
# Models
# -------------------------------------------------------------------

class User(db.Model):
    """User Model: Represents a user in the system."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Movie(db.Model):
    """Movie Model: Represents a movie associated with a user."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)