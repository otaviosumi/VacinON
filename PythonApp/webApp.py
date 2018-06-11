from flask import Flask, render_template, request , url_for, redirect, flash, session, abort
import os
app = Flask(__name__)

user = {'username' : 'Bob'}

vacinas = [
	{
		'tipo' : 'caxumba', 'data' : '21/03/2005', 'lote' : '0111944'
	},
	{
		'tipo' : 'febre amarela', 'data' : '19/08/2008', 'lote' : '0111946'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', vacinas=vacinas, user=user)

@app.route("/showlogin")
def login():
	return render_template('showlogin.html')

@app.route("/showlogout")
def logout():
	return render_template('showlogout.html')


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug = True, host='0.0.0.0', port=4000)
