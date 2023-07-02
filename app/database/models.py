from app import db
from flask_login import (
    LoginManager, UserMixin, current_user,
    login_required, login_user, logout_user)



class User(db.Model, ):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)