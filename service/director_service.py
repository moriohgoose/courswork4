from dao.director_dao import DirectorDao


class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def get_by_id(self, did):
        return self.dao.get_one(did)
