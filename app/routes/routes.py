from app import app
from flask import render_template


@app.route('/')
def root():
    return "<h2>Strip it</h2>"

@app.route('/index')
def index():
    return render_template("index.html")