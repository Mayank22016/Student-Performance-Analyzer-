import numpy as np
import pandas as pd

SUBJECTS = [
    "Operating_System",
    "Software_Engineering",
    "Design_and_Analysis_of_Algorithm",
    "Artificial_Intelligence",
    "Computer_Networks"
]

REQUIRED_COLUMNS = [
    "Roll_no",
    "Student_Name",
    "Attendance",
    *SUBJECTS
]


def validate_dataset(data):
    """Check the structure and values of the student dataset."""

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    if data.empty:
        raise ValueError("The dataset contains no student records.")

    data = data.copy()

    data["Roll_no"] = data["Roll_no"].astype(str).str.strip()
    data["Student_Name"] = data["Student_Name"].astype(str).str.strip()

    if data["Roll_no"].eq("").any():
        raise ValueError("Student roll numbers cannot be empty.")

    if data["Roll_no"].duplicated().any():
        raise ValueError("Duplicate roll numbers were found.")

    if data["Student_Name"].eq("").any():
        raise ValueError("Student names cannot be empty.")

    numeric_columns = ["Attendance", *SUBJECTS]

    for column in numeric_columns:
        data[column] = pd.to_numeric(
            data[column],
            errors="coerce"
        )

    values = data[numeric_columns].to_numpy(dtype=float)

    if not np.isfinite(values).all():
        raise ValueError(
            "Attendance and marks must contain valid numbers."
        )

    if not data["Attendance"].between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100.")

    if not data[SUBJECTS].apply(
        lambda column: column.between(0, 100)
    ).all().all():
        raise ValueError("Subject marks must be between 0 and 100.")

    return data