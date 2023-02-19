from flask import request
from flask_restx import Resource, Namespace

from implemented import director_service, director_schema, directors_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        director = director_service.get_by_id(did)
        return director_service.dump(director), 200

