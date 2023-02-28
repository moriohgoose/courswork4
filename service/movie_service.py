from dao.movie_dao import MovieDao


class MovieService:

    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters):
        movies = self.dao.get_all(filters)
        return movies

    def update(self, data):
        self.dao.update(data)
        return self.dao

    def create(self, data):
        return self.dao.create(data)

    def delete(self, mid):
        self.dao.delete(mid)
