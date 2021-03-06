from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from survey import db, login_manager
from flask_login import UserMixin
from flask import current_app
import datetime

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(20), nullable=False)
	lastname = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	gender = db.Column(db.String(5), nullable=False)
	password = db.Column(db.String(60), nullable=False)
	is_admin = db.Column(db.Boolean, default=False)
	response = db.relationship('Response', backref='user', lazy=True)

	def get_reset_token(self, expires_sec=1800):
		s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)

	def __repr__(self):
		return f"User('{self.firstname}', '{self.lastname}','{self.gender}', '{self.email}')"


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	response = db.relationship('Response', backref='category', lazy=True)
	poll = db.relationship('Poll', backref='category', lazy=True)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	description = db.Column(db.String(500), nullable=False, default='There is currrentlly no information. Please wait for update')
	end_date = db.Column(db.DateTime, nullable=False)

	def __repr__(self):
 		return f"Category('{self.name}')"


class Poll(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	rank = db.Column(db.Integer, nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
	response = db.relationship('Response', backref='poll', lazy=True)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	video_url = db.Column(db.String(200), nullable=False, default="https://www.youtube.com/embed/m_NeIyG98Nc")
	description = db.Column(db.String(500), nullable=False, default='Get more information by clicking the play button!!!')

	def __repr__(self):
 		return f"Poll('{self.name}', '{self.rank}')"


class Response(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
	pool_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.date.today())

	def __repr__(self):
		return f"Response('{self.user.id}', '{self.category.id}', '{self.poll.id}', '{self.date_posted}')"





