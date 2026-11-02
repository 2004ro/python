# #Question 5:
def fibonacci():
    a=0
    b=1
    for i in range(10):
        yield a
        a,b=b,a+b
               
result=fibonacci()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))