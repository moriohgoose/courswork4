from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service, user_schema, users_schema

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):

    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        data = request.json
        user = user_service.create(data)
        return '', 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):

    def get(self, uid):
        user = user_service.get_one(uid)
        return user_schema.dump(user), 200

    def patch(self, uid):
        data = request.json
        if "id" not in data:
            data["id"] = uid
        return user_service.update(data), 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


@user_ns.route("/password")
class UpdateUserPasswordViews(Resource):

    def put(self):
        data = request.json
        email = data.get("email")
        old_password = data.get("old_password")
        new_password = data.get("new_password")

        user = user_service.get_by_email()

        if user_service.compare_passwords(user.password, old_password):
            user.password = user_service.make_password_hash(new_password)
            result = user_schema.dump(user)
            user_service.update(result)
            print("Пароль обновлён")
        else:
            print("Пароль не обновлён")

        return "", 201

