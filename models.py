from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Name', db.String())
    date = db.Column('Date', db.String())
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.String())
    github = db.Column('GitHub', db.String())

    def __repr__(self):
        return f'''<Project (Name: {self.name}
                Date: {self.date}
                Description: {self.description}
                Skills: {self.skills}
                GitHub: {self.github})'''
