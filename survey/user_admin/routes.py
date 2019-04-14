from flask import render_template, Blueprint
from survey.models import User

user_admin = Blueprint('user_admin', __name__)

@user_admin.route("/user_admin")
def index():
	users = User.query.all()
	return render_template('user_admin.html', users=users, title="Admin")

