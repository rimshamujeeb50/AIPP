"""
•	Ask AI to generate test cases for assign_grade(score) function. Handle boundary and invalid inputs.
Requirements
•	AI should generate test cases for assign_grade(score) where: 90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
•	Include boundary values and invalid inputs (e.g., -5, 105, "eighty").

Expected Output#2
Generate a python code for the grade assignment function passing test suite and take input from the user for the score and print the grade.
 
PROMPT:

# Python: Generate test cases and implementation for assign_grade(score).
# Grades: A (90-100), B (80-89), C (70-79), D (60-69), F (<60).
# Include boundary cases (60, 89, 100) and invalid inputs (-5, 105, "text").
# Then, implement the function and add code to take user input for the score and print the result.

"""
def assign_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"                      

score = int(input("Enter the score: "))
print(assign_grade(score))

