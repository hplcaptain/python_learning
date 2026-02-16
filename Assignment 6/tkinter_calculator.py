from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('300x400')

entry_btn = Entry(root, width=16, font=("Arial", 24), borderwidth=5 )
entry_btn.place(x=0, y=0)

def click(num):
    result = entry_btn.get()
    entry_btn.delete(0,END)
    entry_btn.insert(0, str(result)+ str (num))

b = Button(root, text='1', width=10, font=("Arial", 12), command=lambda:click(1))
b.place(x=10, y=60)

b = Button(root, text='2', width=10, font=("Arial", 12), command=lambda:click(2))
b.place(x=80, y=60)

b = Button(root, text='3', width=10, font=("Arial", 12), command=lambda:click(3))
b.place(x=170, y=60)

b = Button(root, text='4', width=10, font=("Arial", 12), command=lambda:click(4))
b.place(x=10, y=120)

b = Button(root, text='5', width=10, font=("Arial", 12), command=lambda:click(5))
b.place(x=80, y=120)

b = Button(root, text='6', width=10, font=("Arial", 12), command=lambda:click(6))
b.place(x=170, y=120)

b = Button(root, text='7', width=10, font=("Arial", 12), command=lambda:click(7))
b.place(x=10, y=180)

b = Button(root, text='8', width=10, font=("Arial", 12), command=lambda:click(8))
b.place(x=80, y=180)

b = Button(root, text='9', width=10, font=("Arial", 12), command=lambda:click(9))
b.place(x=170, y=180)

b = Button(root, text='0', width=10, font=("Arial", 12), command=lambda:click(0))
b.place(x=10, y=240)

#Operators
def add():
        n1 = entry_btn.get()
        global match
        match = "addition"
        global i
        i = int(n1)
        entry_btn.delete(0,END)
b = Button(root, text='+', width=10, font=("Arial", 12), command=add)
b.place(x=80, y=240)

def sub():
        n1 = entry_btn.get()
        global match
        match = "substraction"
        global i
        i = int(n1)
        entry_btn.delete(0,END)
b = Button(root, text='-', width=10, font=("Arial", 12), command=sub)
b.place(x=170, y=240)

def multi():
        n1 = entry_btn.get()
        global match
        match = "multiplication"
        global i
        i = int(n1)
        entry_btn.delete(0,END)
b = Button(root, text='*', width=10, font=("Arial", 12), command=multi)
b.place(x=10, y=300)

def div():
        n1 = entry_btn.get()
        global match
        match = "division"
        global i
        i = int(n1)
        entry_btn.delete(0,END)
b = Button(root, text='/', width=10, font=("Arial", 12), command=div)
b.place(x=80, y=300)

def equal():
       n2 = entry_btn.get()
       entry_btn.delete(0,END)
       if match == "addition" :
            entry_btn.insert (0, i + int(n2))
       elif match == "substraction":
            entry_btn.insert (0, i - int(n2))
       elif match == "multiplication":
            entry_btn.insert (0, i * int(n2))
       elif match == "division":
            entry_btn.insert (0, i / int(n2))
                    

b = Button(root, text='=', width=10, font=("Arial", 12), command=equal)
b.place(x=170, y=300)

def clear():
      entry_btn.delete(0,END)
b = Button(root, text='Clear', width=10, font=("Arial", 12), command=clear)
b.place(x=10, y=350)

root.mainloop()