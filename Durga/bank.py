# # # ----------------------------------------------------------------------------------------------
# # Convert .py file to .exe file
# pip install pyinstaller
# Choose the(main.py) file of the project = bank.py
# pyinstaller bank.py --onefile
# # # ----------------------------------------------------------------------------------------------
# # Bank Application 
# # # ----------------------------------------------------------------------------------------------
# # # ----Bank name, Customername, Bank balance, zero balance account, deposit operation, withdrawal operation
# # # ----------------------------------------------------------------------------------------------
import sys
class customer:
    '''Customer class with bank related operations''' 
    bankname="Srisha Bank"
    def __init__(self, customername, balance=0):
        self.cname=customername
        self.bal=balance
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("After deposit, of "+str(amount) +" the balance is :",self.bal)
    def withdraw(self,amount):
        if amount > self.bal:
            print("Insufficinet funds, cannot perform this operation")
            sys.exit()                  # # # PVM will stop( but we have to import the module )
        else:
            self.bal=self.bal-amount
            print("After withdrawal, of "+str(amount) +" the balance is :",self.bal)
print("Welcome to",customer.bankname) 
name=input("Enter your name:")   
c=customer(name)
while True:
    print("Welcome",name)
    print("d-Deposit\nw-Withdraw\ne-Exit")
    option=input("Choose your option:")
    if option=="d" or option=="D":
        amount=float(input("Enter the amount  to deposit:"))
        c.deposit(amount)
    elif option=="w" or option=="W":
        amount=float(input("Enter the amount to withdraw:")) 
        c.withdraw(amount)
    elif option=="e" or option=="E":
        print("Thanks for banking with us")
        sys.exit()
    else:
        print("Choose a valid option")