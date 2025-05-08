import csv


class Account:
    def __init__(self, name, balance = 0, password = ""):
        self.__account_name = name
        self.__account_balance = balance
        self.__account_password = password
        self.set_balance(self.__account_balance)

    def set_password(self, password):
        self.__account_password = password

    def check(self, password):
        if password == self.__account_password:
            return True
        else:
            return False


    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            current_balance = self.get_balance()
            self.set_balance(current_balance + amount)
            return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.get_balance():
            return False
        else:
            current_balance = self.get_balance()
            self.set_balance(current_balance - amount)
            return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

    def set_balance(self, value):
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value


    def set_name(self, value):
        self.__account_name = value



    def __str__(self):
        return f'Account Name: {self.get_name()}, Account balance = {self.get_balance():.2f}'


class SavingAccount(Account):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name, password = ""):
        super().__init__(name, SavingAccount.MINIMUM, password)
        self.__deposit_count = 0

    def apply_interest(self):
        if self.__deposit_count >= 5:
            interest = self.get_balance() * SavingAccount.RATE
            new_balance = self.get_balance() + interest
            self.set_balance(new_balance)
            self.__deposit_count = 0


    def deposit(self, amount):
        if super().deposit(amount):
            self.__deposit_count += 1
            if self.__deposit_count >= 5:
                self.apply_interest()
            return True
        return False




    def withdraw(self, amount):
        if amount <= 0 or amount > self.get_balance():
            return False
        elif (self.get_balance() - amount) >= SavingAccount.MINIMUM :
            x = self.get_balance() - amount
            self.set_balance(x)
            return True
        else:
            return False


    def set_balance(self, value):
        if value < SavingAccount.MINIMUM:
            super().set_balance(SavingAccount.MINIMUM)
        else:
            super().set_balance(value)

    def __str__(self):
        return f'SAVING ACCOUNT: {super().__str__()}'


class Bank:
    def __init__(self):
        self.accounts = {}

    def information(self, name, password, account_type):
        key = (name.lower(), account_type.lower())
        if key not in self.accounts:
            if account_type.lower() == "checking":
                self.accounts[key] = (Account(name), password)
            elif account_type.lower() == "saving":
                self.accounts[key] = (SavingAccount(name), password)
            return self.accounts[key][0], True
        else:
            account, stored_password = self.accounts[key]
            if password == stored_password:
                return account, False
            else:
                return None, False





