from flask import render_template, url_for, redirect, request, flash, Blueprint
from survey import db, bcrypt
from survey.users.forms import RegistrationForm, LoginForm, RequestResetFrom, ResetPasswordFrom, accountResetPasswordForm
from survey.models import User
from flask_login import login_user, current_user, logout_user, login_required
from survey.users.utils import send_reset_email

users = Blueprint('users', __name__)


@users.route("/register", methods=['POST', 'GET'])
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
		return redirect(url_for('users.login'))
	return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['POST', 'GET'])
def login():
	form = LoginForm()
	# Using bcrypt to check the password
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			flash('Login successfull', 'success')
			return redirect(next_page) if next_page else redirect(url_for('main.index'))
		else:
			flash('Login unsuccessful. Please check Email and Password', 'danger')
	return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
	logout_user()
	flash('Logout successfull', 'success')
	return redirect(url_for('main.index'))


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	form = RequestResetFrom()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		send_reset_email(user)
		flash('An email has been sent to reset your password', 'info')
		return redirect(url_for('users.login'))
	return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	user = User.verify_reset_token(token)
	if user is None:
		flash('That is an invalid or expired token', 'warning')
		return redirect(url_for('users.reset_request'))
	form = ResetPasswordFrom()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user.password = hashed_password
		db.session.commit()

		flash('Your password has been updated! You are now able to login', 'success')
		return redirect(url_for('users.login'))
	return render_template('reset_token.html', title='Reset Password', form=form, token=token)


@users.route("/account_reset_password", methods=['GET', 'POST'])
@login_required
def account_reset_password():
    form = accountResetPasswordForm()
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        current_user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated.', 'success')
        logout()
        return redirect(url_for('users.login'))
    return render_template('reset_password.html', form=form)


@users.route("/my_account", methods=['GET', 'POST'])
@login_required
def my_account():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    return render_template('account.html')


@users.route("/change_info", methods=['GET', 'POST'])
@login_required
def change_info():
    firstname = request.form['info_firstname']
    lastname = request.form['info_lastname']
    email = request.form['info_email']

    current_user.firstname = firstname
    current_user.lastname = lastname
    current_user.email = email
    db.session.commit()

    return redirect(url_for('users.my_account'))
