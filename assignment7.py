#Q1
r=int(input("enter the radius"))
def area(a):
    a=22/7*r*r
    print(a)
area(22/7*r*r)

#Q2
i=0
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
for i in range(1,1001):
     if(perfect(i)):
         print(i)



#Q3
def table(n,t=1):
    if(t==11):
        return 12
    (print(str(n) + "x" +str(t) + "=" + str(n*t)))
    table(n,t+1)
table(n=12)


#Q4
a=int(input("enter the number"))
b=int(input("enter its exponant value"))
def raise_to_power(a,b):
    if (b==1):
        return a
    else:
        return(a*raise_to_power(a,b-1))
print('%d^%d=%d' %(a,b,raise_to_power(a,b)))



#Q5
def fact(f):
    if (f==1):
        return 1
    g=(f*fact(f-1))
    return g
num=int(input("enter the no."))
h=fact(num)
d={num:h}
print(d)