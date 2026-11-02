#Q3
n = int(input("no of months: "))
pnl = []
for i in range(n):
    pnl.append(int(input()))
k = int(input("max months: "))
sum = []
for i in range(n-k+1):
    s = 0
    for j in range(i,i+k):
        s += pnl[j]
    sum.append(s)
print(max(sum)) 