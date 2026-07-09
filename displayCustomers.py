from tkinter import *
from tkinter import ttk
from dbDemo import DB

root=Tk()
root.title("Display Customers")
root.geometry('700x700')

tree=ttk.Treeview(root)

tree["columns"] = ("ID", "Actnum", "Name", "IFSC","Balance")

tree.column("#0", width=0, stretch=NO)

tree.column("ID", anchor=CENTER, width=80)
tree.column("Name", anchor=CENTER, width=180)
tree.column("Actnum", anchor=CENTER, width=80)
tree.column("IFSC", anchor=CENTER, width=80)
tree.column("Balance", anchor=CENTER, width=80)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Actnum", text="Actnum")
tree.heading("IFSC", text="IFSC")
tree.heading("Balance", text="Balance")





sql="select * from customers order by id"

DB.mycursor.execute(sql)

rows=DB.mycursor.fetchall()

for row in rows:
    # print(row)
    tree.insert("",END, values=row)

tree.pack(fill=BOTH, expand=True)

root.mainloop()


