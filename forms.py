from os import name
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of Student: ")
    submit = SubmitField("Add Student: ")

class DelForm(FlaskForm):
    id = IntegerField("Id number of student to remove: ")
    submit = SubmitField("Remove Student: ")

class AddFatherForm(FlaskForm):
    name = StringField("Name of father: ")
    stu_id = IntegerField("Id of student: ")
    submit = SubmitField("Add Student")