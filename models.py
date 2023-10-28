from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Authentication(db.Model):
    '''
    App login
    '''
    __bind_key__ = "login"
    __tablename__ = "authenticate"
    login_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    username = db.Column(db.String(25))
    password = db.Column(db.String(25))