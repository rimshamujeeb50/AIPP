from flask import Flask, render_template_string, request

app = Flask(__name__)

login_form_html = """
<!DOCTYPE html>
<html>
<body>

<h2>Login Form</h2>

<form method="POST">
    <label>Username:</label>
    <input type="text" name="username"><br><br>

    <label>Password:</label>
    <input type="password" name="password"><br><br>

    <button type="submit">Login</button>
</form>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        if username:
            return f"Login successful! Welcome, {username}"
        else:
            return "Error: Username cannot be empty."
    
    return render_template_string(login_form_html)

if __name__ == "__main__":
    app.run(debug=True)
