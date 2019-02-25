from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from survey.models import User

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