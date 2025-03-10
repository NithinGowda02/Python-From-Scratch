class ATM:
    def __init__(self, balance):
        self.__balance = balance
        print(f"Bank Balance >> {self.__balance}")

    def deposit(self, deposited_amount):
        self.__balance += deposited_amount
        print(f"Balance after depositing {deposited_amount} >> {self.__balance}")   

    def withdrawal(self, withdrawed_amount):
        if self.__balance >= withdrawed_amount:
            self.__balance -= withdrawed_amount
            print(f"Balance after Withdrawing {withdrawed_amount} >> {self.__balance}")
        else:
            print(f"Insufficient Funds...! Current Balance >> {self.__balance}")    

transaction = ATM(1994)
transaction.deposit(2000)
transaction.withdrawal(12350)