from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@dataclass
class Workout(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    exerciseName = db.Column(db.String(50), nullable=False)
    exerciseLink = db.Column(db.String(120), nullable=False)
    muscleGroup = db.Column(db.String(30), nullable=False)
    exerciseTime = db.Column(db.Integer, nullable=False)
    exerciseSets = db.Column(db.Integer, nullable=False)
    exerciseRest = db.Column(db.Integer, nullable=False)
    exerciseCompletion = db.Column(db.Boolean, nullable=False)
