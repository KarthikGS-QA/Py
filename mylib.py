from datetime import datetime


def isEven(n):
    return True if n%2==0 else False




class Trans:
    def __init__(self, actnum, tdate, ttype, tamount, bamount):
        self.__actnum = actnum
        self.__tdate = tdate
        self.__ttype = ttype
        self.__tamount = tamount
        self.__bamount = bamount
        
    def display(self):
        print(f"{self.__actnum},{self.__tdate},{self.__ttype},{self.__tamount},{self.__bamount}")
        

class Bank:
    def __init__(self, name, actnum, ifsc, bal):
        self.__name = name
        self.__actnum = actnum
        self.__ifsc = ifsc
        self.__bal = int(bal)
        self.__cdate = datetime.now()
        self.__tl = []

    def display(self):
        print(f"Name : {self.__name}")
        print(f"Account no : {self.__actnum}")
        print(f"IFSC : {self.__ifsc}")
        print(f"Balance amount : {self.__bal}")
        print(f"Created date : {self.__cdate}")
        
        if len(self.__tl) > 0:
            print(f"----------Trans history---------")
            print(f"Actnum,Tdate,Ttype,Tamt,Balamount")
            print("----------------------------------")
            for tobj in self.__tl:
                tobj.display()
        
    def withdraw(self, wamount):
        self.__bal -= wamount
        tr = Trans(self.__actnum, datetime.now(), "Wit", wamount, self.__bal)
        self.__tl.append(tr)
    
    def deposit(self, damount):
        self.__bal += damount
        tr = Trans(self.__actnum, datetime.now(), "Dep", damount, self.__bal)
        self.__tl.append(tr)
    
    # def match(self, key):
    #     return True if self.__actnum == key else False

    # --- CONVERTED SEARCH METHOD TO CLASS METHOD ---
    @classmethod
    def search(cls, customers, key):
        for cust in customers:
            if cust.__actnum==key:
                return cust
        return None
