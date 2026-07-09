import tkinter as tk
from dbDemo import DB
from tkinter.messagebox import showinfo,showerror
class Mywindow(tk.Tk):
    
    def __init__(self,screenName = None, baseName = None, className="tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry('500x500')
        self.title("Bank Application")
        
        
        self.lbl1=tk.Label(self,text="Account no")
        self.lbl1.place(x=100,y=50)
        self.txtactnum=tk.Entry(self)
        self.txtactnum.place(x=200,y=50)
        
        self.lbl2=tk.Label(self,text="Name")
        self.lbl2.place(x=100,y=80)
        self.txtname=tk.Entry(self)
        self.txtname.place(x=200,y=80)
        
        self.lbl3=tk.Label(self,text="IFSC")
        self.lbl3.place(x=100,y=110)
        self.txtifsc=tk.Entry(self)
        self.txtifsc.place(x=200,y=110)
        
        self.lbl4=tk.Label(self,text="Balance Amt")
        self.lbl4.place(x=100,y=140)
        self.txtbal=tk.Entry(self)
        self.txtbal.place(x=200,y=140)
        
        self.btnSave=tk.Button(self,text=" Save ",bg="cyan",command=self.saveCustomer )
        self.btnSave.place(x=100,y=190)

    
    def saveCustomer(self):
        
        actnum=self.txtactnum.get()
        name=self.txtname.get()
        ifsc=self.txtifsc.get()
        balance=self.txtbal.get()
        
        sql=f"insert into customers(actnum,name,ifsc,balance) values('{actnum}','{name}','{ifsc}',{balance})"
        
        print(sql)
        try:
            flag=DB.runQuery(sql)
            
            if flag==1:
                showinfo("Success","Customer deatails saved !")
            else:
                showerror("Error","Duplicate Entry not allowed !")
                
        except Exception as e:
            print(e)
            
            

        


window=Mywindow(None,None,"Good day")

window.mainloop()