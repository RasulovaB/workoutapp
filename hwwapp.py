"""
 * FILENAME: [hww-app]
 * AUTHOR: [Team Workout App]
 * COURSE: [CMSC 495 7383]
 * PROFESSOR: [Jeff Sanford]
 * CREATEDATE: [04/16/2022]

"""
from crypt import methods
from flask import Flask, render_template, url_for, flash, redirect

# from matplotlib.pyplot import title
from hwwforms import SignupForm, LoginForm

app = Flask(__name__)

# secret key will protect from modifying cookies & CSRF in our forms
app.config["SECRET_KEY"] = "52992f130b1b1510c545cd95f94a4d86"


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # create instance of the form to send to the app
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("signup-page.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # temporary test until db is ready
        if form.email.data == "admin@hww.com" and form.password.data == "password":
            return redirect(url_for("workoutbuilder"))
        else:
            flash("Please check username and password", "danger")
    return render_template("login-page.html", title="Login", form=form)


@app.route("/workoutbuilder")
def workoutbuilder():
    return render_template("workout-builder.html", title="HIIT Workout Builder")


# run file with python3 cmd
if __name__ == "__main__":
    app.run(debug=True)
