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

    # Built workout json hardcoded for now. Need to replace with calculated workout
    exampleJson = {
        "exerciseTime":30,
        "restTime":30,
        "numSets":4,
        "exercises":[
            {"exercise":"Standard Pushup",
                "description":"Get into a plank position with your arms straight, aligned with chest/nipples and shoulder width apart. Look down at the floor to keep your spine in perfect alignment. While squeezing your glutes and core muscles, lower your chest so that it almost touches the floor, keeping your elbows close to the body. Push yourself back up to the starting position and repeat.",
                "video":"https://www.youtube.com/embed/IODxDxX7oi4"
            },
            {"exercise":"Tricep Dips",
                "description":"Sitting down on a bench, chair or couch put your palms face down on the edge of the seat just outside your hips. Keeping your feet together, move them outwards from the seat keeping your legs straight until your butt just hangs off the edge. Lower your butt towards the ground until your arms hit a 90-degree angle and then lift yourself back up.",
                "video":"https://www.youtube.com/embed/0326dy_-CzM"
            },
            {"exercise":"Crunches",
                "description":"Start with your back on the ground, knees together bent towards the ceiling and feet together on the ground. Lift yourself a few inches up off the ground squeezing your core muscles and then back down.",
                "video":"https://www.youtube.com/embed/Xyd_fa5zoEU"
            }
        ]
    }
    json_string = json.dumps(exampleJson)
    return render_template("workout-overview.html", title="HIIT Workout Overview", json=json_string)


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
