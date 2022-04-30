# from flask_sqlalchemy import SQLAlchemy
# from hwwapp import db

# db = SQLAlchemy()


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     # workout = db.relationship('Item', backref='author', lazy=True)
#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"
