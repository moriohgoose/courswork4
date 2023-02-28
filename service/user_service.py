import hashlib
import base64
import hmac

from dao.user_dao import UserDao
from config import Config
from dao.model.user import UserSchema


class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def update(self, user_data):
        self.dao.update(user_data)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def make_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            Config.PWD_SALT,
            Config.PWD_ITERATIONS
        ))

    def compare_passwords(self, password, other_password):
        return hmac.compare_digest(
            base64.b64decode(password),
            hashlib.pbkdf2_hmac('sha256', other_password.encode('utf-8'), Config.PWD_SALT, Config.PWD_ITERATIONS)
        )


