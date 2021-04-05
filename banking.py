class Account():
    
    def __init__(self):
        self.amount = 0.0
        self.owner = None
    

    def deposit(self,amount):
        if amount < 0:
            return ("Amount can't be negative")
        else:
            self.amount = self.amount+amount
            return self.checkBalance()
    def checkBalance(self):
        return self.amount

    def withDrawl(self,amount):
        if self.amount == 0 and amount > 0:
            return ("Insufficient funds")
        elif self.amount < amount:
            return ("Insufficient funds")
        elif amount < 0:
            return ("Amount can't be negative")
        else:
            self.amount = self.amount - amount
            return self.checkBalance()
   





n = int(input())
w = Account()
for i in range(n):
    s = input().split(" ")
    if(s[0] == 'withDrawl'):
        print(w.withDrawl(float(s[1])))
    elif(s[0] == 'deposit'):
        print(w.deposit(float(s[1])))
    elif(s[0] == 'checkBalance'):
        print(w.checkBalance())



