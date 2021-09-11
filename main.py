from flask import Flask, redirect, url_for, render_template
from flask import g

app = Flask(__name__)

# 1. ** working off example at https://www.py4u.net/discuss/194000 
# reference for Flask.g: https://www.kite.com/python/docs/flask.g 
# 2. https://www.notion.so/How-to-run-our-app-be3740b6406741888b89b8727acb3739 
# 3. Python dictionaries: https://www.w3schools.com/python/python_dictionaries.asp



@app.route("/")
def first():
    default_info = {"name": None, "age": None, "indoors":False}
    information = getattr(g, "information", default_info)

    return render_template("index.html", information=information)

# @app.route("/second")
# def second():
