# # name=input("Enter the name: ")
# # age=int(input("Enter the age: "))
# # maths_marks=int(input("Enter  Maths marks: "))
# # eng_marks=int(input("Enter English marks: "))
# # science_marks=int(input("Enter Science marks: "))
# # result=int(((maths_marks+eng_marks+science_marks)/300*100))
# # print(name, "Scored",result,"% marks")


# age=int(input("Enter age: "))
# if(age>=0 and age<=17):
#     print("Non-adult")
# elif(age>=18 and age<=59):
#     print("Adult")
# elif(age>=60 and age<=80):
#     print("Senior")
# else:
#     print("Super Senior")


# set1={5,9,2}   # sets are mutable but they  are not based on index these are unorderd if we can add the element at any place or at anywhere.
# set1.add(10)
# print(set1)

# dict1={"name":"Ronak","marks":89}
# dict1["marks"]=56
# # dict1.update({"age":21})  # update is use to add new key-value pairs we can add more than one also
# dict1.update({"name":"Hii"})
# print(dict1)

# s1="Python"
# print(s1)
# print(s1.replace("P","p"))
# print(s1)

# x=56.789
# print(round(x,2))

# s1="Hello"
# s2="World"
# print(s1+" "+s2)

# set1={1,False,True,0}
# print(set1)

# lan="Python"
# version=str(3.13)
# print(lan+version)

# # Iteration means how many times the loop is repeating
# li=[1,6,7,2,3,4,5,10,18,45]
# for i in li:
#     if(i%2==0):
#         print(i)   

# s1="Hello there we are learning"
# print(s1.find("is"))    # -1 means not present
# print(s1.find("there"))  # positive means present indexing of first come


# marks=[34,66,45,23,89,80]
# print(marks[:3])
# print(marks[-5:-2])
# print(marks[2:6:-1])   #It is logically incorrect but not give any error instead of it gives empty list[].

# #max 
# li=[5,6,9,2,11,3,77,64]
# max=li[0]
# for i in li:
#     if i > max:
#         max=i
# print(max)


# count the string and put it in dict
# str=input("Enter the string: ")
# dict={}
# for i in str:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)


# Second largest number
# li=[15,6,9,2,11,3,10]
# largest=float('-inf')
# second_largest=float('-inf')
# for i in li:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif largest>i>second_largest:
#         second_largest=i
# print("Second largest: ",second_largest)


# given list and given element that sums of element:- 2 sum problem
# x=[5,7,0,9,3,4]
# ele=10
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]+x[j]==ele:
#             print(x[i],x[j])

#2nd
# x=[5,7,0,9,3,4]
# set1=set()
# ele=9
# for i in x:
#     z= ele-i
#     if (z in set1):
#         out.append((i,z))
#     else:
#         set1.add(i)
# print(out)


# to remove duplicates
# x=[5,7,2,7,2,5,7,3,2,1,3]
# li=[]
# for i in x:
#     if i not in li:
#         li.append(i)
# print(li)

#Time complexity :- how much time the program is taking to give the output
    #O(n) :- it means only one for loop.
    #O(n^2) :- it means two for loops and it is slower than O(n).
    # O(log n):- alomst half of O(n).
    # O(n log n).
    # O(2^n). 



# li=[2,6,9,1,12,3,7]
# target=3

# # Linear search  :-  Time complexity is :-  as only one loop O(n)
# for i in li:
#     if i==target:
#         print("Found")
#         break


#Binary search :- search an element using binary search   :- it divides the list in half until we want to search the element that we want .it means find first  the middle one.
#Binary search is faster than linear search .Time complexity is O(log n)
#First the list should be sorted .
# def bin_search(arr,target):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]==target:
#             return mid
#         elif target>arr[mid]:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1

# arr=[3,5,6,8,9,15,18]
# target =15
# result=bin_search(arr,target)
# if result != -1:
#     print("Element found at index",result)
# else:
#     print("Element not found")

 
# Write a  program that string is a palindrome or not.


# str=input("Enter the string: ")
# rev=str[::-1]
# if str==rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


#2nd

# st="a man , a plan, a canal: Panama"
# # str=str.replace(" ","")
# str=""
# for ch in st:
#     if ch.isalpha():
#         str += ch

# str=str.lower()
# print(str)
# def palindrome(str): 
#    left=0
#    right=len(str)-1
#    while left<=right:
#         if str[left]==str[right]:
#            left=left+1
#            right=right-1
        
#         else:
#             return -1
        
# result = palindrome(str)
# if result != -1:
#     print("Is a Palindrome")
# else:
#     print("Not a Palindrome")


