from flask import Flask, render_template
app = Flask(__name__)

@app.route('/one')
def page_one():
	return render_template("one.html")

@app.route('/two')
def page_two():
	return render_template("two.html")

@app.route('/text_one', methods=["POST"])
def text_one():
	pass

@app.route('/text_two', methods=["POST"])
def text_two():
	pass
