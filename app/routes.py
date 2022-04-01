from flask import Flask, render_template, flash, redirect
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from app import myobj

name = 'Lisa'
city_names = ['Paris','London', 'Rome', 'Tahiti']

class CityForm(FlaskForm):
	city = StringField('City Name', validators=[DataRequired()])
	submit = SubmitField("Submit")

@myobj.route('/', methods=('GET', 'POST'))
def home():
	form=CityForm()
	if form.validate_on_submit():
		flash('{0}'.format(form.city.data))
	return render_template('home.html', len=len(city_names), name = name, city_names = city_names, form=form)
