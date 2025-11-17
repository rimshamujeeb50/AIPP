class Employee:
    """
    A class representing an employee with a name and salary.
    Provides methods to increase salary and display employee details.
    """
    def __init__(self, name, salary):
        """
        Initialize an Employee object
        :param name: Employee's name
        :param salary: Employee's salary (float or int)
        """
        self.name = name
        self.salary = salary
    def increase_salary(self, percentage):
        """
        Increase the employee's salary by a given percentage.
        :param percentage: Percentage by which salary is increased
        """
        self.salary += (self.salary * percentage / 100)
    def display_info(self):
        """Print formatted employee information."""
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary:.2f}")
# ----------- Input from User -----------
name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
increase_percent = float(input("Enter salary increase percentage: "))
# Create Employee object
emp = Employee(name, salary)
# Apply salary increase
emp.increase_salary(increase_percent)
# Display updated information
print("\nUpdated Employee Details:")
emp.display_info()