# Anagram 
# s1="eat"
# s2="tea"

# dict={}
# dict1={}
# for ch in s1:
#     if ch in dict:
#         dict[ch]+=1
#     else:
#         dict[ch]=1
# print(dict)
# for ch in s2:
#     if ch in dict1:
#         dict1[ch]+=1
#     else:
#         dict1[ch]=1
# print(dict1)
    
# if dict == dict1:
#     print("Anagram")
# else:
#     print("not")

## Factorial   
# n=int(input("Enter num: "))
# product=1
# for i in range(1,n+1):
#     product =product*i
# print(product)
    
#Recursion :- Function calls itself .
# def fact(n):
#     if n==1 or n==0 :
#         return 1
    
#     else:
#         return n*fact(n-1)
# result=fact(5)
# print(result)


#Left rotation of an array by k elements
# x=[1,2,3,4,5]
# k=6
# # k=k%len(x)   # it is used to avoid the index out of range error
# # a=x[k:]+x[:k]
# # print(a)
# #Reverse techinque
# li=x[::-1]
# print(li)


#First non-repeating ch
# a="swiss"
# s={}
# for i in a:
#     if  i in s:
#         s[i]+=1    
#     else:
#         s[i]=1
# for i in a:
#     if s[i] == 1:
#         print("First non-repeating ch:", i) 
#         break  

# shift all the repeating elements to the right
x=[0,1,0,3,7,0,2]
count=0
# for i in x:
#     if i== count:
#         x.remove(i)
#         x.append(i)
# print(x)

# j=0
# for i in range(len(x)):
#     if x[i]!=0:
#         x[i],x[j]=x[j],x[i]
#         j+=1
# print(x)


#reverse the character
# s="Python is fun"
# s=s.split()
# s=s[::-1]
# s = " ".join(s)
# print(s)

#return the index of s2
# s1="Python full is fun"
# s2="fun"
# n2=len(s2)
# for i in range(len(s1)):
#             if s1[i:i+n2]==s2:
#                     print(i)
#                     break
# else:
#         print(-1)

            
# def removeDuplicates(name,price,weight):
#     pr=set()
#     duplicate=0
#     for i in range(len(name)):
#         pr_tuple=(name[i],price[i],weight[i])
#         if pr_tuple in pr:
#             duplicate+=1
#         else:
#             pr.add(pr_tuple)
#     return duplicate


# name=["ball","ball","glove","glove","glove"]
# price=[2,3,1,2,1]
# weight=[2,5,1,1,1]
# result=removeDuplicates(name,price,weight)
# print(result)







# def kSub(k, nums):
    
    # remainder_counts = {0: 1}
    
    # current_sum = 0
    # total_k_subarrays = 0
    
    # for num in nums:
    #     current_sum += num
        
        
    #     remainder = current_sum % k
        
        
    #     if remainder in remainder_counts:
    #         total_k_subarrays += remainder_counts[remainder]
    #         remainder_counts[remainder] += 1
    #     else:
    #         remainder_counts[remainder] = 1
            
    # return total_k_subarrays


#question:-3
# s1="google.com"
# dict={}
# for i in s1:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

#question:-4
# product = {'soap': 50, 'oil': 200, 'laptop': 60000, 'phone': 25000, 'mouse': 500}
# max=0
# for i in product:
#     if product[i]>max:
#         max=product[i]
    
# for i in product:
#     if product[i]==max:
#         print("Costlist product is:",i)

#Question:-5
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New york'} 
# d.pop('name')
# d.pop('salary')
# print(d)

##Question:1-
# n=int(input("Enter the num: "))
# s=[]
# count=0
# for i in range(n):
#     li=input(" ")
#     s.append(li)
# print(s)
# for i in s:
#     if len(i)>2 and i==i[::-1]:
#         count +=1
#     else:
#         continue
# print(count) 

##Question-2
# s1 = input("Enter the string: ")
# s1=s1.split(" ")
# li=[]
# for i in s1:
#     if (len(i)>4 or len(i)==4) and (i.startswith("W")or i.startswith("w"))and (i not in li):
#         li.append(i)
# print(li)



# b={4,5,6,78}
# b.pop()
# print(b)


# x=[5,2,1,3]
# out=[]
# for i in x:
#     out.append(i**2)
# print(out)



#List comprehension  :- it is a compact way to create a list  from the another list in one line of code.
# x=[5,2,1,3]
# out=[i**2 for i in x]
# print(out)

