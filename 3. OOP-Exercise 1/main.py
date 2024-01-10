import bankaccount
import savingsaccount
import checkingaccount


if __name__ == "__main__":
    account1 = bankaccount.BankAccount("Alice", 1000)
    account2 = savingsaccount.SavingsAccount("Bob", 500)
    account3 = checkingaccount.CheckingAccount("Charlie", 800)

    account1.deposit(200)
    account2.withdraw(50)
    account3.deposit(300)
    account1.withdraw(150)

    account3.withdraw(1200)


    print(f"Account 1 Balance: ${account1.get_balance()}")
    print(f"Account 2 Balance: ${account2.get_balance()}")
    print(f"Account 3 Balance: ${account3.get_balance()}")

    bankaccount.BankAccount.display_total_accounts()

    account2.add_interest()

    # Checking account balances after interest added
    print(f"Account 1 Balance: ${account1.get_balance()}")
    print(f"Account 2 Balance: ${account2.get_balance()}")
    print(f"Account 3 Balance: ${account3.get_balance()}")
