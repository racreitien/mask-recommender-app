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
    information = []

    return render_template("index.html", information=information)


@app.route("/second", methods = ["POST"])
def second():
    if request.method == "POST":
        # get information form first form
        form_data = request.form
        user_info = {}
        for key, value in form_data.items():
            user_info[key] = value

        # initialize g object information
        g._information = {}
        setattr(g, "_information", user_info)

        print("user_info data: \n")
        for info in user_info:
            print(info + ": " + user_info[info])

        # no mask if 2 or younger
        if (user_info["age"] == "no"): 
            return render_template("nomask.html", form_data=form_data)
        # mask if pre-existing conditions or unvaccinated indoors
        elif (user_info["hr"] == "yes" or (user_info["vaccinated"] == "no" and user_info["indoors"] == "yes")):
            return render_template("maskup.html", form_data=form_data)
        else:
            return render_template("third.html")


@app.route("/third", methods = ["POST"])
def third():
    
    # get more info 
    return render_template("third.html")


@app.route("/fifth")
def fifth():
    default_info = {"everyoneVax":False}
    information = getattr(g, "information", default_info)

    return render_template("fifth.html", information=information)

@app.route("/sixth")
def sixth():
    default_info = {"lowRisk":False}
    information = getattr(g, "information", default_info)

    return render_template("sixth.html", information=information)
