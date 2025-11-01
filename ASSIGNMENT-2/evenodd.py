# /C:/Users/HP/Desktop/evenodd.py

def parity(n: int) -> str:
    """Return 'even' or 'odd' using a single-line conditional expression."""
    return "even" if n % 2 == 0 else "odd"

if __name__ == "__main__":
    try:
        n = int(input("Enter an integer: ").strip())
    except ValueError:
        print("Please enter a valid integer.")
    else:
        print(parity(n))