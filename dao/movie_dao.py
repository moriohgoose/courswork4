from .model.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        page = filters.get('page')
        status = filters.get('status')
        stmt = self.session.query(Movie)
        if status == 'new':
            stmt.order_by(Movie.year.desc())

        return stmt.paginate(page=page, per_page=12).items

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

