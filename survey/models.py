from survey import db




class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(20), nullable=False)
	lastname = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.firstname}', '{self.lastname}', '{self.email}')"