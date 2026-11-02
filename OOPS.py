#OOPS Concept
#class:- blueprint or template or design or mould of an object class has two :- one is property (attributes or variables)and second is functionality(functions or methods)
#object:- it is instance or example of class.
#l1=[1,2,3]  here l1 is the object of class list  

#Constructor:-It creates an object.
# __init__() is not a constructor in Python.If it is initializer google and chatgpt is showing that it is constructor it is not their fault it is magical word by __new__() dunder between it so it is showing that is is constructor.
#__new__() is a constructor in Python

# class Student:
#     pass
# stu1=Student()   #stu1 is an object of class student and to see that stu1 is object of class student to see this type()
# print(type(stu1))

# help(list)
# help(student)


#instance method:- method defined inside a class which is bounded to object/instance means it calls the object itself as a first argument

# class Student:
#     def studying(self):   # self :-why :-becuse the object calls itself.
#         print("Student studies for 1 hour")
#         print(f"self => {self}")

# stu1=Student()
# print(f"stu1 => {stu1}")     #here the stu1 and self have the same memory address.
# stu1.studying()  #Python calls studying(stu1)


# __init__() method or the initilizer it is a instace method that is used to intialize the instace variables.
# it is an instance method it means it has also has the self argument.
#It is used to create a initilizer
#__init__() can be anywhere but for our easyness it is the first method in the class.
#syntax to create a instance variable:- object.var=value 

# class Student:
#     ##here instance methods are __init__(),studying() 
#     ##here instance variables are in __init__ that is like (self.roll etc)
#     ## we cannot call explicitly __init__()  when we make object it is automatically called.
#     ##instance variables are different for every object

#     def __init__(self,roll,name,depart):
#         print(f"Initalizing the object = {self}")
#         self.roll=roll
#         self.name=name
#         self.department=depart

#     def studying(self):   
#         print("Student studies for 1 hour")
#         print(f"self => {self}")
# s1=Student(101,"John","CSE") #It will call __init__() automatically
# print(s1.name)

# s2=Student(102,"Jill","ECE") #It will again call __init__() automatically
# print(s2.name)


# #class variables: they are shared b/w the objects
# print("\n CLASS VARIABLES:\n")
# class Student:
    
#     college="LPU" # class variable

#     def __init__(self,roll,name,depart):
#         print(f"Initalizing the object = {self}")
#         self.roll=roll
#         self.name=name
#         self.department=depart

#     def studying(self):   
#         print("Student studies for 1 hour")
#         print(f"self => {self}")

# #Class variables are shared b/w the objects
# s1=Student(101,"Jhon","CSE")
# print(f"College of {s1.name} is {s1.college}")

# s2=Student(102,"Jill","ECE")
# print(f"College of {s2.name} is {s2.college}")

# print(f"College name using the Class: {Student.college}")

#class methods:- A method defined inside a class which is bound to the class not to the object.
#How differnce b/w class method and instance method :- THere is a decorator called class method decorator @classmethod 
#bydefualt the methods defined in the class are instance method.To create class method we use @classsmethod decorator
#To capture the class method we use the argument(cls) in class method.
#What is decorator:- It is another function that changes behaviour of existing function.Without changing the existing function we can change behaviour of that function with the help of decorator.
# class Welcome:
#     @classmethod
#     def greet(cls):
#         print("Hello everyone,good morning!")
#         print(cls)
# w1=Welcome()
# w1.greet()


#WAP that initalize length,breadth and make a instance method of area,perimeter
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth

#     def area(self):
#         print(f"Area Of Reactangle : {self.length*self.breadth}")
    
#     def perimeter(self):
#         print(f"Perimeter of Rectangle :{ 2*(self.length+self.breadth)}")

# R1=Rectangle(24,34)
# R2=Rectangle(45,55)
# R3=Rectangle(22,33)
# R1.length=66
# print(R1.length)
# R1.area()
# R1.perimeter()
# R2.area()
# R2.perimeter()
# R3.area()
# R3.perimeter()


#WAP(a) create a class contacts and define a __init__() method and take 2 attributes while intiallizing -name and mobile number.
# (b) DEfine a class variable-contact list -in which te objects of the contacts will be appended at the time of instantiation(Here instantiation means in the __inti__ method)
#(c)Define a method which takes a "name" of a contact (object) as an argument and returns the mobile number of that contact(object).
# class Contacts:
#     contact_list=[]

#     def __init__(self,name,mobile):
#         self.name=name
#         self.mobile=mobile
#         Contacts.contact_list.append(self)
        

#     def cont(self,name):
#         for contact in Contacts.contact_list:
#             if contact.name==name:
#                 return contact.mobile
        
#         return "Not Found!"


