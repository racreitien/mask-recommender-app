from flask import Flask, redirect, url_for, render_template, request
from flask import g

app = Flask(__name__)

# 1. ** working off example at https://www.py4u.net/discuss/194000 
# reference for Flask.g: https://www.kite.com/python/docs/flask.g 
# 2. https://www.notion.so/How-to-run-our-app-be3740b6406741888b89b8727acb3739 
# 3. Python dictionaries: https://www.w3schools.com/python/python_dictionaries.asp
# 4. Get/Post Tutorial https://www.askpython.com/python-modules/flask/flask-forms
# 5. Radio button tutorial https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio

user_info = {}

@app.route("/") # form 1   first 
def first():

    return render_template("index.html")


@app.route("/form1-data", methods = ["POST"])
def form1_data(): # form 1 data  second 
    if request.method == "POST":
        # get information form first form
        form_data = request.form
        for key, value in form_data.items():
            user_info[key] = value

        print("Page 1 --- user_info data: \n")
        for info in user_info:
            print(info + ": " + user_info[info])

        # no mask if 2 or younger
        if (user_info["age"] == "no"): 
            return render_template("nomask.html")
        # mask if pre-existing conditions or unvaccinated indoors
        elif (user_info["hr"] == "yes" or (user_info["vaccinated"] == "no" and user_info["indoors"] == "yes")):
            return render_template("maskup.html")
        
        return redirect("/q2")


@app.route("/q2") # form 2      third
def second():

    return render_template("q2.html")   


@app.route("/form2-data", methods = ["POST"]) # data form 2         fourth 
def form2_data():
    if request.method == "POST":
        # get information form first form
        form_data = request.form
        user_info["locations"] = form_data["locations"]
        
        print("Page 2 --- user_info data: \n")
        for info in user_info:
            print(info + ": " + user_info[info])

        if (user_info["locations"] == "yes"):
            return render_template("maskup.html")
        
        return redirect("/q3")


@app.route("/q3") # form 3          fifth
def third():

    return redirect("/form3-data")


@app.route("/form3-data", methods = ["POST"]) # form 3 data             sixth
def form3_data():

    #elif (user_info["locations"] == "no" and (user_info["indoors"] == "no"):
    #    return render_template("nomask.html")

    return redirect("/q4")

@app.route("/q4") # form 4  
def fourth():

    return redirect("/form4-data")

@app.route("/form4-data", methods = ["POST"]) # form 4 data
def form4_data():

    return redirect("/q5")

@app.route("/q5") # form 4                                  
def fourth():

    return redirect("/form5-data")