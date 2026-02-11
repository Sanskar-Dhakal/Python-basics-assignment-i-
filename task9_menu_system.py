# Global variables to store data
student_name = ""
roll_number = ""
marks = []


def enter_student_details():
    global student_name, roll_number

    student_name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")

    print("Student details saved successfully!\n")


def enter_marks():
    global marks

    marks.clear()   # Clear old marks

    num_subjects = int(input("Enter number of subjects: "))

    if num_subjects <= 0:
        print("Number of subjects must be greater than 0.\n")
        return

    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    print("Marks saved successfully!\n")


def calculate_average():
    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)


def determine_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def view_result():
    if student_name == "" or roll_number == "":
        print("Please enter student details first.\n")
        return

    if len(marks) == 0:
        print("Please enter marks first.\n")
        return

    avg = calculate_average()
    grade = determine_grade(avg)

    print("\n------ Result Summary ------")
    print("Name:", student_name)
    print("Roll No:", roll_number)
    print("Marks:", marks)
    print(f"Average: {avg:.2f}")
    print("Grade:", grade)
    print("----------------------------\n")


def main_menu():
    while True:

        print("===== Student Utility System =====")
        print("1. Enter Student Details")
        print("2. Enter Marks")
        print("3. View Result Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            enter_student_details()

        elif choice == "2":
            enter_marks()

        elif choice == "3":
            view_result()

        elif choice == "4":
            print("Thank you! Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.\n")


# Start program
main_menu()

