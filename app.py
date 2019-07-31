from functools import wraps
from flask import (Flask, flash, g, redirect, render_template, request,
                   session, url_for)
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# config settings (includes DB connection, debugger, and secret_key)
import os
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object(config.DevelopmentConfig)


# create the sqlalchemy object
db = SQLAlchemy(app)

# after the above db is set up then we can import our tables from models.py
from models import *


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to log in to access this page')
            return redirect(url_for('login'))
    return wrap


##################Page Routes##############################

# Route: Home Page
@app.route('/')
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


# Route: Welcome page
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


# Route: login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid User Name or Password; please try again'
        else:
            session['logged_in'] = True
            flash('You\'re good to go!')
            return redirect(url_for('name_and_shame'))
    return render_template("login.html", error=error)


# Route: logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You\'re logged out')
    return redirect(url_for('home'))


# Route: Name and shame page
@app.route('/name-and-shame')
@login_required
def name_and_shame():
    return render_template("name_and_shame.html")
