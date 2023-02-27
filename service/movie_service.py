from dao.movie_dao import MovieDao


class MovieService:

    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        return self.dao.update(movie)

    def add_movie(self, data):
        new_movie = self.dao.create(data)

        return new_movie

    def filters(self, data):
        if data.get('genre_id') is not None:
            return self.dao.get_by_genre_id(data.get('genre_id'))
        elif data.get('director_id') is not None:
            return self.dao.get_by_director_id(data.get('director_id'))
        elif data.get('year') is not None:
            return self.dao.get_by_year(data.get('year'))
        else:
            return self.dao.get_all()

    def del_movie(self, mid):
        movie = self.get_one(mid)
        self.dao.delete(movie)