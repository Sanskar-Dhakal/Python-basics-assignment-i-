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
'''
Why is returning values better than printing inside functions?
Returning values from functions is generally better than printing inside functions for several reasons:
1. Reusability: When a function returns a value, that value can be reused in different contexts. 
You can store it in a variable, pass it to other functions, or use it in calculations. 
Printing, on the other hand, limits the function's utility to just displaying information.
2. Separation of Concerns: Functions that return values focus on computation and logic,
while printing is a side effect related to user interaction. By separating these concerns, your code becomes cleaner and easier to maintain.
3. Testing and Debugging: Functions that return values are easier to test and debug. 
You can call the function with different inputs and verify the returned output without dealing with printed output.
4. Flexibility: Returning values allows for greater flexibility in how the results are used. 
For example, you might want to log results to a file, send them over a network, or display them in a GUI, 
all of which are not possible if the function only prints to the console.
5. Composability: Functions that return values can be composed together to build more complex functionality. 
You can chain function calls and pass results from one function to another seamlessly.
Overall, returning values enhances the modularity, testability, and flexibility of your code, making it easier to work with in various scenarios.

'''