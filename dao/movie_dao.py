from .model.movie import Movie
from config import Config


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):

        page = filters.get('page')
        status = filters.get('status')

        if status == 'new' and page is not None:
            result = self.session.query(Movie).order_by(Movie.year.desc()). \
                paginate(page=int(page), per_page=Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE, error_out=False).items
            return result

        elif status == 'new':
            result = self.session.query(Movie).order_by(Movie.year.desc()).all()
            return result

        elif page is not None:
            result = self.session.query(Movie).\
                paginate(page=int(page), per_page=Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE, error_out=False).items
            return result

        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director_id(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre_id(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()

