from flask import Flask
from flask_sqlalchemy import SQLAlchemy

sql:SQLAlchemy = None

class SQL_Handler:
    app:Flask = None

    def __init__(self, app : Flask = None):
        self.app = app

    def connect(self, host = "localhost", user = "postgres", password = "postgres", db = ""):
        if self.app is None:
            return
        self.app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://%s:%s@%s/%s' % (user, password, host, db)

        sql = SQLAlchemy(self.app)

# Models
class SQL_Model_Membership(sql.Model):
    id = sql.Column(sql.Serial, primary_key=True)
    fullname = sql.Column(sql.Text, unique=True, nullable=False)
    email = sql.Column(sql.Text, unique=True, nullable=False)
    country = sql.Column(sql.Text, nullable=False)
    state = sql.Column(sql.Text, nullable=False)
    questionData = sql.Column(sql.Text, nullable=False)
    creationData = sql.Column(sql.Date, default=sql.CURRENT_DATE, nullable=False)
    expiredate = sql.Column(sql.Date, nullable = False)
    paiduntil = sql.Column(sql.Date, nullable = False)
    logs = sql.Column(sql.Text, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.fullname

