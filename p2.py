# from line 493 for this code in p1.py
# 1st for importing the module and using the function from that module
#modules are the files with the extension of ( .py)
# import p1
# result=p1.gen_alpha('f','q',1)
# print(list(result))

# result1=p1.even_num(2,10,2)
# print(list(result1))



# 2nd for importing the function from the module and using that function
from p1 import gen_alpha,even_num
result = gen_alpha('f', 'q', 1)
print(list(result))

result1 = even_num(2, 10, 2)
print(list(result1))