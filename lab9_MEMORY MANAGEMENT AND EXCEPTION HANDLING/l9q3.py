class Bank:
    def __init__(self, name, age, account_number, account_type, balance):
        self.name = name
        if 18 <= age <= 100:
            self.age = age
        else:
            raise ValueError("Age should be between 18 and 100.")
        if 10000 <= account_number <= 99999:
            self.account_number = account_number
        else:
            raise ValueError("Account Number should be a 5-digit number.")
        if account_type in ['S', 'C']:
            self.account_type = account_type
        else:
            raise ValueError("Account Type should be 'S' for Savings or 'C' for Current.")
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Invalid amount for withdrawal.")

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Account Number: {self.account_number}")
        if self.account_type == 'S':
            print("Account Type: Savings")
        else:
            print("Account Type: Current")
        print(f"Balance: ${self.balance}")

# Create an empty list to store bank accounts
bank_accounts = []

# Menu-driven program for bank operations
while True:
    print("\nMenu:")
    print("1. Create a new account")
    print("2. Deposit to an account")
    print("3. Withdraw from an account")
    print("4. Print account details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        account_number = int(input("Enter the account number: "))
        account_type = input("Enter the account type (S for Savings, C for Current): ")
        balance = float(input("Enter the initial balance: "))
        new_account = Bank(name, age, account_number, account_type, balance)
        bank_accounts.append(new_account)
        print("New account created successfully.")

    elif choice == 2:
        account_number = int(input("Enter the account number: "))
        amount = float(input("Enter the amount to deposit: "))
        for account in bank_accounts:
            if account.account_number == account_number:
                account.deposit(amount)
                break
        else:
            print("Account not found.")

    elif choice == 3:
        account_number = int(input("Enter the account number: "))
        amount = float(input("Enter the amount to withdraw: "))
        for account in bank_accounts:
            if account.account_number == account_number:
                account.withdraw(amount)
                break
        else:
            print("Account not found.")

    elif choice == 4:
        account_number = int(input("Enter the account number: "))
        for account in bank_accounts:
            if account.account_number == account_number:
                account.print_details()
                break
        else:
            print("Account not found.")

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
        

# Menu:
# 1. Create a new account
# 2. Deposit to an account
# 3. Withdraw from an account
# 4. Print account details
# 5. Exit
# Enter your choice: 1
# Enter the name: MADHU
# Enter the age: 19
# Enter the account number: 12345
# Enter the account type (S for Savings, C for Current): S
# Enter the initial balance: 10000
# New account created successfully.
#
# Menu:
# 1. Create a new account
# 2. Deposit to an account
# 3. Withdraw from an account
# 4. Print account details
# 5. Exit
# Enter your choice: 2
# Enter the account number: 12345
# Enter the amount to deposit: 1234
# Deposited $1234.0. New balance: $11234.0
#
# Menu:
# 1. Create a new account
# 2. Deposit to an account
# 3. Withdraw from an account
# 4. Print account details
# 5. Exit
# Enter your choice: 3
# Enter the account number: 12345
# Enter the amount to withdraw: 1234
# Withdrew $1234.0. New balance: $10000.0
#
# Menu:
# 1. Create a new account
# 2. Deposit to an account
# 3. Withdraw from an account
# 4. Print account details
# 5. Exit
# Enter your choice: 4
# Enter the account number: 12345
# Name: MADHU
# Age: 19
# Account Number: 12345
# Account Type: Savings
# Balance: $10000.0
#
# Menu:
# 1. Create a new account
# 2. Deposit to an account
# 3. Withdraw from an account
# 4. Print account details
# 5. Exit
# Enter your choice: 5
# Exiting the program.
#
# Process finished with exit code 0
