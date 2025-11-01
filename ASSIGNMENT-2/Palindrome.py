"""
1)Write function to check if string is Palindrome.
2)  Read the string input from user.
"""
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get user input
user_input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")