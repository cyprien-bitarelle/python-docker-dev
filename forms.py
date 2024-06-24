from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField


class SelectionForm(FlaskForm):
    pc_tam = BooleanField("Pc Tamara")
    pc_cypri = BooleanField("Pc Cyprien")
    nas = BooleanField("NAS")
    submit = SubmitField("Allumer")