# with map:- map(function,iterable) :- it is used to apply a function to all the items in an iterable.
# x=[5,2,1,3]
# def square(x):
#     return x**2
# m1=map(square,x)
# print(list(m1))

# lambda function:- it is a anonymous function which can have any number of arguments but only one expression.
# lambda arg1,arg2,....:expression
# x=[5,2,1,3]
# m1=map(lambda x:x**2,x)
# print(list(m1))

# *args:- variable length arguments it is used to pass a variable number of arguments to a function.
 #filter function:- filter(function,iterable object):- it uses a function on based on coniyion on iterable object.it returns filter object.
# x=[4,2,3,9,5,6]
# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# out=filter(is_even,x)
# print(list(out))

# #2nd 
# f1=filter(lambda x:x%2==0,x)
# print(list(f1))
#if the output is true it will store the return true elements in the filter object if the output is false it will not stored in the filter object.

#iterator:-
#next:- it is function for iterator to help it 1 by 1 fatch the iterator obeject element
# l1=[1,8,9,3]
# i1=iter(l1)
# print(next(i1))   #1
# print("hii")
# print(next(i1))    #8
# print(next(i1))   #9
# print(next(i1))    #3

# # print(next(i1))     #stopIteration error   if we don't want error we can use exception handling  (try,except)
# print(l1)
# print(type(i1))

#Generator:- it is a function or a type of object that generates a sequence of values .it is a user-defined function that uses the yield statement . yield function continue upto the condition is True and it will return the values like a return function.
#range function:- it is a built-in function that generates a sequence of numbers(integers).

# def gen_1(start,stop,step):
#     while start<stop:
#         #generate the value
#         # print(start)
#         #instead of print we use yield to make it generator function
#         yield start
#         start +=step
# out=gen_1(2.5,8.5,1)
# print(out) 
# # Genators are special type of iterators.so we can use next() function to get the next value from the generator object.
# #If we have in-built function range() then why we need to create our own generator function?  :- 1. range() is used only on integers so for float ,list other datatype we have need of generator.
# print(next(out))  #5
# print(list(out))


##Question:-write a program to generate a generator function gen_alpha('a','p',step)
# def gen_alpha(start,stop,step):
#     while ord(start)<=ord(stop):
#         yield start
#         start=chr((ord(start))+step)
# # out=gen_alpha('a','p',1)
# # print(list(out))

# def even_num(start,stop,step):
#     while start<=stop:
#         yield start
#         start +=step

# res=even_num(2,10,2)
# print(list(res))

#Defult argument:- it is a argument that takes a default value if no value is provided for that argument when the function is called.
#module:- it is a file that contains python code and can be imported into other python files to use the functions, classes, and variables defined in that module.The file with extension .py is called module.We can import the module using import keyword.

# double underscore:- (dunder name) 
# if __name__ == "__main__":    #the __name__ dunder name is used here to distinguish between the main the the other file.
#     out=gen_alpha('a','p',1)
#     print(list(out))

## agar apn ye p1.py ko run karty h  to dunder name "__main__" hoga aur agar apn p2.py ko run karty h to dunder name "p1" hoga. means jo file run hoga uska dunder name "__main__" hoga aur jo file import hoga uska dunder name "file name" hoga.
## always that file we run will be dunder name "__main__" and the file we import will be "file name".



#File handling
#creating a file
# fh=open("f1.txt","xt")   # "xt" is used only for creating file 
# fh.write("Hello")
# fh.close()

#Overwrite the file
# fh=open("f1.txt","wt")
# fh.write("Hello everyone.\n hii")
# fh.close()    # it is very important to close the file to release the memory and if we don't close the file the content of file don't be saved.

#Reading the file
# fh=open("f1.txt","rt")
# content=fh.read()
# fh.close()
# print(type(content))
# print(content)

#using 'with'

# with open("f1.txt","rt") as fh:
#     data = fh.read()
# print(data)

# x=fh.read()  # to make sure the\at file is closed   #ValueError: I/O operation on closed file.

##JSON
# import json
# d1={"roll":101,"name":"John","percent":80.5}
# with open("student.json","wt") as fh:
#     json.dump(d1,fh,indent=4)    #here indent means indentation given so that it loooks good in json

# d2={"roll":102,"name":"Jill","marks":[45,65,34],"address":{"street":"ABC street","city":"Delhi"},"percent":86.6}
# with open("student2.json","wt") as fh:
#     json.dump(d2,fh,indent=4)   #here dump means write in the file


# #Reading the JSON file
# with open("student2.json","rt") as fh:
#     data=json.load(fh)   #here load means read the file
# print(data)
# print(type(data))

