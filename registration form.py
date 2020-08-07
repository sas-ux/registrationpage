from tkinter import *
import sqlite3 as sq
from tkinter import messagebox

window = Tk()
window.title("HEALTHRX")
window.geometry('1000x600')
header = Label(window, text="STUDENT DETAILS", font=("arial",30,"bold"), fg="steelblue").pack()

con = sq.connect('python.db')
c = con.cursor()


L1 = Label(window, text = "Registration no. : ", font=("arial", 18)).place(x=10,y=100)
L2 = Label(window, text = "Year of registration : ", font=("arial",18)).place(x=10,y=150)
L3 = Label(window, text = "Year of passing :", font=("arial",18)).place(x=10,y=200)
L4 = Label(window, text = "Student Name :", font=("arial",18)).place(x=10,y=250)
L5 = Label(window, text = "Mobile Number : ", font=("arial",18)).place(x=10,y=300)
L6 = Label(window, text = "Father's Name :", font=("arial",18)).place(x=10,y=350)
L7 = Label(window, text = "Father's Mobile : ", font=("arial",18)).place(x=10,y=400)
L8 = Label(window, text = "Departement : ", font=("arial",18)).place(x=10,y=450)
dept = StringVar(window)
dept.set('select')
depts={'Software','CSE','IT','Biotech','Aerospace','Mechanical'}
deptd=OptionMenu(window,dept,*depts)
deptd.place(x=240,y=450)

regno = StringVar(window)
year = StringVar(window)
grad = StringVar(window)
name = StringVar(window)
mob = StringVar(window)
fname = StringVar(window)
fmob = StringVar(window)

search = StringVar(window)

reg = Entry(window, textvariable = regno)
reg.place(x=240, y=100)

yea = Entry(window, textvariable = year)
yea.place(x=240, y=150)

gra = Entry(window, textvariable = grad)
gra.place(x=240, y=200)

nam = Entry(window, textvariable = name)
nam.place(x=240, y=250)

mo = Entry(window, textvariable = mob)
mo.place(x=240, y=300)

fna = Entry(window, textvariable = fname)
fna.place(x=240, y=350)

fmo = Entry(window, textvariable = fmob)
fmo.place(x=240, y=400)


def send():
    print("New Record inserted")
       
    c.execute('CREATE TABLE IF NOT EXISTS student (Reg TEXT,YOR TEXT,YOP TEXT,Name TEXT,Mob INTEGER,FName TEXT,FMob INTEGER,Dept TEXT)')
       
    c.execute('INSERT INTO student (Reg,YOR,YOP,Name,Mob,FName,FMob,Dept) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',(regno.get(), year.get(), grad.get(), name.get(), mob.get(), fname.get(), fmob.get(), dept.get()))
    con.commit()

    regno.set('')
    year.set('')
    grad.set('')
    name.set('')
    mob.set('')
    fname.set('')
    fmob.set('')
    dept.set('select')
    


def new():
    regno.set('')
    year.set('')
    grad.set('')
    name.set('')
    mob.set('')
    fname.set('')
    fmob.set('')
    dept.set('select')


def display():
    c.execute('SELECT * FROM student')

    frame = Frame(window)
    frame.place(x= 400, y = 150)
   
    Lb = Listbox(frame, height = 8, width = 60,font=("arial", 12))
    Lb.pack(side = LEFT, fill = Y)
   
    scroll = Scrollbar(frame, orient = VERTICAL)
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set)
   

    Lb.insert(0, '| Reg No. | YOR | YOP | Name | Mob | Fname | Fmob | Dept |')
   
    data = c.fetchall()
   
    for row in data:
        Lb.insert(1,row)

    L7 = Label(window, text =  ' STUDENT DB     ',
               font=("arial", 16)).place(x=400,y=100)

    L8 = Label(window, text = "Newly added record is diplayed first",
               font=("arial", 16)).place(x=400,y=350)
    con.commit()

def course():
    c.execute('SELECT * FROM course')

    frame = Frame(window)
    frame.place(x= 400, y = 150)
   
    Lb = Listbox(frame, height = 8, width = 60,font=("arial", 12))
    Lb.pack(side = LEFT, fill = Y)
   
    scroll = Scrollbar(frame, orient = VERTICAL)
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set)
   

    Lb.insert(0, '| Reg No. | Course | Faculty |')
   
    data = c.fetchall()
   
    for row in data:
        Lb.insert(1,row)

    L7 = Label(window, text =  ' Course DB     ',
               font=("arial", 16)).place(x=400,y=100)

    L8 = Label(window, text = "Newly added record is diplayed first",
               font=("arial", 16)).place(x=400,y=350)
    con.commit()

   
submit = Button(window, text="Submit",command=send)
submit.place(x=240,y=500)

new = Button(window,text= "New Registration",command=new)
new.place(x=10,y=550)

display = Button(window,text= "Display",command=display)
display.place(x=150,y=550)

course = Button(window,text= "Display Courses",command=course)
course.place(x=240,y=550)    

window.mainloop()
