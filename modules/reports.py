from modules.data_validation import SUBJECTS


def show_directory(data):
    print("\nSTUDENT DIRECTORY")
    print("-" * 70)

    print(
        data[["Roll_no", "Student_Name", "Attendance"]]
        .to_string(index=False)
    )


def show_results(data):
    columns = [
        "Roll_no",
        "Student_Name",
        "total",
        "average",
        "percentage",
        "grade",
        "result"
    ]

    print("\nACADEMIC RESULTS")
    print("-" * 70)

    print(data[columns].round(2).to_string(index=False))


def show_student_report(data, roll_number):
    matches = data[data["Roll_no"] == roll_number]

    if matches.empty:
        print("No student found with that roll number.")
        return

    student = matches.iloc[0]

    print("\nINDIVIDUAL STUDENT REPORT")
    print("-" * 45)

    print("Name:", student["Student_Name"])
    print("Roll Number:", student["Roll_no"])
    print("Attendance:", f'{student["Attendance"]:.1f}%')

    print("\nSubject Marks:")

    for subject in SUBJECTS:
        print(
            f"{subject.title():15} "
            f"{student[subject]:.1f}/100"
        )

    print(
        "\nTotal Marks:",
        student["total"],
        "/",
        len(SUBJECTS) * 100
    )

    print("Average:", round(student["average"], 2))
    print("Percentage:", round(student["percentage"], 2), "%")
    print("Grade:", student["grade"])
    print("Result:", student["result"])


def show_class_statistics(data):
    print("\nCLASS PERFORMANCE")
    print("-" * 45)

    print("Total Students:", len(data))
    print(
        "Class Average:",
        round(data["percentage"].mean(), 2),
        "%"
    )
    print(
        "Highest Percentage:",
        round(data["percentage"].max(), 2),
        "%"
    )
    print(
        "Lowest Percentage:",
        round(data["percentage"].min(), 2),
        "%"
    )

    passed = int((data["result"] == "Pass").sum())
    failed = int((data["result"] == "Fail").sum())

    print("Students Passed:", passed)
    print("Students Failed:", failed)

    if len(data) > 0:
        pass_percentage = passed / len(data) * 100

        print(
            "Pass Percentage:",
            round(pass_percentage, 2),
            "%"
        )


def show_subject_comparison(data):
    summary = data[SUBJECTS].agg(
        ["mean", "max", "min"]
    ).T

    summary.columns = ["Average", "Highest", "Lowest"]

    summary["Pass Count"] = (
        data[SUBJECTS] >= 40
    ).sum()

    summary["Fail Count"] = (
        data[SUBJECTS] < 40
    ).sum()

    print("\nSUBJECT COMPARISON")
    print("-" * 65)
    print(summary.round(2).to_string())

    best_subject = summary["Average"].idxmax()
    weakest_subject = summary["Average"].idxmin()

    print("\nStrongest Subject:", best_subject.title())
    print("Weakest Subject:", weakest_subject.title())


def show_merit_list(data):
    ranking = data.sort_values(
        by=["percentage", "Student_Name"],
        ascending=[False, True]
    ).copy()

    ranking = ranking[
        ["Roll_no", "Student_Name", "percentage", "grade", "result"]
    ]

    ranking.insert(
        0,
        "rank",
        ranking["percentage"].rank(
            method="min",
            ascending=False
        ).astype(int)
    )

    print("\nSTUDENT MERIT LIST")
    print("-" * 65)
    print(ranking.round(2).to_string(index=False))


def show_attendance_watchlist(data):
    watchlist = data[
        data["Attendance"] < 75
    ].sort_values(by="Attendance")

    print("\nATTENDANCE WATCHLIST")
    print("-" * 60)

    if watchlist.empty:
        print("All students meet the attendance threshold.")
        return

    print(
        watchlist[
            [
                "Roll_no",
                "Student_Name",
                "Attendance",
                "attendance_status"
            ]
        ].to_string(index=False)
    )