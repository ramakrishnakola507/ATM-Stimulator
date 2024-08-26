# ATM Machine Simulation in Python

class Account:
    """
    A class to represent a bank account with basic ATM functionalities.
    """
    def __init__(self, pin, balance=0):
        """
        Initialize the account with a PIN, initial balance, and empty transaction history.
        
        :param pin: The account's PIN code as a string.
        :param balance: The initial balance as a float. Defaults to 0.
        """
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        """
        Returns the current account balance.
        
        :return: The account balance as a float.
        """
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.
        
        :param amount: The amount to withdraw as a float.
        :return: A tuple (success: bool, message: str).
        """
        if amount <= 0:
            return False, "Withdrawal amount must be positive."
        if amount > self.balance:
            return False, "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f"Withdrew ${amount:.2f}")
        return True, f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        
        :param amount: The amount to deposit as a float.
        :return: A tuple (success: bool, message: str).
        """
        if amount <= 0:
            return False, "Deposit amount must be positive."
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount:.2f}")
        return True, f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def change_pin(self, old_pin, new_pin):
        """
        Changes the account PIN after verifying the old PIN.
        
        :param old_pin: The current PIN as a string.
        :param new_pin: The new PIN as a string.
        :return: A tuple (success: bool, message: str).
        """
        if old_pin != self.pin:
            return False, "Incorrect current PIN."
        if not new_pin.isdigit() or len(new_pin) != 4:
            return False, "New PIN must be a 4-digit number."
        self.pin = new_pin
        self.transaction_history.append("PIN changed")
        return True, "PIN successfully changed."

    def get_transaction_history(self):
        """
        Returns the list of transaction history.
        
        :return: A list of strings describing each transaction.
        """
        return self.transaction_history


def atm_simulation():
    """
    Simulates an ATM machine interface allowing users to perform various transactions.
    """
    # Initialize the account with a default PIN and balance
    account = Account(pin="1234", balance=1000.00)
    
    print("Welcome to the ATM Simulation.")
    
    # Allow the user up to 3 attempts to enter the correct PIN
    for attempt in range(3):
        entered_pin = input("Please enter your 4-digit PIN: ")
        if entered_pin == account.pin:
            print("PIN accepted. Access granted.\n")
            break
        else:
            print("Incorrect PIN. Please try again.\n")
    else:
        print("Too many incorrect PIN attempts. Exiting.")
        return  # Exit the simulation
    
    while True:
        # Display the menu of options
        print("Please choose from the following options:")
        print("1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. PIN Change")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Enter the number corresponding to your choice: ")
        print()  # Add a blank line for better readability
        
        if choice == '1':
            # Account Balance Inquiry
            balance = account.check_balance()
            print(f"Your current balance is: ${balance:.2f}\n")
        
        elif choice == '2':
            # Cash Withdrawal
            try:
                amount_str = input("Enter the amount to withdraw: $")
                amount = float(amount_str)
                success, message = account.withdraw(amount)
                print(message + "\n")
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")
        
        elif choice == '3':
            # Cash Deposit
            try:
                amount_str = input("Enter the amount to deposit: $")
                amount = float(amount_str)
                success, message = account.deposit(amount)
                print(message + "\n")
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")
        
        elif choice == '4':
            # PIN Change
            old_pin = input("Enter your current PIN: ")
            new_pin = input("Enter your new 4-digit PIN: ")
            success, message = account.change_pin(old_pin, new_pin)
            print(message + "\n")
        
        elif choice == '5':
            # Transaction History
            history = account.get_transaction_history()
            if not history:
                print("No transactions have been made yet.\n")
            else:
                print("Transaction History:")
                for idx, transaction in enumerate(history, start=1):
                    print(f"{idx}. {transaction}")
                print()  # Add a blank line after the history
        
        elif choice == '6':
            # Exit
            print("Thank you for using the ATM Simulation. Goodbye!")
            break
        
        else:
            # Invalid choice
            print("Invalid selection. Please choose a valid option.\n")


if __name__ == "__main__":
    atm_simulation()