# C1=Contacts("John",895678)
# C2=Contacts("Jill",67894)
# C3=Contacts("Hill",45673)
# print(C1.cont("John"))
# # print(Contacts.cont("Jill"))   #TypeError
# print(Contacts.cont(C2,"Jill"))
# print(C1.cont("Alice"))




#1. Inheritance
#We can access the properties of the another class so we use the inheritance.
#Inheritance is used when a child class inherits the properties or functionalites from the parent or base class.

# class Vehicle:
#     company="ABC Motors"

#     def __init__(self,n_tyres,model_number,mileage):
#         self.n_tyres=n_tyres
#         self.model_number=model_number
#         self.mileage=mileage
    
#     def vehicle_details(self):
#         return f"The vehicle model {self.model_number} has {self.n_tyres} tyres and mileage of {self.mileage}"

# v1=Vehicle(8,"T123",10)
# print(v1.vehicle_details())


#If the child class haas no __init__() method then it will call the parent class __init__() method
# class Car(Vehicle):
#     pass

#Car is the child.derived/sub class
#Vehicle is calles the parent/base/super class

# C1=Car()  #TypeError: Vehicle.__init__() missing 3 required positional arguments: 'n_tyres', 'model_number', and 'mileage'

#when we create an object of the child class and the  chil does not have its own __init__() , then __init__() of the parent classs gets called.
#We have initialize the parent class's instance varibles
        
# C1=Car(4,"T653",20)
# print(C1.vehicle_details())
    
#The chils class has its own __init__() method

# class Car(Vehicle):
#     def __init__(self,n_airbags,sunroof=False):
#         self.n_airbags=n_airbags
#         self.sunroof=sunroof

#     def car_details(self):
#         if self.sunroof:
#            return f"This car has {self.n_airbags} airbags and a sunroof"
#         else:
#            return f"This car has {self.n_airbags} airbags and no sunroof"

# # C1=Car(6,True)
# # print(C1.mileage)  #AttributeError: 'Car' object has no attribute 'mileage'
# #When the chile\d class has its own __init__() ,the child class should manually initialize the parent's attributes

# class Car(Vehicle):
#     def __init__(self,n_tyres,model_number,mileage,n_airbags,sunroof=False):
#         self.n_airbags=n_airbags
#         self.sunroof=sunroof

#      #call parent class __init__() manually in the __init__() of the child class
#         Vehicle.__init__(self,n_tyres,model_number,mileage)
#     def car_details(self):
#         #We can call the instance method of parent in the child instance method .
#         print(self.vehicle_details())
#         if self.sunroof:
#            return f"This car has {self.n_airbags} airbags and a sunroof"
#         else:
#            return f"This car has {self.n_airbags} airbags and no sunroof"

# C1=Car(3,"Y84",30,6,True)
# print(C1.mileage)
# # print(C1.vehicle_details())
# print(C1.car_details())


#inclusive words:-Inclusive language in IT involves replacing terms with discriminatory, ableist, gendered, or violent connotations with neutral, accurate alternatives to create a welcoming environment for all technologists.
#In GitHub there is master as a default to move to the  main branch beacuse of inclusive language in IT.

 

#Triangle class as a parent and child class is equilateral triangle.
# class Triangle:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c

#     def area(self):
#         s=(self.a+self.b+self.c)/2
#         ar= (s*(s-self.a)*(s-self.b)*(s-self.c))**(1/2)
#         return ar
    
# class Equilateral(Triangle):
#     def __init__(self,side):
#         self.side=side
#         Triangle.__init__(self,side,side,side)


# T1=Equilateral(5)
# print(T1.area())

#super() :-in-built function in OOPS concept .it is used when the parent class __init__()  function is called in child class.and beacuse of super() inbuilt function we don't have to give self attribute.
#super() bydeault to the first  parent class .It does not means that we cannot use it in multiple inheritance the syntax is different.
# class Vehicle:
#     company="ABC Motors"

#     def __init__(self,n_tyres,model_number,mileage):
#         self.n_tyres=n_tyres
#         self.model_number=model_number
#         self.mileage=mileage
    
#     def vehicle_details(self):
#         return f"The vehicle model {self.model_number} has {self.n_tyres} tyres and mileage of {self.mileage}"

# v1=Vehicle(8,"T123",10)
# print(v1.vehicle_details())

# class Car(Vehicle):
#     def __init__(self,n_tyres,model_number,mileage,n_airbags,sunroof=False):
#         self.n_airbags=n_airbags
#         self.sunroof=sunroof

#         super().__init__(n_tyres,model_number,mileage)
#     def car_details(self):
#         #We can call the instance method of parent in the child instance method .
#         print(self.vehicle_details())
#         if self.sunroof:
#            return f"This car has {self.n_airbags} airbags and a sunroof"
#         else:
#            return f"This car has {self.n_airbags} airbags and no sunroof"
# C1=Car(4,"C33",20,6,True)
# print(C1.car_details())


