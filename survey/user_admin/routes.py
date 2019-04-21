from flask import render_template, Blueprint, flash, redirect, url_for, json, request
from survey.models import User, Category, Pool, Response
from survey.user_admin.forms import RegistrationForm, NewCategoryForm
from survey import db, bcrypt
from survey.user_admin.utils import admin_login_required

user_admin = Blueprint('user_admin', __name__)

@user_admin.route("/user_admin", methods=['GET'])
@admin_login_required
def user_index():
	users = User.query.all()
	categories = Category.query.all()
	polls = Pool.query.all()
	responses = Response.query.all()
	user_form = RegistrationForm()
	category_form = NewCategoryForm()
	return render_template('user-admin/user_admin.html', 
		users=users, categories=categories, polls=polls, responses=responses,
		user_form=user_form, category_form = category_form,
		title="Admin")


@user_admin.route("/add_user", methods=['POST'])
@admin_login_required
def add_user():
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


@user_admin.route("/admin_delete_user", methods=['POST'])
@admin_login_required
def admin_delete_user():
	email = request.get_json()['email']
	user = User.query.filter_by(email=email).first()
	db.session.delete(user)
	db.session.commit()
	return json.dumps({'status':'OK','message':'User ' + email + ' has been successfuly deleted'});


@user_admin.route("/add_category", methods=['POST'])
@admin_login_required
def add_category():
	form = NewCategoryForm()
	if form.validate_on_submit():
		category = Category(name = form.name.data)
		db.session.add(category)
		db.session.commit()
		flash('New category has been added!', 'success')
		return redirect(url_for('user_admin.user_index'))


@user_admin.route("/admin_delete_category", methods=['POST'])
@admin_login_required
def admin_delete_category():
	id = request.get_json()['id']
	category = Category.query.filter_by(id=id).first()
	db.session.delete(category)
	db.session.commit()
	return json.dumps({'status':'OK','message':"Category has been successfuly deleted"});