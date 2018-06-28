#Q1
from tkinter import *
from tkinter import messagebox
d={'Sonali':9800000089,'Aman':9000898989,'Aditi':2020000001,'Aina':9001010001,'Lovisha':9877800000}
root=Tk()
lb1=Label(root,text="Phone Directory")
lb1.pack()
scrl=Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
myList=Listbox(root,yscrollcommand=scrl.set)
i=1
for line in d:
    myList.insert(i,line+"-"+str(d[line]))
    i=i+1
myList.pack(side=LEFT,fill=BOTH)
scrl.config(command=myList.yview)
lbname=Label(root,text="Enter Name")
lbphn=Label(root,text="Enter phone No.")
e1=Entry(root)
e2=Entry(root)
btn=Button(root,text="Save")

lbname.pack()
e1.pack()
lbphn.pack()
e2.pack()
btn.pack()
mainloop()





#Q2
fL = {}
from tkinter import *
from tkinter import messagebox
d={'Sonali':9800000089,'Aman':9000898989,'Aditi':2020000001,'Aina':9001010001,'Lovisha':9877800000}
def savephnn():
    if (e1.index(END)==0 or e2.index(END)==0):
        messagebox.showwarning("Warning","Please enter all values")
    else:
        nam = e1.get()
        phn = int(e2.get())
        myList.insert(i, nam + "-" + str(phn))

        e1.delete(0, END)
        e2.delete(0, END)
        messagebox.showinfo("Congrats","Contact addded")
root=Tk()
lb1=Label(root,text="Phone Directory")
lb1.pack()
scrl=Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
myList=Listbox(root,yscrollcommand=scrl.set)
i=1
for line in d:
    myList.insert(i,line+"-"+str(d[line]))
    i=i+1
myList.pack(side=LEFT,fill=BOTH)
scrl.config(command=myList.yview)
lblname=Label(root,text="Enter Name")
lblphn=Label(root,text="Enter phone No.")
e1=Entry(root)
e2=Entry(root)
btn=Button(root,text="Save",command=savephnn)

lblname.pack()
e1.pack()
lblphn.pack()
e2.pack()
btn.pack()
mainloop()






