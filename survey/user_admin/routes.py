from flask import render_template, Blueprint, flash, redirect, url_for, json, request
from survey.models import User
from survey.user_admin.forms import RegistrationForm
from survey import db, bcrypt
from survey.user_admin.utils import admin_login_required

user_admin = Blueprint('user_admin', __name__)

@user_admin.route("/user_admin", methods=['POST', 'GET'])
@admin_login_required
def user_index():
	users = User.query.all()
	form = RegistrationForm()
	# Check Form input and encrypt the password before store them
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(firstname = form.firstname.data, 
			lastname = form.lastname.data,
			email = form.email.data,
			gender = form.gender.data,
			password = hashed_password,
			is_admin = form.is_admin.data)
		db.session.add(user)
		db.session.commit()
		flash('New user account has been created!', 'success')
		return redirect(url_for('user_admin.user_index'))
	return render_template('user_admin.html', users=users, title="Admin", form=form)


@user_admin.route("/admin_delete_user", methods=['POST'])
@admin_login_required
def admin_delete_user():
	email = request.get_json()['email']
	user = User.query.filter_by(email=email).first()
	db.session.delete(user)
	db.session.commit()
	return json.dumps({'status':'OK','message':'User ' + email + ' has been successfuly deleted'});