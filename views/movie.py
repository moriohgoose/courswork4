from flask import request
from flask_restx import Resource, Namespace

from implemented import movie_service, movie_schema, movies_schema
from parsers import page_parser

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        status = request.args.get("director_id")
        page = request.args.get("genre_id")
        filters = {
            "status": status,
            "page": page,
        }
        # filters = page_parser.parse_args()
        all_movies = movie_service.get_all(filters)

        return movies_schema.dump(all_movies), 200

    def post(self):
        data = request.json
        new_movie = movie_service.add_movie(data)
        return '', 201, {'location': f'/movies/{new_movie.id}'}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movies_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data[id] = mid
        movie_service.update(data)

        return 'updated', 204

    def delete(self, mid):
        movie_service.del_movie(mid)
        return 'deleted', 204