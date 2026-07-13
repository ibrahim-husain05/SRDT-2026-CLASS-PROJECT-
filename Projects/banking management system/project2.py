#bank management system using oops
from abc import ABC, abstractmethod
class bankAccount(ABC):
    def __init__(self,name,balance):
        self.name=name 
        self.__balance = balance#encapsulation
    def deposit(self,amount):
        self.__balance += amount#add money to accout
        print("₹",amount,"successfully deposited.")
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -=amount#withdraw money
            print("₹",amount,"successfully withdrawn.")
        else:
            print("insufficient funds.")
    def checkBalance(self):
        #balance checking
        print("current balaance in your account is : ₹",self.__balance)

    @abstractmethod
    def accountType(self):
        pass
class savingAccount(bankAccount):
    #child class with parent class , inheritance is used also
    def accountType(self):
        #overriding (runtime polymorphism)
        print("\n Saving account.")
class currentAccount(bankAccount):
    def accountType(self):
        #overriding (runtime polymorphism)
        print("\n Current account.")

print("--------BANK MANAGEMENT SYSTEM-----------")
name = input("Enter your name : ")
balance = float(input("Enter the balance : "))
print("1 : \n Savings account")
print("2 : \n Current account")
choice = int(input("Select your account type : "))
if choice == 1:
    account = savingAccount(name,balance)
elif choice == 2:
    account = currentAccount(name,balance)   
else:
    print("Invalid choice.")
    exit

while True:
    #infinite loop
    print("----------MENU-----------")
    print("1.\nDEPOSIT")
    print("2.\nWITHDRAW")
    print("3.\nCHECK BALANCE")
    print("4.\nACCOUNT TYPE")
    print("5.\nEXIT")

    option = int(input("Enter your choice: "))
    if option == 1:
        amount = float(input("Enter the amount to deposit:"))
        account.deposit(amount)
    elif option == 2:
        amount = float(input("Enter the amount you want to withdraw: "))
        account.withdraw(amount)
    elif option == 3:
        account.checkBalance()
    elif option == 4:
        account.accountType()
    elif option == 5:
        print("Thank you for visiting.")
        break
    else:
        print("Invalid choice.")


    
