from flask import Flask, render_template, request , url_for, redirect, flash, session, abort
import os
app = Flask(__name__)

@app.route("/")
def main():
	if not session.get('logged_in'):
		return render_template('showsignup.html')
	else:
		return render_template('index.html')

@app.route('/showsignup', methods=['POST', 'GET'])
def showSignUp():
	if request.form['password']=='password' and request.form['username'] == 'user':
		session['logged_in'] = True
	else:
		flash('Senha incorreta!!!')
	return main()

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug = True, host='0.0.0.0', port=4000)

