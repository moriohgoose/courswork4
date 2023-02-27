from .model.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        page = filters.get('page')
        stmt = self.session.query(Genre)
        return stmt.paginate(page=page, per_page=12).items

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)