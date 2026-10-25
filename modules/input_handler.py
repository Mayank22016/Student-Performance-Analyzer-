def get_roll_number(message):
    """Accept a roll number as text."""
    return input(message).strip()


def pause_screen():
    """Wait before returning to the menu."""
    input("\nPress Enter to return to main menu...")