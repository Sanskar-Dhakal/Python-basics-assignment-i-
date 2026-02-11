def average(marks):
    total = sum(marks)
    avg = total / len(marks)
    return avg


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


def formatting():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    num_subjects = int(input("Enter number of subjects: "))

    if num_subjects <= 0:
        print("Number of subjects must be greater than 0.")
        return

    marks = []

    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    avg = average(marks)
    grade = determine_grade(avg)

    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Grade: {grade}")
formatting()
