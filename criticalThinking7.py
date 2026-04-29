def main():
    rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 a.m."
    }

    try:
        course = input("Enter a course number: ").strip().upper()

        if course in rooms:
            print("-" * 30)
            print(f"Details for {course}:")
            print(f"Room:       {rooms[course]}")
            print(f"Instructor: {instructors[course]}")
            print(f"Time:       {times[course]}")
            print("-" * 30)
        else:
            print(f"Error: {course} was not found.")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()