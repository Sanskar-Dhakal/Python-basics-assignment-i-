attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter total marks: "))

if attendance < 75:
    print("Not eligible due to low attendance")
else:
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "Fail"
    print("Eligible")
    print("Grade:", grade)