def sum_of_squares():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a**2 + b**2
        print("Sum of squares:", result)
        return result
    except ValueError:
        print("Please enter valid numbers.")

sum_of_squares()
