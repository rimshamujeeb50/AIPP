import math
import sys

"""
prime_number.py

Defines _prime(n) to check primality and reads a number from user input.
"""


def _prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False.
    n must be an integer.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    s = input("Enter an integer: ").strip()
    try:
        # accept integers and floats that are whole numbers (e.g. "7.0")
        if "." in s or "e" in s or "E" in s:
            f = float(s)
            if not f.is_integer():
                print("Input is not an integer.")
                sys.exit(1)
            n = int(f)
        else:
            n = int(s)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        sys.exit(1)

    if _prime(n):
        print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")