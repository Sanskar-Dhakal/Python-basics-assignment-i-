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

'''Validation is better handled with while loops than for loops because validation requires repeating a process until a correct condition is met, 
and the number of attempts is not known in advance. A while loop runs based on a condition, 
making it suitable for checking input repeatedly until it becomes valid. 
In contrast, a for loop is mainly used when the number of repetitions is fixed, 
which is not suitable for validation.'''