#Single Inheritance:- When a child class has ONLY ONE Parent class.
#Muliple Inheritance:- When a child class has more than 1 parent class.


# class Color:
#     def __init__(self,color,shade):
#         self.color=color
#         self.shade=shade
    
#     def color_details(self):
#         return f"Color: {self.color} ,Shade: {self.color}"
    
#We will inherit both Vehicle and Color class in car class
#the default argumwnt should be at the end

# class Car(Vehicle,Color):
#     def __init__(self,n_tyres,model_number,mileage,n_airbags,color,shade,sunroof=False):
#         self.n_airbags=n_airbags
#         self.sunroof=sunroof

#         super().__init__(n_tyres,model_number,mileage)
#         # Color.__init__(self,color,shade)
#         # super().__init__(color,shade)    TypeError: Vehicle.__init__() missing 1 required positional argument: 'mileage' because bydefault super() function is always point to the first parent class.
#         super(Vehicle,self).__init__(color,shade)  # here this works but we have to give the previous parent class and sel

#     def car_details(self):
#         #We can call the instance method of parent in the child instance method .
#         print(self.vehicle_details())
#         print(self.color_details())
#         if self.sunroof:
#            return f"This car has {self.n_airbags} airbags and a sunroof"
#         else:
#            return f"This car has {self.n_airbags} airbags and no sunroof"
        
# c1=Car(4,"C22",20,6,"Black","dark",True)
# print(c1.car_details())

#Multi-level Inheritance:- One class is inherited by one parent class and that parent class is inherited by another class.
#  A --> B --> C
#Here if A is the parent class and  B is inherited by A and C is inherited by B then C can access the properties and functions of A and B both.
# class Company:
#     company_name="ABC"

# class Department(Company):
#     depart_name="IT"

# class Employee(Department):
#     def __init__(self,empid,empname):
#         self.empid=empid
#         self.empname=empname

#     def details(self):
#         return f" {self.empname} works for {self.depart_name} and for {self.company_name} company." 
    
# e1=Employee(101,"John")
# print(e1.details())





#2. Polymorphism:-
#Polymorphism:-Any entity that looks the same but behaves differently.Example:- (+[It is for conc for string and addition for numbers] and *[is is for repitation fr string and multiply for numbers]) operators and this is operator overloading.
#How does python know that it has to do conct or addition?
#Every operator has a dunder method.


#Operator Overloading
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth

#     def Area(self):
#         return self.length * self.breadth
    
# r1=Rectangle(6,4)
# print(r1.Area())
# r2=Rectangle(10,7)
# print(r2.Area())
# print(r1+r2)   #TypeError: unsupported operand type(s) for +: 'Rectangle' and 'Rectangle' when we haven't introduce in rectangle class __add__()
#__add__() :- this dunder method is used to add the enitites
#__str__():- this dunder method is used to print the string of object rather than memory address of class.
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth

#     def __add__(self, other):
#         # l=self.length+other.length
#         # b=self.breadth+other.breadth
#         # return l,b
#         return self.Area()+other.Area()

#     def __str__(self):
#         return f"{self.length,self.breadth} "
    
#     def __repr__(self):
#         return f"{self.area()}"  
    
#     #If there are __repr__() and __str__() both are there __str__() take the priority .and print the __str__() .If both are not there it will print the memory address of the object.


#     def Area(self):
#         return self.length * self.breadth
    
# r1=Rectangle(6,4)
# print(r1.Area())
# r2=Rectangle(10,7)
# print(r2.Area())
# print(r1+r2)
# print(r1)


# class Square:
#     def __init__(self,a):
#         self.a=a
     
#     def __lt__(self, other):
#         return self.a<other.a
    
#     def __abs__(self,b):
#         return abs(b)
#     def __sub__(self,other):
#         b=self.Area()-other.Area()
#         return abs(b)
#         # return Square.__abs__(self,b)
    
#     def check(self,other):
#         if self.a<other.a:
#             return True
#         else:
#             return False
        
#     def __str__(self):
#         return f"{self.a}"
    
#     def Area(self):
#         return self.a *self.a
    
# s1=Square(2)
# s2=Square(3)
# print(s1.Area())
# print(s2.Area())
# print(s1)
# print(s2)
# print(s1-s2)
# print(s1<s2)
# print(s1.check(s2))


#Method Overloading -------  There is no overloading in Python this concept does not exist in python 
#Same method but different arguments in same class.
# class A:
#     def f1(self,x,y):
#         return x+y
#     def f1(self,a,b,c):
#         return a+b+c

# a1=A()
# print(a1.f1(10,20))
# print(a1.f1(12,33,23))
#It is giving error beacuse there is no method overloading the latest method is called always.



