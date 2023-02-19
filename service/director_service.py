from dao.director_dao import DirectorDao


class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, gid):
        return self.dao.get_one(gid)