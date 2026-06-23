class InsufficientFunds(Exception):
    pass





class Account:
    def __init__(self,account_no):
        self._account_no=account_no
        self._balance=0
        
    def deposit(self,amount):
        if amount <=0:
            raise Exception("Negative amount")
        else:
            self._balance+=amount
            
    def withdraw(self,amount):
        if amount <= 0:
            raise Exception("Negative amount")
        else:
            if amount > self._balance:
                raise InsufficientFunds("Insufficientfundserror")
            else:
                self._balance-=amount
    def __str__(self):
         return f"Account_no:{self._account_no}"
    
    def __repr__(self):
         return f"Account no:{self._account_no}"
    
    def return_balance(self):
        return self._balance
    def __eq__(self,other):
        if not isinstance(other,Account):
            return NotImplemented
        return self._account_no == other._account_no
    
    def __lt__(self,other):
        return self._balance < other._balance

    def get_accountno(self):
        return self._account_no


class SavingsAccount(Account):
    def __init__(self,account_no,interest_rate):
        super().__init__(account_no)
        self._interest_rate=interest_rate
    
    def apply_interest(self):
        self._balance+=self._balance * self._interest_rate
    

class CheckingAccount(Account):
    def __init__(self,account_no,overdraft_limit):
        super().__init__(account_no)
        self._overdraft_limit=overdraft_limit
    
    def withdraw(self,amount):
        if amount <=0:
            raise Exception("Negative amount")
        if self._balance-amount < -self._overdraft_limit:
            raise InsufficientFunds("Overdraft limit crossed")
        else:
            self._balance-=amount

class Bank:
    def __init__(self):
        self.Accounts=[]
    
    def add_account(self,account):
        self.Accounts.append(account)
        
    def search_account(self,account_no):
        for a in self.Accounts:
            if a._account_no == account_no:
                return a 
        return None
    def transfer(self,from_no,to_no,amount):
        fro=self.search_account(from_no)
        to=self.search_account(to_no)
        
        if fro != None and to != None:
           try:
             fro.withdraw(amount)
             to.deposit(amount)
           except InsufficientFunds:
               print("Transfer Failed:Insufficient funds")
        else:
            print("One or both accounts dont exist")
    
    def list_accounts(self):
        return sorted(self.Accounts)

Meezan=Bank()
s1=SavingsAccount(12345,0.076)
s2=CheckingAccount(1267,2000)
Meezan.add_account(s1)
Meezan.add_account(s2)

s1.deposit(20000)
s2.deposit(10000)
Meezan.transfer(12345,1267,1000)
account_list=Meezan.list_accounts()

for m in account_list:
    print (f"Account_no:{m.get_accountno()} Balance:{m.return_balance()}")
    
    