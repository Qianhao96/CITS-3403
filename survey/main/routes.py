from flask import render_template, Blueprint
from flask import request
import urllib.request
import json
from survey.models import User, Response, Poll, Category

main = Blueprint('main', __name__)
access_key='4c0fc23c4090d22cf284ecce6d043517'

client = [None]*7

def get_info(address: str):
	api = 'http://api.ipstack.com/' + address + '?access_key=' + access_key
	result = urllib.request.urlopen(api).read()
	result = result.decode()
	result = json.loads(result)
	return result

def get_client():
	return client

def process():
	ip = request.remote_addr
	result = get_info(ip)
	info = [ip,
			result['country_name'],
			result['region_name'],
			result['city'],
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


