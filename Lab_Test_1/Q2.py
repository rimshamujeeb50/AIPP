#Refactor the following poorly commented Python function by improving variable names, adding complete docstrings, adding helpful inline comments, 
# and fixing any missing error handling.

def factorial(number):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Args:
        number (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of the provided integer.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number < 0:
        raise ValueError("Input must be a non-negative integer.")
    if number == 0:
        return 1
    return number * factorial(number - 1)

if __name__ == "__main__":
    try:
        user_input = input("Enter a non-negative integer to calculate its factorial: ")
        user_number = int(user_input)
        result = factorial(user_number)
        print(f"The factorial of {user_number} is {result}.")
    except ValueError:
        print("Error: Input must be a non-negative integer.")
    except TypeError as e:
        print(f"Error: {e}")

