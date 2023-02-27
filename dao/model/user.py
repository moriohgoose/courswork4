from marshmallow import Schema, fields
from setup_db import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String())
    name = db.Column(db.String())
    surname = db.Column(db.String())
    favorite_genre = db.Column(db.String())


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    password = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.String()
