import pandas as pd

from modules.menu import show_menu
from modules.input_handler import get_roll_number, pause_screen
from modules.data_validation import validate_dataset
from modules.performance import prepare_results
from modules import reports


def load_students():
    """Load and validate the CSV dataset."""
    try:
        data = pd.read_csv("Students_records.csv", dtype={"Roll_no": str})
        data["Roll_no"] = data["Roll_no"].str.strip()

        return validate_dataset(data)

    except FileNotFoundError:
        print("Error: Students_records.csv was not found in the project folder.")
    except (ValueError, KeyError) as error:
        print("Dataset error:", error)
    except pd.errors.ParserError:
        print("Error: the CSV file could not be read.")

    return None


def run_application():
    students = load_students()

    if students is None:
        return

    analyzed_students = prepare_results(students)

    print("\nStudent data loaded successfully.")
    print("Records available:", len(analyzed_students))

    while True:
        choice = show_menu()

        if choice == "1":
            reports.show_directory(students)

        elif choice == "2":
            reports.show_results(analyzed_students)

        elif choice == "3":
            roll_number = get_roll_number(
                "Enter student roll number: "
            )
            reports.show_student_report(
                analyzed_students, roll_number
            )

        elif choice == "4":
            reports.show_class_statistics(analyzed_students)

        elif choice == "5":
            reports.show_subject_comparison(students)

        elif choice == "6":
            reports.show_merit_list(analyzed_students)

        elif choice == "7":
            reports.show_attendance_watchlist(
                analyzed_students
            )

        elif choice == "0":
            print(
                "\nThank you for using Student Assessment Analyzer."
            )
            break

        else:
            print("Invalid option. Choose a number from 0 to 7.")
            continue

        pause_screen()


if __name__ == "__main__":
    run_application()