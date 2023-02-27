from flask import request
from flask_restx import Resource, Namespace

from implemented import director_service, director_schema, directors_schema
from parsers import page_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        filters = page_parser.parse_args()
        directors = director_service.get_all(filters)
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        director = director_service.get_by_id(did)
        return director_service.dump(director), 200

