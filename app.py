from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

if __name__=='__main__':
    app.run(debug=True)