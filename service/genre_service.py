from dao.genre_dao import GenreDao


class GenreService:
    def __init__(self, dao: GenreDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, gid):
        return self.dao.get_one(gid)