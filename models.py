from flask import Flask
from flask.blueprints import DeferredSetupFunction
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    title = db.Column('Title', db.String())
    date = db.Column('Date', db.String())
    desc = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.String())
    github = db.Column('GitHub', db.String())

    def __repr__(self):
        return f'''<Project (Title: {self.title}
                Date: {self.date}
                Description: {self.desc}
                Skills: {self.skills}
                GitHub: {self.github})'''
