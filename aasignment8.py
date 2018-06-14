#Q1
print("there is a popular time module available in python which provides functions for working with times,"
      " and for converting between representations.Thefunction time.time() returns the current system time in ticks since 12:00am,January 1,1970(epoch)")
'''print("index     attributes     values"
      "0         tm_year        2008"
      "1         tm_mon         1 to 12"
      "2         tm_mday        1 to 31"
      "3         tm_hour        0 to23"
      "4         tm_min         0 to 59"
      "5         tm_sec         0 to 61(60 or 61 are leap seconds"
      "6         tm_wday        0 to 6"
      "7         tm_yday        1 to 366"
      "8         tm_isdst       -1,0,1 where -1 means libray determines DST")'''
#Q2
import time
print(time.asctime())


#Q3
import datetime
d=(datetime.date.today())
print(d.month)


#Q4
import datetime
d=(datetime.date.today())
print(d.day)

#Q5
import datetime
d='2021-01-11'
a=(datetime.datetime.strptime(d,"%Y-%m-%d"))
print(a.day)


#Q6
import time
print(time.asctime(time.localtime()))


#Q7
import math
a=int(input("enter the no."))
print(math.factorial(a))



#Q8
import math
a=int(input("enter the no."))
b=int(input("enter the no."))
print(math.gcd(a,b))


#Q9
import os
print(os.getcwd)
print(os.environ)

