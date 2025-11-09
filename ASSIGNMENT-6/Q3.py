# Age Classification Function using Nested If-Elif-Else
# This function classifies a person's age into different groups based on standard age ranges.
# It uses nested conditional statements to handle the classification logic.
"""
def classify_age(age):
   
    #Classifies the given age into age groups using nested if-elif-else statements.
    #Parameters:
    #age (int): The age of the person (must be a non-negative integer).
    #Returns:
    #str: The age group classification.
    
    if age < 0:
        return "Invalid age"
    elif age <= 1:
        return "Infant"
    elif age <= 12:
        if age <= 5:
            return "Toddler"
        else:
            return "Child"
    elif age <= 19:
        if age <= 15:
            return "Early Teen"
        else:
            return "Late Teen"
    elif age <= 64:
        if age <= 35:
            return "Young Adult"
        else:
            return "Middle-aged Adult"
    else:
        if age <= 80:
            return "Senior"
        else:
            return "Elderly"

# Example usage: Ask user for their age and display the age group
if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        group = classify_age(age)
        print(f"Your age group is: {group}")
    except ValueError:
        print("Invalid input. Please enter a valid integer age.")"""

# Explanation:
# - The function uses nested if-elif-else to create a hierarchical classification.
# - Outer conditions check broad ranges (e.g., <=1 for Infant, <=12 for Child/Teen, etc.).
# - Inner conditions provide more specific sub-classifications within those ranges.
# - This structure allows for detailed categorization while maintaining readability.
# - Alternatives could use dictionaries, match-case (Python 3.10+), or chained comparisons,
#   but nested if-elif-else is chosen here for clarity in demonstrating conditional nesting.

# Alternative using chained comparisons and elif (non-nested):
def classify_age_alternative(age):
     if age < 0:
         return "Invalid age"
     elif 0 <= age <= 1:
         return "Infant"
     elif 2 <= age <= 5:
         return "Toddler"
     elif 6 <= age <= 12:
         return "Child"
     elif 13 <= age <= 15:
         return "Early Teen"
     elif 16 <= age <= 19:
         return "Late Teen"
     elif 20 <= age <= 35:
         return "Young Adult"
     elif 36 <= age <= 64:
         return "Middle-aged Adult"
     elif 65 <= age <= 80:
         return "Senior"
     else:
         return "Elderly"
if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        group = classify_age_alternative(age)
        print(f"Your age group is: {group}")
    except ValueError:
        print("Invalid input. Please enter a valid integer age.")
