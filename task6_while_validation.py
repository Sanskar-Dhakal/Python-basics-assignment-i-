'''TASK 6: Input Validation with while Loops 
Concepts: while, Validation, Loop Termination 
Accept subject marks only between 0 and 100. 
Re-prompt until valid input is entered. 
'''
marks = float(input("Enter marks (0-100): "))
while marks < 0 or marks > 100:
    print("Invalid input. Please enter marks between 0 and 100.")
    marks = float(input("Enter marks (0-100): "))
print(f"Valid marks entered: {marks}")
