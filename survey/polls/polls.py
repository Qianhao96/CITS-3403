from flask import Blueprint, render_template,json,request
from survey import db
from survey.models import User, Category, Poll, Response
from flask_login import current_user, login_required


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

	responses = Response.query.filter_by(user_id=current_user.id)
	for response in responses:
		if response.pool_id is poll_id:
			return json.dumps({'status':'unsuccess','message':"You have voted"})

	poll = Poll.query.filter_by(id = poll_id).first()
	category_id = poll.category_id

	response = Response(user_id=current_user.id, category_id=category_id,pool_id=poll_id)
	db.session.add(response)

	rank = poll.rank
	poll.rank = rank + 1

	db.session.commit()

	return json.dumps({'status':'OK','message':"Vote success"})



