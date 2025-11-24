#Write a Python class named Stack that implements a stack data structure with the methods push(), pop(), and peek().
# The Stack function must also implement error handling for empty stack operations.
#Read the  input from user
class Stack:
    """
    A simple implementation of a Stack data structure using a Python list.
    Supports push, pop, and peek operations.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """
        Push an item onto the top of the stack.

        Args:
            item: The value to be pushed.
        """
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """
        Remove and return the top element of the stack.
        Prints a message if the stack is empty.

        Returns:
            The removed element, or None if stack is empty.
        """
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        removed = self.items.pop()
        print(f"Popped: {removed}")
        return removed

    def peek(self):
        """
        Return the top element of the stack without removing it.
        Prints a message if the stack is empty.

        Returns:
            The top element, or None if stack is empty.
        """
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        print(f"Top element: {self.items[-1]}")
        return self.items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if stack has no elements, False otherwise.
        """
        return len(self.items) == 0


if __name__ == "__main__":
    stack = Stack()

    # Simple menu-driven program for user interaction
    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Handle user's choice
        if choice == "1":
            value = input("Enter value to push: ")
            stack.push(value)

        elif choice == "2":
            stack.pop()

        elif choice == "3":
            stack.peek()

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")
