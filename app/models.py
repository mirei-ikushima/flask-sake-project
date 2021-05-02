from app import create_app
from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from time import time
import jwt


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

    def get_reset_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in},
                          create_app().config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_token(token):
        try:
            id = jwt.decode(token, create_app().config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except Exception as e:
            print(token)
            print(create_app().config['SECRET_KEY'])
            raise e

        return User.query.get(id)

    @classmethod
    def users_with_bottles(cls):
        return cls.query.join(cls.bottles).group_by(cls.id, Bottle.id).having(Bottle.id >= 1)

    @classmethod
    def bottles_total(cls, name):
        return cls.query.join(cls.bottles).filter(cls.username == name).count()

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
    notes = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_bottle(self):
        db.session.add(self)
        db.session.commit()

    def delete_bottle(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def total_collections(cls):
        return cls.query.distinct(cls.user_id).count()
