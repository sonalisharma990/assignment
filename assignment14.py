#Q1
f=open("file.txt",encoding="utf8")
j=(f.readlines())
j.reverse()
n=int(input("enter the no. of line you want"))
for i in range(0,n):
    print(j[i])
f.close()




#Q2
a="dance"
f=open("file6.txt",'r')
b=f.read()
c=b.split()
print(b.count(a))



#Q3
f=open("file2.txt",encoding="utf8")
f1=open("file3.txt","w")
for story in f:
 f1.write(story)
f.close()




#Q4
i=0
f=open("file1.txt",encoding="utf8")
x=(f.readlines())
f1=open("file4.txt",encoding="utf8")
y=(f1.readlines())
f3=open("file5.txt","w")
for i,j in zip(x,y):
    f3.write(i+j)
f.close()
f1.close()
f3.close()


#Q5
import random
list=[]
sortedlist=[]
for i in range(0,10):
    list.append(random.randint(1,10))
f=open("random.txt","w")
for s in list:
    r="".join(str(s))
    f.write(r)
f.close()
f1=open("random.txt","r")
t=f1.read()
for u in t:
    if(u.isdigit()):
        v="".join(u)
        sortedlist.append(v)
sortedlist.sort()
w=open("sorted.txt","w")
w.write(str(sortedlist))
f.close()


