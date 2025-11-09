def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Parameters:
    n (int): The position in the Fibonacci sequence to retrieve.

    Returns:
    int: The nth Fibonacci number.
    """
    # Base case: the first two Fibonacci numbers are 0 and 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
    

# Take input from the user
n = int(input("Enter the position of the Fibonacci number you want to calculate: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")