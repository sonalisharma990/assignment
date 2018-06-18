#Q1
class Animal:
    def animal_attribute(self):
        print("it has two eyes")
class Tiger(Animal):
    def animal_type(self):
        print("it belongs to cat family ")
t=Tiger()
t.animal_attribute()



#Q2
#A,B
#A,B



#Q3
class Cop:
    def __init__(self,name,age,work_experience,designation):
        self.name=name
        self.age=age
        self.work_experience=work_experience
        self.designation=designation
    def display(self):
        print("display the information")
        print("name",self.name)
        print("age",self.age)
        print("work_experience",self.work_experience)
    def _update_(self,name,age,work_experience,designation):
        self.name=name
        self.age=age
        self.work_experience=work_experience
        self.designation=designation
class Mission(Cop):
    def add_mission_details(self,name,age,work_experience,designation):
        print("updated information")
        print("name:")
        self.name=name
        print(name)
        print('age:')
        self.age=age
        print(age)
        print("work_experience")
        self.work_experience=work_experience
        print(designation)
        self.designation=designation
        print(designation)
m=Mission("sonali",20,5,"dancer")
name=input("enter your name")
age=int(input("enter your age"))
work_experience=int(input("enter your work_experience"))
designation=input("enter your designation")
m.display()
n=Mission(name,age,work_experience,designation)
n.add_mission_details(name,age,work_experience,designation)



#Q4
class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

class Rectangle(Shape):
    def area(self):
        area=(self.length*self.breadth)
        print("area of rectangle is")
        print(area)

class Square(Shape):
    def area(self):
        area=(self.length*self.breadth)
        print("area of square is")
        print(area)
r=Rectangle(3,5)
s=Square(6,6)
r.area()
s.area()