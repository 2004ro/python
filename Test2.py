# #Question-1:
# x=[x for x in range(1,51) if x%3==0]
# print(x)
# print(len(x))

# ##Question 2:
# words = ["python", "fun", "java", "ai", "data analysis", "practice", "patience", "go"] 
# x=filter(lambda x:len(x)>5,words)
# print(list(x))

# #Question 3:
# def calculate_tax(*salaries):
#     try:
#         sal=map(lambda x:(x*10/100),salaries)
#         s=list(sal)
#         sum=0
#         for i in s:
#             sum+=i
#         return sum
#     except TypeError:
#         print("Enter a valid salary entries.")
#     except Exception as e:
#         print(e)

# total=calculate_tax(45000,8000,30000)
# print("total tax: ",total)


# #Question 4:
# l=[12,34,56]
# x=map(lambda t:(t*9/5)+32,l)
# i=list(x)
# print(i)
# y=filter(lambda a:a>100,i)
# print(list(y))


# #Question 5:
# def fibonacci():
#     a=0
#     b=1
#     for i in range(10):
#         yield a
#         a,b=b,a+b
               
# result=fibonacci()
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


##question 6:
import student_utils
import json
students = []

for i in range(1, 4):
    print(f"\nStudent {i} :- ")  
    name = input("Name: ")

    try:
        m1 = float(input("Sub 1 Marks: "))
        m2 = float(input("Sub 2 Marks: "))
        m3 = float(input("Sub 3 Marks: "))

        for m in [m1, m2, m3]:
            if m < 0 or m > 100:
                raise ValueError("Marks b/w 0 and 100")

        # student_utils module ke functions sahi se call kiye
        avg = student_utils.calculate_avg(m1, m2, m3)
        grade = student_utils.get_grade(avg)

        students.append(
            {"name": name, "marks": [m1, m2, m3], "average": avg, "grade": grade}
        )

    except Exception as e:
        print(f"Error: {e}")
    

# with open("report.txt","wt") as fh:
#     for i in students:
#         fh.write(f"Name: {s['name']} | Average: {s['average']:.2f} | Grade: {s['grade']}\n")
