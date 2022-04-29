from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@dataclass
class User(db.Model):
    userID: int
    username: str
    email: str
    password: str

    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    exerciseTime: db.Column(db.Integer, default=0, nullable=False)
    exerciseSets: db.Column(db.Integer, default=0, nullable=False)
    exerciseRest: db.Column(db.Integer, default=0, nullable=False)

    exerciseTime: int = 0
    exerciseSets: int = 0
    exerciseRest: int = 0
