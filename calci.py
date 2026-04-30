import tkinter as tk
from tkinter.messagebox import showerror

msg=""
def calclulate( p ):
    # print(f"you clicked button {p}")

    try:

        global msg

        if p=='=':
            res=eval(msg)
            lbldisplay.config(text=res)
            msg=str(res)
        else:
            msg=msg+p
            lbldisplay.config(text=msg)

    except Exception as e:
        print(e)
        showerror("Warning",e)





    


window=tk.Tk()

window.geometry('500x500')

window.title("My Calci")

lbldisplay=tk.Label(window,bg="white",width=30,bd=1, relief="solid")
lbldisplay.place(x=150,y=80)

btn7=tk.Button(window,text="7" , command=lambda : calclulate('7') )
btn7.place(x=150,y=130)

btn8=tk.Button(window,text="8", command=lambda : calclulate('8'))
btn8.place(x=180,y=130)

btn9=tk.Button(window,text="9", command=lambda : calclulate('9'))
btn9.place(x=210,y=130)

btnplus=tk.Button(window,text=" + ", command=lambda : calclulate('+'))
btnplus.place(x=240,y=130)



btn4=tk.Button(window,text="4", command=lambda : calclulate('4'))
btn4.place(x=150,y=180)

btn5=tk.Button(window,text="5", command=lambda : calclulate('5'))
btn5.place(x=180,y=180)

btn6=tk.Button(window,text="6", command=lambda : calclulate('6'))
btn6.place(x=210,y=180)

btnminus=tk.Button(window,text=" - ", command=lambda : calclulate('-'))
btnminus.place(x=240,y=180)


btn1=tk.Button(window,text="1", command=lambda : calclulate('1'))
btn1.place(x=150,y=230)

btn2=tk.Button(window,text="2", command=lambda : calclulate('2'))
btn2.place(x=180,y=230)

btn3=tk.Button(window,text="3", command=lambda : calclulate('3'))
btn3.place(x=210,y=230)

btnprod=tk.Button(window,text=" * ", command=lambda : calclulate('*'))
btnprod.place(x=240,y=230)

btn0=tk.Button(window,text="0", command=lambda : calclulate('0'))
btn0.place(x=150,y=280)

btndot=tk.Button(window,text=" . ", command=lambda : calclulate('.'))
btndot.place(x=180,y=280)

btndiv=tk.Button(window,text=" / ", command=lambda : calclulate('/'))
btndiv.place(x=210,y=280)

btnmod=tk.Button(window,text=" % ", command=lambda : calclulate('%'))
btnmod.place(x=240,y=280)

btnres=tk.Button(window,text=" = ",width=15,bg="cyan", command=lambda : calclulate('='))
btnres.place(x=150,y=330)






window.mainloop()