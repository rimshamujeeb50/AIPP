def greet_user(name, gender):
    if gender.lower() == "male":
        title = "Mr."
    elif gender.lower() == "female":
        title = "Mrs."
    else:
        title = "Mx."
    return f"Hello, {title} {name}! Welcome."

# Taking input from the user
user_name = input("Please enter your name: ")
user_gender = input("Please enter your gender (male/female/gender neutral): ")

# Greeting the user
greeting = greet_user(user_name, user_gender)
print(greeting)