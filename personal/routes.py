from . import *
from flask import render_template

@app.route("/")
def hello_world():
    return render_template('page.html')