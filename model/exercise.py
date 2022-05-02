from dataclasses import dataclass

from db.db import db


@dataclass
class Exercise(db.Model):
    exerciseID: int = db.Column(db.Integer, primary_key=True)
    exerciseName: str = db.Column(db.String(15), nullable=False)
    exerciseLink: str = db.Column(db.String(15), nullable=False)
    muscleGroup: str = db.Column(db.String(15), nullable=False)


def init_model(app):
    with app.app_context():
        db.create_all()
        db.session.add(Exercise(
            exerciseID=1, exerciseName='crunches', exerciseLink='https://www.youtube.com/embed/Xyd_fa5zoEU',
            muscleGroup='Abs'
        ))
        db.session.commit()
