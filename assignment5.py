#Q1
a=int(input("enter the year"))
if(a%4==0):
    print("it is a leap year")
else:
    print("not a leap year")


#Q2
l=int(input("enter the value of length"))
b=int(input("enter the value for breadth"))
if(l==b):
    print("it is a square")
else:
    print("it is a rectangle")


#Q3
a=int(input("enter the age of first person"))
b=int(input("enter the age of second person"))
c=int(input("enter the age of third person"))
if(a>b and a>c):
    print("a is the oldest")
elif(b>a and b>c):
    print("b is oldest")
elif(c>a and c>b):
    print("c is oldest")
else:
    print("they all have same age")


#Q4
p=int(input("enter the points"))
if(p>1 and p<50):
    print(" sorry no prize")
elif(p>51 and p<150):
    print("get wooden dog")
elif(p>151 and p<180):
    print("book")
elif(p>181 and p<200):
    print("chocolates")
else:
    print("congratulations you won")


#Q5
q=int(input("enter the quantity"))
if(q*100>1000):
    print("discount is there"+str(q*100-0.10*q*100))
else:
    print(q*100)