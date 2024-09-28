l=[1,2,3,'abc','def',20]
n=0
for i in l:
    if type(i)==int or type(i)==float:
        n+=i
print(n)