#Method Overriding ----
#In case of inheritance when we want to change behaviour of an inherited method in the child class , we use method overriding.

# class Employee:
#     def working_hours(self):
#         return 9
    
# class Intern(Employee):
#     pass
# i1=Intern()
# print(i1.working_hours())
# #here i want to print 8 hours but I don't want to change the employee hours so if i want that i have to give the method to the intern .

# class Intern(Employee):
#     def working_hours(self):
#         return 8
# i2=Intern()
# print(i2.working_hours())
#MRO:-(Method Resolution order) Firstly it calls its own class.and It tells the order of the class .It tells which one  function is called in the inheritance.Means firstly it checks in chlid classs if the method is not found it will check in parent class.
#MRO:- If there are multiple classes with same method name MRO tells which one will get called.

# class A:
#     def f1(self):
#         print("Class A")

# class B:
#     def f1(self):
#         print("Class B")


# class C(B):
#     def f1(self):
#         print("Class c")


# class D(A,C):
#     pass


# class E(D):
#     pass
# obj=E()
# obj.f1()
# print(E.__mro__)
# help(E)



#Access Specifier
#Public : any normal variable    --> This is access everywhere.
# Protected : Using _(one underscore)   -->This is access within the class and and no outside the class and to the child class only.But in Python there is TRUE PROTECTED variable in Python.
# Private: Using __(double underscore)   -->This is access within the class and no outside the class and no to the child class.

# class Employee:
#     name = "John"    #Public
#     _empid=1011     #Protected
#     __salary=60000  #Private

# emp1=Employee()
# print(emp1.name)
# print(emp1.__salary)  #AttributeError: 'Employee' object has no attribute '__salary'
# print(emp1._empid)
#There is TRUE PROTECTED variable in python Irt is a convention to start the protected variable.
# Using _ to inform other developers that this is protected variable.

#To access the private variable   by obj._classname__var and this is called Name Mangling and this is only in Python.
# print(emp1._Employee__salary)

#Encapsulation:- Binding the data in class.This helps for abstraction.

#Abstraction:-Hiding the implementation.
# In abstraction there is concpet of abstract class
# If we have similiar methods in different classes and it is mandatory to make all the methods then we use abstract class. 
#Example:- Working of remotes .

# class Rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def Area(self):
#         return f"Area of Rectangle: {self.l*self.b}"
    
# class Circle:
#     def __init__(self,r):
#         self.r=r
    
    
# r1=Rectangle(3,4)
# print(r1.Area())

# c1=Circle(2)
# print(c1.Area())   #AttributeError: 'Circle' object has no attribute 'Area'


#To make sure all the shape classes area method we create abstract class.
#Abstract class is a class having atleast one abstract method.
# Abstract methods is a method which has a defination but NO  implementation.

#To make sure all the shape classes - Rectangle,Circle .. have 
#the area() method , we need to inherit the Shape abstract class in Shape class.
# from abc import ABC,abstractmethod       #Here ABC is abstarctcbaseclass
# class Shape(ABC):
#     @abstractmethod  #It is a decorator for abstract class
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

# r1=Rectangle(3,4)   #TypeError: Can't instantiate abstract class Rectangle without an implementation for abstract method 'area'


#We use abstract class beacuse it force all the child classes to implement the same method it makes mandatory and if we don n't allowed to make an object of that class.
#This enforces all the shape classes to have the abstract methods  implementation.


#Abstarct class should have atleast one abstarct method(not have implementation) and there can be (non-abstract or concret) methods.
#And we can't make the objects or instance of abstract class.

#Interface :--- It is a special type of abstract class .It has only abstract methods.

# help(object)  #object is the  parent of all the classes or ancenstor class or in-built class for all .
#If somebody ask where is __new__() we could say it is in the ancenstor class that is object class.


#WAP make 2 classes in which it is mandatory to make 2 methods place_order and deliver_order.
from abc import ABC ,abstractmethod
class food_delivery(ABC):
    @abstractmethod
    def place_order(self):
        pass
    def deliver_food(self):
        pass

class Swiggy(food_delivery):
    def __init__(self,name,location):
        self.name=name
        self.location=location
        
    def place_order(self):
        return f"Your order is placed by name : {self.name}"
    
    def deliver_food(self):
        return f"We have delivered the food to your {self.location} location"

class Zomato(food_delivery):
    def __init__(self,name,account):
        self.name=name
        self.account=account
    
    def place_order(self):
        return f" Your order place with {self.name} and with {self.account}"
    
    def deliver_food(self):
        return f" We have delivered your order give us your feedback"

s1=Swiggy("John","road no.3 jalandhar")
print(s1.place_order())

z1=Zomato("Jill","34F56")
print(z1.deliver_food())
