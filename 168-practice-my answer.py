from tkinter import *
from tkinter import ttk

window=Tk()

def kg_to_grams():
    print(e1_value.get())
    grams=float(e1_value.get())*1000
    t1.insert(END,grams)
    
def kg_to_pounds():
    print(e1_value.get())
    pounds=float(e1_value.get())*2.20462
    t2.insert(END,pounds)
    
def kg_to_ounces():
    print(e1_value.get())    
    ounces=float(e1_value.get())*35.274
    t3.insert(END,ounces)

b1=ttk.Button(window,text="Kg")
b1.grid(row=0,column=0)

b2=ttk.Button(window,text="Convert",command=kg_to_grams)
b2=ttk.Button(window,text="Convert",command=kg_to_pounds)
b2=ttk.Button(window,text="Convert",command=kg_to_ounces)
b2.grid(row=0,column=2)


e1_value=StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=10)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=10)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=10)
t3.grid(row=1,column=2)

window.mainloop()    