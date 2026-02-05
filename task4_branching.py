attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter total marks: "))
yearly_income=float(input("enter the yearly income: "))
roundoff=round(yearly_income,2)

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
    print("Grade:", grade)
    if grade > "A" and attendance>90 and yearly_income<400000:
        print("Eligible for Scholarship")
    else:
        print("Not Eligible for Scholarship")