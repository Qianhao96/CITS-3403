class Config:
	SECRET_KEY = '53b240c28fcb03bab6e190ecb565d0aa'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///survey.db'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = ''
	MAIL_PASSWORD = ''