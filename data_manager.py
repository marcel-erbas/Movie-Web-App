from models import db, User, Movie


# -------------------------------------------------------------------
# Data Manager Class
# -------------------------------------------------------------------

class DataManager():
    
    # -------------------------------------------------------------------
    # User Methods
    # -------------------------------------------------------------------

    def create_user(self, name):
        """Creates a new user in the database."""
        new_user = User(name=name)
        try:
            db.session.add(new_user)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            db.session.rollback()
            return False

    def get_users(self):
        """Retrieves all users."""
        return User.query.all()

    def delete_user(self, user_id):
        """Deletes a user and all their associated movies."""
        user = User.query.get(user_id)
        if user:
            try:
                # Delete all movies of the user first
                Movie.query.filter_by(user_id=user_id).delete()
                # Then delete the user
                db.session.delete(user)
                db.session.commit()
                return True
            except Exception as e:
                print(f"Error deleting user: {e}")
                db.session.rollback()
                return False
        return False

    # -------------------------------------------------------------------
    # Movie Methods
    # -------------------------------------------------------------------

    def get_movies(self, user_id):
        """Retrieves all movies for a specific user."""
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie):
        """Adds a new movie to the database."""
        try:
            db.session.add(movie)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Error adding movie: {e}")
            db.session.rollback()
            return False

    def update_movie(self, movie_id, new_title):
        """Updates the title of a movie."""
        movie = Movie.query.get(movie_id)
        if movie:
            try:
                movie.title = new_title
                db.session.commit()
                return True
            except Exception as e:
                print(f"Error updating movie: {e}")
                db.session.rollback()
                return False
        return False

    def delete_movie(self, movie_id):
        """Deletes a movie from the database."""
        movie = Movie.query.get(movie_id)
        if movie:
            try:
                db.session.delete(movie)
                db.session.commit()
                return True
            except Exception as e:
                print(f"Error deleting movie: {e}")
                db.session.rollback()
                return False
        return False

    