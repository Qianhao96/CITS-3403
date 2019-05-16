from flask import Blueprint, render_template

references = Blueprint('references', __name__)

@references.route("/reference", methods=['GET'])
def reference():
	return render_template('reference/reference.html')
