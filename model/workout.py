from dataclasses import dataclass
from datetime import date

from db.db import db


@dataclass
class Workout(db.Model):
    workoutID: int = db.Column(db.Integer, primary_key=True, nullable=False)
    difficulty: int = db.Column(db.Integer, nullable=False)
    userRating: int = db.Column(db.Integer, nullable=False)
    workoutCompletion: bool = db.Column(db.Boolean, nullable=False)
    startDate: date = db.Column(db.Date, nullable=False)
    completionDate: date = db.Column(db.Date, nullable=False)


def init_model():
    db.create_all()
