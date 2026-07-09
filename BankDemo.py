from datetime import datetime
from mylib import Bank,Trans


if __name__ == '__main__':
    customers = []
    
    while True:
        print("1: New account\n2: Display\n3. Withdraw\n4: Deposit\n5. Exit\nEnter your choice : ")
        choice = int(input())
        
        if choice == 1:
            name, actnum, ifsc, bal = input("Enter Name,Accout no,IFSC,Balance amount : ").split()
            b1 = Bank(name, actnum, ifsc, bal)
            customers.append(b1)
            print("-----Customer detailed added to database ------")
        
        elif choice == 2:
            key = input('Enter the account no : ')
            
            # Called via the class syntax: Bank.search(...)
            res = Bank.search(customers, key)
            
            if res is None:
                print(f"Sorry,Account no : {key} not found !")
            else:
                res.display()
                print(f"--Customer details displayed ---")
            
        elif choice == 3:
            key = input("Enter account no : ")
            
            # Called via the class syntax: Bank.search(...)
            cust = Bank.search(customers, key)
            
            if cust is None:
                print(f"----Sorry account no : {key} not found !")
            else:
                wamount = int(input("Enter withdraw amount : "))
                cust.withdraw(wamount)
                print("-----Withdraw done !! -----")
                
        elif choice == 4:
            key = input("Enter account no : ")
            
            # Called via the class syntax: Bank.search(...)
            cust = Bank.search(customers, key)
            
            if cust is None:
                print(f"----Sorry account no : {key} not found !")
            else:
                damount = int(input("Enter deposit amount : "))
                cust.deposit(damount)
                print("-----Deposit done !! -----")
                
        elif choice == 5:
            break
        
        input()