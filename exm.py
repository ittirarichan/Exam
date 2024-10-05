# A
# B A
# C B A


a=65
for i in range(3):
    for j in range(i+1):
        print(chr(a-j),end='\t')
    print()
    a+=1