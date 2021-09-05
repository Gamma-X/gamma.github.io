k,r=input().split()
k=int(k);r=int(r)

i=1
while True:
    if (i*k)%10 in [r,0]:
        minm=i
        break
    else:
        i=i+1

print(minm)

