from dataclasses import dataclass

from db.db import db


@dataclass
class Exercise(db.Model):
    exerciseID: int = db.Column(db.Integer, primary_key=True)
    workoutID: int = db.Column(db.Integer, db.ForeignKey('workout.workoutID'))
    exerciseName: str = db.Column(db.String(15), nullable=False)
    exerciseLink: str = db.Column(db.String(15), nullable=False)
    muscleGroup: str = db.Column(db.String(15), nullable=False)


def init_model():
    db.create_all()
