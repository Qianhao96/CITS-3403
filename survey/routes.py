from flask import render_template, url_for
from survey import app
from survey.forms import RegistrationForm, LoginForm
from survey.models import User


@app.route("/")
def index():
	return render_template('base.html')


@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', 
		title='Register', form=form)


@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)