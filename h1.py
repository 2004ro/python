#operators :- these are used to do some operations on variables
#1. Arithemtic operators:-+,-,/,*,**,//,%
#2.Assignment operator:- +=,-=,*=,=
#3.Comparison operators:-==,!=,<=,>=,<,>
#4.Logical operator:- and , or ,not
#conditional statements:-if ,elif,else
# Loops in Python:-for , while
#Functions
#List:-It is mutable ,duplicates ,ordered,heterogenous
#set :- hashing value 
# Exception handling:-try,except,else,finally
#arithmatic,assignment,logical,bitwise,comparison,identity,member


#List comprehension:- it is a concise syntex in python to create a new list from a existing iterable
# x=[1,2,3,4,5,6]
# y=[i for i in x if i%2==0]
# print(y)

# t=["Even" if x%2==0 else "Odd" for x in range(5)]
# print(t)

# x=[1,2,3,4,5,6]
# y=[i**2 for i in x]
# print(y)

#map function:- it maps means it do some operation at a time to all the iteams of iterator
# map(function,iterator)
# x=[2,3,4,5,6]
# def seq(x):
#     return x**2
# y=map(seq,x)
# print(list(y))

# # lambda function:- it is a anormous function without name with any length of arguments
# x=[9,8,7,6]
# y=map(lambda x:x**2,x)
# print(list(y))

#filter function :- it is used to filter the list
#filter(function,iterator)
# x=[1,2,3,4,5,6,7,8,9]
# # y=filter(lambda x:x%2==0,x)
# # print(list(y))
# def filt(x):
#     if x%2==0:
#         return x
# y=filter(filt,x)
# print(list(y))

#iterator:-    # next
# x=[1,2,3,4]
# i1=iter(x)
# print(next(i1))
# print(next(i1))
# print(next(i1))
# print(next(i1))
# print(next(i1))


# def gen(start,stop,step):
#     while start<stop:
#         yield start
#         start+=step
# out=gen(1.2,5.5,1)
# print(next(out))
# print(next(out))

# def gen_1(start,stop,step):
#     while ord(start)<=ord(stop):
#         yield start
#         start=chr(ord(start)+step)
# out=gen_1('a','p',2)
# print(list(out))

# fh=open("f.txt","xt")
# fh.close()

# fh=open("f.txt","wt")
# fh.write("hii,hello ")
# fh.close()
# fh=open("f.txt","rt")
# out=fh.read()
# print(out)

# with open("f.txt","wt") as fh:
#     fh.write("hii,hello\n how are you?")

# with open("f.txt","rt") as fh:
#     content=fh.read()
# print(content)

#JSON
# import json
# d1={"name":"Hill","Rollno":23,"Percent":90}
# with open("st.json","wt") as fh:
#     json.dump(d1,fh,indent=4)

# with open("st.json","rt") as fh:
#     content=json.load(fh)
# # print(content)

# with open("st.json","rt") as fh:
#     data=json.load(fh)

# data["marks"]=98
# with open("st.json","wt") as fh:
#     json.dump(data,fh)


# a=input("Enter the string: ")
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# print(b)

# if b==a:
#     print("palindrome")
# else:
#     print("Not")

# s=input("Enter the string: ")
# countc=0
# counti=0
# counts=0
# for i in s:
#     if i.isalpha():
#         countc+=1
#     elif i.isdigit():
#         counti+=1
#     else:
#         counts+=1
# print(countc,counti,counts)

# a=256
# while a>0:
#     print(a%10)
#     a=a//10


# def introduce(name,age=None):
#     if age is not None:
#         return f"My name is {name} . I am {age} years old."
#     else:
#         return f"My name is {name}.My age is secret"
# print(introduce("John",20))
# print (introduce("John"))


# def drop_min(*args):
#     li=list(args)
#     m=li[0]
#     for i in li:
#         if i<m:
#             m=i
#     li.remove(m)
#     return li
# print(drop_min(5,-2,8,4,-5,7,10))


# a= lambda x,y:x+y
# result=a(4,5)
# print(result)

# def find_max(a,b,c):
#     result = max(a,b,c)
#     return result
# def main():
#     a=int(input("Enter the a: "))
#     b=int(input("Enter the b: "))
#     c=int(input("Enter the c: "))
#     print(find_max(a,b,c))
# main()


# words=["python", "fun", "java", "await", "data analysis", "practice", "pateince", "burger", "pizza"]
# out=filter(lambda x: x.startswith("p")or x.startswith("P") in words,words)
# print(list(out))


# def employee(**salary):
#     sum=0
#     m=max(salary.values())
#     for i in salary:
#         sum=sum+salary[i]
  
#         if salary[i]==m:
#             n=i
#     avg=int(sum/len(salary))
#     return f"Avg salary is {avg}\n {n} gets highest salary"
# print(employee(john=50000,jill=70000,mark=60000))

# import os
# a=input("Enter the filename: ")
# if os.path.exists(a):
#     print("Exists")
# else:
#     print("Not avaliable")


# try:
#    with open("s.txt","xt") as fh:
#         fh.write("Python is easy to learn\n File handling is important\nPractice makes perfect")
#    with open("s.txt","rt") as fh:
#        content=fh.read()
#    print(content)
# except FileExistsError as e:
#     print(e)
# except Exception as e:
#     print(e)

