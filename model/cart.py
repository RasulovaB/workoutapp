from dataclasses import dataclass

from db.db import db


@dataclass
class Cart(db.Model):
    exerciseID: int = db.Column(db.Integer, primary_key=True)
    workoutID: int = db.Column(db.Integer, db.ForeignKey('workout.workoutID'))
    muscleGroup: str = db.Column(db.String, nullable=False)


def init_model(app):
    with app.app_context():
        db.create_all()
