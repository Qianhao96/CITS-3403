from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, BooleanField, TextField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from survey.models import User
from flask_login import current_user
from survey import bcrypt
from flask_wtf.file import FileField, FileAllowed
from survey.models import User, Response, Poll, Category

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
	is_admin = BooleanField('New admin?')
	submit = SubmitField('Creat New User')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one')

	def validate_gender(self, gender):
		if gender.data == 'None':
			raise ValidationError('Please secect your gender')


class NewCategoryForm(FlaskForm):
	category_name = StringField('Category name', validators=[DataRequired(), Length(min=1, max=50)])
	end_date = DateField('Poll End Date', format='%d/%m/%Y', validators=[DataRequired()])
	catergory_description = StringField('Please briefly describe the new catergory(limited to 500 character)', validators=[DataRequired(), Length(min=1, max=500)])
	catergory_picture = FileField('Update category Picture (345 * 299Px)', validators=[FileAllowed(['jpg', 'png'])])
	category_submit = SubmitField('Creat New Category')


class NewPollForm(FlaskForm):
	poll_name = StringField('Name', validators=[DataRequired()])
	rank = IntegerField('Rank (Please initial this field with 0)', validators=[NumberRange(max=1, min=-1)])
	category_poll = SelectField('Category Name', choices=[])
	description = StringField('Please briefly describe the new poll(limited to 500 character)', validators=[DataRequired(), Length(min=1, max=500)])
	picture = FileField('Update Poll Picture (220 * 320Px)', validators=[FileAllowed(['jpg', 'png'])])
	video = StringField('Video Url (A video that describe thsi poll)', validators=[DataRequired()])
	poll_submit = SubmitField('Creat New Poll')








