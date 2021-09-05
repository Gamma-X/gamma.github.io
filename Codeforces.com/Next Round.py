n,k=input().split()
a=input().split()
w=0
for i in range(len(a)):
    if int(a[i])>=int(a[int(k)-1])  and int(a[i])>0:
        w=i+1
print(w)
