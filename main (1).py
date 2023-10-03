class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number  # Private attribute
        self.__account_holder_name = account_holder_name  # Private attribute
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance}")


# Create an instance of the BankAccount class
account = BankAccount("123456", "John Doe", 1000)

# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()