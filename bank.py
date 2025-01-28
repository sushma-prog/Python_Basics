#first of all, lets create our abstract parent class. the first thing we are gonna need is a simple constructor. this is gonna take name, balance and minimum balance for the account.
class Account:
    def __init__(self, name, balance, min_balance):#we are gonna take constructor's parameters, name balance and minimum balance.
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    #since each account will deposit money so lets make a method for that
    def deposit(self,amount): #since you deposit money so amount is parameter here.
        self.balance += amount #this is same as self.balance = self.balance + amount.

    #so each account can withdraw money. but only if you have enough amount.
    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance: # here we will check that we wethdraw only when balance after withdrawn is equal or more that minimum balance requirement.
            self.balance -= amount #this is same as self.balance = self.balance - amount.
        else:
            print("sorry, not enough funds!")

    #account will give you a statement too.
    def statement(self):
        print(f"account balance: £{self.balance}") #this is same as .format(self.balance)

#lets make a child class current account that will inherit from our generic class Account.
class Current(Account):
    def __init__(self, name, balance): #here, in this constructor name, balance these parameters are the options they have to enter in order to create a current account.

        #now we will need to pass this data to the parent class. so, we will call the super method.
        super().__init__(name, balance, min_balance = -1000)#name, balance and min_balance = -1000(sice min balance for current account is -1000) this data will be passed to the parent class. 

    #in order to avoid <__main__.Current object at 0x0000021E91F7DFA0> we will define a string function or method.
    def __str__(self):
        return f"{self.name}'s Current Account : Balance £{self.balance}."#now when we print the object account then it will print {self.name}'s Current Account : Balance £{self.balance}. and not <__main__.Current object at 0x0000021E91F7DFA0>.
        
##lets make a child class savings account that will inherit from our generic class Account.
class Savings(Account):
    def __init__(self,name,balance,):

        #now lets call the parent constructor to do all the setup 
        super().__init__(name, balance, min_balance = 0)#since it is a savings account this time, min_balance is going to be zero because you cant go less than zero.
    
    #now as previously the string function:
    def __str__(self):
        return f"{self.name}'s Savings Account : Balance £{self.balance}."
    
#now lets make a account
z = Current("ziad",500)
t = Savings("tom",300)
print(t)
#lets withdraw 300 from tom's account
t.withdraw(300)
t.statement()
t.withdraw(1)
#for ziad's account:
print(z)
#ziad can withdraw up to -1000 because it ia a current account
z.withdraw(1500)
z.statement()
#since now min_balance limit is reached, we cant withdraw anymore
z.withdraw(1)
