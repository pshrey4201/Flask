from flask import Blueprint, render_template, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import subprocess
import socket

serverIP = socket.gethostbyname(socket.gethostname())
# subprocess.call("set FLASK_APP=__init__", shell=True)
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Caleb:Jumpy123@server/db'
#Init the applicatoin
db.init_app(app)
#SQLAlchemy().create_all(app=create_app())
#from __init__ import db, create_app
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
#@auth.route('/login, methods=['POST'])
#def login_post():
@app.route('/signup')
def signup():
    return render_template('signup.html')
#@auth.route('/signup', methods='[POST'])
#def signup_post():
@app.route('/logout')
def logout():
    return redirect(url_for('index'))
@app.route('/profile')
def profile():
    return render_template('profile.html')
if __name__ == '__main__':
app.run(host=serverIP, port="80", debug=True)
