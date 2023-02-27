from dao.user_dao import UserDao
from dao.model.user import UserSchema


class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_by_email(self, email):
        usr = self.dao.get_by_email(email)
        # return UserSchema().dump(usr)
        return usr

    def create(self, user_data):
        user_password = user_data.get('password')
        if user_password:
            user_data['password'] = self.dao.get_hash(user_password)
        usr = self.dao.create(user_data)
        return UserSchema().dump(usr)

    def compare_passwords(self, password, other_password):
        password_hash = self.dao.get_hash(other_password)
        return self.dao.compare_passwords(password,password_hash)


