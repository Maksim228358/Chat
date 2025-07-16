import random
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash , check_password_hash

db = SQLAlchemy()
def random_color():
    return "#{:06x}".format(random.randint(0,0xFFFFFF))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique = True,nullable = False)
    passworld_hash = db.Column(db.String(150),nullable = False)