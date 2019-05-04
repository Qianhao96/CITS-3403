from flask import Blueprint, render_template,json,request,jsonify
from survey import db
from survey.models import User, Category, Poll, Response
from flask_login import current_user, login_required
from datetime import datetime, timedelta


polls = Blueprint('polls', __name__)

@polls.route("/polls", methods=['GET'])
def active_polls():
	Categories = Category.query.all()
	movies = Poll.query.filter_by(category_id = 1)
	musics = Poll.query.filter_by(category_id = 2)
	recipes = Poll.query.filter_by(category_id = 3)

	voted_movie = False
	voted_music = False
	voted_recipe = False

	if current_user.is_active:
		responses = Response.query.filter_by(user_id=current_user.id)
		for response in responses:
			if response.category_id is 1:
				voted_movie = True
			if response.category_id is 2:
				voted_music = True
			if response.category_id is 3:
				voted_recipe = True

	return render_template('polls/polls.html',
						   Categories=Categories,
						   movies=movies,
						   musics=musics,
						   recipes=recipes,
						   voted_movie=voted_movie,
						   voted_music=voted_music,
						   voted_recipe=voted_recipe)


@polls.route("/vote", methods=['POST'])
@login_required
def user_votting():
	poll_id = None
	try:
		poll_id = request.get_json()['id']
		poll_id = int(poll_id)
	except:
		return json.dumps({'status':'unsuccess','message':"Bad socket message"})
	finally:
		if poll_id is None:
			return json.dumps({'status':'unsuccess','message':"Bad socket message"})

	poll = Poll.query.filter_by(id = poll_id).first()
	category_id = poll.category_id

	responses = Response.query.filter_by(user_id=current_user.id)
	for response in responses:
		if response.category_id is category_id:
			return json.dumps({'status':'unsuccess','message':"You have voted"})

	response = Response(user_id=current_user.id, category_id=category_id,pool_id=poll_id)
	db.session.add(response)

	rank = poll.rank
	poll.rank = rank + 1

	db.session.commit()

	return json.dumps({'status':'OK','message':"Vote success"})


# @polls.route("/index", methods=['GET'])
# def home():
# 	categorys = Category.query
# 	return render_template('index.html', categorys=categorys, client= get_client())


def normalizeData(catId):
	if catId is None:
		return [],[]
	name = []
	data = []
	polls = Poll.query.filter_by(category_id=catId).order_by(Poll.rank.desc())
	for poll in polls:
		name.append(poll.name)
		data.append(poll.rank)
	return name, data


@polls.route("/getOverview", methods=['POST'])
def getData():
	categoryId = None
	try:
		categoryId = request.get_json()['id']
		categoryId = int(categoryId)
	except:
		return json.dumps({'status':'unsuccess','message':"Bad socket message"})
	finally:
		if categoryId is None and Category.query.filter_by(id=categoryId) is None:
			return json.dumps({'status':'unsuccess','message':"Bad socket message"})
	data = normalizeData(categoryId)
	return jsonify({'status':'unsuccess', 'data': data})


def normalizeElab(catId):
	label = []
	responses = Response.query.filter_by(category_id=catId).order_by(Response.date_posted)

	if responses.count() is 0:
		return None,None

	startDate = responses[0].date_posted
	days = (responses[responses.count()-1].date_posted - startDate).days + 1
	datas = {}
	nameDict = {}

	for name in Poll.query.filter_by(category_id=catId):
		nameDict[name.id] = name.name
		datas[name.name] = [0]*days
	for i in range(days):
		date = startDate + timedelta(days=i)
		for response in responses.filter_by(date_posted = date):
			for j in range(i,days):
				datas[nameDict[response.pool_id]][j] +=1
		label.append(str(date).split(' ')[0])

	return label,datas


@polls.route("/getElaborate", methods=['POST'])
def getEData():
	categoryId = None
	try:
		categoryId = request.get_json()['id']
		categoryId = int(categoryId)
	except:
		return json.dumps({'status':'unsuccess','message':"Bad socket message"})
	finally:
		if categoryId is None and Category.query.filter_by(id=categoryId) is None:
			return json.dumps({'status':'unsuccess','message':"Bad socket message"})
	label, datas = normalizeElab(categoryId)

	return jsonify({'status':'unsuccess','label':label,'data':datas})


