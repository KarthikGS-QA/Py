from tkinter import *
from tkinter.messagebox import showwarning


class AddEmployee(Toplevel):
    def __init__(self,Master=None):
        super().__init__(Master)
        self.title("Add new employee")
        self.geometry("500x500")

    def destroy(self):
        MainWindow.newEmp=False

        print("Add new ")
        return super().destroy()

class DisplayEmployee(Toplevel):
    def __init__(self,Master=None):
        super().__init__(Master)
        self.title("Display employee")
        self.geometry("500x500")

class MainWindow(Tk):

    newEmp=False

    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry("700x700")
        self.title("Employee Management System")

        self.btnAdd=Button(self,text="Add Employee",command=self.addEmployee).pack()
        self.btnDisplay=Button(self,text="Display Employee",command=self.displayEmployee).pack()

    def addEmployee(self):
        if MainWindow.newEmp:
            addemp=AddEmployee(self)
            MainWindow.newEmp=True
        else:
            showwarning(self,"Window already Created !")

    def displayEmployee(self):
        disemp=DisplayEmployee(self)


if __name__=='__main__':
    root=MainWindow()
    root.mainloop()
