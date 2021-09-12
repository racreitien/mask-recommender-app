from flask import Flask, redirect, url_for, render_template, request
from flask import g

app = Flask(__name__)

user_info = {}

@app.route("/")  
def first():

    return render_template("index.html")


@app.route("/form1-data", methods = ["POST"])
def form1_data():
    
    if request.method == "POST":

        user_info = get_user_info(request.form)
        #testing
        # no mask if 2 or younger
        if (user_info["age"] == "no"): 
            return render_template("nomask.html")
        # mask if pre-existing conditions or unvaccinated indoors
        elif (user_info["hr"] == "yes" or (user_info["vaccinated"] == "no" and user_info["indoors"] == "yes")):
            return render_template("maskup.html")
        
        return redirect("/q2")


@app.route("/q2") 
def second():

    return render_template("q2.html")   


@app.route("/form2-data", methods = ["POST"]) 
def form2_data():
    if request.method == "POST":

        user_info = get_user_info(request.form)

        if (user_info["locations"] == "yes"):
            return render_template("maskup.html")
        
        return redirect("/q3")


@app.route("/q3") 
def third():

    return render_template("q3.html")


@app.route("/form3-data", methods = ["POST"])
def form3_data():
    if request.method == "POST":

        user_info = get_user_info(request.form)

        if (user_info["crowded"] == "no" and user_info["indoors"] == "no"):
            return render_template("nomask.html")
        elif (user_info["crowded"] == "yes"):
            return render_template("maskup.html")

        return redirect("/q4")


@app.route("/q4")
def fourth():

    return render_template("q4.html")


@app.route("/form4-data", methods = ["POST"])
def form4_data():
    if request.method == "POST":

        user_info = get_user_info(request.form)
        
        if (user_info["everyone-vaxxed"] == "yes" and user_info["vaccinated"] == "yes"):
            return render_template("nomask.html")
        
        return redirect("/q5")


@app.route("/q5")                                
def fifth():

    return render_template("q5.html")


@app.route("/form5-data", methods = ["POST"])
def form5_data():
    if request.method == "POST":

        user_info = get_user_info(request.form)
        
        if (user_info["lr"] == "no"):
            return render_template("maskup.html")
        
        return render_template("nomask.html")


def get_user_info(request_data):
    # get information form POST response
    form_data = request_data
    for key, value in form_data.items():
        user_info[key] = value
    
    return user_info