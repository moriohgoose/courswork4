from .model.genre import Genre
from config import Config


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        page = filters.get('page')

        if page is not None:
            result = self.session.query(Genre).paginate(page=int(page), per_page=Config.ITEMS_PER_PAGE,
                                                        max_per_page=Config.MAX_PAGE, error_out=False).items
            return result

        return self.session.query(Genre).all()

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)