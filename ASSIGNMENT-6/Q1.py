class Student:
    def __init__(self, student_id, name, age, grade):
        """Initialize student attributes"""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_details(self):
        """Display student information"""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

if __name__ == "__main__":
    # Get input from user
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    # Create a student object with user input
    student1 = Student(student_id, name, age, grade)
    
    # Display student details
    print("\nStudent Details:")
    student1.display_details()