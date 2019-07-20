from functools import wraps
from flask import (Flask, flash, g, redirect, render_template, request,
                   session, url_for)
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# create the sqlalchemy object
db = SQLAlchemy(app)

# function for database connection
# we've replaced this with the SQLAlchemy connection
# def connect_db():
#    return sqlite3.connect(app.database)

# Placeholder secret_key (must be replaced later)
app.secret_key = 'My Precious'

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
    posts = []
    try:
        g.db = connect_db()
        cur = g.db.execute('select * from posts')
        # Below variable utilises list comprehension for displaying the posts
        posts = [dict(title=row[0], description=row[1])
                 for row in cur.fetchall()]
        g.db.close()
    except sqlite3.OperationalError:
        flash("You have no DataBase")
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


######################## Debugger #########################
if __name__ == '__main__':
    app.run(debug=True)
