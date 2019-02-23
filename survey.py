from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '53b240c28fcb03bab6e190ecb565d0aa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey.db'
db = SQLAlchemy(app)



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


if __name__ == '__main__':
	app.run(debug=True)