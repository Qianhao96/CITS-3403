from flask import render_template, Blueprint, flash, redirect, url_for, json, request
from survey.models import User, Category, Poll, Response
from survey.user_admin.forms import RegistrationForm, NewCategoryForm, NewPollForm
from survey import db, bcrypt
from survey.user_admin.utils import admin_login_required, save_picture, delete_picture


user_admin = Blueprint('user_admin', __name__)

@user_admin.route("/user_admin", methods=['GET'])
@admin_login_required
def user_index():
	users = User.query.all()
	categories = Category.query.all()
	polls = Poll.query.all()
	responses = Response.query.all()
	user_form = RegistrationForm()
	category_form = NewCategoryForm()
	poll_form = NewPollForm()
	poll_form.rank.data = 0
	return render_template('user-admin/user_admin.html', 
		users=users, categories=categories, polls=polls, responses=responses,
		user_form=user_form, category_form = category_form, poll_form=poll_form,
		title="Admin", data={'form_checking':False})
	

@user_admin.route("/add_user", methods=['POST'])
@admin_login_required
def add_user():
	users = User.query.all()
	categories = Category.query.all()
	polls = Poll.query.all()
	responses = Response.query.all()
	user_form = RegistrationForm()
	category_form = NewCategoryForm()
	poll_form = NewPollForm()
	# Check Form input and encrypt the password before store them
	if user_form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(user_form.password.data).decode('utf-8')
		user = User(firstname = user_form.firstname.data, 
			lastname = user_form.lastname.data,
			email = user_form.email.data,
			gender = user_form.gender.data,
			password = hashed_password,
			is_admin = user_form.is_admin.data)
		db.session.add(user)
		db.session.commit()
		flash('New user account has been created!', 'success')
		return redirect(url_for('user_admin.user_index'))
	flash(u'New user account has not been created! Please try again, or look the log error', 'danger')
	return render_template('user-admin/user_admin.html', 
		users=users, categories=categories, polls=polls, responses=responses,
		user_form=user_form, category_form = category_form, poll_form=poll_form,
		title="Admin", data={'form': 'user_form', 'form_checking': True})

@user_admin.route("/admin_delete_user", methods=['POST'])
@admin_login_required
def admin_delete_user():
	email = request.get_json()['id']
	user = User.query.filter_by(email=email).first()
	db.session.delete(user)
	db.session.commit()
	return json.dumps({'status':'OK','message':'User ' + email + ' has been successfuly deleted'});


@user_admin.route("/add_category", methods=['POST'])
@admin_login_required
def add_category():
	users = User.query.all()
	categories = Category.query.all()
	polls = Poll.query.all()
	responses = Response.query.all()
	user_form = RegistrationForm()
	category_form = NewCategoryForm()
	poll_form = NewPollForm()
	if category_form.validate_on_submit():
		category = Category(name = category_form.category_name.data)
		db.session.add(category)
		db.session.commit()
		flash('New category has been added!', 'success')
		return redirect(url_for('user_admin.user_index'))
	return render_template('user-admin/user_admin.html', 
		users=users, categories=categories, polls=polls, responses=responses,
		user_form=user_form, category_form = category_form, poll_form=poll_form,
		title="Admin", data={'form': 'category_form', 'form_checking': True})


@user_admin.route("/admin_delete_category", methods=['POST'])
@admin_login_required
def admin_delete_category():
	id = request.get_json()['id']
	category = Category.query.filter_by(id=id).first()
	db.session.delete(category)
	db.session.commit()
	return json.dumps({'status':'OK','message':"Category has been successfuly deleted"});


@user_admin.route("/admin_add_poll", methods=['POST'])
@admin_login_required
def admin_add_poll():
	users = User.query.all()
	categories = Category.query.all()
	polls = Poll.query.all()
	responses = Response.query.all()
	user_form = RegistrationForm()
	category_form = NewCategoryForm()
	poll_form = NewPollForm()
	if poll_form.validate_on_submit():
		if poll_form.picture.data:
			picture_file = save_picture(poll_form.picture.data)
			poll = Poll(name = poll_form.poll_name.data,
				rank = poll_form.rank.data,
				category_id = poll_form.category_poll.data,
				image_file = picture_file,
				video_url = poll_form.video.data)
			db.session.add(poll)
			db.session.commit()
			flash('New poll has been added!', 'success')
			return redirect(url_for('user_admin.user_index'))
	print('failed')
	return render_template('user-admin/user_admin.html', 
		users=users, categories=categories, polls=polls, responses=responses,
		user_form=user_form, category_form = category_form, poll_form=poll_form,
		title="Admin", data={'form': 'poll_form', 'form_checking': True})


@user_admin.route("/admin_delete_poll", methods=['POST'])
@admin_login_required
def admin_delete_poll():
	id = request.get_json()['id']
	poll = Poll.query.filter_by(id=id).first()
	delete_picture(poll.image_file)
	db.session.delete(poll)
	db.session.commit()
	return json.dumps({'status':'OK','message':"Poll has been successfuly deleted"});


@user_admin.route("/admin_delete_response", methods=['POST'])
@admin_login_required
def admin_delete_response():
	id = request.get_json()['id']
	category = Response.query.filter_by(id=id).first()
	db.session.delete(category)
	db.session.commit()
	return json.dumps({'status':'OK','message':"category has been successfuly deleted"});
