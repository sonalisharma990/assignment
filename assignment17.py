from tkinter import*
master=Tk()
frame=Frame(master,bg='red')
frame.pack()
bluebutton=Button(frame,text='Hello World',fg='blue')
bluebutton.pack(side=LEFT)
orangebutton=Button(frame,text='Exit',fg='orange',command=exit)
orangebutton.pack(side=LEFT)
master.mainloop()