from flask import render_template, flash, url_for, redirect
from app import app
from app.forms import LoginForm

@app.route('/', methods = ['GET','POST'])
@app.route('/login', methods = ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('index'))
	return render_template('login.html', form = form)