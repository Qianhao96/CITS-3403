from flask import Blueprint, render_template
from survey.main.routes import get_client


references = Blueprint('references', __name__)

@references.route("/reference", methods=['GET'])
def reference():
	return render_template('reference/reference.html', client= get_client())
