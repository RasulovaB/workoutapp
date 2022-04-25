import json
from typing import List

from flask import Blueprint, render_template, request, jsonify, flash

from controller.auth_blueprint import login_required
from model.exercise import Exercise

app = Blueprint('workout', __name__)

selected_exercises: List[Exercise] = []


@app.route("/workout_builder")
@login_required
def workout_builder():
    return render_template("workout-builder.html", title="HIIT Workout Builder")


@app.route("/workout_overview")
@login_required
def workout_overview():
    return render_template("workout-overview.html", title="HIIT Workout Overview")


@app.route("/workout_completed")
@login_required
def workout_completed():
    return render_template("workout-completed.html", title="HIIT Workout Completed")


@app.route('/get_exercises', methods=['GET'])
@login_required
def get_exercises():
    response = jsonify(selected_exercises)
    return response


@app.route('/add_exercise', methods=['POST'])
@login_required
def add_exercise():
    # Create id for the exercise added
    id = len(selected_exercises)

    # Get data from request and find exercise name
    data = json.loads(request.data)
    exercise_name = data['name']

    # Logic to fetch exercise
    exercise_name += '_' + str(id)

    # Create exercise object
    exercise = Exercise(id=id, name=exercise_name)
    selected_exercises.append(exercise)

    # Jsonify a response that will be sent to JS
    response = jsonify(exercise)
    return response


@app.route('/delete_exercises', methods=['DELETE'])
@login_required
def delete_exercises():
    exercise_to_remove = Exercise(**json.loads(request.data))

    selected_exercises.remove(exercise_to_remove)

    response = jsonify(success=True)
    return response


@app.route('/mark_exercise_completed', methods=['POST'])
@login_required
def mark_exercise_completed():
    exercise = Exercise(**json.loads(request.data))

    response = jsonify(success=True)
    return response


@app.route('/get_workout', methods=['GET'])
@login_required
def get_workout():
    data = json.loads(request.data)

    response = jsonify(success=True)
    return response


@app.route('/submit_workout', methods=['POST'])
@login_required
def submit_exercises():
    data = json.loads(request.data)

    if len(data) == 0:
        return "Unspecified skill level", 400
    else:
        difficulty = data['difficulty']
        response = jsonify(success=True)

    return response


@app.route('/mark_workout_completed', methods=['POST'])
@login_required
def mark_workout_completed():
    response = jsonify(success=True)
    return response


@app.route('/submit_rating', methods=['GET'])
@login_required
def submit_rating():
    response = jsonify(success=True)
    return response
