#Question -1:- Test-1 set-3
def t(text):
    for i in text:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for i in dict:
        if dict[i]>=k:
            li.append(i)
    return li
        
text=input("Enter the text: ")
text=text.split(" ")
dict={}
k=int(input("Enter the k: "))
li=[]
print(t(text))