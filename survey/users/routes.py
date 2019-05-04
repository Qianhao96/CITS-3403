from flask import render_template, url_for, redirect, request, flash, Blueprint, json
from survey import db, bcrypt
from survey.users.forms import RegistrationForm, LoginForm, RequestResetFrom, ResetPasswordFrom, accountResetPasswordForm, accountForm
from survey.models import User, Response, Poll, Category
from flask_login import login_user, current_user, logout_user, login_required
from survey.users.utils import send_reset_email
from survey.main.routes import get_client

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
	return render_template('user/register.html', title='Register', form=form, client= get_client())


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
	return render_template('user/login.html', title='Login', form=form, client= get_client())


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
	return render_template('user/reset_request.html', title='Reset Password', form=form, client= get_client())


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
	return render_template('user/reset_token.html', title='Reset Password', form=form, token=token, client= get_client())


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
	return render_template('user/reset_password.html', form=form, client= get_client())


@users.route("/my_account", methods=['GET', 'POST'])
@login_required
def my_account():
	form = accountForm()

	response_table = []
	responses = Response.query.filter_by(user_id=current_user.id)
	i = 0
	for response in responses:
		print(response)
		poll_name = Poll.query.filter_by(id = response.pool_id).first().name
		response_table.append([i, poll_name, str(response.date_posted).split()[0], response.pool_id])
		i+=1

	if not current_user.is_authenticated:
		return redirect(url_for('users.login'))

	if form.validate_on_submit():
		current_user.firstname = firstnames
		current_user.lastname = lastnames
		current_user.email = emails
		db.session.commit()
	return render_template('user/account.html', form = form, response_table=response_table, client= get_client())


@users.route("/delete_response", methods=['POST'])
@login_required
def remove_response():
	poll_id = None
	try:
		poll_id = request.get_json()['rm_poll_id']
		poll_id = int(poll_id)
	except:
		return json.dumps({'status':'unsuccess','message':"Bad socket message"})
	finally:
		if poll_id is None:
			return json.dumps({'status':'unsuccess','message':"Bad socket message"})

	responses = Response.query.filter_by(user_id=current_user.id)
	for response in responses:
		if response.pool_id is poll_id:
			db.session.delete(response)
			poll = Poll.query.filter_by(id = poll_id).first()
			rank = poll.rank
			poll.rank = rank - 1
			db.session.commit()
			return json.dumps({'status':'OK','message':"Vote successfully removed"})
	return json.dumps({'status':'unsuccess','message':"You have not yet voted this poll"})



