class BankAccount:
    """
    A simple BankAccount class that allows depositing money, withdrawing money,
    and checking the current balance.
    """
    def __init__(self):
        """
        Initializes a new BankAccount instance with a balance of 0.
        """
        self._balance = 0.0  # Private attribute to store the account balance
    def deposit(self, amount):
        """
        Deposits a specified amount into the account.
        Args:
            amount (float): The amount to deposit. Must be positive.
        Raises:
            ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount  # Add the amount to the balance
    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.
        Args:
            amount (float): The amount to withdraw. Must be positive.
        Raises:
            ValueError: If the amount is not positive or if there are insufficient funds.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount  # Subtract the amount from the balance

    def balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current account balance.
        """
        return self._balance  # Return the private balance attribute


# Test the BankAccount class with user input
if __name__ == "__main__":
    account = BankAccount()
    print("Welcome to BankAccount Tester!")
    print(f"Initial balance: {account.balance()}")

    while True:
        action = input("Enter 'deposit', 'withdraw', 'balance', or 'quit': ").strip().lower()
        if action == 'quit':
            break
        elif action == 'balance':
            print(f"Current balance: {account.balance()}")
        elif action == 'deposit':
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print(f"Deposited {amount}. New balance: {account.balance()}")
            except ValueError as e:
                print(f"Error: {e}")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                print(f"Withdrew {amount}. New balance: {account.balance()}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid action. Try again.")
