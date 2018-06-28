#Q1
from tkinter import*
master=Tk()
frame=Frame(master,bg='blue')
frame.pack()
bluebutton=Button(frame,text='Hello World',fg='blue')
bluebutton.pack(side=LEFT)
orangebutton=Button(frame,text='Exit',fg='orange',command=exit)
orangebutton.pack(side=LEFT)
master.mainloop()


#Q2
from tkinter import*
root=Tk()
frame=Frame(root,bg='blue')
frame.pack()
def cmd1():
    lb1.config(text='hello world')
bluebutton=Button(root,text='Hello World',command=cmd1)
bluebutton.pack(side=LEFT)
orangebutton=Button(root,text='Exit',fg='orange',command=exit)
orangebutton.pack(side=LEFT)
lb1=Label(root,text='')
lb1.pack()
mainloop()

#Q3
from tkinter import*
root=Tk()
frame=Frame(root,bg='white')
frame.pack()
def cmd1():
    lb1.config(text='Ek Tha Tiger')
bluebutton=Button(frame,text='Click',command=cmd1)
bluebutton.pack(side=LEFT)
orangebutton=Button(frame,text='Exit',fg='orange',command=exit)
orangebutton.pack(side=LEFT)
lb1=Label(frame,text='Tiger Zinda Hai')
lb1.pack()
root.mainloop()



#Q4
from tkinter import*
root=Tk()
frame=Frame(root,bg='white')
frame.pack()
Label(frame,text='Enter Name').grid(row=0)
Label(frame,text='Enter Age').grid(row=1)
e1=Entry(frame)
e2=Entry(frame)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
def cal():
    a=e1.get()
    b=e2.get()
    c=a+''+b
    lb1=Label(frame,text=c)
    lb1.grid(row=2,column=1)
    lb1.config(text=a+b)
lb1=Label(frame,text='')
lb1.grid(row=2,column=1)
db=Button(frame,text='sonali',fg='green',command=cal)
db.grid(row=4,column=1)
mainloop()
