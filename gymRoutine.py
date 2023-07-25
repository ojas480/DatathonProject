import pandas as pd
from random import randint

def get_workout_plan(plan_type, days_per_week, body_part, level, plan_option):

    if level == "beginner":
        max_workouts_per_day = 4
    elif level == "intermediate":
        max_workouts_per_day = 5
    elif level == "expert":
        max_workouts_per_day = 6
    else:
        return "Invalid fitness level, please try again."

    if plan_type == "week":
        return plan_type_week(plan_type, days_per_week, level, plan_option, max_workouts_per_day)

    elif plan_type == "day":
        return plan_type_day(plan_type, body_part, max_workouts_per_day)

def plan_type_day(plan_type, body_part, max_workouts_per_day):
    df = pd.read_csv("megaGymDataset.csv")
    if body_part in df["BodyPart"].unique():
        body_part_df = df[df["BodyPart"] == body_part]
        exercise_count = body_part_df["Title"].count()
        workouts_done = 0
        result = ""
        while workouts_done < max_workouts_per_day and workouts_done < exercise_count:
            if exercise_count > 0:
                exercise = body_part_df.sample(n=1)["Title"].values[0]
                r1 = randint(3,4)
                r2 = randint(8, 15)
                result += f"Exercise {workouts_done + 1}: {exercise} " + str(r1) + "x" + str(r2) + "\n"
                body_part_df = body_part_df[body_part_df["Title"] != exercise]
                workouts_done += 1
            else:
                result = "No more exercises available for this body part."
                break
    else:
        result = "Invalid body part, please try again."
    return result

def plan_type_week(plan_type, days_per_week, level, plan_option, max_workouts_per_day):
    df = pd.read_csv("megaGymDataset.csv")
    workout_plan = []

    if level == "beginner":
        max_workouts_per_day = 4
    elif level == "intermediate":
        max_workouts_per_day = 5
    elif level == "expert":
        max_workouts_per_day = 6
    else:
        return "Invalid fitness level, please try again."
    
    if plan_option == "PPL":
        day1 = ["Shoulders", "Triceps", "Chest"]
        day2 = ["Lats", "Lower Back", "Middle Back", "Traps", "Biceps", "Forearms"]
        day3 = ["Abdominals", "Abductors", "Adductors", "Calves", "Glutes", "Hamstrings", "Quadriceps"]
        for i in range(days_per_week):
            if i % 3 == 0:
                workout_plan.append(day1)
            elif i % 3 == 1:
                workout_plan.append(day2)
            else:
                workout_plan.append(day3)
    else:
        day1 = ["Chest", "Lats", "Lower Back", "Middle Back", "Traps"]
        day2 = ["Shoulders", "Triceps", "Biceps", "Forearms"]
        day3 = ["Abdominals", "Abductors", "Adductors", "Calves", "Glutes", "Hamstrings", "Quadriceps"]
        for i in range(days_per_week):
            if i % 3 == 0:
                workout_plan.append(day1)
            elif i % 3 == 1:
                workout_plan.append(day2)
            else:
                workout_plan.append(day3)
    result = ""
    max_workouts_per_day_beginner = 4
    max_workouts_per_day_intermediate = 5
    max_workouts_per_day_advanced = 6
    # max_workouts_per_day = max_workouts_per_day_beginner if level == "beginner" else max_workouts_per_day_intermediate if level == "intermediate" else max_workouts_per_day_advanced
    for i, day in enumerate(workout_plan):
        result += f"Day {i + 1}:\n"
        while max_workouts_per_day > 0:
            already_targeted_muscles = []
            for body_part in day:
                if body_part in already_targeted_muscles:
                    continue
                body_part_df = df[df["BodyPart"] == body_part]
                exercises_per_workout = 1 if body_part_df["Title"].count() > 1 else 2
                workouts_done = 0
                while workouts_done < exercises_per_workout and workouts_done < body_part_df["Title"].count() and max_workouts_per_day > 0:
                    if body_part_df["Title"].count() > 0:
                        exercise = body_part_df.sample(n=1)["Title"].values[0]
                        r1 = randint(3,4)
                        r2 = randint(8, 15)
                        result += f"- for {body_part}: {exercise} " + str(r1) + "x" + str(r2) + "\n"
                        already_targeted_muscles.append(body_part)
                        workouts_done += 1
                        max_workouts_per_day -= 1
                    else:
                        break
            if max_workouts_per_day <= 0:
                break
        max_workouts_per_day = max_workouts_per_day_beginner if level == "beginner" else max_workouts_per_day_intermediate if level == "intermediate" else max_workouts_per_day_advanced
    return result
