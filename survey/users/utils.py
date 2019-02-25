from flask_mail import Message
from flask import url_for
from survey import mail




def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
	msg.body = f''' To reset password, please visit the following links:
{url_for('users.reset_token', token=token, _external=True)}


If you did not make this request, then please ignor this email.
'''
	mail.send(msg)