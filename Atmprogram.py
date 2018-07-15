class Account():
    
    def __init__(self,owner,balance=0):
        
        self.owner = owner
        self.balance = balance
        
    def deposit(self,dep_amt):
        
        self.balance += dep_amt
        print(f"Added {dep_amt} to the balance")
        
    def withdrawl(self,wd_amt):
        
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print("Withdrawl accepted")
        else:
            print("Sorry non enough funds!")
            
    def __str__(self):
            return f"Owner: {self.owner} \nBalance: {self.balance}"
