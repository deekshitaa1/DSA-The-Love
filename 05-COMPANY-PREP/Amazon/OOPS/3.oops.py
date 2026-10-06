# BANK ACCONT

class Bank_Account:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self._balance=balance

    def deposit(self,amount):
        self._balance+=amount
    def withdraw(self,amount):
        self._balance-=amount
    def check_balance(self):
        return self._balance

bank1=Bank_Account("anitha",2000)
bank1._balance += 500
print(bank1.deposit(500))

