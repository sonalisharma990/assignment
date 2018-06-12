#Q1
i=0
while(i<10):
    num=input("enter your no.")
    i=i+1
    print("entered no. is" + num)



#Q2
while True:
    print("infinite")



#Q3
num=[]
sq=[]
for i in range(0,3):
    x=input("enter the no.")
    num.append(x)
    sq.append(int(x)*int(x))
print(num,sq)



#Q4
l=[1,2,"sonali",0.8,4,2]
a=[]
b=[]
c=[]
for i in l:
    if(type(i)==int):
        a.append(i)
    elif(type(i)==str):
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)




#Q5
even=[]
odd=[]
for i in range(1,101):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)



#Q6
k=4
for i in range(0,k):
    for j in range(0,i+1):
        print("*",end='')
    print("\r")



#Q7
d={'name':'sonali',
    'age':20}
for i in d:
    print(d[i])



#Q8
i=0
l=[] 
while(i<4):
    n=int(input("enter the no."))
    l.append(n)
    i=i+1
n=int(input("enter a no. to be searched"))
for i in l:
    if(n==i):
        l.remove(i)
print(l)

