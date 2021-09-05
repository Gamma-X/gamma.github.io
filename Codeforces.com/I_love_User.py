n=int(input())
cd=[int(i)for  i in input().split()]

j,k=cd[0],cd[0]
p=0
for i in range(1,n):
    if cd[i]>j:
        p=p+1
        j=cd[i]
    if cd[i]<k:
        p=p+1
        k=cd[i]

print(p)
        
        
