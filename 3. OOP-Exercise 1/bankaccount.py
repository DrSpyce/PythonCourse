class BankAccount:
    total_accounts = 0

    def __init__(self, account_holder, initial_balance):
        BankAccount.total_accounts += 1
        self.account_number = BankAccount.total_accounts
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def get_balance(self):
        return self.balance

    @classmethod
    def display_total_accounts(cls):
        print(f"Total number of accounts created: {cls.total_accounts}")