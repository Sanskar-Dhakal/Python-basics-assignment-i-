''' Variable Modeling & Data Representation '''

Full_name ="Rishi Karki"
Age=20
CGPA=3.7
current_semester= 3
Enrollment_Status= True

print(f"The name of student is {Full_name}: datatype is ", type(Full_name))
print(f"The age of student is {Age}L datatype is ", type(Age))
print(f"The current_semester of student is {current_semester}: datatype is", type(current_semester))
print(f"The student is enrolled {Enrollment_Status}: datatype is", type(Enrollment_Status))


''' Python uses dynamic typing, which means a variable does not have a fixed data type. 
    Instead, the type is determined at runtime based on the value assigned to it. 

    At runtime, Python checks data types while the program is running. 
    This makes coding easier and more flexible,
    It also means type errors are found during execution instead of before running the program. 
    Although this causes a small performance problem, it allows faster development and simpler code.
''' 

