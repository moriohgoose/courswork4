from service.user_service import UserService
from datetime import datetime
import calendar
import jwt
from flask import abort
from config import Config


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            abort(404)

        if not self.user_service.compare_passwords(user.password, password):
            abort(400)

        data = {
            'email': user.email,
        }

        # 30 minutes access token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, Config.SECRET_HERE, algorithm=Config.JWT_ALGO)

        # 130 days for refresh token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, Config.SECRET_HERE, algorithm=Config.JWT_ALGO)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=Config.SECRET_HERE, algorithm=Config.JWT_ALGO)
        email = data.get('email')

        user = self.user_service.get_by_email(email=email)

        if user is None:
            abort(404)
        return self.generate_tokens(email, user.password, is_refresh=True)

    def validate_tokens(self, access_token, refresh_token):
        for token in [access_token, refresh_token]:
            try:
                jwt.decode(jwt=token, key=Config.SECRET_HERE, algorithm=Config.JWT_ALGO)
            except Exception as e:
                return False
        return True

