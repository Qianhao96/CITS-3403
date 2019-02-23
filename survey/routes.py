from flask import render_template, url_for, redirect, request, flash
from survey import app, db, bcrypt
from survey.forms import RegistrationForm, LoginForm
from survey.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def index():
	return render_template('base.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
	form = RegistrationForm()
	# Check Form input and encrypt the password before store them
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(firstname = form.firstname.data, 
			lastname = form.lastname.data,
			email = form.email.data,
			gender = form.gender.data,
			password = hashed_password)
		db.session.add(user)
		db.session.commit()

		flash('Your account has been created! You are now able to login', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
	form = LoginForm()
	# Using bcrypt to check the password
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			flash('Login successfull', 'success')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		else:
			flash('Login unsuccessful. Please check Email and Password', 'danger')
	return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
	logout_user()
	flash('Logout successfull', 'success')
	return redirect(url_for('index'))


@app.route("/account")
# login_required makes this rout only can be accessed by an authenticated user
@login_required 
def account():
	return render_template('account.html')







