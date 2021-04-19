from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    bottles = db.relationship('Bottle', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("You cannot see the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User {0}'.format(self.username)


class Bottle(db.Model):
    __tablename__ = "bottles"

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String)
    label = db.Column(db.String)
    identifier = db.Column(db.String)
    photo = db.Column(db.String)
    category = db.Column(db.String)
    maker = db.Column(db.String)
    status = db.Column(db.String)
    region = db.Column(db.String)
    price = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_bottle(self):
        db.session.add(self)
        db.session.commit()

    def delete_bottle(self):
        db.session.delete(self)
        db.session.commit()
