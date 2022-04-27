"""
File contains scripts that define auth related routes.
/login
/logout
/register
"""
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from hwwforms import SignupForm, LoginForm
from flask_login import login_user, current_user, logout_user

# Blueprint for auth pages.
app = Blueprint("auth", __name__)


# def login_required(func):
#     """
#     Decorator function that checks if the user is authenticated.
#     It is meant to be used with routes that require authentication.
#     :param func: Function to decorate
#     :return: Either original function or decorated function
#     """

#     @wraps(func)
#     def wrapper_func(*args, **kwargs):
#         # Check session for user log in info. If not logged in
#         if "logged_in" not in session or not session["logged_in"]:
#             # Use flash to carry over an error message to page
#             flash("Login required to access this page!")
#             # Return a redirect to login page. Set next as current page
#             # so that we can go back to it after log in
#             return func(*args, **kwargs)
#             # return redirect(url_for('auth.login', next=request.url))

#         # If user logged in, return original function
#         return func(*args, **kwargs)

#     return wrapper_func


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Function that calls the login template. Accepts GET for when we are trying to
    view the page and POST for when we are trying to submit a form
    """
    form = LoginForm()
    if form.validate_on_submit():
        # temporary test until db is ready
        if form.email.data == "admin@hww.com" and form.password.data == "password":
            return redirect(url_for("workout.workout_builder"))
        else:
            flash("Please check username and password", "danger")
    return render_template("login-page.html", title="Login", form=form)


@app.route("/logout")
def logout():
    """
    Function that calls completes the logout procedure.
    Redirects to main page upon log out
    """
#     logout_user()
    return redirect(url_for("main.home"))


@app.route("/register", methods=["POST", "GET"])
def register():
    """
    Function that calls the register template. Accepts GET for when we are trying to
    view the page and POST for when we are trying to submit a form
    """
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("auth.login"))
    return render_template("signup-page.html", title="Register", form=form)

