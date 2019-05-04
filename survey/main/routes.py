from flask import render_template, Blueprint
from flask import request
import urllib.request
import json
from survey.models import User, Response, Poll, Category

main = Blueprint('main', __name__)


def get_client():
	client = process()
	return client

def process():
	ip = request.remote_addr
	info = [ip,
			request.accept_languages[0][0].capitalize(),
			request.user_agent.browser.capitalize(),
			request.user_agent.platform.capitalize()]
	return info

@main.route("/")
def index():
	if request.user_agent.platform is "macos":
		request.user_agent.platform = "mcintosh"
	client = process()
	categorys = Category.query
	return render_template('index.html', categorys=categorys, client= client)


