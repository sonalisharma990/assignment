#Q1
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*r*r
        return(area)
    def circumference(self):
        circumference=2*3.14*r
        return(circumference)
r=int(input("enter the radius"))
a=Circle(r)
print("area of circle:",a.area())
print("circumference of circle:",a.circumference())



#Q2
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
name=input("enter the name")
roll_no=int(input("enter the roll_no"))
a=Student(name,roll_no)
print(a.name)
print(a.roll_no)


#Q3
class Temperature:
    def __init__(self,fahrenheit):
        self.f=fahrenheit
    def celsius(self):
        celsius=(f-32)*5/9
        return celsius
    def __init__(self,celsius):
        self.c=celsius
    def fahrenheit(self):
        fahrenheit=c*9/5+32
        return fahrenheit
f=int(input("enter the temperature"))
a=Temperature(f)
print("temperature in celsius",a.celsius())

c=int(input("enter the temperature"))
b=Temperature(c)
print("temperature in fahrenheit",b.fahrenheit())




#Q4
class MovieDetails:
    def __init__(self,a,b,c,d):
        self.movie_name=a
        self.artist_name=b
        self.year_of_releasing=c
        self.rating=d
    def __update__(self,a,b,c,d):
        print("updated details")
        self.movie_name=a
        print(a)
        self.artist_name=b
        print(b)
        self.year_of_releasing=c
        print(c)
        self.rating=d
        print(d)
x=MovieDetails("Jatt v/s Ielts","Ravneet Singh","22/6/2018","***")
print(x.movie_name)
print(x.artist_name)
print(x.year_of_releasing)
print(x.rating)
movie_name=input("enter mocvie name")
artist_name=input("enter artist name")
year_of_releasing=int(input("enter the year"))
ratings=input("rate the movie")
y=MovieDetails(movie_name,artist_name,year_of_releasing,ratings)
y. __update__(movie_name,artist_name,year_of_releasing,ratings)





#Q5
class Expenditure:
    def __init__(self,expenditure,savings,total=0):
        self.e=expenditure
        self.s=savings
        self.t=0

    def display(self):
        print("total expenditure=",end="")
        print(self.e)
        print("total savings=",end="")
        print(self.s)
    def total_salary(self):
        self.t=self.e+self.s
    def display_salary(self):
        return self.t
n=int(input("enter the expenditure"))
m=int(input("enter savings"))
y=Expenditure(n,m)
y.display()
y.total_salary()
print("total salary=",end="")
print(y.display_salary())


