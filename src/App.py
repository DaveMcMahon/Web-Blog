from flask import Flask
from flask import render_template
from flask import request
from flask import session

# New comment - Dave McMahon - 04/09/2017

from src.common.Database import Database
from src.models.User import User

app = Flask(__name__)
app.secret_key = "5+34Fuj"


@app.route("/")
def login_route():
    return render_template("login.html")


@app.before_first_request
def initialize_database():
    Database.initialise()


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)

    return render_template("profile.html", email=session['email'])


if __name__ == '__main__':
    app.debug = True
    app.run(port=4995)
