import tkinter as tk
# tkinker is the module used to create window 

def isEven():
    # print(" you clicked button")
    n=int(t1.get())
    # print ( f"{n} ", type(n))
    msg = f"{n} is Even " if n%2==0 else f"{n} is odd"

    print( msg)
    dis.config(text=msg,font=("calibri",20),fg ="blue")





window=tk.Tk()

window.geometry('500x500')
window.title("My Window")

lbl=tk.Label(window,text="Enter a Number")
lbl.place(x=100,y=100)

t1=tk.Entry(window)
t1.place(x=200,y=100)

btn=tk.Button(window,text=" is Even ?",command=isEven )
btn.place(x=200 ,y=150)

# msg = isEven()

dis = tk.Label(window)
dis.place(x=100,y=300)




window.mainloop()


