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
        db.session.add(Exercise(
            exerciseID=2, exerciseName='crunches2', exerciseLink='https://www.youtube.com/embed/Xyd_fa5zoEU',
            muscleGroup='Abs'
        ))
        db.session.add(Exercise(
            exerciseID=3, exerciseName='crunches3', exerciseLink='https://www.youtube.com/embed/Xyd_fa5zoEU',
            muscleGroup='Abs'
        ))

        db.session.add(Exercise(
            exerciseID=4, exerciseName='B21', exerciseLink='https://www.youtube.com/embed/Xyd_fa5zoEU',
            muscleGroup='Back'
        ))
        db.session.add(Exercise(
            exerciseID=5, exerciseName='B1', exerciseLink='https://www.youtube.com/embed/Xyd_fa5zoEU',
            muscleGroup='Back'
        ))
        db.session.add(Exercise(
            exerciseID=6, exerciseName='B3', exerciseLink='https://www.youtube.com/embed/Xyd_fa5zoEU',
            muscleGroup='Back'
        ))
        db.session.add(Exercise(
            exerciseID=7, exerciseName='A1', exerciseLink='https://www.youtube.com/embed/Xyd_fa5zoEU',
            muscleGroup='Arms'
        ))
        db.session.commit()
