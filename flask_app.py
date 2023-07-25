from flask import Flask, request, render_template
from gymroutine import get_workout_plan

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/gym_routine", methods=["POST", "GET"])
def generate_workout_plan():
    plan_type = request.form.get("plan_type")
    level = request.form.get("level")
    body_part = request.form.get("body_part")
    days_per_week = request.form.get("days_per_week")
    plan_option = request.form.get("plan_option")


    try:
        s = get_workout_plan(plan_type, days_per_week, body_part, level, plan_option)
        s = s.replace("- for", "")
        s = s.replace("-", "")
        s = s.replace("1:", "1")
        s = s.replace("2:", "2")
        s = s.replace("3:", "3")
        s = s.replace("4:", "4")
        s = s.replace("5:", "5")
        s = s.replace("6:", "6")
    except:
        return render_template("error.html")

    return render_template("workout.html", workout_plan=s)