from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin

from survey.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

from survey.admin.views import MyModelView, MyLoginView, MyLogoutView
from survey.models import User
from survey.models import Response
from survey.models import Category
from survey.models import Pool
admin = Admin(template_mode='bootstrap3')


def create_app(confif_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	admin.init_app(app)
	admin.add_view(MyModelView(User, db.session))
	admin.add_view(MyModelView(Response, db.session))
	admin.add_view(MyModelView(Category, db.session))
	admin.add_view(MyModelView(Pool, db.session))
	admin.add_view(MyLoginView(name='Login', endpoint='login'))
	admin.add_view(MyLogoutView(name='Logout', endpoint='logout'))

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	from survey.users.routes import users
	from survey.main.routes import main
	from survey.errors.error import errors
	from survey.polls.polls import polls
	app.register_blueprint(users)
	app.register_blueprint(main)
	app.register_blueprint(errors)
	app.register_blueprint(polls)


	return app
