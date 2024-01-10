import bankaccount


class CheckingAccount(bankaccount.BankAccount):
    overdraft_limit = 100

    def withdraw(self, amount):
        if amount <= (self.balance + CheckingAccount.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")