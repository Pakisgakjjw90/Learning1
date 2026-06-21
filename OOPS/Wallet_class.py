class Wallet:
    def __init__(self):
        self.__balance=0
    
    def add_money(self,amount):
        self.__balance+=amount
    
    def spend_money(self,amount):
        if amount > self.__balance:
            print("Not enough balance")
        else:
            self.__balance-=amount

    def check_balance(self):
        return self.__balance
    
w1=Wallet()

w1.add_money(20000)
w1.spend_money(30000)

w1.spend_money(10000)

print(w1.check_balance())