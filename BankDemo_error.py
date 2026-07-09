
from datetime import datetime


class Trans:
    
    # def __init__(self,actnum,tdate,ttype,tamount,bamount):
        
    #     self.__actnum=actnum
    #     self.__tdate=tdate
    #     self.__ttype=ttype
    #     self.__tamount=tamount
    #     self.__bamount=bamount
        
    def __init__(self,obj,ttype,tamount):
        
        self.__actnum=obj.actnum
        self.__tdate=datetime.now()
        self.__ttype=ttype
        self.__tamount=tamount
        self.__bamount=obj.__bal
    
    
    def display(self):
        
        print(f"{self.__actnum},{self.__tdate},{self.__ttype},{self.__tamount},{self.__bamount}")
        

class Bank:
    
    
    def __init__(self,name,actnum,ifsc,bal):
        
        self.__name=name
        self.actnum=actnum
        self.__ifsc=ifsc
        self.__bal=int(bal)
        self.__cdate=datetime.now()
        self.__tl=[]

    def display(self):
        print(f"Name : {self.__name}")
        print(f"Account no : {self.actnum}")
        print(f"IFSC : {self.__ifsc}")
        print(f"Balance amount : {self.__bal}")
        print(f"Created date : {self.__cdate}")
        
        if len(self.__tl) > 0:
            
            print(f"----------Trans history---------")
            print(f"Actnum,Tdate,Ttype,Tamt,Balamount")
            print("----------------------------------")
            for tobj in self.__tl:
                tobj.display()
        
    
    def withdraw(self,wamount):
        
        self.__bal-=wamount
        
        tr=Trans(self.__actnum,datetime.now(),"Wit",wamount,self.__bal)
        
        self.__tl.append(tr)
    
    
    def deposit(self,damount):
        
        self.__bal+=damount
        
        tr=Trans(self,"dep",damount)
        
        self.__tl.append(tr)
    
    def match(self,key):
        
        return True if self.actnum==key else False
        




def search(customers,key):
    
    for cust in customers:
        if cust.match(key):
            return cust
    
    return None

if __name__=='__main__':
    
    
    customers=[]
    
    while True:
        
        
        print("1: New account\n2: Display\n3. Withdraw\n4: Deposit\n5. Exit\nEnter your choice : ")
        
        choice=int(input())
        
        
        if choice==1:
            name,actnum,ifsc,bal=input("Enter Name,Accout no,IFSC,Balance amount : ").split()
            b1=Bank(name,actnum,ifsc,bal)
            customers.append(b1)
            
            print("-----Customer detailed added to database ------")
        
        elif choice==2:
            key=input('Enter the account no : ')
            
            
            res=search(customers,key)
            
            if res==None:
                print(f"Sorry,Account no : {key} not found !")
            else:
                res.display()
                print(f"--Customer details displayed ---")
            
            
            # flag=0
            # for cust in customers:
                
            #     if cust.match(key):
            #         cust.display()
            #         flag=1
            #         break
            
            # if flag==0:
            #     print(f"Sorry, account no : {key} does not Exist !")
            # else:
                
            #     print("----Customer details displayed !!---")
            
            
            
        elif choice==3:
            
            key=input("Enter account no : ")
            
            cust=search(customers,key)
            
            if cust==None:
                print(f"----Sorry account no : {key} not found !")
            else:
                
                wamount=int(input("Enter with draw amount : "))
                
                cust.withdraw(wamount)
                
                print("-----Withdraw done !! -----")
        elif choice==4:
            key=input("Enter account no : ")
            
            cust=search(customers,key)
            
            if cust==None:
                print(f"----Sorry account no : {key} not found !")
            else:
                
                damount=int(input("Enter deposit amount : "))
                
                cust.deposit(damount)
                
                print("-----Deposit done !! -----")
        elif choice==5:
            break
        
        input()