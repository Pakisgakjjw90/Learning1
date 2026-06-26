class InsufficientFunds(Exception):
    pass


import json


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
    def get_interest(self):
        return self._interest_rate
    

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
    def return_Overdraft(self):
        return self._overdraft_limit
    
    
    
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

print("Welcome to Meezan Bank")
Meezan=Bank()

try:
    with open("Bank.json","r") as file:
        data=json.load(file)
        for item in data:
            if item["type"] == "SavingsAccount":
                acc=SavingsAccount(item["Accountno"],item["Interestrate"])
                acc._balance=item["balance"]
                Meezan.add_account(acc)
            elif item["type"] == "CheckingAccount":
                acc=CheckingAccount(item["Accountno"],item["Overdraftlimit"])
                acc._balance=item["balance"]
                Meezan.add_account(acc)
except FileNotFoundError:
    pass     
            
        
         

while True:
    option =int(input("1)Add account 2)Deposit 3)Withdraw 4)transfer money 5)List accounts 6)Exit"))
    if option == 1:
        opt=int(input("Enter which account you wanna open 1)savings account 2) checkings account:"))
        if opt == 1:
            account_no=int(input("Enter the account_no:"))
            interest=float(input("Enter interest you want:"))
            interest=interest/100
            s1=SavingsAccount(account_no,interest)
            Meezan.add_account(s1)
        elif opt == 2:
            account_no=int(input("Enter the account_no"))
            overdraft=int(input("Enter the overdraft limit you want:"))
            c1=CheckingAccount(account_no,overdraft)
            Meezan.add_account(c1)
        else:
            print("Invalid option")
    elif option == 2:
        account_no=int(input("Enter your account_no in which you wanna deposit:"))
        amount=int(input("Enter the amount to deposit:"))
        
        flag=False
        try:
                for acc in Meezan.Accounts:
                    acci=acc.get_accountno()
                    if acci == account_no:
                        acc.deposit(amount)
                        flag=True
                        break
                if flag== False:
                    print("Account not found")
        except Exception as e:
                print (e)
    elif option == 3:
            account_no=int(input("Enter your account_no from which you wanna withdraw:"))
            amount=int(input("Enter the amount to withdraw:"))
            flag = False
            try:
                for acc in Meezan.Accounts:
                    acci=acc.get_accountno()
                    if acci == account_no:
                        acc.withdraw(amount)
                        flag=True
                        break
                if flag== False:
                    print("Account not found")
            except Exception as e:
                print (e)
    elif option == 4:
        fro=int(input("Enter senders account no:"))
        to=int(input("Enter receivers account no:"))
        amount=int(input("Enter the amount you wanna send:"))
        Meezan.transfer(fro,to,amount)
    
    elif option == 5:
        li=Meezan.list_accounts()
        for acc in li:
            print("Account_no:",acc.get_accountno(),"Balance:",acc.return_balance())
   
    elif option == 6:
        data=[]
        for item in Meezan.Accounts:
            if isinstance(item,SavingsAccount):
                data.append({"type":"SavingsAccount","Accountno":item.get_accountno(),
                             "balance":item.return_balance(),"Interestrate":item.get_interest()})
        
            elif isinstance(item,CheckingAccount):
                data.append({"type":"CheckingAccount","Accountno":item.get_accountno(),
                             "Balance":item.return_balance(),
                             "Overdraftlimit":item.return_Overdraft()})
            
        with open("Bank.json","w") as file:
            json.dump(data,file)
        
        
        
        print("Exiting bank")
        break
    else:
        print("Invalid option")
        