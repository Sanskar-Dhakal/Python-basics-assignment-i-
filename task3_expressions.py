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
Floating-point precision errors mean computers can’t store some decimal numbers exactly. 
Because of this, small rounding mistakes happen. In real life, this can cause wrong money calculations, slightly incorrect scientific results, or pricing errors in billing systems. 
Over time, these tiny errors can add up and cause big problems.
'''