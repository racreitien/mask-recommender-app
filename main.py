from flask import Flask, redirect, url_for, render_template, request
from flask import g

app = Flask(__name__)

# 1. ** working off example at https://www.py4u.net/discuss/194000 
# reference for Flask.g: https://www.kite.com/python/docs/flask.g 
# 2. https://www.notion.so/How-to-run-our-app-be3740b6406741888b89b8727acb3739 
# 3. Python dictionaries: https://www.w3schools.com/python/python_dictionaries.asp
# 4. Get/Post Tutorial https://www.askpython.com/python-modules/flask/flask-forms
# 5. Radio button tutorial https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio

@app.route("/")
def first():
    default_info = {"name": None, "age": None, "indoors":False}
    information = getattr(g, "information", default_info)

    return render_template("index.html", information=information)

@app.route("/second", methods = ["POST"])
def second():
    if request.method == "POST":
        form_data = request.form
        return render_template("second.html", form_data=form_data)

@app.route("/third")
def third():
    default_info = {"Locations":False}
    information = getattr(g, "information", default_info)

    return render_template("third.html", information=information)   
      
@app.route("/fourth")
def fourth():
    default_info = {"Crowded":False}
    information = getattr(g, "information", default_info)

    return render_template("fourth.html", information=information)