# #updating the items in the json file  #first load means read,second update as we do in dict and then dump means write it.
# data["address"]["city"]="Bangalore"
# data["address"]["state"]="Karnataka"
# print(data)

# with open("student2.json","wt") as fh:
#     json.dump(data,fh,indent=4)


# Modes with write:-  x:- create   , w:-first create if not exists and overwrite   ,a:-add the content att the last of file
#Mode:- readline()
#readlines
# with open("f1.txt","rt") as fh:
#     contents=fh.readlines()
# print(contents)

# for i in contents:
#     print(i)

# #WAP to count the occurence of 'e' in f1.txt
# count=0
# with open("f1.txt","rt") as fh:
#     content=fh.read()
# for i in content:
#     if i=="e" or i=="E":
#         count+=1
# print(count)

#WAP to count the 'e' or 'E' in each line of f1.txt
# with open("f1.txt","rt") as fh:
#     content=fh.readlines()
# for i in content:
#     res=i.count("e")+i.count("E")
#     print(res)

# #"a" or append mode 
# with open("f1.txt","at") as fh:
#     fh.write("\n New content added")

#WAP copy the f1.txt to another file
# with open("f1.txt","rt") as fh:
#     content=fh.read()

# with open("f2.txt","xt") as fh:
#     fh.write(content)

#using os module to check if file exists before creation
# import os
# print(os.path.exists("f1.txt"))
# file_name=input("Enter the filename: ")
# if os.path.exists(file_name):
#     print("Cannot create! file already exist")
# else:
#     with open(file_name,"xt") as fh:
#         fh.write("some content")

#WAP to take 2 integers from user and divide them
# num1=int(input("Enter the num1: "))
# num2=int(input("Enter the num2: "))
# res=num1/num2
# print(res)

#To handle errors in python , we do exception handling using try-except!
# try:
#     num1=int(input("Enter the num1: "))
#     num2=int(input("Enter the num2: "))
#     res=num1/num2
#     print(res)
# except Exception  as e:
#     print(e)
#      print(type(e))
# # except ValueError:
# #     print("Invalid input: please enter integers.")
# # except ZeroDivisionError:
# #     print("Cannot divide by zero.")

#if there are more except block for the same error occured then only the first block will be executed and the other are ignored.



# import os
# file=input("enter the filename: ")
# if os.path.exists(file):
#     print("File exists")
# else:
#     print("File not found")

 
# if we don't know when we have to stop the loop we use
# if we want to go once in the while loop we should use while True
# while True:
#     try:
#         num1=int(input("Enter the number: "))
#         num2=int(input("Enter the number: "))
#         result =num1/num2
#         print(result)
#     except Exception as e:
#         print(e)
    
#     choice=input("Enter any char to exit and 'y' to continue: ")
#     if choice !="y":
#         break

# def add(*args):   # it stored in tuple   # (*) here used to accept the arguments and while calling we don't (*) in it.
#     print(sum(args))
# add(10,20) #30
# add(1,5,3) # 9  
# add(1,0,-1,8)

# def f1(**kwargs):  #It stored in dict   #(**) here is used to accept the arguments 
#     print(kwargs)
#     v=kwargs.values()
#     print(sum(v))
# f1(x=1,y=3)

# def drop_min(*args):
#     li=[]
#     li=list(args)
#     li.remove(min(args))
#     return li
# print(drop_min(5,-2,8,4,-5,7,10))

#WAP to drop the minimum in *args
# def drop_min(*args):
#     li=list(args)
#     m=li[0]
#     for i in li:
#         if i<m:
#             m=i
#     li.remove(m)
#     return li
# print(drop_min(5,-2,8,4,-5,7,10))


#WAP to find avg salary and the name of the person who have the highest salary using **kwargs.
#pass:- it is a placeholder
# def employee(**salary):
#     sum=0
#     m=max(salary.values())
    
#     for i in salary:
#         sum+=salary[i]
#         if salary[i]==m:
#             n=i

#     avg=int(sum/len(salary))
#     return f" avg salary is {avg}\n {n} gets highest salary"
# print(employee(john=50000,jill=70000,mark=60000))


# def employee(**salary):
#     sum=0
#     m=0
#     for i in salary.values():
#         if i>m:
#             m=i
    
    
#     for i in salary:
#         sum+=salary[i]
#         if salary[i]==m:
#             n=i

#     avg=int(sum/len(salary))
#     return f" avg salary is {avg}\n {n} gets highest salary"
# print(employee(john=50000,jill=70000,mark=60000))

