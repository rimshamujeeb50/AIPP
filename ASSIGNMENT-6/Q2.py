# Q2.py
# Task: print the first 10 multiples of a number using loops
# Contains two controlled-loop implementations and a short analysis.

def print_multiples_for(n):
    """Print first 10 multiples of n using a for loop."""
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def print_multiples_while(n):
    """Print first 10 multiples of n using a while loop (alternative)."""
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1

# Analysis (brief):
# - Both functions produce the same output: multiples 1..10 of the given n.
# - for loop version is concise and idiomatic for a known fixed range.
# - while loop version demonstrates manual counter control.
# - Time complexity: O(k) where k=10 (constant), effectively O(1) for this fixed task.

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer to print its first 10 multiples: ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        print("\nUsing for loop:")
        print_multiples_for(num)
        print("\nUsing while loop:")
        print_multiples_while(num)

# If you want another controlled-loop variant (e.g., recursion, generator, itertools),
# ask to generate that alternative implementation.