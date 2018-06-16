from flask import Flask, render_template, request , url_for, redirect, flash, session, abort
import os
import datetime
from pymongo import MongoClient

#Starting and creating DB###################################################################
client = MongoClient('localhost', 27017)
db = client['database']

users = db['users-collection']

allergies = [
	{
		'origin' : 'Acido acetil', 'severity' : 'Grave'
		},
		{
		'origin' : 'Alcool', 'severity' : 'Leve'
		},
		{
		'origin' : 'Dipirona', 'severity' : 'Risco de vida'
		},
		{
		'origin' : 'Chocolate', 'severity' : 'Mediana'
		}
]

vaccines = [
	{
		'tipo' : 'caxumba', 'data' : '21/03/2005', 'lote' : '0111944'
	},
	{
		'tipo' : 'febre amarela', 'data' : '19/08/2008', 'lote' : '0111946'
	}
]

user = {
		'_id' : 1,
		'username' : 'Bob',
		'sus' : 3928840,
		'age' : '26',
		'bloodType' : 'A+',
		'birthday' : '24/02/1992',
		'dateInserted' : datetime.datetime.now(),
		'allergies' : allergies,
		'vaccines' : vaccines
		}

usuarios = db.users

if usuarios.find_one({'username' : 'Bob'}):
	usuarios.remove({})
	print('User inserted')
	usuarios.insert_one(user)
else:
	print('User inserted')
	usuarios.insert_one(user)

def findUserBySUS(susNumber):
	return usuarios.find_one({'sus' : susNumber})

def getUserVaccines(susNumber):
	return usuarios.find_one({'sus' : susNumber})['vaccines']

#End of DB start code #DB###################################################################

username = 'Bob'

app = Flask(__name__)





@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', vacinas=getUserVaccines(3928840), user=findUserBySUS(3928840))

@app.route("/showlogin")
def login():
	return render_template('showlogin.html')

@app.route("/showlogout")
def logout():
	return render_template('showlogout.html')


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug = True, host='0.0.0.0', port=4000)
