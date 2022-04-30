"""
File contains scripts that define auth related routes.
/login
/logout
/register
"""
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from hiitwa.hwwforms import SignupForm, LoginForm
from flask_login import login_required, login_user, current_user, logout_user
from hiitwa.models import db, User


# Blueprint for auth pages.
app = Blueprint("auth", __name__)
# from hiitwa import db
bcrypt1 = Bcrypt()


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Function that calls the login template. Accepts GET for when we are trying to
    view the page and POST for when we are trying to submit a form
    """
    if current_user.is_authenticated:
        return redirect(url_for("workout.workout_builder"))

    form = LoginForm()
    if form.validate_on_submit():
        # temporary test until db is ready
        # if form.email.data == "admin@hww.com" and form.password.data == "password":
        #     return redirect(url_for("workout.workout_builder"))

        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt1.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return (
                redirect(next_page)
                if next_page
                else redirect(url_for("workout.workout_builder"))
            )
        else:
            flash("Please check username and password", "danger")
    return render_template("login-page.html", title="Login", form=form)


@app.route("/logout")
@login_required
def logout():
    """
    Function that calls completes the logout procedure.
    Redirects to main page upon log out
    """
    logout_user()

    return redirect(url_for("main.home"))


@app.route("/register", methods=["POST", "GET"])
def register():
    """
    Function that calls the register template. Accepts GET for when we are trying to
    view the page and POST for when we are trying to submit a form
    """
    if current_user.is_authenticated:
        return redirect(url_for("workout.workout_builder"))

    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt1.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("auth.login"))
    return render_template("signup-page.html", title="Register", form=form)
