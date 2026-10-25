import numpy as np

from modules.data_validation import SUBJECTS

#Defining the passing criteria
PASSING_MARKS = 40


def assign_grade(percentage):
    """Assign a letter grade based on percentage."""

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def prepare_results(data):
    """Calculate totals, averages, grades, and results."""

    results = data.copy()

    results["total"] = results[SUBJECTS].sum(axis=1)

    results["average"] = results[SUBJECTS].mean(axis=1)

    results["percentage"] = (
        results["total"] / (len(SUBJECTS) * 100)
    ) * 100

    results["grade"] = results["percentage"].apply(
        assign_grade
    )

    results["result"] = np.where(
        (results[SUBJECTS] < PASSING_MARKS).any(axis=1),
        "Fail",
        "Pass"
    )

    results["attendance_status"] = np.where(
        results["Attendance"] < 75,
        "Low Attendance",
        "Satisfactory"
    )

    return results