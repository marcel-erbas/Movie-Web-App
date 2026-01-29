from models import db, User, Movie

class DataManager():
    def create_user(self, name):
        new_user = User(name=name)
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            print(f"Error creating user: {e}")
            db.session.rollback()

    def get_users(self):
        return User.query.all()

    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie):
        try:
            db.session.add(movie)
            db.session.commit()
        except Exception as e:
            print(f"Error adding movie: {e}")
            db.session.rollback()

    def update_movie(self, movie_id, new_title):
        movie = Movie.query.get(movie_id)
        if movie:
            try:
                movie.title = new_title
                db.session.commit()
            except Exception as e:
                print(f"Error updating movie: {e}")
                db.session.rollback()

    def delete_movie(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            try:
                db.session.delete(movie)
                db.session.commit()
            except Exception as e:
                print(f"Error deleting movie: {e}")
                db.session.rollback()

    