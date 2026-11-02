## SET-3 Question:2

n=[1.01,1.99,2.5,1.5,1.01]
k=float(input("Num: "))
s=0
se=set()
trips=0
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        s=n[i]+n[j]
        if s<=k and i not in se and j not in se:
            se.add(i)
            se.add(j)
            trips+=1
for i in range(len(n)):
    if i not in se:
        trips+=1
print(trips)