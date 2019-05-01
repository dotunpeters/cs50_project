"""
Routes and views for the flask application.
"""
  
from flask import render_template
from FlaskWebApp import app
from FlaskWebApp.variables import *


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts, title="Home", yearNow=yearNow)


@app.route("/about")
def about():
    return render_template('about.html', title='About', yearNow=yearNow)