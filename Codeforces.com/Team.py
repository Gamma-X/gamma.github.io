l=[]
for i in range(int(input())):
    n=input().split()
    l.append(n)
w=0
for j in range(len(l)):
    c=0
    for k in range(3):
        if l[j][k]=='1':
            c=c+1
    if c>=2:
        w=w+1
print(w)
    
