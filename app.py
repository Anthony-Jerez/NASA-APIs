# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/yourimage', methods = ['GET', 'POST'])
def yourimage():
    userImageChoice = request.form["imagechoice"]
    myimageURL = getImageUrlFrom(userImageChoice)
    return render_template("yourgif.html", time = datetime.now(), imgURL = myimageURL)
#return 'You got your Image' + user_imagechoice