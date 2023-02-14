from flask import Flask, render_template, request, flash

# initial application which takes in our main module reprented by name.
# This command creates a class for our app
app = Flask(__name__)
app.secret_key = "gjKJKhghgHJJJ"  # to set secret key

# select a rout for our app


@app.route("/hello")  # "hello" represents the last part of our URL
# associating this route to a function that displays only our html template
def index():
    flash("what's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")
