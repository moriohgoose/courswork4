from .model.director import Director
from config import Config


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        page = filters.get('page')

        if page is not None:
            result = self.session.query(Director).paginate(page=int(page), per_page=Config.ITEMS_PER_PAGE,
                                                           max_per_page=Config.MAX_PAGE, error_out=False).items
            return result

        return self.session.query(Director).all()

    def get_one(self, did):
        return self.session.query(Director).get(did)



