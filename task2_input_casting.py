#  with type casting 
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))

result = income - expenses
print(result)

''' 
1) answer
Because Python decides data types while the program is running.
x = input("Enter a number: ")
print(x + 5)
Here: input() gives text (string)
Python only discovers this when it reaches that line So the error appears during execution, not before.
'''

'''
Since, the computer trusts the user’s input.
Example: 
Billing system
amount = float(input("Enter amount: "))
total = amount - 100

If user enters:
abc → program crashes
-500 → wrong bill
10000000 → wrong records
'''