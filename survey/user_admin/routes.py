from flask import render_template, Blueprint

user_admin = Blueprint('user-admin', __name__)

@user_admin.route("/user_admin")
def index():
	return render_template('user_admin.html')

