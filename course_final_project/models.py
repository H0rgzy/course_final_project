from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), index= True, unique= True)
    email = db.Column(db.String(50), index= True, unique= True)
    password_hash = db.Column(db.String(50))
    visits = db.relationship('Visit', backref='user', lazy='dynamic')

    def __repr__(self):
        return "User is {}".format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    place = db.Column(db.String(100), index= True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer, index= True, unique = False)

