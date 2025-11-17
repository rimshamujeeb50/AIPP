def discount(price, category):
    # Dictionary-based rules: category → (threshold, high_rate, low_rate)
    discount_rules = {
        "student": (1000, 0.90, 0.95),
        "other":   (2000, 0.85, 1.00)
    }

    # Select rules based on category; default to "other"
    threshold, high_rate, low_rate = discount_rules.get(category, discount_rules["other"])

    # Apply correct rate based on price threshold
    return price * (high_rate if price > threshold else low_rate)


# ----------- User Input -----------
try:
    price = float(input("Enter the price: "))
    category = input("Enter category (student/other): ").strip().lower()

    if category not in ["student", "other"]:
        print("Invalid category! Please enter 'student' or 'other'.")
    else:
        final_price = discount(price, category)
        print(f"Discounted Price: {final_price}")

except ValueError:
    print("Invalid input! Please enter a numeric price.")
