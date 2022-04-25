from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    userId: int
    userName: str
    email: str
    password: str

    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
