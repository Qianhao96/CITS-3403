from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('base.html')


@app.route("/account_creation")
def account_creation():
	return render_template('account_creation.html')


if __name__ == '__main__':
	app.run(debug=True)