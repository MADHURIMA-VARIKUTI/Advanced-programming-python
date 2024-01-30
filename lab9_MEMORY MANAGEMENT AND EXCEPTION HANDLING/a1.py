class InsufficientBalanceError(Exception):
    pass

class DailyDepositLimitExceededError(Exception):
    pass

class DailyWithdrawalLimitExceededError(Exception):
    pass

class Bank:
    def __init__(self, balance=1000):
        self.balance = balance
        self.daily_deposits = 0
        self.daily_withdrawals = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount should be greater than zero.")
        
        if self.daily_deposits + amount > 10000:
            raise DailyDepositLimitExceededError("Daily deposit limit exceeded.")
        
        self.balance += amount
        self.daily_deposits += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount should be greater than zero.")
        
        if amount > 5000:
            raise DailyWithdrawalLimitExceededError("Daily withdrawal limit exceeded.")
        
        if self.balance - amount < 1000:
            raise InsufficientBalanceError("Insufficient balance after withdrawal.")
        
        self.balance -= amount
        self.daily_withdrawals += amount

    def get_balance(self):
        return self.balance

class BookNotAvailableError(Exception):
    pass

class InsufficientCopiesError(Exception):
    pass

class Book:
    def __init__(self, title, author, copies=0):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies == 0:
            raise BookNotAvailableError("Book is not available.")
        self.copies -= 1

    def return_book(self):
        self.copies += 1

if __name__ == "__main__":
    bank = Bank()
    try:
        bank.deposit(5000)
        print(f"Balance after deposit: Rs. {bank.get_balance()}")
        bank.withdraw(2000)
        print(f"Balance after withdrawal: Rs. {bank.get_balance()}")
        bank.deposit(8000)  # This will raise DailyDepositLimitExceededError
    except InsufficientBalanceError as e:
        print(f"Error: {e}")
    except DailyDepositLimitExceededError as e:
        print(f"Error: {e}")
    except DailyWithdrawalLimitExceededError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

    book = Book("Python Basics", "John Doe", copies=3)
    try:
        book.borrow()
        print(f"{book.title} borrowed, {book.copies} copies remaining.")
        book.borrow()  # This will raise BookNotAvailableError
    except BookNotAvailableError as e:
        print(f"Error: {e}")

    book.return_book()
    print(f"{book.title} returned, {book.copies} copies available.")
    book.return_book()
    print(f"{book.title} returned, {book.copies} copies available.")
    book.borrow()
    book.borrow()  # This will raise InsufficientCopiesError
