import os
# from forms import AddForm, DelForm, AddFatherForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import backref

app = Flask(__name__)

app.config['SECRET_KEY'] = "knowledgeshelf"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer,primary_keys=True)
    name = db.Column(db.Text)
    father = db.relationship('Father',backref='student', uselist =False)

    def __int__(self,name):
        self.name = name

    def __repr__(self):
        if self.father:
            return f"student name is {self.name}, id is {self.id} and father name is {self.father.name}."
        else :
            return f"student name is {self.name}, id is {self.id} and father name is."

class Father(db.Model):
    __tablename__ = "fathers"
    id = db.Column(db.Integer,primary_keys=True)
    name = db.Column(db.Text)
    father = db.Column(db.Integer, db.ForeignKey('students_id'))

    def __init__(self, name, student_id):
        self.name = name
        self.students_id = student_id
    
    def __repr__(self):
        return f"Father name: {self.name}"


@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)