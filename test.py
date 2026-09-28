#block E
class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance = amount + self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            print("Withdrawal amount cannnot exceed balance, please try again")
            return None
        else:
            self.balance = self.balance - amount


account = BankAccount()
account.deposit(100)
print(account.balance)

account.withdraw(30)
print(account.balance)

account.withdraw(1000)
print(account.balance)