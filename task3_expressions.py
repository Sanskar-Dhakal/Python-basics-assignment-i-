assignment = float(input("Enter assignment score: "))
lab = float(input("Enter lab score: "))
exam = float(input("Enter exam score: "))

# Weighted 
final_score = (assignment * 0.3) + (lab * 0.2) + (exam * 0.5)
print("Final Score:", round(final_score, 2))
