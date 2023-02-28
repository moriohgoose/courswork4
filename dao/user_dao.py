import hashlib
import base64
import hmac
from config import Config
from .model.user import User


class UserDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all

    def create(self, user_data):
        usr = User(**user_data)
        self.session.add(usr)
        self.session.commit()
        return usr

    def delete(self, uid):
        usr = self.get_one(uid)
        self.session.add(usr)
        self.session.commit()

    def update(self, user_data):
        usr = self.get_one(user_data.get("id"))

        for k, v in user_data.items():
            setattr(usr, k, v)

        self.session.add(usr)
        self.session.commit()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).one_or_none()

