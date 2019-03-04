import os
import secrets
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from survey.models import User
from flask_login import current_user
from survey import bcrypt
from flask import flash, url_for

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
    ##set up the page
    dashboard = TextField('Dashboard')
    myPolls = TextField('My Polls')
    editAccount = TextField('Edit Account')
    changePassword = TextField('Change Password')

    #update password section
    odd_password = PasswordField('Odd Password', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    reset_password= SubmitField('Reset Password')

    def validate_odd_password(self, odd_password):
        PWD = User.query.filter_by(email=current_user.email).first()
        if  not bcrypt.check_password_hash(PWD.password, odd_password.data):
            raise ValidationError('Pasword Incorrect')
