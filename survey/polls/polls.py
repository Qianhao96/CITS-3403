from flask import Blueprint, render_template
from survey import db
from survey.models import User, Category, Pool, Response
from flask_login import current_user, login_required

polls = Blueprint('polls', __name__)

@polls.route("/polls", methods=['GET'])
@login_required
def active_polls():
	Categories = Category.query.all()
	movies = Pool.query.filter_by(category_id = 1)
	musics = Pool.query.filter_by(category_id = 2)
	recipes = Pool.query.filter_by(category_id = 3)

	voted_movie = False
	voted_music = False
	voted_recipe = False

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

