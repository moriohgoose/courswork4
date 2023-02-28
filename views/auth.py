from flask import request, jsonify
from flask_restx import abort, Namespace, Resource

from implemented import user_service, auth_service


auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthRegisterView(Resource):

    def post(self):
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if None in [email, password]:
            abort(400)

        return user_service.create(data), 201


@auth_ns.route('/login')
class AuthLoginView(Resource):
    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            abort(400)

        tokens = auth_service.generate_tokens(email=email, password=password)

        return tokens, 201

    def put(self):
        data = request.json

        access_token = data.get('access_token')
        refresh_token = data.get('refresh_token')

        validated = auth_service.validate_tokens(access_token, refresh_token)

        if not validated:
            return "Invalid token", 400

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201