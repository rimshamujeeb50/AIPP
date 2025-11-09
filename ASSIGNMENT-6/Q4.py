# Sum to N Function using For Loop
# This function calculates the sum of the first n natural numbers using a for loop.

def sum_to_n_for(n):
    """
    Calculates the sum of the first n natural numbers using a for loop.

    Parameters:
    n (int): A positive integer representing the number up to which to sum.

    Returns:
    int: The sum of the first n natural numbers.
    """
    if n < 1:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Sum to N Function using While Loop
# This function calculates the sum of the first n natural numbers using a while loop.

def sum_to_n_while(n):
    """
    Calculates the sum of the first n natural numbers using a while loop.

    Parameters:
    n (int): A positive integer representing the number up to which to sum.

    Returns:
    int: The sum of the first n natural numbers.
    """
    if n < 1:
        return 0
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# Mathematical Formula Approach (for comparison)
# This is not a loop but uses the formula n*(n+1)/2 for efficiency.

def sum_to_n_formula(n):
    """
    Calculates the sum of the first n natural numbers using the mathematical formula.

    Parameters:
    n (int): A positive integer representing the number up to which to sum.

    Returns:
    int: The sum of the first n natural numbers.
    """
    if n < 1:
        return 0
    return n * (n + 1) // 2

# Example usage
if __name__ == "__main__":
    n = 10
    print(f"Sum of first {n} numbers using for loop: {sum_to_n_for(n)}")
    print(f"Sum of first {n} numbers using while loop: {sum_to_n_while(n)}")
    print(f"Sum of first {n} numbers using formula: {sum_to_n_formula(n)}")

# Explanation:
# - The for loop version iterates from 1 to n, accumulating the sum in a variable.
# - The while loop version uses a counter variable to achieve the same result.
# - Both loop-based functions have O(n) time complexity, while the formula has O(1) time complexity.
# - The formula is the most efficient for large n, but loops demonstrate iterative control structures.
# - Input validation ensures n is at least 1; otherwise, returns 0.

# Suggestions for other controlled looping:
# 1. Use recursion: def sum_to_n_recursive(n): return n + sum_to_n_recursive(n-1) if n > 0 else 0
# 2. Use list comprehension with sum: def sum_to_n_list(n): return sum([i for i in range(1, n+1)])
# 3. Use generator expression: def sum_to_n_gen(n): return sum(i for i in range(1, n+1))
# 4. Use reduce from functools: from functools import reduce; def sum_to_n_reduce(n): return reduce(lambda x, y: x + y, range(1, n+1), 0)
# These alternatives vary in readability, efficiency, and Pythonic style.
