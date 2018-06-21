#Q1
#ZeroDivisionError
try:
    a=3
    if(a<4):
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("the no. is not divisible by zero and gives the zero division error")





#Q2
#IndexError
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("the no. is more than list elements")





#Q3
#An exception






#Q4
#-5.0
#a/b result in 0





#Q5
#1.
try:
    import tiger
except ImportError:
    print("file not found")


try:
    import threading
except ImportError:
    print("file not found")

#2.
try:
    a=int(input("enter the value"))
    print(a)
except ValueError:
    print("the value is not found")

#3.
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("the no. is more than list elements")

try:
    l=[1,2,3]
    print(l[2])
except IndexError:
    print("the no. is more than list elements")






#Q6
class AgeTooSmallError(Exception):
    pass
a=True
while(a):
    try:
        a=int(input("enter the age"))
        if(a>=18):
            a=False
            raise AgeTooSmallError
        else:
            print(a)
    except AgeTooSmallError:
        print("the age is less than 18")
    except ValueError:
        print("enter the value")