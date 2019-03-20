from . import db
#Can change the attributions later or can add them.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.string(100), unique=True)
    password = db.Column(db.string(100))
    name = db.Column(db.string(1000))