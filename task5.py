'''TASK 5: Iteration Using for Loops 
Concepts: Iteration, Accumulators, Loop Control 
Create a marks analyzer: 
● Input marks for n subjects 
● Output total, average, highest, lowest 

'''
n = int(input("Enter number of subjects: "))
i=0
total = 0
average = 0
highest = 0
lowest = 100
for i in range(n):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total += marks
    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks
average = total / n
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")