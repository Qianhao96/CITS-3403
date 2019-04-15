from flask import render_template, Blueprint
from survey.models import User
from survey.user_admin.forms import RegistrationForm

user_admin = Blueprint('user_admin', __name__)

@user_admin.route("/user_admin", methods=['POST', 'GET'])
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
			password = hashed_password)
		db.session.add(user)
		db.session.commit()

		flash('Your account has been created! You are now able to login', 'success')
	return render_template('user_admin.html', users=users, title="Admin", form=form)
