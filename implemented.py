from dao.movie_dao import MovieDao
from dao.genre_dao import GenreDao
from dao.director_dao import DirectorDao
from dao.user_dao import UserDao

from service.movie_service import MovieService
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.user_service import UserService
from service.auth import AuthService

from dao.model.movie import MovieSchema
from dao.model.director import DirectorSchema
from dao.model.genre import GenreSchema
from dao.model.user import UserSchema

from setup_db import  db

director_dao = DirectorDao(session=db.session)
director_service = DirectorService(director_dao)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_dao = GenreDao(session=db.session)
genre_service = GenreService(genre_dao)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

movie_dao = MovieDao(session=db.session)
movie_service = MovieService(movie_dao)
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

user_dao = UserDao(session=db.session)
user_service = UserService(user_dao)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

auth_service = AuthService(user_service=user_service)
