from dataclasses import dataclass

from db.db import db


@dataclass
class Cart(db.Model):
    cartID: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID: int = db.Column(db.Integer, db.ForeignKey('user.userID'))
    exerciseID: int = db.Column(db.Integer, db.ForeignKey('exercise.exerciseID'))
    muscleGroup: str = db.Column(db.String(20), db.ForeignKey('exercise.muscleGroup'))


def init_model():
    db.create_all()
