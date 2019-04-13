import os
import secrets
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from survey.models import User
from flask_login import current_user
from survey import bcrypt

class RegistrationForm(FlaskForm):
	firstname = StringField('Firstname',
		validators=[DataRequired(), Length(min=2, max=20)])
	lastname = StringField('Lastname',
		validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', 
		validators=[DataRequired(), Email()])
	gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', 
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign up ')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one')

	def validate_gender(self, gender):
		if gender.data == 'None':
			raise ValidationError('Please secect your gender')


class LoginForm(FlaskForm):
	email = StringField('Email', 
		validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class RequestResetFrom(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('There is no account with taht email. You must register first')


class ResetPasswordFrom(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset Password')


class accountResetPasswordForm(FlaskForm):
	old_password = PasswordField('Old Password', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
	reset_password= SubmitField('Reset Password')

	def validate_old_password(self, old_password):
		PWD = User.query.filter_by(email=current_user.email).first()
		if not bcrypt.check_password_hash(PWD.password, old_password.data):
			raise ValidationError('Pasword Incorrect')

class accountForm(FlaskForm):
	new_firstname = StringField('First Name', validators=[DataRequired()])
	new_lasttname = StringField('Lirst Name', validators=[DataRequired()])
	new_email = StringField('Email', validators=[DataRequired(), Email()])
	change_info= SubmitField('Change Info')

	def validate_new_firstname(self, new_firstname):
		user = User.query.filter_by(firstname=new_firstname.data).first()
		if user:
			raise ValidationError('That first name is taken. Please choose a different one')

	def validate_new_email(self, new_email):
		user = User.query.filter_by(email=new_email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one')


