from tkinter import *
from tkinter import ttk

window = Tk()　　　　　　　　　　　　　　　　　　　　　　　　　　#首先建立一个窗口

def km_to_miles():                                                       #build a function define km_to_miles
    print(e1_value.get())                                                #input the value in e1
    miles=float(e1_value.get())*1.6                                      # e1 * 1.6 and get a result.  because what we have input in e1 is a string, so need to appoint a float input.
    t1.insert(END,miles)                                                 # insert the result into t1

b1 = ttk.Button(window,text="Execute",command=km_to_miles)         #先指定给window添加一个button(Execute)  / comand a button to do someting need comand function(km_to_miles)
b1.grid(row=0,column=0)                                            #给上面的button设置一个位置。

e1_value=StringVar()                                               # StringVar what you will input here will be a string
e1 = Entry(window,textvariable=e1_value)                           #Add an entry widge belongs to window
e1.grid(row=0,column=1)                                            #The place of entry widge

t1 = Text(window,height=1,width=20)                                # a text widge to reply the entry widge 
t1.grid(row=0,column=2)


window.mainloop()                                        #与首句window=TK()呼应，必须有的句子，放在程序末尾
