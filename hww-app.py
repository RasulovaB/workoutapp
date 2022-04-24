"""
 * FILENAME: [hww-app]
 * AUTHOR: [Team Workout App]
 * COURSE: [CMSC 495 7383]
 * PROFESSOR: [Jeff Sanford]
 * CREATEDATE: [04/16/2022]

"""
from flask import Flask, render_template
from matplotlib.pyplot import title
import json

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
    

@app.route("/workoutbuilder")
def workoutbuilder():
    return render_template("workout-builder.html", title="HIIT Workout Builder")

@app.route("/workout")
def workoutsummary():
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
    return render_template("workout-summary.html", title="Your HIIT Workout", json=json_string)


# run file with python3 cmd
if __name__ == "__main__":
    app.run(debug=True)
