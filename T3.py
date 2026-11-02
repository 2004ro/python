# #Question 3:
def calculate_tax(*salaries):
    try:
        sal=map(lambda x:(x*10/100),salaries)
        s=list(sal)
        sum=0
        for i in s:
            sum+=i
        return sum
    except TypeError:
        print("Enter a valid salary entries.")
    except Exception as e:
        print(e)

total=calculate_tax(45000,8000,30000)
print("total tax: ",total)