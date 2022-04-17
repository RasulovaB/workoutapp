"""
 * FILENAME: [hww-app]
 * AUTHOR: [Team Workout App]
 * COURSE: [CMSC 495 7383]
 * PROFESSOR: [Jeff Sanford]
 * CREATEDATE: [04/16/2022]

"""
from flask import Flask, render_template
from matplotlib.pyplot import title

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login-page.html", title="Login")


@app.route("/register")
def register():
    return render_template("signup-page.html", title="Register")


# run file with python3 cmd
if __name__ == "__main__":
    app.run(debug=True)
