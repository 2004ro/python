# #Question 4:
l=[12,34,56]
x=map(lambda t:(t*9/5)+32,l)
i=list(x)
print(i)
y=filter(lambda a:a>100,i)
print(list(y))
