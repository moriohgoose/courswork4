from .model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        page = filters.get('page')
        stmt = self.session.query(Director)
        return stmt.paginate(page=page, per_page=12).items

    def get_one(self, did):
        return self.session.query(Director).get(did)



