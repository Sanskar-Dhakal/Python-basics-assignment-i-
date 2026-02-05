assignment = float(input("Enter assignment score: "))
lab = float(input("Enter lab score: "))
exam = float(input("Enter exam score: "))

# Weighted 
final_score = (assignment * 0.3) + (lab * 0.2) + (exam * 0.5)
print("Final Score:", round(final_score, 2))

'''
1
Because computers follow strict math rules, and a small mistake can change the result.
Operator precedence ensures calculations happen in the correct order.
Example
result = 100 + 20 * 5

==Python calculates:==
20 * 5 = 100
100 + 100 = 200

==But if someone meant:==
result = (100 + 20) * 5
That becomes:
120 * 5 = 600
'''

'''
Unvalidated user input in Python can let attackers manipulate data or logic.
In a voting system, invalid inputs could allow multiple votes, 
fake candidate IDs, or corrupted results. 
Proper input validation prevents fraud, crashes, and data tampering by ensuring inputs are correct, safe, and within expected limits.
'''