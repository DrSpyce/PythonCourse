import bankaccount


class SavingsAccount(bankaccount.BankAccount):
    interest_rate = 0.02

    def add_interest(self):
        interest_amount = self.balance * SavingsAccount.interest_rate
        print(f"Interest added: ${interest_amount}")
        self.deposit(interest_amount)
