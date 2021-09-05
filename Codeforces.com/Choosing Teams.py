n,k=input().split()
k=int(k)
y=input().split()
t=0
for i in  y:
    if  k+int(i)<=5:
        t=t+1
print(t//3)
