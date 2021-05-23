from tkinter import *
from p52 import database

db = database()

def getsr(event):
    global st
    index = lb.curselection()[0]
    st = lb.get(index)
    e1.delete(0,END)
    e1.insert(END,st[1])
    e2.delete(0,END)
    e2.insert(END,st[2])
    e3.delete(0,END)
    e3.insert(END,st[3])
    e4.delete(0,END)
    e4.insert(END,st[4])
    return(st)

def vc():
    lb.delete(0,END)
    for row in db.view():
        lb.insert(END, row)

def se():
    lb.delete(0,END)
    for row in db.search(title.get(), author.get(), year.get(), isbn.get()):
        lb.insert(END, row)

def ae():
    db.insert(title.get(), author.get(), year.get(), isbn.get())
    lb.delete(0,END)
    lb.insert(END,(title.get(), author.get(), year.get(), isbn.get()))

def ds():
    db.delete(st[0])

def us():
    db.upadte(st[0], title.get(), author.get(), year.get(), isbn.get())
    lb.delete(0,END)
    lb.insert(END,(st[0], title.get(), author.get(), year.get(), isbn.get()))

ba = Tk()
ba.title("BOOK APP")


l1 = Label(ba,text="TITLE", activebackground = "red")
l1.grid(row = 0, column = 0)

l2 = Label(ba,text="YEAR")
l2.grid(row = 1, column = 0)

l3 = Label(ba,text="AURTHOR")
l3.grid(row = 0, column = 2)

l4 = Label(ba,text="ISBN")
l4.grid(row = 1, column = 2)

title = StringVar()
e1 = Entry(ba, textvariable = title, bg = "pink", highlightcolor = "blue")
e1.grid(row = 0, column = 1)

author = StringVar()
e2 = Entry(ba, textvariable = author, bg = "pink", highlightcolor = "blue")
e2.grid(row = 0, column = 3)

year = StringVar()
e3 = Entry(ba, textvariable = year, bg = "pink", highlightcolor = "blue")
e3.grid(row = 1, column = 1)

isbn = StringVar()
e4 = Entry(ba, textvariable = isbn, bg = "pink", highlightcolor = "blue")
e4.grid(row = 1, column = 3)

lb = Listbox(ba, height = 6 , width = 35)
lb.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb = Scrollbar(ba)
sb.grid(row = 4, column = 2)

lb.configure(yscrollcommand = sb.set)
sb.configure(command = lb.yview)

lb.bind('<<ListboxSelect>>',getsr)

b1 = Button(ba, text = "VIEW ALL", width = 12, command = vc, activebackground = "red", activeforeground = "blue")
b1.grid(row = 2, column = 3)

b2 = Button(ba, text = "SEARCH ENTRY", width = 12, command = se, activebackground = "red", activeforeground = "blue")
b2.grid(row = 3, column = 3)

b3 = Button(ba, text = "ADD ENTRY", width = 12, command = ae, activebackground = "red", activeforeground = "blue")
b3.grid(row = 4, column = 3)

b4 = Button(ba, text = "UPDATE SELECTED", width = 12, command = us, activebackground = "red", activeforeground = "blue")
b4.grid(row = 5, column = 3)

b5 = Button(ba, text = "DELETE SELECTED", width = 12, command = ds, activebackground = "red", activeforeground = "blue")
b5.grid(row = 6, column = 3)

b6 = Button(ba, text = "CLOSE", width = 12, command = ba.destroy, activebackground = "red", activeforeground = "blue")
b6.grid(row = 7, column = 3)
"""
p1 = PhotoImage(file = 'bookimg.jpg') 
ba.iconphoto(False, 'bookimg.jpg') 
"""
ba.mainloop()