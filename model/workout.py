from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@dataclass
class Workout(db.Model):
    exerciseId: int
    userID: int
    exerciseName: str
    exerciseLink: str
    muscleGroup: str
    exerciseTime: int
    exerciseSets: int
    exerciseRest: int
    exerciseCompletion: bool

    exerciseId = db.Column(db.Integer, primary_key=True, nullable=False)
    userID = db.Column(db.Integer, nullable=False)
    exerciseName = db.Column(db.String(50), nullable=False)
    exerciseLink = db.Column(db.String(120), nullable=False)
    muscleGroup = db.Column(db.String(30), nullable=False)
    exerciseTime = db.Column(db.Integer, nullable=False)
    exerciseSets = db.Column(db.Integer, nullable=False)
    exerciseRest = db.Column(db.Integer, nullable=False)
    exerciseCompletion = db.Column(db.Boolean, nullable=False)
