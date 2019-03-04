from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, login_user, logout_user
from flask import redirect, url_for, Blueprint, render_template, flash
from flask_admin import BaseView, expose
from survey.models import User


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

class MyModelView(ModelView):
	def is_accessible(self):
		return current_user.is_authenticated


	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for("admin.index"))


class MyLoginView(BaseView):

	def is_accessible(self):
		return not current_user.is_authenticated

	@expose('/', methods=['POST', 'GET'])
	def index(self):
		form = AdminLoginForm()
		if form.validate_on_submit():
			user = User.query.filter_by(email=form.email.data).first()
			if user.is_admin and user.password == form.password.data:
				login_user(user)
				flash('Login successfull', 'success')
				return redirect(url_for('admin.index'))
			else:
				flash('Login unsuccessful. Please check Email and Password', 'danger')
		return self.render('admin/login.html', form=form)



class MyLogoutView(BaseView):
	def is_accessible(self):
		return current_user.is_authenticated
	
	@expose('/')
	def index(self):
		logout_user()
		flash('Logout successfull', 'success')
		return redirect(url_for('admin.index'))
		


class AdminLoginForm(FlaskForm):
	email = StringField('Email', 
		validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')
